# Scripts

This directory contains evaluation scripts for the CFLT (Core-First Language Theory) methodology.

## Setup

```bash
python -m venv venv
source venv/bin/activate            # Windows: venv\Scripts\activate
pip install -r scripts/requirements.txt
```

## Configuration

API keys are read from environment variables (or a `.env` file in the project root):

```env
OPENAI_API_KEY=...
ANTHROPIC_API_KEY=...
GOOGLE_API_KEY=...
```

Local models go through [Ollama](https://ollama.com/) at `http://localhost:11434`.

Registered model tags live in `scripts/llm_eval/utils.py` under `MODELS_CONFIG`.

---

# LLM Evaluation Suite (`llm_eval/`)

Two complementary experiments validating the claims in
[`docs/zh/methodology/llm-prompting.md`](../docs/zh/methodology/llm-prompting.md).

| Script | What it measures | Maps to doc section |
| :-- | :-- | :-- |
| `part1_human_cflt_eval.py` | Whether an LLM can act as a CFLT *transformer* — produce a structurally compliant CFLT JSON from natural-language input. | §3 (Sanitization Workflow) |
| `part2_llm_cflt_eval.py` | Whether feeding a *core-first reordered* utterance to the main model improves extraction accuracy and changes token cost vs. the natural reason-first wording. | §5.2, §6 (Validation) |

Both consume the same shared `dataset.json` (v2.0.0).

---

## Shared dataset (`dataset.json`)

Twenty-four cases across four difficulty levels and two languages
(L1–L4 × {EN, ZH} × 3 scenarios). Each case provides:

| Field | Role |
| :-- | :-- |
| `instruction` *(from `metadata.instructions[language]`)* | System prompt used by Part II. Declares only the output schema (`action / target / location / time`) — never the ground-truth values. |
| `utterance_control` | Natural-language phrasing, typically reason-first. |
| `utterance_cflt` | The **same lexical content** reordered Core → Reason → Space → Time. No `[CORE]` / `[REASON]` markup — the difference is clause order only. |
| `ground_truth` | Canonical expected extraction in lowercase English. |

Synonyms live in `metadata.value_synonyms[field][canonical_value]` and
`metadata.key_aliases[field]`. To accept a new surface form, edit the dataset
metadata — **never** the comparison code.

### Level signature

| Level | Test focus | Expected behavior if CFLT works |
| :-- | :-- | :-- |
| **L1** | Single action, 2 fields | Both arms near-ceiling; little signal expected. |
| **L2** | Action + location + time, 4 fields | Both arms still high; mild token differences. |
| **L3** | Same as L2 plus *distractor* clauses (red herrings, ongoing context). | Larger token gap; control may drop accuracy if model gets distracted. |
| **L4** | Multiple candidate actions, the *decided* one is buried at end-of-utterance in control. | **Key primacy test.** If position-0 attention matters, control should fail on competing actions while CFLT (decision-first) succeeds. |

---

## Part I — CFLT Transformer Benchmark

`part1_human_cflt_eval.py` evaluates whether an LLM, prompted as a *Universal
CFLT Transformer* (see `SYSTEM_PROMPT_TEMPLATE` in `utils.py`), produces a
structurally valid CFLT JSON from each case's `utterance_control`. It scores
three compliance metrics defined in `utils.validate_cflt_compliance`:

- **SC (Slot Order)** — slots emerge in `core → reason → space → time` order.
- **SR (Subject Retention)** — the `core` slot has non-empty `content_l1`.
- **IV (Inference Validity)** — any `is_inferred: true` slot carries
  `suggestions`.

### Run

```bash
# Single ad-hoc input
python scripts/llm_eval/part1_human_cflt_eval.py \
  --input "外面下雨了，请把窗户关上。" \
  --model google/gemini-3.1-pro --source zh --target en

# Full benchmark across all cases (omit --model to sweep MODELS_CONFIG)
python scripts/llm_eval/part1_human_cflt_eval.py --benchmark
python scripts/llm_eval/part1_human_cflt_eval.py --benchmark --model openai/gpt-5
```

Outputs land in `results/part1_eval_report.md` and `results/part1_eval_raw.json`.

---

## Part II — CFLT Verification (Control vs. Experimental)

`part2_llm_cflt_eval.py` tests the **falsifiable** claims of §5.2:

1. **Accuracy** — does core-first ordering raise instruction-following
   accuracy on the same extraction task?
2. **Token cost** — does CFLT reordering shift `prompt_tokens` and/or
   `completion_tokens`? (Reported **separately** — never merged into a single
   "gain" number, because the two move in different directions for different
   reasons.)

### Design guarantees

The 2025-11 redesign removed several methodological landmines that had
inflated earlier accuracy numbers. The current script enforces:

| Constraint | Enforcement |
| :-- | :-- |
| No ground-truth leakage in the system prompt | `instruction` comes from `metadata.instructions[lang]` and contains only the schema (`action / target / location / time`). |
| Two arms differ only in clause order | The dataset stores both `utterance_control` and `utterance_cflt` with the **same lexical content**; no `[CORE]` markers, no compression. |
| Per-case variance reported | Each arm runs `--runs N` times (default 3) at `temperature=0`. Models that reject `temperature=0` are retried with provider defaults automatically. |
| Token metrics are not conflated | `prompt_tokens` and `completion_tokens` reported in independent columns. |
| Comparison is not silently relaxed over time | All accepted synonyms live in `dataset.json → metadata.value_synonyms`. The compare path in `utils.compare_extraction` does **not** do substring or string-to-dict fallback. |

### CLI flags

| Flag | Default | Meaning |
| :-- | :-- | :-- |
| `--models` | `openai/gpt-5` | Comma-separated model tags from `MODELS_CONFIG`. With `--rejudge`, used as a *filter* over stored blocks. |
| `--levels` | *(all)* | Comma-separated level filter, e.g. `3,4` to skip easy cases. |
| `--runs` | `3` | **How many times each arm is repeated per case** — see below. |
| `--force` | off | Replace an already-stored block for the same model tag instead of erroring out. |
| `--fresh` | off | Ignore any existing `part2_eval_raw.json` and start over. Equivalent to deleting the file first. |
| `--rejudge` | off | **Skip all API calls.** Re-score the stored outputs with the current `compare_extraction` + `dataset.json` synonyms. Use after fixing a synonym-table bug to refresh past results for free. |

#### `--runs N` — what it does and why it matters

For every case, **both the control arm and the CFLT arm are called `N` times
independently**. The script reports `mean ± std` of accuracy and token counts
across those `N` calls.

Total API calls per model: `N × 24 cases × 2 arms`.

| `--runs` | Calls per model | When to use |
| :-- | :-- | :-- |
| `1` | 48 | Smoke test only — gives no variance information; **not** suitable for drawing conclusions. |
| `3` (default) | 144 | Standard run. Distinguishes "model is unstable on this case" (std > 0) from "model is deterministic" (std = 0). |
| `5` | 240 | Tighter confidence intervals; use when comparing close numbers across models. |
| `≥10` | 480+ | Publication-grade evidence. Check provider quota first. |

Why `N > 1` is needed even with `temperature=0`:

- Some providers do not guarantee bit-exact determinism at `temperature=0`
  (floating-point reduction order on GPU, batch scheduling, MoE routing).
- Several frontier models (reasoning-mode GPT-5 / o-series) **reject the
  `temperature` parameter entirely** — the script falls back to provider
  defaults, at which point outputs are genuinely stochastic. `N > 1` is the
  only way to estimate that noise.
- If `std` is consistently `0` on a deterministic model, you can drop to
  `--runs 1` on subsequent passes to save quota; but the first pass should
  always use `≥ 3` so you know whether it's safe to.

### Append-by-default workflow

The evaluator **appends** new model results to `results/part2_eval_raw.json`
rather than overwriting. This lets you build up a cross-model comparison
incrementally without paying to re-run earlier models. The corresponding
report (`part2_llm_eval_report.md`) auto-regenerates and grows a
**Cross-Model Comparison** section as soon as ≥ 2 models are present.

```bash
# 1. Establish a baseline
python scripts/llm_eval/part2_llm_cflt_eval.py --models openai/gpt-5 --runs 3
# → raw contains [gpt-5]

# 2. Add a second model (incremental, ~144 new calls)
python scripts/llm_eval/part2_llm_cflt_eval.py --models google/gemini-3.1-pro --runs 3
# → raw contains [gpt-5, gemini-3.1-pro]
# → report grows a "Cross-Model Comparison" section automatically

# 3. Add a third (or more) the same way
python scripts/llm_eval/part2_llm_cflt_eval.py --models anthropic/claude-4-sonnet --runs 3

# 4. Re-run an existing model (e.g. with --runs 5 for tighter CI)
python scripts/llm_eval/part2_llm_cflt_eval.py --models openai/gpt-5 --runs 5 --force

# 5. Fixed a synonym in dataset.json? Refresh ALL stored models for free
python scripts/llm_eval/part2_llm_cflt_eval.py --rejudge

# 6. Refresh only one stored model's scores
python scripts/llm_eval/part2_llm_cflt_eval.py --rejudge --models openai/gpt-5

# 7. Wipe and restart
python scripts/llm_eval/part2_llm_cflt_eval.py --models openai/gpt-5 --fresh
```

#### Collision behavior

If you try to run a model whose tag is already in `part2_eval_raw.json`
without `--force`, the evaluator exits before any API call:

```
error: Block(s) already exist for: openai/gpt-5. Use --force to replace, or --fresh to start over.
```

This is intentional — it prevents the common mistake of "I just wanted to
look at the help and burned 144 API calls overwriting yesterday's data."

#### Dataset drift

Each model block stores the case IDs it was run against. If you append a
new model *after* adding/removing cases in `dataset.json`, the report's
top adds a warning so you don't compare apples to oranges:

```
> ⚠️ Dataset drift detected — model blocks were run against different
> case-id sets. Cross-model comparison may have gaps.
> `openai/gpt-5` missing 1 case(s): EN_L4_04
```

To recover: either re-run the older models with `--force`, or accept the
gap (the per-level tables handle missing cells with `—`).

#### `--rejudge` (offline rescoring)

Synonym tables are dataset-driven and grow as you observe new surface
forms (e.g. `"6 PM today"` ≡ `"today 6 PM"`). Whenever you add a synonym,
all *prior* runs are stale: they were scored under the old table and
might falsely show CFLT failures that current logic would now mark as
correct.

`--rejudge` walks every stored output and re-applies
`utils.compare_extraction` with the current `dataset.json` synonyms. It
makes **zero** API calls. After it finishes, the report shows the
updated accuracy numbers but uses the same recorded prompt/completion
token counts (those don't depend on the judge).

```bash
# Typical sequence after spotting a synonym gap
vim scripts/llm_eval/dataset.json            # add the missing surface form
python scripts/llm_eval/part2_llm_cflt_eval.py --rejudge
git diff results/part2_llm_eval_report.md   # see which cases now pass
```

### Run

```bash
# Default: openai/gpt-5, N=3, all levels (errors if a gpt-5 block already exists)
python scripts/llm_eval/part2_llm_cflt_eval.py

# Quick smoke test — single call per arm (still respects collision rules)
python scripts/llm_eval/part2_llm_cflt_eval.py --runs 1 --levels 1 --fresh

# Restrict to the primacy-sensitive levels (L3 distractors, L4 multi-action)
python scripts/llm_eval/part2_llm_cflt_eval.py --levels 3,4

# Cross-model comparison in a single command (no append needed — same outcome)
python scripts/llm_eval/part2_llm_cflt_eval.py \
  --models openai/gpt-5,google/gemini-3.1-pro,anthropic/claude-4-sonnet \
  --runs 5 --fresh
```

### Report format

`results/part2_llm_eval_report.md` is laid out as follows:

**Per model section:**

1. **📊 Summary** — at the top of each model's block:
   - Section 1 (*Accuracy*): a **non-ceiling Δacc** headline that excludes
     levels where control already hits ≥ 90% (i.e. levels where CFLT has
     no room to improve and would dilute the verdict). The verdict against
     doc §5.2's `+15-20pp` prediction is evaluated on this non-ceiling
     number, not on the overall average. Per-level rows are marked
     **🔒 saturated** or **📈 informative**.
   - Section 2 (*Token Cost*): `prompt_tokens`, `completion_tokens`, and
     `total_tokens` each with their own verdict against doc §5.2's
     `-30 to -50%` prediction.
   - Confidence indicator (🔴 LOW / 🟡 MEDIUM / 🟢 HIGH) based on N and
     case count.
   - Data-driven recommended next steps (test other language, second
     model, etc.).
2. **Per-case table** — `Acc Ctrl`, `Acc CFLT`, `Δacc`, prompt-tokens
   (control/experimental), completion-tokens (control/experimental). Means
   carry their standard deviation across the N repeats.
3. **Aggregate-by-level table** — averages over each level's cases.
4. **Overall accuracy delta** — the diluted headline number, kept for
   transparency but de-emphasized in favor of the non-ceiling figure.

**Cross-Model Comparison section** (appears only when ≥ 2 models are
present in the raw file):

- **Accuracy table** — one row per model showing informative levels,
  saturated levels, and the non-ceiling Δacc with its verdict. Answers
  *"does CFLT's primacy effect generalize across models?"* directly.
- **Per-level accuracy heatmap** — control/experimental for each model
  side by side, with 🔒/📈 markers so you can spot quickly which model
  was saturated where.
- **Token cost direction** — prompt Δ%, completion Δ%, total Δ% per
  model. Reveals e.g. "GPT-5 spends more completion tokens under CFLT but
  Gemini doesn't" patterns.

Raw per-run output is preserved in `results/part2_eval_raw.json` for audit.

---

## Reading the results

The doc's predictions (§5.2) are:

- ≥30–50% reduction in syntactic-filler tokens
- 15–20% accuracy gain on long-context / distractor tasks

The benchmark is set up so these can either **confirm** or **falsify** that:

- **L1/L2** likely show near-ceiling accuracy in both arms with modest token
  differences — this *cannot* support a strong CFLT claim and shouldn't be
  read as such.
- **L3/L4** are where a real CFLT effect should show up — if `Δacc` on L4 is
  near zero across multiple frontier models, that is direct evidence against
  the primacy claim.

Treat reports across **at least three frontier-class models** before drawing
any conclusion about CFLT itself; a single model's idiosyncrasy is not the
theory's verdict.

---

## Adding cases or models

- **New case.** Append to `dataset.json → test_cases`. Required fields:
  `id`, `level`, `language`, `category`, `utterance_control`,
  `utterance_cflt`, `ground_truth`. If you introduce a new canonical value,
  add its surface forms to `metadata.value_synonyms[field][value]` — do not
  bury synonyms in code.
- **New model.** Add to `MODELS_CONFIG` in `utils.py` with the OpenAI-compatible
  base URL and the appropriate env-var lookup for the API key.

## Sanity check before a real run

```bash
cd scripts/llm_eval
python -c "
import json
from utils import compare_extraction
ds = json.load(open('dataset.json', encoding='utf-8'))
ka, vs = ds['metadata']['key_aliases'], ds['metadata']['value_synonyms']
bad = [c['id'] for c in ds['test_cases']
       if not compare_extraction(c['ground_truth'], c['ground_truth'], ka, vs)]
print('round-trip failures:', bad or 'none')
"
```

A non-empty list means a case's `ground_truth` value is missing from
`metadata.value_synonyms` — fix the synonym table before running the model.
