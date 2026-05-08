---
title: 核心优先语言理论 (CFLT) 宣言
description: 从第一性原理重构全球双语教育的统一理论框架。
---

# 核心优先语言理论 (CFLT)：从第一性原理重构全球双语教育

> 项目主页：corefirst.world
> 状态：理论层已锁定
>
> *本中文版基于英文权威版本翻译；如有歧义，以 [English version](../en/manifesto.md) 为准。*

## 1. 摘要

**核心优先语言理论 (Core-First Language Theory, CFLT)** 是一个面向跨语言通信与双语教育的统一理论与操作框架。它提出一条话语层级 (discourse-level) 的核心原则——*话语的认知核心，也是其在任何语言中被普遍优先排列的线性位置*——并由此定义出一套可教学、可被 AI 支持的排序协议（**CFLT 协议**），用以最小化任意两种自然语言之间的认知摩擦。

通过识别全人类共享的认知"硬件"（乔姆斯基 (Chomsky) 的普遍语法 (Universal Grammar)，并经由 *核心语法 (core grammar)* ↦ *核心优先排序 (core-first sequencing)* 的扩展），同时中和文化"软件"层面的偏差（萨丕尔-沃尔夫假说 (Sapir-Whorf Hypothesis)），CFLT 借助 AI 在任意两种语言之间构建无缝桥梁。

**分层命名：**

| 层级 | 名称 | 角色 |
|---|---|---|
| 项目 / 品牌 | **CoreFirst** (corefirst.world) | 涵盖理论与应用的伞品牌 |
| 框架 | **CFLT — 核心优先语言理论** | 统一了学术理论与操作协议的品牌 |
| 实施 | **CFLT 协议** | 具体的 `[Core] → [Modifiers]` 排序规则 |

项目以 **CFLT** 作为科学基础与实践方法的统一名称。术语 **CFLT 协议** 特指操作层面的排序规则。

---

## 2. 理论基础

> §2.1–§2.3 的概述刻意保持简洁。如需深入论述（含诚实的局限性与引用），请参阅配套文档：
> - **[`foundations/core-concept.md`](foundations/core-concept.md) — 请先阅读此篇。** 定义"Core"的含义：**显著性锚点 (salience anchor)**，而不是动词或谓词。可避免误读其他基础文档中的类比。
> - [`foundations/linguistics.md`](foundations/linguistics.md) — 普遍语法、信息结构、认知语言学、言语生成
> - [`foundations/logic.md`](foundations/logic.md) — 谓词逻辑、λ 演算、组合范畴语法 (CCG)、言语行为、关联理论
> - [`foundations/mathematics.md`](foundations/mathematics.md) — 信息论、均匀信息密度 (UID)、最优编码、线性化
> - [`foundations/llm.md`](foundations/llm.md) — Transformer 注意力偏差、提示词顺序、思维链 (CoT)
> - [`bibliography.md`](./bibliography.md) — 统一参考文献

### 2.1 普遍语法与 *核心语法*（诺姆·乔姆斯基 Noam Chomsky）
**概念：** 人类大脑天生具有一种生物学层面的"语言习得装置 (Language Acquisition Device, LAD)"。在管辖与约束理论 (Government-Binding Theory) 与"原则与参数 (Principles & Parameters)"框架下，乔姆斯基将一种语言的 *核心语法 (core grammar)*（带参数的普遍原则）与其 *边缘 (periphery)*（特异、需后天习得的部分）相区分。

**CFLT 扩展：** 乔姆斯基的 *核心语法* 是一种 **静态结构** 区分（哪些规则属于核心），而 CFLT 提出一种 **动态线性化 (dynamic linearization)** 原则：*认知核心同时也是话语在普遍意义上被优先放置的句首位置*。CFLT 由此将乔姆斯基的"core"概念从一个结构范畴扩展为一条排序规则。这是本宣言的核心理论贡献。

### 2.2 萨丕尔-沃尔夫假说（语言相对论）
**概念：** 一种语言的结构会塑造其使用者的认知过程与世界观。
**CFLT 应用：** 来自"主语显著 (subject-prominent)"或"重语境 (context-heavy)"语言背景（如汉语、日语、韩语）的学习者，在切换到"谓词显著 (predicate-prominent)"语言（如英语）时，会面临高昂的认知摩擦。CFLT 定义了一种**中性缓冲序列 (Neutral Buffer Sequence)**，以消除心智上下文切换的成本。

### 2.3 自然语义元语言（安娜·维兹比卡 Anna Wierzbicka）
**概念：** 所有复杂的人类含义都可以被还原为一组小型的普遍概念，称为 **语义原语 (Semantic Primes)**（如 *I, You, Do, Good, Because*）。
**CFLT 应用：** AI 利用这些原语作为 **原子词汇 (Atomic Vocabulary)**，在 Core-First 序列建立后，辅助学习者从母语 (L1) 过渡到目标语言 (L2)。

---

## 3. 核心框架：核心优先排序协议

### 3.1 原则："核心在前，补充在后"
CFLT 规定一种标准化的信息序列以统一人类表达：

**`[核心动作/结果] → [条件/原因] → [空间/语境] → [时间]`**

在 **规范（无标记）序列 (canonical, unmarked sequence)** 中，四个元素全部为强制项。教学材料与具体实现在教授默认形式时，必须保持这一四元素排序；丢弃任意元素（例如丢弃 `[空间/语境]`）的部分序列**不符合**规范形式。

> **重要适用范围说明。** 四元素规范序列定义的是 CFLT 的 **无标记默认 (unmarked default)** 形式 —— 即流利说话者在没有特殊修辞目的时所产出的形式。它**并不**禁止成熟流利度所需的有标记偏离 (marked deviation)：话题化 (topicalization)、前置 (fronting)、分裂句 (clefts)、句末重置 (end-weight repackaging) 等。每一种自然语言都对同一命题内容拥有多种表达形式，CFLT 通过将自身定位为 *基线 (baseline)* 来兼容这一现实——有意的有标记偏离将在掌握基线之后才被引入。完整的无标记/有标记区分参见 [`foundations/core-concept.md`](foundations/core-concept.md) §7。

### 3.2 演示 CFLT 转换

CFLT 中的 Core 是一个**显著性锚点 (salience anchor)**，而不是动词（参见 [`foundations/core-concept.md`](foundations/core-concept.md)）。下面四个例子分别展示该协议所兼容的四种 Core 类型。

#### 例 1 —— 动作型 Core
**L1（中文，重语境顺序）：** *昨天下雨，我在家没出去。* —— 时间 → 原因 → 结果
**CFLT 重构形式：** *我没出去，因为下雨，在家，昨天。* —— Core → 原因 → 空间 → 时间
**英语 (CFLT-L2)：** *I didn't go out, because it rained, at home, yesterday.*

#### 例 2 —— 身份／描述型 Core
**L1（中文）：** *那个穿红衣服的女孩是我妹妹。* —— 修饰语堆叠的名词短语 → 身份
**CFLT 重构形式：** *那个女孩是我妹妹，穿着红衣服，在照片里，去年夏天。* —— Core（身份）→ 描述 → 空间 → 时间
**英语 (CFLT-L2)：** *That girl is my sister, wearing a red dress, in the photo, from last summer.*

#### 例 3 —— 状态型 Core
**L1（中文）：** *开了一下午会，我在办公室都累瘫了。* —— 原因 → 空间 → 状态
**CFLT 重构形式：** *我累瘫了，因为开了一下午会，在办公室，刚才。* —— Core（状态）→ 原因 → 空间 → 时间
**英语 (CFLT-L2)：** *I'm exhausted, because of the meeting, in the office, just now.*

#### 例 4 —— 请求／言语行为型 Core
**L1（中文）：** *现在能在桌上帮我递一下盐吗？* —— 时间 → 空间 → 请求
**CFLT 重构形式：** *能帮我递一下盐吗，请，在桌上，现在？* —— Core（请求）→ 礼貌标记 → 空间 → 时间
**英语 (CFLT-L2)：** *Could you pass the salt, please, on the table, now?*

**CFLT 的优势：** 在上述四种 Core 类型中，一旦学习者在母语思维中采用了 Core-First 排序，生成目标语言便从一项**结构重组**降格为一项**词元替换 (token replacement)** 任务。协议本身保持一致；填充 0 号位置的内容随说话者的意图而变。

---

## 4. 与相邻文献的区分

CFLT 必须与文献中已存在的、表面相似的一个短语审慎区分：

> Ambridge, B. & Wagner, L. (eds.) (2021). *Testable Theories of Core First Language Acquisition*. Special Issue, *Journal of Child Language*, Vol. 48, Special Issue 5.

**结构分析对比：**

| | Ambridge & Wagner (2021) | CFLT（本研究） |
|---|---|---|
| 短语切分 | `[core] + [first language acquisition]` | `[core-first] + [language theory]` |
| 主题 | 儿童习得 L1 的**核心机制** | 跨语言话语的**核心优先排序**规则 |
| 研究对象 | 习得母语的儿童 | 产出 L2 的双语学习者 |
| 学科领域 | 发展心理语言学 | 应用语言学 + AI 辅助双语教学 |

两个字符串在三元组 "core first language" 处重叠，但其底层概念互不相关。CFLT 不涉及 L1 习得；Ambridge / Wagner 卷不涉及双语排序。在任何可能与 L1 习得文献被一同检索到的工作中，作者必须援引此项区分。

---

## 5. AI 驱动的实施路线图

### 阶段 1：认知重塑（LLM 作为逻辑导师）
AI 训练用户使用 Core-First 序列，在母语中表达意图。该阶段聚焦于打破 L1 特有的句式模式。

### 阶段 2：原子映射（LLM 作为词元置换器）
AI 在已建立的 Core-First 框架中引入目标语言的"词元 (token)"。语法通过模式识别隐式习得，而非显式规则记忆。

### 阶段 3：文化精修（高级模块）
当通过 CFLT 实现功能性流利度后，AI 引入文化特有的习语、隐喻与高级文体细微差别。

---

## 6. 全球愿景：任意-到-任意双语 (Any-to-Any Bilingualism)

CFLT 不局限于中-英对。它被设计为一种 **人类通信的通用协议 (Universal Protocol for Human Communication)**。通过将 Core-First 序列采纳为"全球中介语 (Global Interlingua)"，我们可以将双语教育扩展到任意语言对：
*   **日语-法语：** 以 `[Core Action]` 作为转换轴。
*   **阿拉伯语-西班牙语：** 以 `[NSM Primes]` 作为语义桥梁。

项目主页与权威参考为 **corefirst.world**。

---

## 7. 产品实现：CoreFirst

### 7.1 "语义乐高 (Semantic Lego)"哲学
CoreFirst 不把语法作为僵硬规则来教，而是把语言视为一组功能积木。目标是 **以最小认知负荷 (Minimum Cognitive Load) 实现最大通信效率 (Maximum Communicative Efficiency)**。

### 7.2 核心语言要素的实现

#### A. 词类 → 逻辑积木
语法术语（名词、动词）被替换为直观的功能范畴：
*   **`[谁/什么 (Who/What)]`**（主语/宾语）
*   **`[动作 (Action)]`**（谓词）
*   **`[语境 (Context)]`**（时间、地点等状语）

#### B. 时态 → 语义时间词元
为解决英语时态的复杂性，CFLT 采用"时间词元 (Time Tokens)"。
*   *输入：* "I eat [Time: Yesterday]"
*   *AI 增强：* 自动精修为 "I ate"，同时校验语义意图（过去）已被正确传达。

#### C. 复杂结构 → 扁平化逻辑
避免嵌套从句（如关系从句）。使用线性、可加的逻辑。
*   *传统形式：* "The man who is standing there is my boss."
*   *CFLT 逻辑：* "That man is my boss, [描述] he is standing there."

### 7.3 产品逻辑：语义优先，语法其次
1.  **语义核心 (Semantic Core)：** 优先保证 CFLT 逻辑的正确排序。
2.  **语法叠加 (Grammar Overlay)：** AI 作为非侵入式的"自动校正"插件，将用户的 CFLT 输出精修为地道的 L2，而不打断思维流动。

---

## 8. CFLT 内容生态：通用教学法

### 8.1 跨年龄适配
CFLT 作为各年龄段教育内容的基础：
- **早期学习者：** 聚焦"视觉化 CFLT (Visual CFLT)"，使用动画图标与约 500 个语义原语的受限集合，构建直觉性的概念-逻辑映射。
- **成人学习者：** 聚焦"效率化 CFLT (Efficiency CFLT)"，针对专业场景使用行业特定词元与复杂逻辑连接词。

### 8.2 行业特化模块："IT 英语"案例
CFLT 框架特别适合技术沟通。在 **IT 行业**，"动作-结果优先"的逻辑与工程文档及协作编码完美契合。
- **示例词元：** *deploy, refactor, debug, latency, endpoint, scalability.*
- **逻辑映射：** 不再说 "If we have high latency, we should refactor the code"，而是 CFLT 推荐："**Refactor the code**, because of **high latency**, in the **backend**, now."
- **收益：** IT 专业人员可以跨文化即时、准确地传达关键技术决策。

同样的模块化词汇注入模式可扩展到医疗、金融、技术、酒店服务等领域，而无需更改底层认知协议。

### 8.3 多模态交付（音视频合成）
- **音频优先 (Audio-Primary)：** 优先提供语音输出，韵律与重音模式强调 CFLT 块的 `[Core Action]`。
- **视觉支撑 (Visual-Support)：** AI 生成的图像或短片为核心概念提供即时视觉反馈，绕过母语翻译的需求。

### 8.4 自动化课件生成
借助 LLM，CFLT 框架可基于简单提示词（如"为 8 岁儿童设计的医院场景"）自主生成完整课程。这确保所有教育内容都与"Core First"排序原则保持一致。

---

## 9. 语音迁移：利用学习者既有的知识系统

### 9.1 拼音-到-IPA 桥梁
对于亚洲学习者（尤其是中文背景），CFLT 利用其对**拼音 (Pinyin)** 的既有掌握来加速发音习得。
- **重叠音素集：** 直接迁移两套系统中共有的音，如 /b/、/p/、/m/、/f/。
- **修正指引：** 不使用抽象的发音器官描述，而提供"相对调整"。例如：要发英语的 /v/，从拼音 'f' 的肌肉位置开始，但加入声带振动。
- **从零到一的音素：** 对于母语系统中完全缺失的音（如 /θ/），AI 基于相邻的母语口型生成类比。

### 9.2 肌肉智能 (Muscular Intelligence)
语言学习是一项体能技能。通过识别 L1 与 L2 之间的"肌肉重叠 (Muscle Overlap)"，CFLT 减少学习"新"音的认知阻力，将其视为熟悉动作的变体。这与 Core-First 排序原则互补：§3 减少**句法摩擦**，§9 减少**发音摩擦**。两者都源于同一第一性原理思路——利用学习者大脑与身体已经编码的内容。

---

## 10. 命名决策：为何不用"元语言逻辑 (Meta-Language Logic)"？

在项目早期框架阶段，候选名 **"MLL — Meta-Language Logic"** 曾被考虑作为伞名词。它在发布前因以下三个原因被否决，记录于此，以便 CFLT 这一选择可以基于其本身的优劣被评估，而不是被当作默认。

1. **术语精确性。** "Meta-language"（元语言）在语言学与计算机科学中专指用于描述另一种语言的语言（BNF、XML Schema、塔尔斯基式真值定义）。本文档所述框架在此技术意义上**并非**元语言——它是一种话语排序协议。采用"Meta-Language Logic"将构成对既有术语的误用，任何具有语言学或形式语言背景的同行评审者都会指出这一点。
2. **同领域缩写冲突。** "MLL" 在相邻的生物医学 AI 文献中已被占用（Mixed Lineage Leukemia，混合谱系白血病）；"MLM" 是 AI/NLP 的标准缩写，指 Masked Language Modeling（BERT 及其后继）。两类冲突都会损害可发现性，并可能导致本工作在目标领域被搜索引擎与学术索引错误归类。
3. **自解释命名。** "Meta-Language Logic" 没有传达框架的核心运行规则。**Core-First Language Theory** 直接命名了那条规则：核心总是在前。§3.1 的原则（"核心在前，补充在后"）与伞名词如今指向同一个概念。

本节作为设计决策记录保留，以免未来贡献者重新讨论该问题。

---

*由 CoreFirst AI 项目创建，2026。项目主页：corefirst.world。*
