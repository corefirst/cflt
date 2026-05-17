"""CFLT Part I — Logic Transformer Benchmark.

Tests whether an LLM can act as the CFLT Transformer (Step 1 of the two-step
workflow from llm-prompting.md §3). Evaluates two dimensions per case:

  Structural compliance (format)
  ─────────────────────────────
  SC  Slot order is Core → Reason → Space → Time
  SR  Core slot has non-empty content_l1
  IV  Inferred slots carry at least one suggestion

  Downstream accuracy (effectiveness)
  ────────────────────────────────────
  DX  The transformer's cflt_l1 output is fed to an extraction model and
      scored against the ground truth.  This is the only metric that answers
      "does the transformer actually help?" — a structurally valid CFLT can
      still fail to surface the right action.

      DX is compared against two Part II baselines:
        ctrl_baseline  ≈ 61–78 %  (natural-order input, from Part II)
        cflt_ceiling   = 100 %    (human-crafted CFLT, from Part II)
      A good transformer should bring DX close to the human ceiling.
"""

from __future__ import annotations

import json
import os
import statistics
import time
import argparse
from typing import Any, Dict, List, Optional

from utils import (
    call_transformer,
    compare_extraction,
    validate_cflt_compliance,
    load_dataset,
    get_client_and_model,
    MODELS_CONFIG,
    LANG_MAP,
    RESULTS_DIR,
    SYSTEM_PROMPT_TEMPLATE,
)

REPORT_PATH = os.path.join(RESULTS_DIR, "part1_eval_report.md")
RAW_PATH    = os.path.join(RESULTS_DIR, "part1_eval_raw.json")

# Part II baselines (from llm-part2-verification.md) for DX comparison.
# The distractor level (L3) is where CFLT's effect is strongest.
PART2_L3_CTRL_BASELINE  = 0.65   # ~avg across 4 models
PART2_L3_CFLT_CEILING   = 1.00   # human-crafted CFLT
PART2_OTHER_CTRL_BASELINE = 0.96  # L1/L2/L4 are near-ceiling in both arms


# ---------------------------------------------------------------------------
# Helper: extract the reordered source text from transformer output
# ---------------------------------------------------------------------------

def _cflt_text(transformer_res: Dict[str, Any]) -> Optional[str]:
    """Return the CFLT-reordered source text from transformer JSON output.

    Tries cflt_l1 first; falls back to reconstructing from slot content_l1 fields.
    Returns None if the output is malformed or empty.
    """
    if not isinstance(transformer_res, dict) or "error" in transformer_res:
        return None
    t = (transformer_res.get("cflt_l1") or "").strip()
    if t:
        return t
    parts = []
    for slot_type in ("core", "reason", "space", "time"):
        for s in transformer_res.get("slots", []):
            if s.get("type") == slot_type:
                c = (s.get("content_l1") or "").strip()
                if c and c.upper() not in ("NULL", "N/A", ""):
                    parts.append(c)
                break
    return ", ".join(parts) if parts else None


# ---------------------------------------------------------------------------
# DX: downstream accuracy
# ---------------------------------------------------------------------------

def _score_dx(
    client,
    model_name: str,
    cflt_text: str,
    instruction: str,
    gt: Dict[str, Any],
    key_aliases: Dict,
    value_synonyms: Dict,
    runs: int = 1,
) -> float:
    """Run the extractor on transformer-generated CFLT and return mean accuracy."""
    scores: List[float] = []
    for _ in range(runs):
        try:
            try:
                resp = client.chat.completions.create(
                    model=model_name,
                    temperature=0,
                    messages=[
                        {"role": "system", "content": instruction},
                        {"role": "user",   "content": cflt_text},
                    ],
                    response_format={"type": "json_object"},
                )
            except Exception as e:
                if any(tok in str(e).lower() for tok in ("temperature", "unsupported")):
                    resp = client.chat.completions.create(
                        model=model_name,
                        messages=[
                            {"role": "system", "content": instruction},
                            {"role": "user",   "content": cflt_text},
                        ],
                        response_format={"type": "json_object"},
                    )
                else:
                    raise
            content = json.loads(resp.choices[0].message.content)
            scores.append(1.0 if compare_extraction(content, gt, key_aliases, value_synonyms) else 0.0)
        except Exception:
            scores.append(0.0)
    return statistics.mean(scores) if scores else 0.0


# ---------------------------------------------------------------------------
# Benchmark
# ---------------------------------------------------------------------------

def run_benchmark(
    transformer_tag: Optional[str] = None,
    extractor_tag:   Optional[str] = None,
    runs: int = 1,
    include_local: bool = False,
    level_filter: Optional[List[int]] = None,
):
    """
    transformer_tag  Model used to convert natural language → CFLT JSON.
    extractor_tag    Model used to score DX (defaults to transformer_tag).
    runs             How many times DX is evaluated per case for variance.
    include_local    If True, also test ollama/* tags (skipped by default).
    """
    os.makedirs(RESULTS_DIR, exist_ok=True)
    dataset = load_dataset()
    meta = dataset.get("metadata", {})
    instructions  = meta.get("instructions", {})
    key_aliases   = meta.get("key_aliases", {})
    value_synonyms = meta.get("value_synonyms", {})

    cases = dataset["test_cases"]
    if level_filter:
        cases = [c for c in cases if c["level"] in level_filter]

    tags_to_test = [transformer_tag] if transformer_tag else list(MODELS_CONFIG.keys())

    all_results: List[Dict[str, Any]] = []

    for tag in tags_to_test:
        if not include_local and tag.startswith("ollama/"):
            continue
        try:
            client, model_name, _ = get_client_and_model(tag)
        except ValueError as e:
            print(f"[skip] {tag}: {e}")
            continue

        # Extractor can differ from transformer (e.g. small transformer, big extractor)
        ext_tag = extractor_tag or tag
        try:
            ext_client, ext_model, _ = get_client_and_model(ext_tag)
        except ValueError as e:
            print(f"[skip extractor] {ext_tag}: {e}")
            ext_client, ext_model = client, model_name

        print(f"\n=== Transformer: {tag}  |  Extractor: {ext_tag} (N={runs}) ===")
        model_block = {"transformer": tag, "extractor": ext_tag, "cases": []}

        for case in cases:
            cid  = case["id"]
            lang = case["language"]
            gt   = case["ground_truth"]
            instruction = instructions.get(lang, instructions.get("en", ""))
            source_text = case.get("utterance_control") or case.get("control")
            lang_full = LANG_MAP.get(lang, lang)

            # Step 1: transform (source = target = case's own language for in-language reordering)
            transformer_res = call_transformer(
                client, model_name, source_text,
                source_lang=lang_full, target_lang=lang_full, ui_lang=lang_full,
            )
            compliance      = validate_cflt_compliance(transformer_res)
            cflt_text       = _cflt_text(transformer_res)

            # Step 2: downstream accuracy on transformer output
            dx = 0.0
            if cflt_text:
                dx = _score_dx(ext_client, ext_model, cflt_text, instruction,
                               gt, key_aliases, value_synonyms, runs)
            dx_flag = "ok" if cflt_text else "no_cflt_text"

            sc = compliance["sc"]
            sr = compliance["sr"]
            iv = compliance["iv"]

            print(
                f"  {cid:14s}  SC={'✅' if sc else '❌'}  SR={'✅' if sr else '❌'}"
                f"  IV={'✅' if iv else '❌'}  DX={dx:.2f}"
                + ("  ⚠ could not extract cflt text" if dx_flag != "ok" else "")
            )

            model_block["cases"].append({
                "id": cid, "level": case["level"], "language": lang,
                "ground_truth": gt, "cflt_text": cflt_text,
                "sc": sc, "sr": sr, "iv": iv, "dx": dx,
                "transformer_response": transformer_res,
            })

        all_results.append(model_block)

    if all_results:
        _write_outputs(all_results, runs)
    else:
        print("No transformer model produced results.")


# ---------------------------------------------------------------------------
# Report generation
# ---------------------------------------------------------------------------

def _write_outputs(results: List[Dict[str, Any]], runs: int):
    with open(RAW_PATH, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    print(f"\nRaw: {RAW_PATH}")

    lines: List[str] = []
    lines.append("# CFLT Part I — Logic Transformer Benchmark\n")
    lines.append(f"**Generated:** {time.strftime('%Y-%m-%d %H:%M:%S')}  ")
    lines.append(f"**DX runs per case:** {runs}  ")
    lines.append("**SC** Slot order (Core→Reason→Space→Time)  ")
    lines.append("**SR** Subject retained in Core  ")
    lines.append("**IV** Inferred slots have suggestions  ")
    lines.append("**DX** Downstream extraction accuracy on transformer-generated CFLT\n")
    lines.append(f"> Part II baselines: L3 ctrl ≈{PART2_L3_CTRL_BASELINE:.0%}  "
                 f"/ L3 human-CFLT = {PART2_L3_CFLT_CEILING:.0%}.  "
                 "A good transformer should bring DX close to the human ceiling.\n")

    for block in results:
        lines.append(f"\n## Transformer: `{block['transformer']}`  |  Extractor: `{block['extractor']}`\n")

        # Per-case table
        lines.append("### Per-case results\n")
        lines.append("| ID | L | Lang | SC | SR | IV | DX | CFLT text preview |")
        lines.append("| :-- | :- | :-- | :-- | :-- | :-- | :-- | :-- |")
        for c in block["cases"]:
            preview = (c["cflt_text"] or "")[:60].replace("|", "\\|")
            lines.append(
                f"| {c['id']} | {c['level']} | {c['language']} "
                f"| {'✅' if c['sc'] else '❌'} "
                f"| {'✅' if c['sr'] else '❌'} "
                f"| {'✅' if c['iv'] else '❌'} "
                f"| {c['dx']:.2f} "
                f"| {preview} |"
            )

        # Aggregate by level
        lines.append("\n### DX by level (vs Part II baselines)\n")
        lines.append("| Level | N | SC% | SR% | IV% | DX (transformer) | L3 ctrl baseline | L3 human ceiling |")
        lines.append("| :-- | :- | :-- | :-- | :-- | :-- | :-- | :-- |")
        cases = block["cases"]
        for lvl in sorted({c["level"] for c in cases}):
            sub = [c for c in cases if c["level"] == lvl]
            n   = len(sub)
            sc_pct = sum(1 for c in sub if c["sc"]) / n
            sr_pct = sum(1 for c in sub if c["sr"]) / n
            iv_pct = sum(1 for c in sub if c["iv"]) / n
            dx_avg = statistics.mean(c["dx"] for c in sub)
            if lvl == 3:
                ctrl_ref  = f"{PART2_L3_CTRL_BASELINE:.0%}"
                cflt_ref  = f"{PART2_L3_CFLT_CEILING:.0%}"
            else:
                ctrl_ref  = f"{PART2_OTHER_CTRL_BASELINE:.0%} (sat.)"
                cflt_ref  = "—"
            lines.append(
                f"| L{lvl} | {n} "
                f"| {sc_pct:.0%} | {sr_pct:.0%} | {iv_pct:.0%} "
                f"| **{dx_avg:.0%}** | {ctrl_ref} | {cflt_ref} |"
            )

        # Overall DX
        all_dx = [c["dx"] for c in cases]
        lines.append(f"\n**Overall DX:** {statistics.mean(all_dx):.0%}  "
                     f"(SC {sum(c['sc'] for c in cases)/len(cases):.0%}, "
                     f"SR {sum(c['sr'] for c in cases)/len(cases):.0%}, "
                     f"IV {sum(c['iv'] for c in cases)/len(cases):.0%})\n")

    report = "\n".join(lines) + "\n"
    with open(REPORT_PATH, "w", encoding="utf-8") as f:
        f.write(report)
    print(f"Report: {REPORT_PATH}")


# ---------------------------------------------------------------------------
# Single-input mode (interactive)
# ---------------------------------------------------------------------------

def run_single_input(text: str, model_tag: Optional[str], source: str, target: str):
    source_full = "its original language" if source.lower() == "auto" else LANG_MAP.get(source, source)
    target_full = LANG_MAP.get(target, target)
    model_tag   = model_tag or "openai/gpt-5"

    try:
        client, model_name, _ = get_client_and_model(model_tag)
    except ValueError as e:
        print(f"Error: {e}")
        return

    print(f"Processing: '{text}'")
    print(f"Route: {source_full} → {target_full}  (Model: {model_tag})")

    res = call_transformer(client, model_name, text, source_full, target_full, target_full)
    if "error" in res:
        print(f"Failed: {res['error']}")
        return

    print("\n--- CFLT Transformation ---")
    print(json.dumps(res, indent=2, ensure_ascii=False))

    m = validate_cflt_compliance(res)
    print("\n--- Structural Compliance ---")
    for k, label in [("sc", "SC (Order)"), ("sr", "SR (Subject)"), ("iv", "IV (Inference)")]:
        print(f"  {label}: {'✅' if m[k] else '❌'}")

    cflt_text = _cflt_text(res)
    if cflt_text:
        print(f"\n--- CFLT text extracted ---\n  {cflt_text}")
    else:
        print("\n⚠ Could not extract cflt_l1 from output.")


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="CFLT Part I: Logic Transformer Benchmark (SC/SR/IV + downstream DX)"
    )
    parser.add_argument("--input",     type=str,  help="Single input text (interactive mode)")
    parser.add_argument("--model",     type=str,  help="Transformer model tag")
    parser.add_argument("--extractor", type=str,  help="Extractor model tag for DX (defaults to --model)")
    parser.add_argument("--source",    type=str,  default="auto",
                        help="Source language code for --input mode (default: auto)")
    parser.add_argument("--target",    type=str,  default="en",
                        help="Target language code for --input mode (default: en)")
    parser.add_argument("--benchmark", action="store_true", help="Run the full benchmark suite")
    parser.add_argument("--runs",      type=int,  default=1,
                        help="DX repetitions per case (default 1; use 3 for variance estimate)")
    parser.add_argument("--levels",    type=str,  default="",
                        help="Comma-separated level filter, e.g. '3,4'")
    parser.add_argument("--include-local", action="store_true",
                        help="Also test ollama/* models (skipped by default)")
    args = parser.parse_args()

    level_filter = [int(x) for x in args.levels.split(",") if x.strip()] if args.levels else None

    if args.input:
        run_single_input(args.input, args.model, args.source, args.target)
    elif args.benchmark or args.model:
        run_benchmark(
            transformer_tag=args.model,
            extractor_tag=args.extractor,
            runs=args.runs,
            include_local=args.include_local,
            level_filter=level_filter,
        )
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
