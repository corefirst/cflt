"""CFLT Part II — LLM extraction evaluator.

Experimental design (aligned with docs/zh/methodology/llm-prompting.md §5.2 / §6):

  * Both arms receive an IDENTICAL system prompt declaring the output schema
    (action / target / location / time). The system prompt does NOT contain
    any ground-truth value or key hint.
  * Both arms receive a user utterance carrying the same lexical content.
    The only between-arm difference is clause order:
        - control      = natural language, typically reason-first
        - experimental = same words reordered Core → Reason → Space → Time
  * Each case is repeated N times (default 3) at temperature=0 to estimate
    per-case variance. Some providers reject explicit temperature; we fall
    back to defaults on that error.
  * Two metrics, reported separately and never merged:
        - Accuracy: 1.0 if the extracted JSON matches the ground truth under
          the metadata-declared key/value synonym tables, else 0.0.
        - Tokens: prompt_tokens and completion_tokens reported independently.
"""

from __future__ import annotations

import argparse
import json
import os
import statistics
import sys
import time
from typing import Any, Dict, List, Tuple

from utils import (
    get_client_and_model,
    load_dataset,
    compare_extraction,
    RESULTS_DIR,
)

REPORT_PATH = os.path.join(RESULTS_DIR, "part2_llm_eval_report.md")
RAW_PATH = os.path.join(RESULTS_DIR, "part2_eval_raw.json")
DEFAULT_RUNS = 3


class BlockExistsError(Exception):
    """Raised when --force is needed because a block for a model already exists."""


def _load_existing_raw() -> List[Dict[str, Any]]:
    """Load existing raw blocks (one per model). Returns [] if missing or malformed."""
    if not os.path.exists(RAW_PATH):
        return []
    try:
        with open(RAW_PATH, encoding="utf-8") as f:
            data = json.load(f)
    except (json.JSONDecodeError, OSError) as e:
        print(f"[warn] cannot read {RAW_PATH}: {e}; starting fresh")
        return []
    if not isinstance(data, list):
        print(f"[warn] {RAW_PATH} is not a list of model blocks; starting fresh")
        return []
    for block in data:
        if not (isinstance(block, dict) and "model" in block and "cases" in block):
            print(f"[warn] {RAW_PATH} has an unexpected block shape; starting fresh")
            return []
    return data


def _merge_block(existing: List[Dict[str, Any]], new_block: Dict[str, Any], force: bool) -> List[Dict[str, Any]]:
    """Merge new_block into existing list by `model` tag. Raises BlockExistsError on collision unless force=True."""
    tag = new_block["model"]
    for i, b in enumerate(existing):
        if b.get("model") == tag:
            if not force:
                raise BlockExistsError(
                    f"a block for '{tag}' already exists in {RAW_PATH}. "
                    f"Use --force to replace it, or --fresh to start over."
                )
            existing[i] = new_block
            return existing
    existing.append(new_block)
    return existing


def _infer_runs_for_block(block: Dict[str, Any]) -> int:
    """Estimate N (runs per arm) by inspecting stored outputs in the block."""
    n = 0
    for c in block.get("cases", []):
        for arm in ("control", "cflt"):
            arm_d = c.get(arm, {})
            n = max(n, len(arm_d.get("outputs", [])))
    return n or DEFAULT_RUNS


def _parse_json_lenient(text: str):
    """Parse JSON from text, tolerating markdown code fences and surrounding prose.

    Some providers (notably Anthropic Claude via OpenRouter) return JSON wrapped
    in ```json ... ``` or with leading/trailing commentary, even when the OpenAI
    response_format parameter is honored. This helper tries three escalating
    strategies: direct parse → strip markdown fences → extract first {...} block.
    Returns the parsed dict or None if no valid JSON could be extracted.
    """
    if not text:
        return None
    import re
    # Strategy 1: direct parse (works for OpenAI / Gemini / Qwen / DeepSeek).
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        pass
    # Strategy 2: strip markdown code fence (```json ... ``` or ``` ... ```).
    fence_match = re.search(r"```(?:json)?\s*\n?(.*?)\n?```", text, re.DOTALL)
    if fence_match:
        try:
            return json.loads(fence_match.group(1))
        except json.JSONDecodeError:
            pass
    # Strategy 3: extract the first balanced {...} block (handles leading prose).
    brace_match = re.search(r"\{.*\}", text, re.DOTALL)
    if brace_match:
        try:
            return json.loads(brace_match.group(0))
        except json.JSONDecodeError:
            pass
    return None


def call_extract(
    client,
    model: str,
    instruction: str,
    utterance: str,
    temperature: float = 0.0,
) -> Dict[str, Any]:
    """One LLM call. Returns {'content': dict, 'prompt_tokens', 'completion_tokens'} or {'error'}."""
    base_kwargs = {
        "model": model,
        "messages": [
            {"role": "system", "content": instruction},
            {"role": "user", "content": utterance},
        ],
        "response_format": {"type": "json_object"},
    }
    try:
        try:
            response = client.chat.completions.create(temperature=temperature, **base_kwargs)
        except Exception as e:
            msg = str(e).lower()
            # Reasoning models (o-series, some gpt-5 variants) reject temperature; retry without it.
            if any(tok in msg for tok in ("temperature", "unsupported", "not supported")):
                response = client.chat.completions.create(**base_kwargs)
            # Some providers (Anthropic via OpenRouter) reject response_format; retry without it.
            # The lenient JSON parser below recovers JSON from markdown-wrapped output.
            elif any(tok in msg for tok in ("response_format", "json_object", "json mode")):
                base_kwargs.pop("response_format", None)
                response = client.chat.completions.create(temperature=temperature, **base_kwargs)
            else:
                raise

        usage = response.usage
        content_text = response.choices[0].message.content
        content = _parse_json_lenient(content_text)
        if content is None:
            return {"error": f"Non-JSON output: {(content_text or '')[:200]}"}

        return {
            "content": content,
            "prompt_tokens": getattr(usage, "prompt_tokens", 0) or 0,
            "completion_tokens": getattr(usage, "completion_tokens", 0) or 0,
        }
    except Exception as e:
        return {"error": str(e)}


def evaluate_case(
    client,
    model: str,
    case: Dict[str, Any],
    instruction: str,
    key_aliases: Dict[str, List[str]],
    value_synonyms: Dict[str, Dict[str, List[str]]],
    runs: int,
) -> Dict[str, Any]:
    """Run both arms `runs` times each and return per-arm statistics."""
    gt = case["ground_truth"]

    def run_arm(utterance: str) -> Dict[str, Any]:
        accs: List[float] = []
        prompts: List[int] = []
        completions: List[int] = []
        outputs: List[Any] = []
        errors: List[str] = []
        for _ in range(runs):
            res = call_extract(client, model, instruction, utterance)
            if "error" in res:
                errors.append(res["error"])
                outputs.append(None)
                continue
            outputs.append(res["content"])
            prompts.append(res["prompt_tokens"])
            completions.append(res["completion_tokens"])
            ok = compare_extraction(res["content"], gt, key_aliases, value_synonyms)
            accs.append(1.0 if ok else 0.0)
        return {
            "acc_mean": statistics.mean(accs) if accs else 0.0,
            "acc_std": statistics.pstdev(accs) if len(accs) > 1 else 0.0,
            "prompt_tokens_mean": statistics.mean(prompts) if prompts else 0,
            "completion_tokens_mean": statistics.mean(completions) if completions else 0,
            "n_success": len(accs),
            "n_error": len(errors),
            "outputs": outputs,
            "errors": errors,
        }

    return {
        "id": case["id"],
        "level": case["level"],
        "language": case["language"],
        "category": case.get("category", ""),
        "ground_truth": gt,
        "utterance_control": case["utterance_control"],
        "utterance_cflt": case["utterance_cflt"],
        "control": run_arm(case["utterance_control"]),
        "cflt": run_arm(case["utterance_cflt"]),
    }


def run_benchmark(
    model_tags: List[str],
    runs: int,
    level_filter: List[int] | None = None,
    force: bool = False,
    fresh: bool = False,
):
    os.makedirs(RESULTS_DIR, exist_ok=True)

    # Start from existing raw (default) or empty list (--fresh).
    existing_blocks: List[Dict[str, Any]] = [] if fresh else _load_existing_raw()
    if fresh and os.path.exists(RAW_PATH):
        print(f"[--fresh] ignoring existing {RAW_PATH}; all prior model blocks will be replaced.")

    # Pre-flight: detect collisions before doing any expensive API work.
    if not force and existing_blocks:
        existing_tags = {b.get("model") for b in existing_blocks}
        collisions = [t for t in model_tags if t in existing_tags]
        if collisions:
            raise BlockExistsError(
                f"Block(s) already exist for: {', '.join(collisions)}. "
                f"Use --force to replace, or --fresh to start over."
            )

    dataset = load_dataset()
    meta = dataset.get("metadata", {})
    instructions = meta.get("instructions", {})
    key_aliases = meta.get("key_aliases", {})
    value_synonyms = meta.get("value_synonyms", {})

    cases = dataset["test_cases"]
    if level_filter:
        cases = [c for c in cases if c["level"] in level_filter]

    new_blocks: List[Dict[str, Any]] = []

    for tag in model_tags:
        try:
            client, model_name, _ = get_client_and_model(tag)
        except ValueError as e:
            print(f"[skip] {tag}: {e}")
            continue

        print(f"\n=== Model: {tag} (N={runs} per arm) ===")
        model_block = {"model": tag, "runs": runs, "cases": []}

        for case in cases:
            instruction = instructions.get(case["language"], instructions.get("en", ""))
            print(f"  Case {case['id']} (L{case['level']}, {case['language']})")
            result = evaluate_case(
                client,
                model_name,
                case,
                instruction,
                key_aliases,
                value_synonyms,
                runs,
            )
            ctrl_acc = result["control"]["acc_mean"]
            cflt_acc = result["cflt"]["acc_mean"]
            print(
                f"    acc: ctrl={ctrl_acc:.2f}  cflt={cflt_acc:.2f}  "
                f"prompt_toks: {result['control']['prompt_tokens_mean']:.0f}/"
                f"{result['cflt']['prompt_tokens_mean']:.0f}  "
                f"completion_toks: {result['control']['completion_tokens_mean']:.0f}/"
                f"{result['cflt']['completion_tokens_mean']:.0f}"
            )
            model_block["cases"].append(result)

        new_blocks.append(model_block)
        existing_blocks = _merge_block(existing_blocks, model_block, force=True)

    if new_blocks:
        write_outputs(existing_blocks, runs)
    elif existing_blocks:
        # No new runs (every tag was skipped) but we still have prior data — regenerate report.
        print("No new model produced results; rendering report from existing raw.")
        write_outputs(existing_blocks, runs)
    else:
        print("No model produced results.")


def rejudge_existing(model_filter: List[str] | None = None) -> None:
    """Re-score every stored output using the CURRENT compare_extraction + dataset
    synonyms, then rewrite the raw JSON and the markdown report. No API calls.

    Use this after fixing a synonym-table bug to retroactively re-judge prior runs
    without paying for new API calls.
    """
    existing = _load_existing_raw()
    if not existing:
        print(f"No existing raw at {RAW_PATH} to rejudge.")
        return

    dataset = load_dataset()
    meta = dataset.get("metadata", {})
    key_aliases = meta.get("key_aliases", {})
    value_synonyms = meta.get("value_synonyms", {})

    blocks_touched = 0
    arms_changed = 0
    arms_total = 0
    for block in existing:
        if model_filter and block.get("model") not in model_filter:
            continue
        blocks_touched += 1
        for c in block.get("cases", []):
            gt = c.get("ground_truth", {})
            for arm_name in ("control", "cflt"):
                arm = c.get(arm_name, {})
                outputs = arm.get("outputs", []) or []
                accs = [
                    1.0 if (o is not None and compare_extraction(o, gt, key_aliases, value_synonyms)) else 0.0
                    for o in outputs
                    if o is not None
                ]
                if not accs:
                    continue
                new_mean = statistics.mean(accs)
                new_std = statistics.pstdev(accs) if len(accs) > 1 else 0.0
                arms_total += 1
                if abs(arm.get("acc_mean", -1.0) - new_mean) > 1e-9:
                    arms_changed += 1
                arm["acc_mean"] = new_mean
                arm["acc_std"] = new_std

    if blocks_touched == 0:
        print(
            f"--models filter matched no existing block. "
            f"Stored models: {[b.get('model') for b in existing]}"
        )
        return

    print(
        f"Rejudged {blocks_touched} block(s); "
        f"{arms_changed}/{arms_total} arm-scores changed under current synonyms."
    )
    # Use any block's stored runs (or DEFAULT) — header is informational only.
    runs_for_header = _infer_runs_for_block(existing[0])
    write_outputs(existing, runs_for_header)


def _agg(cases: List[Dict[str, Any]], arm: str, field: str) -> float:
    vals = [c[arm][field] for c in cases if c[arm].get("n_success", 0) > 0]
    return statistics.mean(vals) if vals else 0.0


# Doc-predicted ranges from docs/zh/methodology/llm-prompting.md §5.2
DOC_ACC_GAIN_MIN_PP = 15.0   # +15pp predicted
DOC_TOKEN_SAVE_MIN_PCT = -30.0  # -30% predicted (negative = savings)
DOC_TOKEN_SAVE_MAX_PCT = -50.0  # -50% predicted

# Thresholds for verdicts
ACC_TIE_PP = 5.0   # |Δacc| < 5pp counted as a tie

# A level is "ceiling-saturated" when control accuracy already at/above this.
# CFLT has no room to demonstrate improvement on such levels, so they are
# uninformative for verdicting the primacy hypothesis.
CEILING_THRESHOLD = 0.90


def _pct_change(old: float, new: float) -> float:
    if old <= 0:
        return 0.0
    return (new - old) / old * 100.0


def _build_summary(model: str, cases: List[Dict[str, Any]], runs: int) -> List[str]:
    """Generate the Summary block prepended before per-model tables."""
    n_cases = len(cases)
    ctrl_acc = _agg(cases, "control", "acc_mean") * 100.0
    cflt_acc = _agg(cases, "cflt", "acc_mean") * 100.0
    d_acc_pp = cflt_acc - ctrl_acc

    ctrl_pt = _agg(cases, "control", "prompt_tokens_mean")
    cflt_pt = _agg(cases, "cflt", "prompt_tokens_mean")
    pt_pct = _pct_change(ctrl_pt, cflt_pt)

    ctrl_ct = _agg(cases, "control", "completion_tokens_mean")
    cflt_ct = _agg(cases, "cflt", "completion_tokens_mean")
    ct_pct = _pct_change(ctrl_ct, cflt_ct)

    # Identify ceiling-saturated vs informative levels by control accuracy.
    # A level where ctrl ≥ CEILING_THRESHOLD has no room for CFLT to improve,
    # so dilutes the verdict if mixed into the overall mean.
    levels_in_run = sorted({c["level"] for c in cases})
    level_ctrl_acc = {}
    for lvl in levels_in_run:
        sub = [c for c in cases if c["level"] == lvl]
        level_ctrl_acc[lvl] = _agg(sub, "control", "acc_mean")
    saturated = [lvl for lvl, a in level_ctrl_acc.items() if a >= CEILING_THRESHOLD]
    informative = [lvl for lvl, a in level_ctrl_acc.items() if a < CEILING_THRESHOLD]

    informative_cases = [c for c in cases if c["level"] in informative]
    if informative_cases:
        nc_ctrl = _agg(informative_cases, "control", "acc_mean") * 100.0
        nc_cflt = _agg(informative_cases, "cflt", "acc_mean") * 100.0
        nc_delta = nc_cflt - nc_ctrl
    else:
        nc_ctrl = nc_cflt = nc_delta = None

    # The verdict uses the non-ceiling delta when available — that's where
    # CFLT actually has room to show signal. Falling back to overall otherwise.
    effective_delta = nc_delta if nc_delta is not None else d_acc_pp
    sat_label = ", ".join(f"L{l}" for l in saturated)
    nc_label = ", ".join(f"L{l}" for l in informative)
    sat_str = f"; {sat_label} ceiling-saturated" if saturated and informative else ""

    # Headline
    if not informative:
        headline = (
            f"⚠️ All {len(saturated)} level(s) ceiling-saturated "
            f"(ctrl ≥ {CEILING_THRESHOLD*100:.0f}% everywhere); dataset cannot show CFLT effect on this model"
        )
    elif effective_delta > ACC_TIE_PP:
        headline = (
            f"✅ On non-saturated cases ({nc_label}), CFLT improved accuracy by "
            f"**{effective_delta:+.1f}pp** ({nc_ctrl:.0f}% → {nc_cflt:.0f}%){sat_str}"
        )
    elif effective_delta < -ACC_TIE_PP:
        headline = (
            f"❌ On non-saturated cases ({nc_label}), CFLT hurt accuracy by "
            f"**{effective_delta:+.1f}pp** ({nc_ctrl:.0f}% → {nc_cflt:.0f}%){sat_str}"
        )
    else:
        headline = (
            f"➖ No meaningful accuracy difference (Δ={effective_delta:+.1f}pp on non-saturated cases){sat_str}"
        )

    # Verdict against doc §5.2 prediction — use effective_delta (informative cases only)
    if not informative:
        v_acc = "⚠️ Cannot evaluate — all levels saturated"
    elif effective_delta >= DOC_ACC_GAIN_MIN_PP:
        v_acc = f"✅ Supported (+{effective_delta:.1f}pp ≥ predicted +{DOC_ACC_GAIN_MIN_PP:.0f}pp on informative cases)"
    elif effective_delta > 0:
        v_acc = f"⚠️ Weak (+{effective_delta:.1f}pp, below predicted +{DOC_ACC_GAIN_MIN_PP:.0f}pp floor)"
    else:
        v_acc = f"❌ Not supported ({effective_delta:+.1f}pp; CFLT did not improve)"

    if pt_pct <= DOC_TOKEN_SAVE_MAX_PCT:
        v_pt = f"✅ Supported ({pt_pct:.1f}% within predicted -30 to -50%)"
    elif pt_pct <= DOC_TOKEN_SAVE_MIN_PCT:
        v_pt = f"⚠️ Partial ({pt_pct:.1f}% below predicted floor of -30%)"
    elif pt_pct < 0:
        v_pt = f"⚠️ Weak ({pt_pct:.1f}%; far below predicted -30 to -50%)"
    else:
        v_pt = f"❌ Not supported ({pt_pct:+.1f}%; CFLT did not save prompt tokens)"

    # Completion token verdict (doc speaks of "token economy" broadly; we report direction)
    if ct_pct < -5:
        v_ct = f"✅ CFLT reduced completion tokens by {-ct_pct:.1f}%"
    elif ct_pct < 5:
        v_ct = f"➖ No meaningful change ({ct_pct:+.1f}%)"
    else:
        v_ct = f"❌ CFLT *increased* completion tokens by {ct_pct:.1f}% (contra doc §4.1)"

    # Confidence
    total_calls = runs * 2 * n_cases
    if runs <= 1:
        conf = "🔴 **LOW** — N=1 per arm: no variance estimate possible, results are directional only"
    elif runs < 3 or n_cases < 8:
        conf = f"🟡 **MEDIUM** — N={runs}, {n_cases} cases ({total_calls} calls): basic variance, narrow scope"
    elif runs < 5 and n_cases < 16:
        conf = f"🟡 **MEDIUM** — N={runs}, {n_cases} cases ({total_calls} calls): reasonable but wide CIs"
    else:
        conf = f"🟢 **HIGH** — N={runs}, {n_cases} cases ({total_calls} calls): adequate for cross-model comparison"

    # Next-step recommendation, driven by current data
    next_steps: List[str] = []
    if runs < 3:
        next_steps.append("`--runs 3` (or higher) to get a real variance estimate")
    missing_levels = sorted(set([1, 2, 3, 4]) - set(levels_in_run))
    if missing_levels:
        next_steps.append(
            f"add the missing levels (`--levels 1,2,3,4`) — currently only L{levels_in_run} ran"
        )
    if not informative:
        next_steps.append(
            "all levels are at ceiling — the dataset can no longer probe CFLT on this model; "
            "consider adding harder distractor / multi-action cases at L3-L4 with longer contexts"
        )
    if effective_delta > ACC_TIE_PP and len({c["language"] for c in cases}) == 1:
        next_steps.append("test the other language to check whether the signal generalizes")
    if effective_delta > ACC_TIE_PP:
        next_steps.append(
            "re-run on a second frontier model (e.g. `--models google/gemini-3.1-pro` or `anthropic/claude-4-sonnet`) — "
            "a single-model result is anecdote, not evidence"
        )
    if abs(pt_pct) < 5:
        next_steps.append(
            "token-economy claim (doc §5.2 -30 to -50% prompt reduction) is **not testable with this dataset by design**: "
            "both arms have lexically identical content. To test it, add a third 'compressed CFLT' arm "
            "with slot tags and NULL fillers."
        )
    # Double-failure heuristic — only fires if synonym gaps still exist.
    double_fails = [c["id"] for c in cases if c["control"]["acc_mean"] == 0 and c["cflt"]["acc_mean"] == 0]
    if double_fails:
        next_steps.append(
            f"investigate {len(double_fails)} double-failure case(s) ({', '.join(double_fails)}) — "
            "check raw outputs for synonym-table gaps before treating these as honest CFLT failures"
        )

    ctrl_total = ctrl_pt + ctrl_ct
    cflt_total = cflt_pt + cflt_ct
    total_pct = _pct_change(ctrl_total, cflt_total)
    if total_pct < -5:
        v_total = f"✅ CFLT reduced total tokens by {-total_pct:.1f}%"
    elif total_pct < 5:
        v_total = f"➖ No meaningful change in total tokens ({total_pct:+.1f}%)"
    else:
        v_total = f"❌ CFLT *increased* total tokens by {total_pct:.1f}%"

    lines: List[str] = []
    lines.append("### 📊 Summary\n")

    # --- Section 1: Accuracy ---
    lines.append("#### 1. 结果正确性 / Accuracy\n")
    lines.append(f"**Headline:** {headline}\n")
    lines.append("| Scope | Control | CFLT | Δ | Verdict (vs. doc §5.2 prediction) |")
    lines.append("| :-- | :-- | :-- | :-- | :-- |")
    # Primary verdict line: non-ceiling Δacc — the only fair test of CFLT.
    if informative:
        nc_count = sum(1 for c in cases if c["level"] in informative)
        lines.append(
            f"| **Non-ceiling ({nc_label}, {nc_count} cases)** | "
            f"**{nc_ctrl:.0f}%** | **{nc_cflt:.0f}%** | **{nc_delta:+.1f}pp** | **{v_acc}** |"
        )
    # Overall (all cases, may be diluted by ceiling levels — show but de-emphasize).
    dilution_note = (
        " *(diluted by saturated levels)*"
        if saturated and informative
        else ""
    )
    lines.append(
        f"| Overall ({n_cases} cases) | {ctrl_acc:.0f}% | {cflt_acc:.0f}% | {d_acc_pp:+.1f}pp |{dilution_note} |"
    )
    # Per-level breakdown with saturation marker.
    if len(levels_in_run) > 1:
        for lvl in levels_in_run:
            sub = [c for c in cases if c["level"] == lvl]
            sc = _agg(sub, "control", "acc_mean") * 100.0
            se = _agg(sub, "cflt", "acc_mean") * 100.0
            marker = "🔒 saturated" if lvl in saturated else "📈 informative"
            lines.append(
                f"| L{lvl} ({len(sub)} cases) | {sc:.0f}% | {se:.0f}% | {se - sc:+.1f}pp | {marker} |"
            )
    lines.append("")

    # --- Section 2: Token consumption ---
    lines.append("#### 2. Token 消耗对比 / Token Cost\n")
    lines.append("| Metric | Control | CFLT | Δ | Verdict |")
    lines.append("| :-- | :-- | :-- | :-- | :-- |")
    lines.append(
        f"| Prompt tokens (mean / case) | {ctrl_pt:.0f} | {cflt_pt:.0f} | **{pt_pct:+.1f}%** | {v_pt} |"
    )
    lines.append(
        f"| Completion tokens (mean / case) | {ctrl_ct:.0f} | {cflt_ct:.0f} | **{ct_pct:+.1f}%** | {v_ct} |"
    )
    lines.append(
        f"| **Total tokens (mean / case)** | **{ctrl_total:.0f}** | **{cflt_total:.0f}** | **{total_pct:+.1f}%** | {v_total} |"
    )
    lines.append("")

    # --- Confidence + next steps ---
    lines.append(f"**Confidence:** {conf}\n")
    if next_steps:
        lines.append("**Recommended next steps:**")
        for i, step in enumerate(next_steps, 1):
            lines.append(f"  {i}. {step}")
        lines.append("")
    return lines


def _build_cross_model_section(results: List[Dict[str, Any]]) -> List[str]:
    """Render the Cross-Model Comparison section (only when >1 model present)."""
    lines: List[str] = []
    lines.append("\n## 🔬 Cross-Model Comparison\n")
    lines.append(
        "_Same dataset, same instruction, same case set — the only thing varying is the model. "
        "If CFLT's primacy effect is a real LLM property (not GPT-5-specific), it should show "
        "the same pattern across rows._\n"
    )

    # --- Accuracy: per-model non-ceiling Δacc ---
    lines.append("### Accuracy (non-ceiling Δacc)\n")
    lines.append("| Model | Informative levels | Saturated levels | Non-ceiling Ctrl | Non-ceiling CFLT | Δacc | Verdict |")
    lines.append("| :-- | :-- | :-- | :-- | :-- | :-- | :-- |")
    for block in results:
        cases = block["cases"]
        levels = sorted({c["level"] for c in cases})
        sat: List[int] = []
        info: List[int] = []
        for lvl in levels:
            sub = [c for c in cases if c["level"] == lvl]
            if _agg(sub, "control", "acc_mean") >= CEILING_THRESHOLD:
                sat.append(lvl)
            else:
                info.append(lvl)
        info_cases = [c for c in cases if c["level"] in info]
        if info_cases:
            nc_ctrl = _agg(info_cases, "control", "acc_mean") * 100.0
            nc_cflt = _agg(info_cases, "cflt", "acc_mean") * 100.0
            nc_delta = nc_cflt - nc_ctrl
            if nc_delta >= DOC_ACC_GAIN_MIN_PP:
                verdict = "✅ Supported"
            elif nc_delta > 0:
                verdict = "⚠️ Weak"
            else:
                verdict = "❌ Not supported"
            nc_ctrl_s = f"{nc_ctrl:.0f}%"
            nc_cflt_s = f"{nc_cflt:.0f}%"
            nc_delta_s = f"{nc_delta:+.1f}pp"
        else:
            nc_ctrl_s = nc_cflt_s = nc_delta_s = "—"
            verdict = "⚠️ All saturated"
        info_s = ", ".join(f"L{l}" for l in info) or "none"
        sat_s = ", ".join(f"L{l}" for l in sat) or "none"
        lines.append(
            f"| `{block['model']}` | {info_s} | {sat_s} "
            f"| {nc_ctrl_s} | {nc_cflt_s} | **{nc_delta_s}** | {verdict} |"
        )

    # --- Per-level accuracy heatmap ---
    all_levels = sorted({c["level"] for b in results for c in b["cases"]})
    if all_levels:
        lines.append("\n### Per-level accuracy across models\n")
        header_models = " | ".join(f"`{b['model']}` (Ctrl / CFLT)" for b in results)
        lines.append(f"| Level | {header_models} |")
        lines.append("| :-- | " + " | ".join(":--" for _ in results) + " |")
        for lvl in all_levels:
            cells: List[str] = []
            for block in results:
                sub = [c for c in block["cases"] if c["level"] == lvl]
                if not sub:
                    cells.append("—")
                    continue
                sc = _agg(sub, "control", "acc_mean") * 100.0
                se = _agg(sub, "cflt", "acc_mean") * 100.0
                delta = se - sc
                marker = "🔒" if sc >= CEILING_THRESHOLD * 100 else "📈"
                cells.append(f"{sc:.0f}% / {se:.0f}% {marker} ({delta:+.0f}pp)")
            lines.append(f"| L{lvl} | " + " | ".join(cells) + " |")
        lines.append("\n_🔒 = control already at ceiling (no room for CFLT to improve); "
                     "📈 = informative level._\n")

    # --- Token direction per model ---
    lines.append("### Token cost direction\n")
    lines.append("| Model | Prompt Δ | Completion Δ | Total Δ |")
    lines.append("| :-- | :-- | :-- | :-- |")
    for block in results:
        cases = block["cases"]
        ctrl_pt = _agg(cases, "control", "prompt_tokens_mean")
        cflt_pt = _agg(cases, "cflt", "prompt_tokens_mean")
        ctrl_ct = _agg(cases, "control", "completion_tokens_mean")
        cflt_ct = _agg(cases, "cflt", "completion_tokens_mean")
        pt_pct = _pct_change(ctrl_pt, cflt_pt)
        ct_pct = _pct_change(ctrl_ct, cflt_ct)
        total_pct = _pct_change(ctrl_pt + ctrl_ct, cflt_pt + cflt_ct)
        lines.append(
            f"| `{block['model']}` | {pt_pct:+.1f}% | {ct_pct:+.1f}% | {total_pct:+.1f}% |"
        )
    lines.append("")
    return lines


def _detect_dataset_drift(results: List[Dict[str, Any]]) -> str | None:
    """If model blocks were run against different case-id sets, return a warning string."""
    if len(results) < 2:
        return None
    per_block_ids = {b["model"]: {c["id"] for c in b["cases"]} for b in results}
    all_ids = set().union(*per_block_ids.values())
    drifted = {m: sorted(all_ids - ids) for m, ids in per_block_ids.items() if all_ids - ids}
    if not drifted:
        return None
    parts = []
    for m, missing in drifted.items():
        sample = ", ".join(missing[:3]) + ("…" if len(missing) > 3 else "")
        parts.append(f"`{m}` missing {len(missing)} case(s): {sample}")
    return (
        "> ⚠️ **Dataset drift detected** — model blocks were run against different case-id sets. "
        "Cross-model comparison may have gaps. "
        + "; ".join(parts)
    )


def write_outputs(results: List[Dict[str, Any]], runs: int):
    with open(RAW_PATH, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    print(f"\nRaw results: {RAW_PATH}")

    # Per-block runs may differ if blocks came from separate invocations.
    block_runs = [b.get("runs") or _infer_runs_for_block(b) for b in results]
    runs_label = str(runs) if len(set(block_runs)) == 1 else "varies by model (see per-model Summary)"

    lines: List[str] = []
    lines.append("# CFLT Part II — LLM Extraction Evaluation\n")
    lines.append(f"**Generated:** {time.strftime('%Y-%m-%d %H:%M:%S')}  ")
    model_list = ", ".join("`" + b["model"] + "`" for b in results)
    lines.append(f"**Models:** {model_list}  ")
    lines.append(f"**Runs per arm:** {runs_label}  ")
    lines.append("**Metric A:** extraction accuracy (1.0 = JSON matches ground truth under metadata synonyms)  ")
    lines.append("**Metric B:** prompt_tokens and completion_tokens (reported separately, never merged)\n")

    drift = _detect_dataset_drift(results)
    if drift:
        lines.append(drift + "\n")

    for block, b_runs in zip(results, block_runs):
        model = block["model"]
        cases = block["cases"]
        lines.append(f"\n## Model: `{model}`\n")

        # Executive summary at the top of each model section.
        lines.extend(_build_summary(model, cases, b_runs))

        # Per-case table
        lines.append("### Per-case results\n")
        lines.append("| ID | L | Lang | Acc Ctrl | Acc CFLT | Δacc | Prompt Tok C/E | Compl Tok C/E |")
        lines.append("| :-- | :- | :-- | :-- | :-- | :-- | :-- | :-- |")
        for c in cases:
            ca = c["control"]
            ce = c["cflt"]
            d_acc = ce["acc_mean"] - ca["acc_mean"]
            lines.append(
                f"| {c['id']} | {c['level']} | {c['language']} "
                f"| {ca['acc_mean']:.2f}±{ca['acc_std']:.2f} "
                f"| {ce['acc_mean']:.2f}±{ce['acc_std']:.2f} "
                f"| {d_acc:+.2f} "
                f"| {ca['prompt_tokens_mean']:.0f} / {ce['prompt_tokens_mean']:.0f} "
                f"| {ca['completion_tokens_mean']:.0f} / {ce['completion_tokens_mean']:.0f} |"
            )

        # Aggregate by level
        lines.append("\n### Aggregate by level\n")
        lines.append("| Level | N cases | Acc Ctrl | Acc CFLT | Δacc | Prompt Tok C/E | Compl Tok C/E |")
        lines.append("| :-- | :-- | :-- | :-- | :-- | :-- | :-- |")
        for lvl in sorted({c["level"] for c in cases}):
            subset = [c for c in cases if c["level"] == lvl]
            ctrl_acc = _agg(subset, "control", "acc_mean")
            cflt_acc = _agg(subset, "cflt", "acc_mean")
            ctrl_pt = _agg(subset, "control", "prompt_tokens_mean")
            cflt_pt = _agg(subset, "cflt", "prompt_tokens_mean")
            ctrl_ct = _agg(subset, "control", "completion_tokens_mean")
            cflt_ct = _agg(subset, "cflt", "completion_tokens_mean")
            lines.append(
                f"| L{lvl} | {len(subset)} "
                f"| {ctrl_acc:.2f} | {cflt_acc:.2f} | {cflt_acc - ctrl_acc:+.2f} "
                f"| {ctrl_pt:.0f} / {cflt_pt:.0f} "
                f"| {ctrl_ct:.0f} / {cflt_ct:.0f} |"
            )

        # Overall
        ctrl_overall = _agg(cases, "control", "acc_mean")
        cflt_overall = _agg(cases, "cflt", "acc_mean")
        lines.append(
            f"\n**Overall accuracy:** control={ctrl_overall:.2f} · "
            f"cflt={cflt_overall:.2f} · Δ={cflt_overall - ctrl_overall:+.2f}"
        )

    # Cross-model comparison appears once at the end, when applicable.
    if len(results) > 1:
        lines.extend(_build_cross_model_section(results))

    report = "\n".join(lines) + "\n"
    with open(REPORT_PATH, "w", encoding="utf-8") as f:
        f.write(report)
    print(f"Report: {REPORT_PATH}")


def main():
    parser = argparse.ArgumentParser(
        description="CFLT Part II evaluator (append-by-default; --force to replace, --rejudge to re-score offline)"
    )
    parser.add_argument(
        "--models",
        type=str,
        default="openai/gpt-5",
        help="Comma-separated model tags (see utils.MODELS_CONFIG). "
             "Also filters --rejudge to a subset of stored blocks.",
    )
    parser.add_argument("--runs", type=int, default=DEFAULT_RUNS, help="Repeats per arm (default 3)")
    parser.add_argument(
        "--levels",
        type=str,
        default="",
        help="Comma-separated levels to run, e.g. '1,2'. Empty = all.",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Replace existing block(s) for the same model tag instead of erroring out.",
    )
    parser.add_argument(
        "--fresh",
        action="store_true",
        help="Ignore any existing raw file; start over (equivalent to deleting it first).",
    )
    parser.add_argument(
        "--rejudge",
        action="store_true",
        help="Skip API calls. Re-score stored outputs with the current synonym table and rewrite the report. "
             "Use after fixing a synonym-table bug.",
    )
    args = parser.parse_args()

    model_tags = [m.strip() for m in args.models.split(",") if m.strip()]
    level_filter = (
        [int(x) for x in args.levels.split(",") if x.strip()] if args.levels else None
    )

    if args.rejudge:
        if args.fresh:
            parser.error("--rejudge and --fresh are mutually exclusive (rejudge needs existing data).")
        # If user explicitly passed --models, treat it as a filter; otherwise rejudge all.
        explicit_models = "--models" in sys.argv
        filter_tags = model_tags if explicit_models else None
        rejudge_existing(filter_tags)
        return

    try:
        run_benchmark(model_tags, args.runs, level_filter, force=args.force, fresh=args.fresh)
    except BlockExistsError as e:
        parser.exit(2, f"error: {e}\n")


if __name__ == "__main__":
    main()
