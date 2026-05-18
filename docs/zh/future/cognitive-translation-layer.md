# 认知翻译层（CTL）：自然语言意图与 AI 可感知工具调用之间的双向协议

> **版本：** 1.0.0（内部草案）
> **状态：** 为博士级研究规划的研究方案。撰写时尚无实现。
> **作者：** CFLT 核心团队
> **许可：** [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)

---

## 1. 为何需要 CTL：缺失的底物桥接层

CFLT（Core-First Language Theory）与 apcore（AI-Perceivable Core）是两个**独立部署**的开源项目；细看之下，它们在**不同底物**上编码了**同一组织原则**。

- **CFLT**（[cflt.center](https://cflt.center)；SocArXiv 预印本 DOI 待审核通过，届时链接发布于 [cflt.center](https://cflt.center)）是篇章层面的线性化协议。它把**"核心先于框架"（Core-then-Frame）** 原则应用于自然语言：强制的事件核心（槽位 0）先于可选的框架修饰（槽位 1–3：理由、空间、时间）。支柱 I 的参考实现（CoreFirst，Next.js + Electron）已落地部署；预印本报告了 5 个前沿 LLM × 720 试次的实证 pilot。
- **apcore**（[github.com/aiperceivable](https://github.com/aiperceivable)，Apache 2.0，OpenSSF Best Practices 认证）是面向 AI 可调用工具接口的模块标准。它把同一组织原则应用于工具描述：强制的核心层（`input_schema`、`output_schema`、`description`）先于可选的标注层（`readonly`、`destructive`、`requires_approval`、`idempotent`、`open_world`、`cacheable`、`paginated`）和可选的扩展层（`x-when-to-use`、`x-preconditions`、`x-postconditions`、`x-common-mistakes`、`x-cost-per-call`）。Python、TypeScript、Rust 的生产级 SDK 已发布；已有第三方采用。

也就是说，两个项目在**不同表面**上部署了**相同的 Core-then-Frame 分层**。**缺失的是一个协议桥** —— 当人类用户发出 CFLT 一致的自然语言请求、AI agent 通过 apcore 可感知的工具调用来履行该请求时，**认知分层须在底物边界上双向保持**。

这一桥接即**认知翻译层（Cognitive Translation Layer, CTL）**。CTL 是这一跨底物研究计划的**整合目标**，也是博士级研究的规划焦点。

---

## 2. 架构定位

```
┌─────────────────────────────────────────────────────────────────┐
│  第 1 层 —— 自然语言层（由 CFLT 治理）                           │
│  自然语言的篇章级线性化协议                                      │
│  已部署：CoreFirst（支柱 I MVP）+ 720 次试验 LLM pilot            │
└──────────────────────────┬──────────────────────────────────────┘
                           │
                           ▼   （缺失的桥接 —— 本文档）
                           │
┌─────────────────────────────────────────────────────────────────┐
│  第 2 层 —— 认知翻译层（CTL）  [规划中]                          │
│  双向协议桥：                                                    │
│    正向：CFLT 结构化意图 → apcore 结构化调用                     │
│    反向：apcore 结构化结果 → CFLT 结构化回应                     │
│    治理：同意门、ACL 评估、错误恢复                              │
└──────────────────────────┬──────────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────────┐
│  第 3 层 —— 工具调用层（由 apcore 治理）                         │
│  AI 可感知的模块标准                                             │
│  已部署：生产级 SDK（Python / TypeScript / Rust）                │
└─────────────────────────────────────────────────────────────────┘
```

CTL 不取代现有的 AI 工具使用脚手架（MCP、OpenAI Function Calling、Anthropic Tool Use、A2A）。后者处理**传输与序列化** —— 工具描述**如何**到达模型。CTL 处理与此正交的问题：**认知分层如何跨越底物边界** —— 即自然语言意图的**哪些成分**映射到工具元数据的**哪些类别**，以及反向映射如何**重建可理解的回应**。

按 apcore 自身的术语（见 [apcore POSITIONING.md](https://github.com/aiperceivable/apcore)），apcore 为 AI agent 区分出**认知接口（Cognitive Interface）**，与 UI（给人）和 API（给程序）并列。CTL **延伸**这一区分，补上 Cognitive Interface 默认存在却并未自行提供的"**人 → agent 翻译层**"。

---

## 3. 槽位 ↔ 层级对应表

让 CTL 成为**有限可完成的博士目标**（而非开放式臆想）的实证前提，是 CFLT 四个篇章槽位与 apcore 三层元数据之间的**结构性对应**。这一对应是 CTL 研究的核心洞察；**验证它在足够代表性的人类意图样本与模块族上非平凡成立**，本身就是研究计划的一部分。

| CFLT 槽位 | 语言学功能 | 典型成分 | apcore 层级 | apcore 字段 | 跨底物功能 |
|---|---|---|---|---|---|
| **槽位 0**（Core 核心） | 事件核心 / 显著性锚点 | 谓词 + 价位绑定的论元 + 方式 + 作用域内算子 | **Core Layer 核心层** | `input_schema`、`output_schema`、`description` | 强制的功能契约 —— 这个操作**是什么** |
| **槽位 1**（Reason 理由） | 因果 / 动机框架 | *因为*、*为了*、*以便*、动机性从句 | **Annotation Layer 标注层** | `requires_approval`、`destructive`、`idempotent`、`open_world` | 治理 —— 在什么条件下该操作可以进行 |
| **槽位 2**（Space 空间） | 处所 / 作用域框架 | *在 X*、*于 Y 之内*、*跨 Z*、限定作用域的从句 | **ACL 访问控制** | `callers`、`targets`、`conditions`、`default_effect` | 权限边界 —— 该操作在系统中**何处**被允许 |
| **槽位 3**（Time 时间） | 时间 / 条件框架 | *之前*、*之后*、*当*、*如果*、*每当*、调度从句 | **Extension Layer 扩展层** | `x-when-to-use`、`x-preconditions`、`x-postconditions`、`x-workflow-hints` | 规划提示 —— 何时以及在什么工作流位置 |

**如何阅读对应表。** 两组列描述的是**同一概念结构**：一个强制的*是什么*（Core / 槽位 0），围绕它有三类可选框架 —— *为什么*（Reason / 治理）、*在哪里*（Space / 权限）、*何时*（Time / 规划）。论断**不是**映射"一一对应且穷尽" —— 自然语言比这复杂得多 —— 而是**类别对齐足够强**，足以支撑"确定性 + 后备方案"的解析策略。

**为何这非平凡。** 如果槽位 0 映射到 Core Layer，而其余三槽全都映射到一个"元数据"大筐里，那就毫不令人惊讶。**非平凡的观察**是：**CFLT 框架槽位的三个类别（理由 / 空间 / 时间）分别映射到 apcore 非核心元数据的三个类别（Annotation Layer / ACL / Extension Layer）**，且每一对都共享一个**先于本研究、独立存在于两个项目中的功能家族**（治理、权限边界、规划提示）。这是同一 Core-then-Frame 组织原则**同时作用于两个底物**的结构性证据。

---

## 4. 双向机制

CTL 是双向的。两个方向**难度不对称**：正向解析的**源表示**是良构的（CFLT 一致的自然语言），但**搜索空间**是模块 Registry；反向生成的**源表示**也良构（结构化的工具结果），但必须遵守"产出流畅的 CFLT 一致自然语言"这一约束。

### 4.1 正向：CFLT 意图 → apcore 调用

```
用户陈述（CFLT 一致）
  │
  ▼
CFLT 解析器
  │  产出：{ 槽位 0: <core>, 槽位 1: <reason>, 槽位 2: <space>, 槽位 3: <time> }
  ▼
Registry 解析
  │  槽位 0 → 候选模块（用 module.description + input_schema 亲和度匹配）
  │  槽位 1 → 治理前置条件（如请求框定为 "因为这是不可逆的" → 推断 destructive=True 标注检查）
  │  槽位 2 → ACL 作用域（解析 caller_id、target 权限匹配）
  │  槽位 3 → 时间绑定（解析为 input_schema 的时间型字段或 x-preconditions 检查）
  ▼
歧义消解（如有多候选）
  │  以 CFLT 一致的澄清问题向用户暴露候选
  ▼
执行前治理门
  │  apcore 标注评估（同意、破坏性、requires_approval）
  │  apcore ACL 评估
  ▼
apcore 调用
  │
  ▼
结构化结果
```

### 4.2 反向：apcore 结果 → CFLT 一致回应

```
结构化的 apcore 结果（按 output_schema 类型化）
  │
  ▼
显著性识别
  │  识别承载答案的成分（= 回应的候选槽位 0）
  ▼
框架重建
  │  操作的理由（← apcore 中间件 trace、治理决策）              → 槽位 1
  │  效应的作用域（← apcore ACL 评估结果、副作用标注）          → 槽位 2
  │  时间上下文（← 时间戳、有效窗口、x-postconditions）         → 槽位 3
  ▼
CFLT 一致线性化
  │  [Core: <答案>] → [Reason: <理由>] → [Space: <作用范围>] → [Time: <何时有效>]
  ▼
自然语言回应
```

### 4.3 错误与治理流程

三个流程必须由 CTL 桥**原生处理** —— 它们恰好处于现有 AI 工具使用脚手架最薄弱的底物边界：

1. **权限拒绝。** 当 apcore ACL 评估**拒绝**某次调用时，拒绝必须翻译为一个保留用户框架的 CFLT 一致解释 —— 不是 "权限不足（错误码 403）"，而是按槽位 0 + 槽位 1 + 槽位 2 重建：*什么被拒绝*、*在哪条治理规则下*、*在什么作用域内*。
2. **同意门。** 当 apcore 标注表明 `requires_approval=True` 时，CTL 必须**生成一个 CFLT 一致的确认提问**，先把破坏性作用域暴露给用户、再放行调用。提问的 Core 是操作本身；Reason 是破坏性；Space 是受影响的作用域；Time 是生效时间。
3. **恢复建议。** 当 apcore 返回带 `ai_guidance`（apcore 错误恢复约定）的错误时，CTL 必须把该建议翻译为**用户可操作**的 CFLT 一致建议。`ai_guidance` 字段成为槽位 0（被建议的操作）；`retryable`、`user_fixable`、错误码喂入槽位 1–3（建议的理由、作用域、时序）。

---

## 5. 理论根基：跨底物假设

"CFLT 与 apcore 共享一个**底物中立的组织原则**" —— 这一**实证主张**本身是 CTL 研究计划的一部分，**不是**自由假设。

### 5.1 Core-then-Frame 作为底物中立的人体工学原则

CFLT 的基础建立在一组认知语言学与心理语言学主张上：前语言的信息（Levelt 1989）允许按显著性锚点分解（Talmy 2000、Langacker 1987）；把显著性锚点置于序列起始位置可降低成人 L2 产出的工作记忆负荷（Hawkins 2004、Kormos 2006）；同样的干预可降低自回归 Transformer 的次序敏感度与 "Lost in the Middle" 效应（Liu et al. 2023）。这些主张共同把 Core-then-Frame 论证为**语言层**的人体工学原则。

apcore 的基础在**不同底物**上做出平行主张：AI agent 通过受限上下文窗口的注意力感知工具描述时，同样受益于 Core-then-Frame 结构 —— 强制的功能契约先于可选的治理与规划提示 —— 因为**同一组首因性与注意力局部性属性**既作用于自然语言 token，也作用于工具元数据。

**跨底物假设**是：上述并非两个独立观察，而是**单一底物中立人体工学原则的两个推论** —— 任何信息处理系统，只要其吞吐受到顺序注意力的瓶颈约束，就会受益于输入的 Core-then-Frame 组织。CTL 是把这一假设**在两个底物之间的桥上操作化**的协议。

### 5.2 与相邻传统的关系

- **框架语义学（Fillmore 1982；FrameNet：Baker, Fillmore & Lowe 1998）**：CFLT 四槽方案与框架语义的角色结构**兼容但不等同**。CTL 在槽位 0 → 模块解析中利用框架语义的亲和性（槽位 0 携带谓词；模块由谓词样的功能契约类型化）。
- **Toolformer（Schick et al. 2023）** 与更广泛的 LLM 工具使用线索：CTL **位于其下游**，因为它**预设**结构化工具接口的存在；同时**位于其上游**，因为它处理 "**自然语言成分如何绑定到工具元数据类别**" 的协议级问题 —— 这是既有工具使用工作通过 ad-hoc prompting 默认解决了的。
- **Schema 强制输出（JSON 模式、structured outputs）**：CTL 把 schema 强制从 LLM 生成的**输出端**延伸到**人类意图 ↔ 工具调用**之间的**双向翻译**，并在桥上叠加治理强制。

### 5.3 CTL 不是什么

- **不是工作流引擎。** CTL 把**单个**意图映射到**单个**（或一个小的歧义消解集合的）调用。多步编排属于上游工作流引擎（apflow、LangChain、CrewAI）。
- **不是 LLM 调用库。** CTL 是 LLM 中立的；LLM 是解析器与生成器组件的一种可能实现，但协议本身不绑定特定模型。
- **不是传输协议。** CTL 叠加在 MCP、A2A、OpenAI Tool Use 等之上；它处理这些协议交给 ad-hoc prompting 的认知分层问题。

---

## 6. 可证伪的子主张

CTL 研究计划围绕**可证伪的子主张**组织，每一项都有明确的**证伪条件**。

### CTL-1：首次调用成功率

**主张。** 由 CTL 解析器产生的 CFLT→apcore 翻译，相对于不具备 CFLT 槽位 ↔ 层级对应的 LLM-only 基线，**首次调用成功率更高**。

**测量。** 在一个由 *N* 条人撰写的 CFLT 一致请求构成的基准之上、对一个具有混合治理元数据的 *M* 模块 Registry，比较 CTL 解析调用与基线的**首次成功**（定义：所选模块正确、input_schema 满足、未违反治理、输出 validates against output_schema）。

**证伪条件。** 如果成功率在**至少 3 个**前沿模型族上未能在 *p* < .05 改善，则 CTL 退化为 "普通的结构化意图解析"，相对既有工具使用脚手架**无协议级价值**。

### CTL-2：越权事件减少

**主张。** 相对于缺失 "槽位 1 → 标注层" 绑定的基线，CTL 中介的调用流程**减少越权事件**（agent 在 `requires_approval=True` 或 `destructive=True` 模块未先暴露同意门的情况下调用）。

**测量。** 在一组**故意同意意向暧昧**的请求基准上，比较 CTL 与基线下的越权事件计数。

**证伪条件。** 如果越权事件在**至少 3 个**前沿模型族上**绝对计数未减少**，则 "槽位 1 → 标注层" 对应**不可协议级落地**，CTL 的治理贡献被驳回。

*为何用绝对计数而非 p 值。* 越权事件在任何良构基准上都是**低基础率的稀有事件**；显著性检验在该 regime 下统计功效低。"在所有评估的模型族上绝对计数下降"因此是更保守的证伪条件。在更大量、刻意倾斜的基准上使用 *p* < .05 的更强检验，留作第 3 年扩展。

### CTL-3：反向理解性保持

**主张。** CFLT 一致地线性化结构化 apcore 结果所得到的回应，在**人评理解性**得分上**高于**原始结构化结果与 ad-hoc LLM 生成的自然语言摘要。

**测量。** 在 *K* 个三元组（原始结构化结果、ad-hoc 摘要、CTL 线性化回应）上做人评研究，以固定 rubric 打分（回应是否暴露答案？是否解释作用域？是否暴露时间有效性？）。

**证伪条件。** 如果 CTL 线性化回应在 rubric 三个维度中的至少两个上未能以 *p* < .05 优于 ad-hoc 摘要，则反向贡献被驳回。

### CTL-4：跨模型泛化

**主张。** CTL 的解析与生成行为**在前沿模型族上稳定** —— 即槽位 ↔ 层级对应是**模型独立的协议属性**，而非模型特定的偶发现象。

**测量。** 在**至少 5 个**前沿模型族（GPT-5、Claude Sonnet、Gemini、Qwen、DeepSeek）上复制 CTL-1、CTL-2、CTL-3，采用模型中立的解析器 / 生成器实现。

**证伪条件。** 如果 CTL-1、CTL-2 或 CTL-3 在不同模型族间显示统计显著的交互效应（模型族 × CTL-vs-baseline，*p* < .05），则 CTL 必须**退缩为按模型族特化的协议**，跨底物泛化被弱化。

*统计学说明。* 未能拒绝 H0（无交互效应）**不等于**确证了跨模型一致性。要正向确证跨模型泛化，还需要：(i) 每个模型上的 CTL 效应**单独**在 *p* < .05 显著；(ii) 跨模型的效应量方差落在**预先注册的等效区间**之内（TOST 等效性检验程序，Lakens 2017）。**只有三条同时满足** —— 无显著交互、单独显著、等效边界内方差 —— CTL-4 才算被**确证**，而不仅仅是**未被证伪**。

---

## 7. 研究路线图（四年博士计划）

CTL 研究计划组织为**四年博士计划**。两端的底物已经独立部署并被验证，是这一时间表**可信**的前提。

### 第 1 年 —— 理论形式化 + 基准设计

- 把 §3 的槽位 ↔ 层级对应**形式化为类型化映射**，并明确边界行为。
- 设计 CTL-1 / CTL-2 / CTL-3 基准：组装 *N* 条 CFLT 一致请求语料、*M* 模块 apcore Registry（治理元数据按设计分布）、CTL-3 的人评 rubric。
- 发表：一篇理论立场论文（目标 venue：*Cognitive Science*、*Topics in Cognitive Science* 或主要 AI 对齐 workshop）。

### 第 2 年 —— 正向原型 + CTL-1、CTL-2 评估

- 把 CTL 正向解析器实现为模型中立库，可从任意 LLM provider 调用。
- 在至少 5 个前沿模型族上跑 CTL-1 与 CTL-2 评估。
- 发表：一篇正向性能实证论文（目标 venue：ACL、EMNLP、NAACL 或 NeurIPS Datasets & Benchmarks）。

### 第 3 年 —— 反向原型 + CTL-3、CTL-4 评估

- 实现 CTL 反向生成器，包括 §4.3 的治理解释、同意门、恢复建议流程。
- 跑 CTL-3 人评研究与 CTL-4 跨模型泛化分析。
- 发表：一篇反向理解性实证论文 + 一篇跨模型泛化论文。

### 第 4 年 —— 整合 + 学位论文

- 整合研究：把 CTL 部署进 CoreFirst 参考应用（支柱 I），测量 CTL 中介与基线交互下的端到端任务完成率。
- 撰写博士学位论文，将 1–3 年工作整合为统一的跨底物研究计划。
- 公开交付物：一份 CTL 规范文档（类比 apcore PROTOCOL_SPEC），适合独立第三方实现。

---

## 8. 不在范围内

CTL 研究计划**不**致力于交付以下任何一项：

- **工作流引擎**，把多次 CTL 中介调用串成多步计划。归属上游工具（apflow、LangChain、CrewAI）。
- **新传输协议**，与 MCP、A2A、OpenAI Tool Use 竞争。CTL 叠加在 apcore 所采用的任何传输之上。
- **新 LLM**。解析器与生成器组件 LLM 中立；LLM 是可替换的实现之一。
- **产品化的 SaaS 桥接服务。** 与 CFLT 本身一样，CTL 是协议规范；产品化是独立组织的工作。
- **槽位 ↔ 层级对应的自动定理证明器。** 该对应是**经验性辩护的主张**，不是逻辑推导；它的支持来自 CTL-1 至 CTL-4，而非形式证明。

---

## 9. 与 CFLT 开放实证议程的关系

CTL 是 CFLT OSF 预印本 §7.7 所述的**整合目标**，把开放实证议程的**六个子计划**联结为单一研究：

- 人类侧产出流畅性计划（P1 / §7.1）为 "槽位 0 → 核心层" 对应提供人类认知锚点。
- 类型学计划（§7.2）决定 R-S-T 框架排序是否普遍或体裁条件化，直接影响 "槽位 1/2/3 → 标注/ACL/扩展" 映射。
- LLM 机制性计划（P2 / §7.3）决定 "槽位 0 → 核心层" 对应是机制性扎根于注意力动态，还是仅止于协议层约定。
- 神经计划（P3 / §7.4）为跨底物主张的人类侧锚点提供双语认知证据。
- 形式语义计划（§7.5）决定槽位 ↔ 层级对应是否具有组合语义基础。
- Agentic 协调计划（§7.6）提供 CTL 运行的多轮底物。

CTL 因此**不**与六个子计划正交 —— 它是要求它们**收敛**的协议。

---

## 10. 状态

本文档描述一个**为博士级研究规划**的研究计划。**撰写时尚无 CTL 实现。** 两个底物端（CFLT、apcore）已独立部署并对公众开放查阅；CTL 是其桥接，其**规范与实证评估**构成规划中的博士贡献。

作者维护本文档、CFLT 框架（cflt.center）、apcore 标准（github.com/aiperceivable）作为**独立的开源工作**（许可宽松）。欢迎就**指导、合作或独立实现**进行问询 —— 可直接邮件（tercel.yi@gmail.com；ORCID [0009-0000-3742-4403](https://orcid.org/0009-0000-3742-4403)），或经 [cflt.center](https://cflt.center) 列出的项目渠道。

---

## 参考文献

- Baker, C. F., Fillmore, C. J. & Lowe, J. B. (1998). The Berkeley FrameNet Project. *Proceedings of COLING-ACL '98*, 86–90.
- Fillmore, C. J. (1982). Frame Semantics. In *Linguistics in the Morning Calm*, Linguistic Society of Korea (ed.). Hanshin.
- Hawkins, J. A. (2004). *Efficiency and Complexity in Grammars.* Oxford University Press.
- Kormos, J. (2006). *Speech Production and Second Language Acquisition.* Erlbaum.
- Lakens, D. (2017). Equivalence Tests: A Practical Primer for *t*-tests, Correlations, and Meta-Analyses. *Social Psychological and Personality Science* 8(4), 355–362.
- Langacker, R. W. (1987). *Foundations of Cognitive Grammar, Vol. 1.* Stanford University Press.
- Levelt, W. J. M. (1989). *Speaking: From Intention to Articulation.* MIT Press.
- Liu, N. F. et al. (2023). Lost in the Middle: How Language Models Use Long Contexts. *TACL.*
- Schick, T. et al. (2023). Toolformer: Language Models Can Teach Themselves to Use Tools. *NeurIPS 2023.*
- Talmy, L. (2000). *Toward a Cognitive Semantics, Vol. 1.* MIT Press.
- apcore Project. (2026). *apcore POSITIONING.md.* <https://github.com/aiperceivable>
- Yi, W. (2026). *Core-First Language Theory (CFLT): A Discourse-Level Linearization Protocol.* SocArXiv Preprint.

---

*文档版本：1.0.0（内部草案）*
*状态：研究路线图。撰写时尚无 CTL 实现。*
*作者：CFLT 核心团队*
