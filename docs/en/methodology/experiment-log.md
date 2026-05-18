# Experiment Log & Benchmarks

This page tracks the empirical validation of Core-First Language Theory (CFLT) through various model benchmarks and human-alignment tests.

## Historical Runs

Detailed reports for each experiment run are archived in the project repository.

| Date / Tag | Focus Area | Key Results |
| :--- | :--- | :--- |
| **2026-05-17** | Full Benchmark | Part I (DX 88%): DeepSeek-v4-pro → GPT-5. Part II (5-model expansion): GPT-5, Gemini 3 Flash, Qwen 3.5 Plus, DeepSeek v4 Pro, Claude 3.5 Sonnet. L3 universal (5/5 reach 100% CFLT). |

## Data & Reproducibility

Full raw data (`.json`) and detailed markdown reports for each run can be found in the [experiment-history/](https://github.com/corefirst/cflt/tree/main/experiment-history) directory of our GitHub repository.

To reproduce a historical snapshot:
```bash
cp experiment-history/2026-05-17/part2_eval_raw.json results/part2_eval_raw.json
python scripts/llm_eval/part2_llm_cflt_eval.py --rejudge
```
