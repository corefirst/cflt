# Experiment Log & Benchmarks

This page tracks the empirical validation of Core-First Language Theory (CFLT) through various model benchmarks and human-alignment tests.

## Historical Runs

Detailed reports for each experiment run are archived in the project repository.

| Date / Tag | Focus Area | Key Results |
| :--- | :--- | :--- |
| **2026-05-17** | Human-CFLT Alignment | deepseek-v4-pro → gpt-5, DX 88% (stable ~96%) |
| **2026-05-17** | LLM Self-Consistency | 4-model baseline: gpt-5 / gemini-3-flash / qwen3.5-plus / deepseek-v4-pro, N=3, L3 +22–44pp |
| **2026-05-17-claude** | Claude Extension | 5-model expansion: baseline + claude-sonnet-4-6. L3 universal (5/5 reach 100% CFLT). |

## Data & Reproducibility

Full raw data (`.json`) and detailed markdown reports for each run can be found in the [experiment-history/](https://github.com/corefirst/cflt/tree/main/experiment-history) directory of our GitHub repository.

To reproduce a historical snapshot:
```bash
cp experiment-history/2026-05-17/part2_eval_raw.json results/part2_eval_raw.json
python scripts/llm_eval/part2_llm_cflt_eval.py --rejudge
```
