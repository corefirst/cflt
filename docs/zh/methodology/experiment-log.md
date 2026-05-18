# 实验日志与基准测试

本页面记录了通过各种模型基准测试和人类对齐测试对核心优先语言理论（CFLT）进行的实证验证。

## 历史运行记录

每次实验运行的详细报告都存档在项目仓库中。

| 日期 / 标签 | 关注领域 | 关键结果 |
| :--- | :--- | :--- |
| **2026-05-17** | 全基准测试 | 第一阶段 (DX 88%): DeepSeek-v4-pro → GPT-5。第二阶段 (5 模型扩展): GPT-5, Gemini 3 Flash, Qwen 3.5 Plus, DeepSeek v4 Pro, Claude Sonnet 4.6。L3 通用（5/5 达到 100% CFLT）。 |

## 数据与可复现性

每次运行的完整原始数据（`.json`）和详细的 Markdown 报告可以在 GitHub 仓库的 [experiment-history/](https://github.com/corefirst/cflt/tree/main/experiment-history) 目录中找到。

如需复现历史快照：
```bash
cp experiment-history/2026-05-17/part2_eval_raw.json results/part2_eval_raw.json
python scripts/llm_eval/part2_llm_cflt_eval.py --rejudge
```
