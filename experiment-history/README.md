# Experiment History

This directory archives benchmark runs for the CFLT evaluation suite. Each run is
a dated snapshot so researchers can review historical results and track how accuracy
evolves as the dataset, synonyms, or production prompt changes.

## Directory structure

```
experiment-history/
  YYYY-MM-DD/          ← one folder per run date
    part1_eval_report.md
    part1_eval_raw.json
    part2_llm_eval_report.md
    part2_eval_raw.json
```

File names are kept identical to what the scripts write into `results/`, so `.json`
files can be dropped back into `results/` and used directly with `--rejudge`.

## How to archive a new run

```bash
mkdir -p experiment-history/YYYY-MM-DD
cp results/part1_eval_report.md   experiment-history/YYYY-MM-DD/
cp results/part1_eval_raw.json    experiment-history/YYYY-MM-DD/
cp results/part2_llm_eval_report.md experiment-history/YYYY-MM-DD/
cp results/part2_eval_raw.json      experiment-history/YYYY-MM-DD/
```

Then commit the new directory.

## Index

| Date / Tag | Part I — transformer (DX) | Part II — models (non-ceiling Δacc) |
| :-- | :-- | :-- |
| [2026-05-17](2026-05-17/part1_eval_report.md) | deepseek-v4-pro → gpt-5, DX 88% (stable ~96%) | 4-model baseline: gpt-5 / gemini-3-flash / qwen3.5-plus / deepseek-v4-pro, N=3, L3 +22–44pp |
| [2026-05-17-claude](2026-05-17-claude/part2_llm_eval_report.md) | (Part II only — Part I unchanged from 2026-05-17 snapshot) | 5-model expansion: baseline + anthropic/claude-sonnet-4-6 via OpenRouter. L3 universal (5/5 reach 100% CFLT; +22 to +44pp). L4 −11pp regression now confined to DeepSeek alone. |

## Reproducing from a historical snapshot

```bash
cp experiment-history/2026-05-17/part2_eval_raw.json results/part2_eval_raw.json
python scripts/llm_eval/part2_llm_cflt_eval.py --rejudge
```
