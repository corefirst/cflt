# 实验日志与基准测试

本页面记录了通过各种模型基准测试和人类对齐测试对核心优先语言理论（CFLT）进行的实证验证。

## 历史运行记录

每次实验运行的详细报告都存档在项目仓库中。

| 日期 / 标签 | 关注领域 | 关键结果 |
| :--- | :--- | :--- |
| **2026-05-17** | 人类-CFLT 对齐 | deepseek-v4-pro → gpt-5, DX 88% (稳定在 ~96%) |
| **2026-05-17** | LLM 自我一致性 | 4 模型基准：gpt-5 / gemini-3-flash / qwen3.5-plus / deepseek-v4-pro, N=3, L3 +22–44pp |
| **2026-05-17-claude** | Claude 扩展测试 | 5 模型扩展：基准 + claude-sonnet-4-6。L3 通用（5/5 达到 100% CFLT）。 |

## 数据与可复现性

每次运行的完整原始数据（`.json`）和详细的 Markdown 报告可以在 GitHub 仓库的 [experiment-history/](https://github.com/corefirst/cflt/tree/main/experiment-history) 目录中找到。

如需复现历史快照：
```bash
cp experiment-history/2026-05-17/part2_eval_raw.json results/part2_eval_raw.json
python scripts/llm_eval/part2_llm_cflt_eval.py --rejudge
```
