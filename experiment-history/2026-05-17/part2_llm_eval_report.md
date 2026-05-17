# CFLT Part II — LLM Extraction Evaluation

**Generated:** 2026-05-16 19:23:42  
**Models:** `openai/gpt-5`, `google/gemini-3-flash-preview`, `qwen/qwen3.5-plus`, `deepseek/deepseek-v4-pro`  
**Runs per arm:** 3  
**Metric A:** extraction accuracy (1.0 = JSON matches ground truth under metadata synonyms)  
**Metric B:** prompt_tokens and completion_tokens (reported separately, never merged)


## Model: `openai/gpt-5`

### 📊 Summary

#### 1. 结果正确性 / Accuracy

**Headline:** ✅ On non-saturated cases (L3), CFLT improved accuracy by **+38.9pp** (61% → 100%); L1, L2, L4 ceiling-saturated

| Scope | Control | CFLT | Δ | Verdict (vs. doc §5.2 prediction) |
| :-- | :-- | :-- | :-- | :-- |
| **Non-ceiling (L3, 6 cases)** | **61%** | **100%** | **+38.9pp** | **✅ Supported (+38.9pp ≥ predicted +15pp on informative cases)** |
| Overall (24 cases) | 90% | 100% | +9.7pp | *(diluted by saturated levels)* |
| L1 (6 cases) | 100% | 100% | +0.0pp | 🔒 saturated |
| L2 (6 cases) | 100% | 100% | +0.0pp | 🔒 saturated |
| L3 (6 cases) | 61% | 100% | +38.9pp | 📈 informative |
| L4 (6 cases) | 100% | 100% | +0.0pp | 🔒 saturated |

#### 2. Token 消耗对比 / Token Cost

| Metric | Control | CFLT | Δ | Verdict |
| :-- | :-- | :-- | :-- | :-- |
| Prompt tokens (mean / case) | 112 | 110 | **-1.5%** | ⚠️ Weak (-1.5%; far below predicted -30 to -50%) |
| Completion tokens (mean / case) | 575 | 579 | **+0.7%** | ➖ No meaningful change (+0.7%) |
| **Total tokens (mean / case)** | **687** | **689** | **+0.3%** | ➖ No meaningful change in total tokens (+0.3%) |

**Confidence:** 🟢 **HIGH** — N=3, 24 cases (144 calls): adequate for cross-model comparison

**Recommended next steps:**
  1. re-run on a second frontier model (e.g. `--models google/gemini-3.1-pro` or `anthropic/claude-4-sonnet`) — a single-model result is anecdote, not evidence
  2. token-economy claim (doc §5.2 -30 to -50% prompt reduction) is **not testable with this dataset by design**: both arms have lexically identical content. To test it, add a third 'compressed CFLT' arm with slot tags and NULL fillers.

### Per-case results

| ID | L | Lang | Acc Ctrl | Acc CFLT | Δacc | Prompt Tok C/E | Compl Tok C/E |
| :-- | :- | :-- | :-- | :-- | :-- | :-- | :-- |
| EN_L1_01 | 1 | en | 1.00±0.00 | 1.00±0.00 | +0.00 | 86 / 87 | 295 / 338 |
| EN_L1_02 | 1 | en | 1.00±0.00 | 1.00±0.00 | +0.00 | 87 / 87 | 425 / 276 |
| EN_L1_03 | 1 | en | 1.00±0.00 | 1.00±0.00 | +0.00 | 85 / 85 | 275 / 339 |
| ZH_L1_01 | 1 | zh | 1.00±0.00 | 1.00±0.00 | +0.00 | 98 / 99 | 338 / 488 |
| ZH_L1_02 | 1 | zh | 1.00±0.00 | 1.00±0.00 | +0.00 | 96 / 97 | 340 / 489 |
| ZH_L1_03 | 1 | zh | 1.00±0.00 | 1.00±0.00 | +0.00 | 97 / 97 | 253 / 318 |
| EN_L2_01 | 2 | en | 1.00±0.00 | 1.00±0.00 | +0.00 | 103 / 105 | 424 / 512 |
| EN_L2_02 | 2 | en | 1.00±0.00 | 1.00±0.00 | +0.00 | 97 / 98 | 372 / 398 |
| EN_L2_03 | 2 | en | 1.00±0.00 | 1.00±0.00 | +0.00 | 98 / 99 | 353 / 438 |
| ZH_L2_01 | 2 | zh | 1.00±0.00 | 1.00±0.00 | +0.00 | 108 / 109 | 789 / 659 |
| ZH_L2_02 | 2 | zh | 1.00±0.00 | 1.00±0.00 | +0.00 | 107 / 109 | 742 / 886 |
| ZH_L2_03 | 2 | zh | 1.00±0.00 | 1.00±0.00 | +0.00 | 108 / 110 | 609 / 660 |
| EN_L3_01 | 3 | en | 0.00±0.00 | 1.00±0.00 | +1.00 | 126 / 125 | 816 / 718 |
| EN_L3_02 | 3 | en | 0.67±0.47 | 1.00±0.00 | +0.33 | 124 / 120 | 714 / 524 |
| EN_L3_03 | 3 | en | 1.00±0.00 | 1.00±0.00 | +0.00 | 121 / 117 | 500 / 500 |
| ZH_L3_01 | 3 | zh | 0.00±0.00 | 1.00±0.00 | +1.00 | 140 / 133 | 922 / 982 |
| ZH_L3_02 | 3 | zh | 1.00±0.00 | 1.00±0.00 | +0.00 | 132 / 126 | 906 / 1120 |
| ZH_L3_03 | 3 | zh | 1.00±0.00 | 1.00±0.00 | +0.00 | 141 / 131 | 823 / 630 |
| EN_L4_01 | 4 | en | 1.00±0.00 | 1.00±0.00 | +0.00 | 129 / 116 | 712 / 457 |
| EN_L4_02 | 4 | en | 1.00±0.00 | 1.00±0.00 | +0.00 | 118 / 117 | 650 / 611 |
| EN_L4_03 | 4 | en | 1.00±0.00 | 1.00±0.00 | +0.00 | 113 / 112 | 541 / 413 |
| ZH_L4_01 | 4 | zh | 1.00±0.00 | 1.00±0.00 | +0.00 | 126 / 120 | 477 / 631 |
| ZH_L4_02 | 4 | zh | 1.00±0.00 | 1.00±0.00 | +0.00 | 125 / 129 | 651 / 762 |
| ZH_L4_03 | 4 | zh | 1.00±0.00 | 1.00±0.00 | +0.00 | 125 / 121 | 863 / 735 |

### Aggregate by level

| Level | N cases | Acc Ctrl | Acc CFLT | Δacc | Prompt Tok C/E | Compl Tok C/E |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| L1 | 6 | 1.00 | 1.00 | +0.00 | 92 / 92 | 321 / 375 |
| L2 | 6 | 1.00 | 1.00 | +0.00 | 104 / 105 | 548 / 592 |
| L3 | 6 | 0.61 | 1.00 | +0.39 | 131 / 125 | 780 / 746 |
| L4 | 6 | 1.00 | 1.00 | +0.00 | 123 / 119 | 649 / 602 |

**Overall accuracy:** control=0.90 · cflt=1.00 · Δ=+0.10

## Model: `google/gemini-3-flash-preview`

### 📊 Summary

#### 1. 结果正确性 / Accuracy

**Headline:** ✅ On non-saturated cases (L3), CFLT improved accuracy by **+22.2pp** (78% → 100%); L1, L2, L4 ceiling-saturated

| Scope | Control | CFLT | Δ | Verdict (vs. doc §5.2 prediction) |
| :-- | :-- | :-- | :-- | :-- |
| **Non-ceiling (L3, 6 cases)** | **78%** | **100%** | **+22.2pp** | **✅ Supported (+22.2pp ≥ predicted +15pp on informative cases)** |
| Overall (24 cases) | 93% | 99% | +5.6pp | *(diluted by saturated levels)* |
| L1 (6 cases) | 100% | 100% | +0.0pp | 🔒 saturated |
| L2 (6 cases) | 100% | 100% | +0.0pp | 🔒 saturated |
| L3 (6 cases) | 78% | 100% | +22.2pp | 📈 informative |
| L4 (6 cases) | 94% | 94% | +0.0pp | 🔒 saturated |

#### 2. Token 消耗对比 / Token Cost

| Metric | Control | CFLT | Δ | Verdict |
| :-- | :-- | :-- | :-- | :-- |
| Prompt tokens (mean / case) | 99 | 98 | **-1.4%** | ⚠️ Weak (-1.4%; far below predicted -30 to -50%) |
| Completion tokens (mean / case) | 35 | 36 | **+1.4%** | ➖ No meaningful change (+1.4%) |
| **Total tokens (mean / case)** | **135** | **134** | **-0.7%** | ➖ No meaningful change in total tokens (-0.7%) |

**Confidence:** 🟢 **HIGH** — N=3, 24 cases (144 calls): adequate for cross-model comparison

**Recommended next steps:**
  1. re-run on a second frontier model (e.g. `--models google/gemini-3.1-pro` or `anthropic/claude-4-sonnet`) — a single-model result is anecdote, not evidence
  2. token-economy claim (doc §5.2 -30 to -50% prompt reduction) is **not testable with this dataset by design**: both arms have lexically identical content. To test it, add a third 'compressed CFLT' arm with slot tags and NULL fillers.

### Per-case results

| ID | L | Lang | Acc Ctrl | Acc CFLT | Δacc | Prompt Tok C/E | Compl Tok C/E |
| :-- | :- | :-- | :-- | :-- | :-- | :-- | :-- |
| EN_L1_01 | 1 | en | 1.00±0.00 | 1.00±0.00 | +0.00 | 80 / 81 | 19 / 19 |
| EN_L1_02 | 1 | en | 1.00±0.00 | 1.00±0.00 | +0.00 | 81 / 81 | 20 / 20 |
| EN_L1_03 | 1 | en | 1.00±0.00 | 1.00±0.00 | +0.00 | 79 / 79 | 19 / 19 |
| ZH_L1_01 | 1 | zh | 1.00±0.00 | 1.00±0.00 | +0.00 | 80 / 81 | 21 / 21 |
| ZH_L1_02 | 1 | zh | 1.00±0.00 | 1.00±0.00 | +0.00 | 78 / 78 | 20 / 21 |
| ZH_L1_03 | 1 | zh | 1.00±0.00 | 1.00±0.00 | +0.00 | 78 / 78 | 20 / 20 |
| EN_L2_01 | 2 | en | 1.00±0.00 | 1.00±0.00 | +0.00 | 97 / 99 | 45 / 48 |
| EN_L2_02 | 2 | en | 1.00±0.00 | 1.00±0.00 | +0.00 | 91 / 92 | 39 / 39 |
| EN_L2_03 | 2 | en | 1.00±0.00 | 1.00±0.00 | +0.00 | 95 / 96 | 45 / 45 |
| ZH_L2_01 | 2 | zh | 1.00±0.00 | 1.00±0.00 | +0.00 | 90 / 93 | 44 / 48 |
| ZH_L2_02 | 2 | zh | 1.00±0.00 | 1.00±0.00 | +0.00 | 86 / 89 | 41 / 41 |
| ZH_L2_03 | 2 | zh | 1.00±0.00 | 1.00±0.00 | +0.00 | 90 / 93 | 44 / 44 |
| EN_L3_01 | 3 | en | 0.00±0.00 | 1.00±0.00 | +1.00 | 121 / 119 | 39 / 45 |
| EN_L3_02 | 3 | en | 1.00±0.00 | 1.00±0.00 | +0.00 | 119 / 115 | 43 / 43 |
| EN_L3_03 | 3 | en | 1.00±0.00 | 1.00±0.00 | +0.00 | 115 / 111 | 39 / 38 |
| ZH_L3_01 | 3 | zh | 0.67±0.47 | 1.00±0.00 | +0.33 | 114 / 111 | 42 / 45 |
| ZH_L3_02 | 3 | zh | 1.00±0.00 | 1.00±0.00 | +0.00 | 112 / 105 | 37 / 34 |
| ZH_L3_03 | 3 | zh | 1.00±0.00 | 1.00±0.00 | +0.00 | 120 / 114 | 43 / 42 |
| EN_L4_01 | 4 | en | 1.00±0.00 | 1.00±0.00 | +0.00 | 124 / 110 | 37 / 37 |
| EN_L4_02 | 4 | en | 1.00±0.00 | 1.00±0.00 | +0.00 | 113 / 113 | 40 / 40 |
| EN_L4_03 | 4 | en | 1.00±0.00 | 1.00±0.00 | +0.00 | 107 / 106 | 38 / 38 |
| ZH_L4_01 | 4 | zh | 1.00±0.00 | 1.00±0.00 | +0.00 | 104 / 98 | 36 / 37 |
| ZH_L4_02 | 4 | zh | 0.67±0.47 | 1.00±0.00 | +0.33 | 105 / 106 | 40 / 40 |
| ZH_L4_03 | 4 | zh | 1.00±0.00 | 0.67±0.47 | -0.33 | 103 / 100 | 39 / 40 |

### Aggregate by level

| Level | N cases | Acc Ctrl | Acc CFLT | Δacc | Prompt Tok C/E | Compl Tok C/E |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| L1 | 6 | 1.00 | 1.00 | +0.00 | 79 / 80 | 20 / 20 |
| L2 | 6 | 1.00 | 1.00 | +0.00 | 92 / 94 | 43 / 44 |
| L3 | 6 | 0.78 | 1.00 | +0.22 | 117 / 112 | 40 / 41 |
| L4 | 6 | 0.94 | 0.94 | +0.00 | 109 / 106 | 38 / 39 |

**Overall accuracy:** control=0.93 · cflt=0.99 · Δ=+0.06

## Model: `qwen/qwen3.5-plus`

### 📊 Summary

#### 1. 结果正确性 / Accuracy

**Headline:** ✅ On non-saturated cases (L2, L3), CFLT improved accuracy by **+22.2pp** (75% → 97%); L1, L4 ceiling-saturated

| Scope | Control | CFLT | Δ | Verdict (vs. doc §5.2 prediction) |
| :-- | :-- | :-- | :-- | :-- |
| **Non-ceiling (L2, L3, 12 cases)** | **75%** | **97%** | **+22.2pp** | **✅ Supported (+22.2pp ≥ predicted +15pp on informative cases)** |
| Overall (24 cases) | 86% | 97% | +10.4pp | *(diluted by saturated levels)* |
| L1 (6 cases) | 100% | 100% | +0.0pp | 🔒 saturated |
| L2 (6 cases) | 89% | 94% | +5.6pp | 📈 informative |
| L3 (6 cases) | 61% | 100% | +38.9pp | 📈 informative |
| L4 (6 cases) | 94% | 92% | -2.8pp | 🔒 saturated |

#### 2. Token 消耗对比 / Token Cost

| Metric | Control | CFLT | Δ | Verdict |
| :-- | :-- | :-- | :-- | :-- |
| Prompt tokens (mean / case) | 111 | 110 | **-1.1%** | ⚠️ Weak (-1.1%; far below predicted -30 to -50%) |
| Completion tokens (mean / case) | 3210 | 1978 | **-38.4%** | ✅ CFLT reduced completion tokens by 38.4% |
| **Total tokens (mean / case)** | **3320** | **2088** | **-37.1%** | ✅ CFLT reduced total tokens by 37.1% |

**Confidence:** 🟢 **HIGH** — N=3, 24 cases (144 calls): adequate for cross-model comparison

**Recommended next steps:**
  1. re-run on a second frontier model (e.g. `--models google/gemini-3.1-pro` or `anthropic/claude-4-sonnet`) — a single-model result is anecdote, not evidence
  2. token-economy claim (doc §5.2 -30 to -50% prompt reduction) is **not testable with this dataset by design**: both arms have lexically identical content. To test it, add a third 'compressed CFLT' arm with slot tags and NULL fillers.

### Per-case results

| ID | L | Lang | Acc Ctrl | Acc CFLT | Δacc | Prompt Tok C/E | Compl Tok C/E |
| :-- | :- | :-- | :-- | :-- | :-- | :-- | :-- |
| EN_L1_01 | 1 | en | 1.00±0.00 | 1.00±0.00 | +0.00 | 94 / 95 | 979 / 783 |
| EN_L1_02 | 1 | en | 1.00±0.00 | 1.00±0.00 | +0.00 | 95 / 95 | 527 / 833 |
| EN_L1_03 | 1 | en | 1.00±0.00 | 1.00±0.00 | +0.00 | 93 / 93 | 465 / 560 |
| ZH_L1_01 | 1 | zh | 1.00±0.00 | 1.00±0.00 | +0.00 | 90 / 91 | 699 / 1054 |
| ZH_L1_02 | 1 | zh | 1.00±0.00 | 1.00±0.00 | +0.00 | 90 / 90 | 631 / 684 |
| ZH_L1_03 | 1 | zh | 1.00±0.00 | 1.00±0.00 | +0.00 | 89 / 90 | 621 / 875 |
| EN_L2_01 | 2 | en | 1.00±0.00 | 0.67±0.47 | -0.33 | 111 / 113 | 559 / 14858 |
| EN_L2_02 | 2 | en | 1.00±0.00 | 1.00±0.00 | +0.00 | 105 / 106 | 2274 / 1176 |
| EN_L2_03 | 2 | en | 1.00±0.00 | 1.00±0.00 | +0.00 | 109 / 110 | 859 / 911 |
| ZH_L2_01 | 2 | zh | 1.00±0.00 | 1.00±0.00 | +0.00 | 99 / 102 | 948 / 721 |
| ZH_L2_02 | 2 | zh | 0.33±0.47 | 1.00±0.00 | +0.67 | 98 / 100 | 7975 / 1043 |
| ZH_L2_03 | 2 | zh | 1.00±0.00 | 1.00±0.00 | +0.00 | 101 / 104 | 1474 / 1244 |
| EN_L3_01 | 3 | en | 0.00±0.00 | 1.00±0.00 | +1.00 | 136 / 135 | 4212 / 916 |
| EN_L3_02 | 3 | en | 1.00±0.00 | 1.00±0.00 | +0.00 | 132 / 128 | 3109 / 902 |
| EN_L3_03 | 3 | en | 1.00±0.00 | 1.00±0.00 | +0.00 | 129 / 125 | 1094 / 780 |
| ZH_L3_01 | 3 | zh | 0.00±0.00 | 1.00±0.00 | +1.00 | 125 / 121 | 5236 / 949 |
| ZH_L3_02 | 3 | zh | 1.00±0.00 | 1.00±0.00 | +0.00 | 118 / 113 | 1463 / 3602 |
| ZH_L3_03 | 3 | zh | 0.67±0.47 | 1.00±0.00 | +0.33 | 123 / 119 | 17092 / 2821 |
| EN_L4_01 | 4 | en | 1.00±0.00 | 1.00±0.00 | +0.00 | 137 / 124 | 904 / 1229 |
| EN_L4_02 | 4 | en | 1.00±0.00 | 1.00±0.00 | +0.00 | 127 / 126 | 1214 / 793 |
| EN_L4_03 | 4 | en | 1.00±0.00 | 1.00±0.00 | +0.00 | 121 / 120 | 736 / 539 |
| ZH_L4_01 | 4 | zh | 0.67±0.47 | 1.00±0.00 | +0.33 | 113 / 107 | 16129 / 1030 |
| ZH_L4_02 | 4 | zh | 1.00±0.00 | 1.00±0.00 | +0.00 | 115 / 115 | 1828 / 2394 |
| ZH_L4_03 | 4 | zh | 1.00±0.00 | 0.50±0.50 | -0.50 | 111 / 111 | 6000 / 6775 |

### Aggregate by level

| Level | N cases | Acc Ctrl | Acc CFLT | Δacc | Prompt Tok C/E | Compl Tok C/E |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| L1 | 6 | 1.00 | 1.00 | +0.00 | 92 / 92 | 654 / 798 |
| L2 | 6 | 0.89 | 0.94 | +0.06 | 104 / 106 | 2348 / 3326 |
| L3 | 6 | 0.61 | 1.00 | +0.39 | 127 / 124 | 5368 / 1662 |
| L4 | 6 | 0.94 | 0.92 | -0.03 | 121 / 117 | 4469 / 2127 |

**Overall accuracy:** control=0.86 · cflt=0.97 · Δ=+0.10

## Model: `deepseek/deepseek-v4-pro`

### 📊 Summary

#### 1. 结果正确性 / Accuracy

**Headline:** ✅ On non-saturated cases (L3, L4), CFLT improved accuracy by **+16.7pp** (69% → 86%); L1, L2 ceiling-saturated

| Scope | Control | CFLT | Δ | Verdict (vs. doc §5.2 prediction) |
| :-- | :-- | :-- | :-- | :-- |
| **Non-ceiling (L3, L4, 12 cases)** | **69%** | **86%** | **+16.7pp** | **✅ Supported (+16.7pp ≥ predicted +15pp on informative cases)** |
| Overall (24 cases) | 83% | 92% | +8.3pp | *(diluted by saturated levels)* |
| L1 (6 cases) | 100% | 100% | +0.0pp | 🔒 saturated |
| L2 (6 cases) | 94% | 94% | +0.0pp | 🔒 saturated |
| L3 (6 cases) | 56% | 100% | +44.4pp | 📈 informative |
| L4 (6 cases) | 83% | 72% | -11.1pp | 📈 informative |

#### 2. Token 消耗对比 / Token Cost

| Metric | Control | CFLT | Δ | Verdict |
| :-- | :-- | :-- | :-- | :-- |
| Prompt tokens (mean / case) | 118 | 117 | **-1.1%** | ⚠️ Weak (-1.1%; far below predicted -30 to -50%) |
| Completion tokens (mean / case) | 218 | 190 | **-12.5%** | ✅ CFLT reduced completion tokens by 12.5% |
| **Total tokens (mean / case)** | **336** | **307** | **-8.5%** | ✅ CFLT reduced total tokens by 8.5% |

**Confidence:** 🟢 **HIGH** — N=3, 24 cases (144 calls): adequate for cross-model comparison

**Recommended next steps:**
  1. re-run on a second frontier model (e.g. `--models google/gemini-3.1-pro` or `anthropic/claude-4-sonnet`) — a single-model result is anecdote, not evidence
  2. token-economy claim (doc §5.2 -30 to -50% prompt reduction) is **not testable with this dataset by design**: both arms have lexically identical content. To test it, add a third 'compressed CFLT' arm with slot tags and NULL fillers.

### Per-case results

| ID | L | Lang | Acc Ctrl | Acc CFLT | Δacc | Prompt Tok C/E | Compl Tok C/E |
| :-- | :- | :-- | :-- | :-- | :-- | :-- | :-- |
| EN_L1_01 | 1 | en | 1.00±0.00 | 1.00±0.00 | +0.00 | 101 / 102 | 252 / 231 |
| EN_L1_02 | 1 | en | 1.00±0.00 | 1.00±0.00 | +0.00 | 102 / 102 | 86 / 82 |
| EN_L1_03 | 1 | en | 1.00±0.00 | 1.00±0.00 | +0.00 | 100 / 100 | 80 / 66 |
| ZH_L1_01 | 1 | zh | 1.00±0.00 | 1.00±0.00 | +0.00 | 98 / 99 | 139 / 70 |
| ZH_L1_02 | 1 | zh | 1.00±0.00 | 1.00±0.00 | +0.00 | 99 / 99 | 102 / 103 |
| ZH_L1_03 | 1 | zh | 1.00±0.00 | 1.00±0.00 | +0.00 | 97 / 98 | 59 / 97 |
| EN_L2_01 | 2 | en | 1.00±0.00 | 1.00±0.00 | +0.00 | 118 / 120 | 127 / 132 |
| EN_L2_02 | 2 | en | 1.00±0.00 | 1.00±0.00 | +0.00 | 112 / 113 | 136 / 152 |
| EN_L2_03 | 2 | en | 1.00±0.00 | 1.00±0.00 | +0.00 | 113 / 114 | 171 / 135 |
| ZH_L2_01 | 2 | zh | 0.67±0.47 | 1.00±0.00 | +0.33 | 109 / 112 | 175 / 135 |
| ZH_L2_02 | 2 | zh | 1.00±0.00 | 0.67±0.47 | -0.33 | 105 / 107 | 128 / 180 |
| ZH_L2_03 | 2 | zh | 1.00±0.00 | 1.00±0.00 | +0.00 | 105 / 108 | 183 / 237 |
| EN_L3_01 | 3 | en | 0.00±0.00 | 1.00±0.00 | +1.00 | 141 / 140 | 400 / 277 |
| EN_L3_02 | 3 | en | 0.33±0.47 | 1.00±0.00 | +0.67 | 140 / 136 | 400 / 235 |
| EN_L3_03 | 3 | en | 1.00±0.00 | 1.00±0.00 | +0.00 | 136 / 132 | 235 / 260 |
| ZH_L3_01 | 3 | zh | 0.33±0.47 | 1.00±0.00 | +0.67 | 130 / 126 | 330 / 132 |
| ZH_L3_02 | 3 | zh | 1.00±0.00 | 1.00±0.00 | +0.00 | 126 / 121 | 159 / 375 |
| ZH_L3_03 | 3 | zh | 0.67±0.47 | 1.00±0.00 | +0.33 | 135 / 129 | 175 / 186 |
| EN_L4_01 | 4 | en | 1.00±0.00 | 1.00±0.00 | +0.00 | 144 / 131 | 462 / 218 |
| EN_L4_02 | 4 | en | 0.67±0.47 | 1.00±0.00 | +0.33 | 134 / 133 | 576 / 155 |
| EN_L4_03 | 4 | en | 1.00±0.00 | 0.67±0.47 | -0.33 | 128 / 127 | 267 / 342 |
| ZH_L4_01 | 4 | zh | 1.00±0.00 | 0.67±0.47 | -0.33 | 121 / 115 | 157 / 189 |
| ZH_L4_02 | 4 | zh | 1.00±0.00 | 1.00±0.00 | +0.00 | 123 / 123 | 165 / 177 |
| ZH_L4_03 | 4 | zh | 0.33±0.47 | 0.00±0.00 | -0.33 | 118 / 118 | 260 / 405 |

### Aggregate by level

| Level | N cases | Acc Ctrl | Acc CFLT | Δacc | Prompt Tok C/E | Compl Tok C/E |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| L1 | 6 | 1.00 | 1.00 | +0.00 | 100 / 100 | 120 / 108 |
| L2 | 6 | 0.94 | 0.94 | +0.00 | 110 / 112 | 153 / 162 |
| L3 | 6 | 0.56 | 1.00 | +0.44 | 135 / 131 | 283 / 244 |
| L4 | 6 | 0.83 | 0.72 | -0.11 | 128 / 124 | 315 / 247 |

**Overall accuracy:** control=0.83 · cflt=0.92 · Δ=+0.08

## 🔬 Cross-Model Comparison

_Same dataset, same instruction, same case set — the only thing varying is the model. If CFLT's primacy effect is a real LLM property (not GPT-5-specific), it should show the same pattern across rows._

### Accuracy (non-ceiling Δacc)

| Model | Informative levels | Saturated levels | Non-ceiling Ctrl | Non-ceiling CFLT | Δacc | Verdict |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| `openai/gpt-5` | L3 | L1, L2, L4 | 61% | 100% | **+38.9pp** | ✅ Supported |
| `google/gemini-3-flash-preview` | L3 | L1, L2, L4 | 78% | 100% | **+22.2pp** | ✅ Supported |
| `qwen/qwen3.5-plus` | L2, L3 | L1, L4 | 75% | 97% | **+22.2pp** | ✅ Supported |
| `deepseek/deepseek-v4-pro` | L3, L4 | L1, L2 | 69% | 86% | **+16.7pp** | ✅ Supported |

### Per-level accuracy across models

| Level | `openai/gpt-5` (Ctrl / CFLT) | `google/gemini-3-flash-preview` (Ctrl / CFLT) | `qwen/qwen3.5-plus` (Ctrl / CFLT) | `deepseek/deepseek-v4-pro` (Ctrl / CFLT) |
| :-- | :-- | :-- | :-- | :-- |
| L1 | 100% / 100% 🔒 (+0pp) | 100% / 100% 🔒 (+0pp) | 100% / 100% 🔒 (+0pp) | 100% / 100% 🔒 (+0pp) |
| L2 | 100% / 100% 🔒 (+0pp) | 100% / 100% 🔒 (+0pp) | 89% / 94% 📈 (+6pp) | 94% / 94% 🔒 (+0pp) |
| L3 | 61% / 100% 📈 (+39pp) | 78% / 100% 📈 (+22pp) | 61% / 100% 📈 (+39pp) | 56% / 100% 📈 (+44pp) |
| L4 | 100% / 100% 🔒 (+0pp) | 94% / 94% 🔒 (+0pp) | 94% / 92% 🔒 (-3pp) | 83% / 72% 📈 (-11pp) |

_🔒 = control already at ceiling (no room for CFLT to improve); 📈 = informative level._

### Token cost direction

| Model | Prompt Δ | Completion Δ | Total Δ |
| :-- | :-- | :-- | :-- |
| `openai/gpt-5` | -1.5% | +0.7% | +0.3% |
| `google/gemini-3-flash-preview` | -1.4% | +1.4% | -0.7% |
| `qwen/qwen3.5-plus` | -1.1% | -38.4% | -37.1% |
| `deepseek/deepseek-v4-pro` | -1.1% | -12.5% | -8.5% |

