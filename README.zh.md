# CFLT — 核心优先语言理论

> **跨语言通信、第二语言教学与人机认知对齐的统一理论框架。**
>
> 项目主页：[cflt.center](https://cflt.center)
>
> *English version: [README.md](./README.md)*

---

## 关于中文版

本仓库的理论文档目前以**英文为权威基准版本**，中文版正在分阶段翻译中。请参见 [TRANSLATION-PRIORITY.md](./TRANSLATION-PRIORITY.md) 了解翻译进度与优先级。

未翻译的页面会自动显示英文原文，并在网站顶部标注。如希望协助翻译，欢迎提交 PR。

---

## CFLT 是什么？

**核心优先语言理论 (CFLT)** 提出一条话语层级的核心原则：

> *话语的认知核心，也是其在任何语言中被普遍优先排列的线性位置。*

由此推导出 **核心优先语言方法 (CFLM)** 的四元素排序规则，既是连接两种自然语言的最小认知摩擦桥梁，也可作为面向大语言模型的结构化提示协议：

```
[核心动作/结果] → [条件/原因] → [空间/语境] → [时间]
```

CFLT 是**理论 + 方法**，而不是产品。理论内容属于开放共享领域（CC BY 4.0）。具体的参考实现位于独立项目中 —— 见 [docs/en/reference-implementations.md](./docs/en/reference-implementations.md)。

---

## 文档结构

```
docs/
├── en/                      ← 权威英文版（默认语言）
│   ├── index.md             ← 站点首页
│   ├── manifesto.md         ← 宣言
│   ├── vision.md            ← 战略愿景
│   ├── foundations/         ← 六大理论基础
│   ├── reference-implementations.md
│   └── bibliography.md
├── zh/                      ← 中文版（翻译进行中）
└── assets/                  ← 跨语言共享资源
```

---

## 参考实现

CFLT 本身是理论与规范。具体实现位于独立项目中。详见 [docs/en/reference-implementations.md](./docs/en/reference-implementations.md)。

第一个参考实现是 [**CoreFirst**](https://github.com/corefirst/corefirst)（[corefirst.world](https://corefirst.world)）—— 一个开源 Next.js 应用，为人类二语学习者实现 CFLM（支柱一）。

---

## 如何引用

如在学术或技术写作中引用 CFLT，建议格式：

> CFLT 核心团队. (2026). *核心优先语言理论 (CFLT)：从第一性原理重构全球双语教育.* 检索自 https://cflt.center

---

## 贡献

欢迎贡献：

- 完善理论基础（补充引用、反驳论证、新学科视角）
- **翻译任意文档**（中文优先；其他语言也欢迎，参见 `docs/{语言代码}/`）
- 在 `reference-implementations.md` 添加采用 CFLM 的项目
- 提供支持或挑战 CFLM 主张的实证证据

---

## 许可

本仓库的理论内容采用 [Creative Commons Attribution 4.0 国际许可协议（CC BY 4.0）](./LICENSE)。在适当署名的前提下，您可以自由分享和改编本材料，包括用于商业目的。
