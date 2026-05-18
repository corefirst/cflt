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
| [2026-05-17](2026-05-17/) | [Part I (DX 88%)](2026-05-17/part1_eval_report.md): DeepSeek-v4-pro → GPT-5. | [Part II (+22–44pp)](2026-05-17/part2_llm_eval_report.md): 5-model expansion (GPT-5, Gemini 3 Flash, Qwen 3.5 Plus, DeepSeek v4 Pro, Claude Sonnet 4.6). L3 universal (5/5 reach 100% CFLT). L4 regression confined to DeepSeek alone. |

## Reproducing from a historical snapshot

```bash
cp experiment-history/2026-05-17/part2_eval_raw.json results/part2_eval_raw.json
python scripts/llm_eval/part2_llm_cflt_eval.py --rejudge
```
