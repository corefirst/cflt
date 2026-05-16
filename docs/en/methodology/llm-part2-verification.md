# LLM Prompting Verification: CFLT Part II Experiment Report

> **Version:** 1.0.0  
> **Date:** 2026-05-16  
> **Dataset:** `scripts/llm_eval/dataset.json` v2.0.0  
> **Script:** `scripts/llm_eval/part2_llm_cflt_eval.py`  
> **Raw data:** `results/part2_eval_raw.json`  
> **Related doc:** [`llm-prompting.md`](./llm-prompting.md) §5.2, §6

---

## 1. Experimental Design

### 1.1 Core Control

This experiment validates the ablation proposed in `llm-prompting.md §6`. **The only variable is clause order** — both arms use identical lexical content with no compression or tagging:

- **Control arm:** Natural word order, typically reason-first.  
- **CFLT arm:** Same content reordered as Core → Reason → Space → Time. No literal `[CORE]` tags.

The **system prompt contains no ground-truth values or field hints**, ensuring that accuracy measures true extraction ability rather than schema compliance.

### 1.2 Dataset Structure

24 cases across 4 difficulty levels (L1–L4), 12 English and 12 Chinese (3 scenarios per level × language):

| Level | Test focus | Expected signal source |
| :-- | :-- | :-- |
| **L1** | Single action, 2 fields | Too simple — both arms saturate, no discriminability |
| **L2** | 4 fields (location + time) | Same — strong models saturate |
| **L3** | 4 fields with distractor clauses | **Primary primacy test** — distractors cause core action to be missed in natural order |
| **L4** | Multiple candidate actions, final decision | Secondary test — see §2.3 for results |

Each case runs N=3 times (temperature=0); report shows mean±std.

### 1.3 Models Tested

| Tag | Type | Provider |
| :-- | :-- | :-- |
| `openai/gpt-5` | Reasoning model | OpenAI |
| `google/gemini-3-flash-preview` | Non-thinking | Google |
| `qwen/qwen3.5-plus` | Thinking model | Alibaba |
| `deepseek/deepseek-v4-pro` | Non-thinking | DeepSeek |

---

## 2. Key Findings

### 2.1 L3 Primacy Effect: CFLT Reaches 100% Across All 4 Models (Main Finding)

| Model | L3 Control | L3 CFLT | Δ | §5.2 Prediction (+15–20pp) |
| :-- | :-- | :-- | :-- | :-- |
| GPT-5 | 61% | **100%** | **+39pp** | ✅ Exceeds |
| Gemini 3 Flash | 78% | **100%** | **+22pp** | ✅ Exceeds |
| Qwen3.5-Plus | 61% | **100%** | **+39pp** | ✅ Exceeds |
| DeepSeek V4 Pro | 56% | **100%** | **+44pp** | ✅ Exceeds |

The variation in control accuracy (56–78%) reflects each model's susceptibility to distractor clauses. CFLT's correction is complete and universal. **L1/L2/L4 control arms are already near-ceiling, providing no signal; L3 is the only informative level.**

This result holds across four companies and three model architectures (reasoning, thinking, non-thinking), constituting strong empirical support for the primacy hypothesis in `llm-prompting.md §2.1`.

### 2.2 Token Mechanism: Thinking Model Reasoning Overhead Reduction

| Model | Prompt Δ | Completion Δ | Total Δ |
| :-- | :-- | :-- | :-- |
| GPT-5 | −1.5% | +0.7% | +0.3% |
| Gemini 3 Flash | −1.4% | +1.4% | −0.7% |
| Qwen3.5-Plus | −1.1% | **−38.4%** | **−37.1%** |
| DeepSeek V4 Pro | −1.1% | **−12.5%** | **−8.5%** |

Qwen3.5-Plus completion tokens dropped 38.4%; DeepSeek V4 Pro dropped 12.5%. **Qwen's total reduction (−37.1%) falls within the §5.2 projected −30–50% range, but the mechanism differs from the original prediction:**

- **Original mechanism assumed:** CFLT compresses prompt → fewer input tokens  
- **Observed mechanism:** CFLT places the core action at position 0 → thinking models converge faster → shorter reasoning traces

Illustrative case (Qwen, ZH_L3_03):
- Control: 17,092 completion tokens (lengthy confused reasoning, wrong answer)  
- CFLT: 2,821 completion tokens (focused reasoning, correct — 6× reduction)

For non-thinking models (Gemini Flash), completion tokens are in noise range (±1.4%), as expected.

### 2.3 L4 Boundary: CFLT Is Mildly Harmful on Multi-Action Decision Cases

| Model | L4 Status | L4 Δ |
| :-- | :-- | :-- |
| GPT-5 | 🔒 Ceiling (100%/100%) | 0 |
| Gemini 3 Flash | 🔒 Ceiling (94%/94%) | 0 |
| Qwen3.5-Plus | 🔒 Near-ceiling (94%/92%) | −3pp (noise) |
| DeepSeek V4 Pro | 📈 Real signal (83%/72%) | **−11pp** |

L4 cases structure: multiple candidate actions, final decision stated at the end of the natural-order utterance. Control's narrative sequence (alternatives → final choice) provides a reasoning scaffold. CFLT front-loads the conclusion, removing that scaffold. DeepSeek V4 Pro is sensitive to this; others are at ceiling.

> **Implication for §3.1 "When NOT to use the two-step workflow":**  
> In cases where user input lists multiple options before a final decision, CFLT reordering may mildly reduce accuracy in non-thinking models (~−10pp). This is opposite to the positive effect on distractor cases (L3). Empirically test before deploying CFLT in this scenario type.

---

## 3. Full Data Tables

### 3.1 Cross-Model Non-Ceiling Δacc

| Model | Informative levels | Non-ceiling Ctrl | Non-ceiling CFLT | Δacc | Verdict |
| :-- | :-- | :-- | :-- | :-- | :-- |
| `openai/gpt-5` | L3 | 61% | 100% | **+38.9pp** | ✅ Supported |
| `google/gemini-3-flash-preview` | L3 | 78% | 100% | **+22.2pp** | ✅ Supported |
| `qwen/qwen3.5-plus` | L2, L3 | 75% | 97% | **+22.2pp** | ✅ Supported |
| `deepseek/deepseek-v4-pro` | L3, L4 | 69% | 86% | **+16.7pp** | ✅ Supported |

### 3.2 Per-Level Accuracy Heatmap

| Level | GPT-5 | Gemini Flash | Qwen3.5 | DeepSeek V4 |
| :-- | :-- | :-- | :-- | :-- |
| L1 | 100% / 100% 🔒 | 100% / 100% 🔒 | 100% / 100% 🔒 | 100% / 100% 🔒 |
| L2 | 100% / 100% 🔒 | 100% / 100% 🔒 | 89% / 94% 📈 | 94% / 94% 🔒 |
| L3 | 61% / 100% 📈 | 78% / 100% 📈 | 61% / 100% 📈 | 56% / 100% 📈 |
| L4 | 100% / 100% 🔒 | 94% / 94% 🔒 | 94% / 92% 🔒 | 83% / 72% 📈 |

_🔒 = control already at ceiling, CFLT effect untestable; 📈 = informative level._

### 3.3 Token Cost Summary (mean per case)

| Model | Ctrl Prompt | CFLT Prompt | Ctrl Compl | CFLT Compl |
| :-- | :-- | :-- | :-- | :-- |
| GPT-5 | 112 | 110 | 575 | 579 |
| Gemini Flash | 99 | 98 | 35 | 36 |
| Qwen3.5-Plus | 111 | 110 | 3210 | 1978 |
| DeepSeek V4 Pro | 118 | 117 | 218 | 190 |

---

## 4. Verdict Against llm-prompting.md Claims

| Section | Claim | Experimental result | Verdict |
| :-- | :-- | :-- | :-- |
| §2.1 Primacy effect | Core-first → attention aligned → more accurate extraction | 4/4 models: L3 CFLT +22 to +44pp | ✅ **Strongly confirmed** |
| §5.2 Accuracy prediction | +15–20pp on long-context / distractor tasks | All 4 models exceed +15pp | ✅ **Confirmed (all exceeded)** |
| §5.2 Token saving | −30–50% "syntactic fluff" tokens | Prompt: −1% (not confirmed); Thinking completion: −38% (Qwen) | ⚠️ **Different mechanism; numerically holds for thinking models** |
| §3.1 Single-call vs two-step | Modern frontier models may not need a pre-processor | L3 strongly needs CFLT (ctrl 56–78% vs cflt 100%); L4 mildly harmed | ⚠️ **Task-type dependent: distractor tasks benefit; multi-action cases, use caution** |

---

## 5. Methodology Notes and Limitations

### 5.1 Dataset Limitations

1. **Token-compression claim is untestable:** Both arms use identical lexical content, so prompt token compression cannot be measured. To test §4.1's token economy claim, a third "compressed CFLT" arm (with NULL fillers and explicit slot labels) is required.

2. **L1/L2 cases are too simple:** Strong models saturate both arms with no discriminability. Future experiments should use L3-style distractor structures as the primary test format.

3. **ZH_L3_02 ground-truth correction:** The original GT included `location: bed_7`, but in Chinese "7床的病人" (the patient in bed 7) functions as a patient identifier rather than an action location — Chinese models consistently omit it, and are semantically correct to do so. The GT was updated to remove location for the Chinese case (EN_L3_02 was kept as-is because English models reliably extract "bed 7" as a location).

### 5.2 Synonym Table Evolution

Several evaluator gaps were discovered and fixed during the experiment (see git history):

- English time expression word-order variants ("6 PM today" ↔ "today at 6 PM")
- Hyphen normalization ("5th-floor" → "5th floor")
- ISO date prefix stripping ("2026-05-16 18:00" → "18:00")
- Chinese digit–measure-word spaces (Qwen3 style "5 楼" → "5楼")
- Singular/plural variants ("backup checkout counter" vs "counters")

All fixes were applied retroactively via `--rejudge` (no additional API calls).

### 5.3 Qwen Data Completeness

On the first Qwen run, EN_L3_01 and ZH_L3_01 control arms failed entirely due to API connection errors. The block was re-run with `--force` to obtain complete data; all figures in this report use the complete N=3 run.

---

## 6. Conclusion

This experiment provides the first multi-model empirical evidence for the primacy hypothesis in `llm-prompting.md §2.1`:

1. **On distractor cases (L3), CFLT raises accuracy to 100% across four models from four different providers**, while natural word-order control sits at 56–78%. This holds across a reasoning model (GPT-5), a thinking model (Qwen3.5), and two non-thinking models (Gemini Flash, DeepSeek V4 Pro).

2. **For thinking models, CFLT simultaneously reduces reasoning overhead:** Qwen3.5-Plus completion tokens dropped 38.4%, DeepSeek V4 Pro dropped 12.5%. The mechanism is that core-first structure enables faster convergence, shortening thinking traces rather than shortening input length.

3. **On multi-action decision cases (L4), CFLT is mildly harmful for some models (DeepSeek −11pp).** Deploy cautiously in this scenario type.

4. **The §5.2 −30–50% token saving claim does not hold at the prompt level** (untestable with identical-content design); it holds numerically at the completion level for thinking models (−37%), with a different mechanism than originally anticipated.

> **Reproduce:** `python scripts/llm_eval/part2_llm_cflt_eval.py --runs 3` — the report is generated into `results/` (gitignored; visible after running locally).
