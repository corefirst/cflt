---
title: CFLT — 核心优先语言理论
description: 跨语言通信、第二语言教学与人机认知对齐的统一理论框架。
hide:
  - navigation
---

# 核心优先语言理论 (Core-First Language Theory)

> *话语的认知核心，也是其被普遍优先排列的线性位置。*
> —— CFLT 的规范性协议层主张（一种无标记默认，而非自然语言语序的描述性普适规律）。参见 [`manifesto.md`](manifesto.md) §1.1 关于协议与描述的区分；参见 [`foundations/core-concept.md`](foundations/core-concept.md) §2.3 关于分层范围界定及 §2.5 关于类型学证据。

**CFLT** 提出了一个话语层级的原则，并由此推导出 **CFLT 协议** —— 一套四元素排序规则，旨在以最小认知摩擦衔接任意两种自然语言，并作为大语言模型的结构化提示词协议：

```
[核心] → [理由] → [空间] → [时间]
```

CFLT 是**理论 + 方法**，而非单一产品。该理论属于开放公共领域 (CC BY 4.0)。参考实现则位于独立的各个项目中。

---

## 如何引用 (How to Cite)

若在学术工作中使用 CFLT 的理论、方法或代码，请按以下格式引用：

```
Yi, W. (2026). Core-First Language Theory (CFLT): A Discourse-Level
Linearization Protocol for Cross-Linguistic Communication and LLM
Alignment. Zenodo. https://doi.org/10.5281/zenodo.20289504
```

理论文档采用 [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) 许可；配套参考实现代码位于姊妹仓库，分别采用 Apache 2.0 / MIT 许可。两类许可均允许在**保留原作者署名**的前提下复用与改编。

## AI 使用说明 (AI Use Disclosure)

作者母语非英语。在英文书面材料的准备过程中，使用了 AI 工具（Claude、GPT）协助进行**英文翻译、文字校对与引用格式整理**。本项目所有理论主张、研究设计、实证试点数据及实质性论证均由作者独立完成。

---

## 从何处开始

- **[宣言 (Manifesto)](manifesto.md)** — 权威理论陈述。
- **[核心概念](foundations/core-concept.md)** — "Core" 的定义（显著性锚点，**不是**动词或谓词）。请在阅读宣言后立即阅读此篇。
- **[战略愿景](vision.md)** — 横跨人类双语教育（支柱 I）与大语言模型协议标准化（支柱 II）的跨项目路线图。

## 理论基础 (Foundations)

CFLT 集成了八个学科的研究成果，并由一篇核心概念澄清文档作为锚点：

- **[语言学](foundations/linguistics.md)** — 普遍语法、信息结构、认知语言学、NSM。
- **[语音学](foundations/phonetics.md)** — 跨语言语音迁移、肌肉智能、拼音-IPA 桥梁。
- **[社会语言学](foundations/sociolinguistics.md)** — 礼貌、语体、敬语作为核心的逻辑包装。
- **[教育学](foundations/pedagogy.md)** — Krashen、Vygotsky、认知负荷理论、TBLT、双语词汇访问。
- **[神经科学](foundations/neuroscience.md)** — 显著性网络、前额叶代谢成本、EIC、程序化。
- **[逻辑学](foundations/logic.md)** — 谓词逻辑、lambda 演算、CCG、言语行为理论。
- **[数学](foundations/mathematics.md)** — 信息论、UID、最优编码、线性化。
- **[大语言模型与 AI](foundations/llm.md)** — Transformer 注意力、迷失在中间、提示词顺序方差、幻觉动态。

## 方法论 (Methodology)

学习如何在真实场景中应用 CFLT：

- **[人类学习](methodology/human-learning.md)** — 通过重构认知肌肉记忆实现 L2 口语流利度的指南。
- **[LLM 提示词](methodology/llm-prompting.md)** — 将 CFLT 协议作为标准化工程协议以减少模型方差。
- **[实证研究议程](methodology/empirical-agenda.md)** — 验证 CFLT 在 AI 和教学法中主张的科学路线图。

## 参考 (Reference)

- **[参考实现](reference-implementations.md)** — 基于 CFLT 构建的项目。
- **[参考文献](bibliography.md)** — 跨语言学、语言哲学、数学、LLM/NLP 和 SLA 教学法的约 80 条引用。

---

## 贡献者 (Contributors)

CFLT 是集体智慧的结晶。我们由衷感谢所有为完善理论及其实现做出贡献的[开发者与研究者](contributors.md)。

## 引用方式

> CFLT 核心团队. (2026). *核心优先语言理论 (CFLT)：从第一性原理重构全球双语教育.* 检索自 https://cflt.center

## 许可

本站理论内容采用 [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) 协议。源码：[github.com/corefirst/cflt](https://github.com/corefirst/cflt)。
