# 认知翻译层（CTL）：自然语言意图与 AI 可感知工具调用之间的双向协议

> **版本：** 1.0.0（内部草案）
> **状态：** **开放研究计划**。撰写时尚无实现。本计划在设计上**允许独立研究者、工业团队及研究生**在任何阶段参与或扩展，无须额外协调成本。
> **作者：** CFLT 核心团队
> **许可：** [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)

---

## 1. 为何需要 CTL：缺失的底物桥接层

CFLT（Core-First Language Theory）与 apcore（AI-Perceivable Core）是两个**独立部署**的开源项目；细看之下，它们在**不同底物**上编码了**同一组织原则**。

- **CFLT**（[cflt.center](https://cflt.center)；Zenodo 归档 DOI 待存档，届时链接发布于 [cflt.center](https://cflt.center)）是篇章层面的线性化协议。它把**"核心先于框架"（Core-then-Frame）** 原则应用于自然语言：强制的事件核心（槽位 0）先于可选的框架修饰（槽位 1–3：理由、空间、时间）。支柱 I 的参考实现（CoreFirst，Next.js + Electron）已落地部署；工作论文报告了 5 个前沿 LLM × 720 试次的实证 pilot。
- **apcore**（[github.com/aiperceivable](https://github.com/aiperceivable)，Apache 2.0，OpenSSF Best Practices 认证）是面向 AI 可调用工具接口的模块标准。它把同一组织原则应用于工具描述：强制的核心层（`input_schema`、`output_schema`、`description`）先于可选的标注层（`readonly`、`destructive`、`requires_approval`、`idempotent`、`open_world`、`cacheable`、`paginated`）和可选的扩展层（`x-when-to-use`、`x-preconditions`、`x-postconditions`、`x-common-mistakes`、`x-cost-per-call`）。Python、TypeScript、Rust 的生产级 SDK 已发布；已有第三方采用。

也就是说，两个项目在**不同表面**上部署了**相同的 Core-then-Frame 分层**。**缺失的是一个协议桥** —— 当人类用户发出 CFLT 一致的自然语言请求、AI agent 通过 apcore 可感知的工具调用来履行该请求时，**认知分层须在底物边界上双向保持**。

这一桥接即**认知翻译层（Cognitive Translation Layer, CTL）**。CTL 是这一跨底物研究计划的**整合目标** —— **对社区贡献开放**。

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
│  apcore 模块标准（Core / Annotations / Extensions + ACL）        │
│  表面适配器（对 CTL 透明）：                                      │
│    apcore-mcp → MCP / OpenAI Tools                               │
│    apcore-a2a → A2A Agent Card                                   │
│    apcore-cli, flask-/fastapi-/django-/nestjs-/axum-apcore → ... │
│  已部署：生产级 SDK（Python / TypeScript / Rust）                │
└─────────────────────────────────────────────────────────────────┘
```

CTL 不取代现有的 AI 工具使用脚手架（MCP、OpenAI Function Calling、Anthropic Tool Use、A2A）。后者处理**传输与序列化** —— 工具描述**如何**到达模型。CTL 处理与此正交的问题：**认知分层如何跨越底物边界** —— 即自然语言意图的**哪些成分**映射到工具元数据的**哪些类别**，以及反向映射如何**重建可理解的回应**。

按 apcore 自身的术语（见 [apcore POSITIONING.md](https://github.com/aiperceivable/apcore)），apcore 为 AI agent 区分出**认知接口（Cognitive Interface）**，与 UI（给人）和 API（给程序）并列。CTL **延伸**这一区分，补上 Cognitive Interface 默认存在却并未自行提供的"**人 → agent 翻译层**"。

**传输无关（精确位置）。** apcore 的 POSITIONING **明确**把 apcore 定位在 MCP / A2A / CLI / REST **之下**，作为模块标准的基础层；而 `apcore-mcp`、`apcore-a2a`、`apcore-cli` 以及框架适配器（`flask-apcore`、`fastapi-apcore`、`django-apcore`、`nestjs-apcore`、`axum-apcore`）则是**表面适配器（Surface Adapters）**，把同一份**正典模块定义**投射到各个传输协议上 —— 包括"标注 → 传输提示"的映射（如 `destructive` → MCP 的 `destructiveHint`）。因此，CTL 发出的是**面向 apcore Registry 的调用**，而非传输特定的调用；表面适配器位于 CTL 下游，对 CTL **透明**。无论 AI 客户端是通过 MCP、A2A、CLI 还是 REST 接触模块，单一的 CTL 实现都能工作。在标注层的分工因此非常清晰：CTL 负责"自然语言 ↔ 标注"的**双向解析**（槽位 1 ↔ `destructive` / `requires_approval` / …）；表面适配器负责"标注 ↔ 协议提示"的**序列化**（`destructive` ↔ MCP `destructiveHint`、A2A skill 描述等）。这是**不同层级上的不同翻译**，互不重叠。

**与 apcore 11 步执行流水线的组合。** apcore 规范的流水线（POSITIONING §"11-Step Execution Pipeline"；PROTOCOL_SPEC 运行时章节）依次为：上下文处理 → 安全检查 → 模块查找 → ACL 强制 → 审批门 → 输入校验 → 前置中间件 → 执行 → 输出校验 → 后置中间件 → 结果返回。CTL **正向流终止于第 3 步（模块查找）的输入**：解析器的输出是一个面向 Registry 的调用（含 caller_id、目标模块、已校验输入、以及任何同意 / 审批的前置证据）。CTL **反向流起始于第 11 步的输出**（带 trace 的类型化结果）。中间的 4–10 步是 apcore 的职责，**保持不变** —— CTL 与流水线**组合**而不**侵入**。这个组合点正是 CTL 能够作为 apcore 之上的**库**实现、而无须修改 apcore 本身的关键。apcore SDK 中 `Executor.validate()`已经实现"纯步骤干跑"语义、返回 `PreflightResult{ checks, requiresApproval, errors, predictedChanges }` —— 这正是 CTL 正向流所需的"构造调用但不执行"组合点的**工程实体**，CTL 实现可直接复用，不需要新增 apcore API。

**`apcore-a2a` 多 agent 流下的对称性。** §4.1 中"用户陈述"是**任何 CFLT 一致语言源**的占位符。在 `apcore-a2a` 下，该源可以是**另一个 agent** 通过 Agent Card 调用某个 skill，而不必是人类。CTL 对此情形对称适用：发起方 agent 发出 CFLT 一致请求；接收方 agent 的 CTL 实例将其解析为 apcore 调用。槽位 ↔ 层级对应**在此替换下不变**，因为 CFLT 本身就是一个对"生产者是人类还是人工"中立的篇章级协议。

---

## 3. 槽位 ↔ 层级对应表

让 CTL 成为**有限可完成的研究目标**（而非开放式臆想）的实证前提，是 CFLT 四个篇章槽位与 apcore 三层元数据之间的**结构性对应**。这一对应是 CTL 研究的核心洞察；**验证它在足够代表性的人类意图样本与模块族上非平凡成立**，本身就是研究计划的一部分。

| CFLT 槽位 | 语言学功能 | 典型成分 | apcore 层级 | apcore 字段 | 跨底物功能 |
|---|---|---|---|---|---|
| **槽位 0**（Core 核心） | 事件核心 / 显著性锚点 | 谓词 + 价位绑定的论元 + 方式 + 作用域内算子 | **Core Layer 核心层** | `input_schema`、`output_schema`、`description` | 强制的功能契约 —— 这个操作**是什么** |
| **槽位 1**（Reason 理由） | 因果 / 动机框架 | *因为*、*为了*、*以便*、动机性从句 | **Annotation Layer 标注层** | `requires_approval`、`destructive`、`idempotent`、`open_world` | 治理 —— 在什么条件下该操作可以进行 |
| **槽位 2**（Space 空间） | 处所 / 作用域框架 | *在 X*、*于 Y 之内*、*跨 Z*、限定作用域的从句 | **ACL 访问控制** | `callers`、`targets`、`conditions`、`default_effect` | 权限边界 —— 该操作在系统中**何处**被允许 |
| **槽位 3**（Time 时间） | 时间 / 条件框架 | *之前*、*之后*、*当*、*如果*、*每当*、调度从句 | **Extension Layer 扩展层** | `x-when-to-use`、`x-preconditions`、`x-postconditions`、`x-workflow-hints` | 规划提示 —— 何时以及在什么工作流位置 |

**如何阅读对应表。** 两组列描述的是**同一概念结构**：一个强制的*是什么*（Core / 槽位 0），围绕它有三类可选框架 —— *为什么*（Reason / 治理）、*在哪里*（Space / 权限）、*何时*（Time / 规划）。论断**不是**映射"一一对应且穷尽" —— 自然语言比这复杂得多 —— 而是**类别对齐足够强**，足以支撑"确定性 + 后备方案"的解析策略。

**为何这非平凡。** 如果槽位 0 映射到 Core Layer，而其余三槽全都映射到一个"元数据"大筐里，那就毫不令人惊讶。**非平凡的观察**是：**CFLT 框架槽位的三个类别（理由 / 空间 / 时间）分别映射到 apcore 非核心元数据的三个类别（Annotation Layer / ACL / Extension Layer）**，且每一对都共享一个**先于本研究、独立存在于两个项目中的功能家族**（治理、权限边界、规划提示）。这是同一 Core-then-Frame 组织原则**同时作用于两个底物**的结构性证据。

**对应强度并不一致。** 上表四条对应在实证强度上**不对称**，应分级阅读：

- **强对应**：槽位 0 ↔ Core Layer —— 双方都是强制功能契约，无论语言学还是工具元数据视角都是同一回事。
- **中等对应**：槽位 3 ↔ Extension Layer —— 双方都关于"何时 / 在何工作流位置"，自然贴合 `x-when-to-use` / `x-preconditions` 等字段。
- **解释性对应**：槽位 1 ↔ Annotation Layer 与 槽位 2 ↔ ACL —— 自然语言的"理由"槽表达用户**动机**，而 Annotation 表达工具**操作属性**；"空间"槽表达事件**作用范围**，而 ACL 表达 caller-on-target 的**权限边界**。两端属于"概念邻近、轴线错位"的关系，绑定靠的是 CTL 解析器在桥上做的**类别归纳**而非语义同构。

工程含义：CTL SDK 应把槽位 ↔ 层级映射做成**可配置**（默认表 + 用户覆盖），而非硬对应。某一条对应在某个领域 / 模块族上失效，不应击穿整套桥；CTL-1 / CTL-2 也据此分条独立验证。

**与 apcore 认知接口生命周期的会聚。** apcore 的 POSITIONING.md 将 AI agent 对模块的使用分解为四阶段生命周期：**Discovery 发现**（description、schema）→ **Strategy 策略**（`x-when-to-use`、`x-common-mistakes`）→ **Governance 治理**（`requires_approval`、`destructive`、ACL）→ **Recovery 恢复**（`ai_guidance`、`retryable`）。对照 CFLT 槽位方案，这一生命周期**因式分解为同样的四个功能类别**：Discovery = 槽位 0 解析（**什么**）；Strategy = 槽位 3 绑定（**何时 / 在哪个工作流位置**）；Governance = 槽位 1（**为何**）+ 槽位 2（**何处**）；Recovery = 反向流的框架重建。

**关于"独立收敛"主张的诚实降格。** 两套模式虽在**不同时期、不同代码库**中成形，但出自共享 Core-then-Frame 先验、同一设计意图的两次落地，并非两个独立观察者的偶然会聚。这一关系仍然是该先验**可在工具元数据底物上独立落地**的有效工程证据，但不应被援引为"两个独立发现汇合"式的实证 —— 该先验在两个底物上的"双重出现"是设计选择，跨底物有效性最终须由 §6 的实证子主张（特别是 CTL-6 关于非 apcore 工具表面的对照）来支持。

**借助 `Annotations.extra` 的非侵入式扩展。** apcore PROTOCOL_SPEC §4.4.1 **规范地**定义了 `Annotations.extra.<命名空间>.<名>` 扩展映射，用于生态特定元数据（既有命名空间包括 `mcp.*`、`cli.*`、`a2a.*`）。CTL 特定的元数据 —— 例如自定义的槽位 1 同意措辞模板、槽位 3 工作流位置提示 —— 可以放在 `extra.cflt.*` / `extra.ctl.*` 之下，**无须 fork apcore 或修改正典的 Annotation 表面**。槽位 ↔ 层级对应因此**完全可以表达在 apcore 已部署的 conformance 范围内**。

---

## 4. 双向机制

CTL 是双向的。两个方向**难度不对称**：正向解析的**源表示**是良构的（CFLT 一致的自然语言），但**搜索空间**是模块 Registry；反向生成的**源表示**也良构（结构化的工具结果），但必须遵守"产出流畅的 CFLT 一致自然语言"这一约束。

**反向方向的风险声明。** 正向方向有 CoreFirst 参考实现中的 `CFLTTransformer`（Zod 严格 schema + 模板化 system prompt + JSON salvage 回退）作为可复用前驱；**反向方向在 CFLT 与 apcore 两侧均无现存基础设施**，且 CTL-3 依赖人评 rubric —— 这是 CTL 研究计划中**风险最高的单一组件**。阶段 3 之前，反向方向的实现策略（prompt 工程范式、是否复用正向 schema 形态、人评 rubric 维度）应保持开放，并优先以小规模 pilot 验证可行性。

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

**关于 Registry 检索能力的说明。** apcore Registry 当前提供精确 ID 查找与前缀枚举（见 apcore-typescript `src/registry/registry.ts`：`get/has/list/iter/getDefinition`），**不提供原生语义检索**。上述"槽位 0 → 候选模块（亲和度匹配）"由 CTL 自带的检索层（embedding 召回 + LLM 重排）实现，且其结果须收敛到 Registry 中存在的 module ID（Zod 校验）。该层属于 CTL 实现责任，不是对 apcore 的扩展要求 —— 这同时意味着 CTL 的"LLM 中立" 在 embedding 模型选择上仍存在打折空间，应在 SDK 设计中显式声明（见 §5.3）。

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

**关于"底物中立"的修饰对象。** 需要明确："底物中立"修饰的是 **Core-then-Frame 原则本身**，**不是 CTL 实现**。CTL 按定义是 CFLT 与 apcore 这一对**具体底物**之间的桥，依赖两侧的具体协议；它**操作化**底物中立原则的方式是"在这一对具体底物上落地该原则"，而非"对任意工具表面可插拔"。CTL 实现依赖 apcore 不构成对该原则的反驳，正如 HTTP/2 实现依赖 TCP 不构成对"传输层抽象"主张的反驳。其他工具表面（裸 MCP、A2A、OpenAI Tool Use 等）的对接是 §6 CTL-6 提议的**扩展实验范畴**，不在 CTL 1.0 承诺面内。

### 5.2 与相邻传统的关系

- **框架语义学（Fillmore 1982；FrameNet：Baker, Fillmore & Lowe 1998）**：CFLT 四槽方案与框架语义的角色结构**兼容但不等同**。CTL 在槽位 0 → 模块解析中利用框架语义的亲和性（槽位 0 携带谓词；模块由谓词样的功能契约类型化）。
- **Toolformer（Schick et al. 2023）** 与更广泛的 LLM 工具使用线索：CTL **位于其下游**，因为它**预设**结构化工具接口的存在；同时**位于其上游**，因为它处理 "**自然语言成分如何绑定到工具元数据类别**" 的协议级问题 —— 这是既有工具使用工作通过 ad-hoc prompting 默认解决了的。
- **Schema 强制输出（JSON 模式、structured outputs）**：CTL 把 schema 强制从 LLM 生成的**输出端**延伸到**人类意图 ↔ 工具调用**之间的**双向翻译**，并在桥上叠加治理强制。

### 5.3 CTL 不是什么

- **不是工作流引擎。** CTL 把**单个**意图映射到**单个**（或一个小的歧义消解集合的）调用。多步编排属于上游工作流引擎（apflow、LangChain、CrewAI）。
- **不是 LLM 调用库。** CTL 是 LLM 中立的；LLM 是解析器与生成器组件的一种可能实现，但协议本身不绑定特定模型。
- **不是传输协议。** CTL 叠加在 apcore 模块层之上，而 apcore 模块层又叠加在表面适配器（`apcore-mcp`、`apcore-a2a`、`apcore-cli`、各框架适配器）之上 —— 后者负责桥接到 MCP、A2A、OpenAI Tool Use 等；CTL 处理的是这些协议交给 ad-hoc prompting 的认知分层问题。
- **不是表面适配器。** `xxx-apcore` 适配器家族已经把 apcore 模块**自动投射**到具体传输上 —— 含标注 → 提示映射、Agent Card 生成、CLI 参数解析、HTTP 路由生成。CTL **严格工作在该层之上**，仅在"自然语言 ↔ apcore 模块调用"边界上活动；不与表面适配器**竞争**。
- **不是 apcore 的 fork。** CTL 特定的元数据按 apcore PROTOCOL_SPEC §4.4.1 放在 `Annotations.extra.cflt.*` / `extra.ctl.*` 命名空间下；apcore-typescript 中 `extra: Readonly<Record<string, unknown>>`（`src/module.ts`）是规范字段、运行时合并规则已定义。**CTL 可实现性不要求对 apcore 做任何规范变更。**
- **不是 LLM-free。** "LLM 中立" 指**提供商中立**（OpenAI / Anthropic / Gemini / 本地模型可换），不指**无须 LLM**。解析器、模块解析、反向线性化均由 LLM 完成；与 ad-hoc prompting 范式的区别在于**契约形态**（Zod 严格 schema + 模板化提示 + JSON salvage），不在于绕开 LLM。Embedding 模型（用于槽位 0 → 模块召回）同样不可避免，是 CTL "模型中立" 主张的已知折扣项。
- **不是跨工具表面通用桥。** CTL 协议规范当前只对 CFLT ↔ apcore 这一对底物**完整定义**。其他工具表面（裸 MCP、A2A、OpenAI Tool Use 等）的对接是 §6 CTL-6 提议的**扩展实验范畴**，不在 CTL 1.0 承诺面内 —— 即使 CTL-1 至 CTL-5 全部通过，也只能证明 "CTL 在 apcore 上 work"，跨底物中立性须由 CTL-6 单独支撑。

---

## 6. 可证伪的子主张

CTL 研究计划围绕**可证伪的子主张**组织，每一项都有明确的**证伪条件**。

### CTL-1：首次调用成功率

**主张。** 由 CTL 解析器产生的 CFLT→apcore 翻译，相对于不具备 CFLT 槽位 ↔ 层级对应的 LLM-only 基线，**首次调用成功率更高**。

**测量。** 在一个由 *N* 条人撰写的 CFLT 一致请求构成的基准之上、对一个具有混合治理元数据的 *M* 模块 Registry，比较 CTL 解析调用与基线的**首次成功**（定义：所选模块正确、input_schema 满足、未违反治理、输出 validates against output_schema）。

*关于"试次（trial）"与"请求（request）"的区分。* CFLT 预印本所述 "720 试次 pilot" = **24 条人撰 CFLT 一致请求 × 5 个前沿模型族 × 6 个实验条件**（控制 / CFLT × 干扰等级 L1–L3）。CTL-1 基准的目标 *N* 应规划为**独立的请求条数**（建议 *N* ≥ 200 以支撑 *p* < .05 的成功率比较），与试次（trials = *N* × 模型数 × 条件数）需在论文与文档中**明确区分**，避免读者把 720 试次误解为 720 条独立请求。

**证伪条件。** 如果成功率在**至少 3 个**前沿模型族上未能在 *p* < .05 改善，则 CTL 退化为 "普通的结构化意图解析"，相对既有工具使用脚手架**无协议级价值**。

### CTL-2：越权事件减少

**主张。** 相对于缺失 "槽位 1 → 标注层" 绑定的基线，CTL 中介的调用流程**减少越权事件**（agent 在 `requires_approval=True` 或 `destructive=True` 模块未先暴露同意门的情况下调用）。

**测量。** 在一组**故意同意意向暧昧**的请求基准上，比较 CTL 与基线下的越权事件计数。

**证伪条件。** 如果越权事件在**至少 3 个**前沿模型族上**绝对计数未减少**，则 "槽位 1 → 标注层" 对应**不可协议级落地**，CTL 的治理贡献被驳回。

*为何用绝对计数而非 p 值。* 越权事件在任何良构基准上都是**低基础率的稀有事件**；显著性检验在该 regime 下统计功效低。"在所有评估的模型族上绝对计数下降"因此是更保守的证伪条件。在更大量、刻意倾斜的基准上使用 *p* < .05 的更强检验，留作后期阶段扩展。

### CTL-3：反向理解性保持

**主张。** CFLT 一致地线性化结构化 apcore 结果所得到的回应，在**人评理解性**得分上**高于**原始结构化结果与 ad-hoc LLM 生成的自然语言摘要。

**测量。** 在 *K* 个三元组（原始结构化结果、ad-hoc 摘要、CTL 线性化回应）上做人评研究，以固定 rubric 打分（回应是否暴露答案？是否解释作用域？是否暴露时间有效性？）。

**证伪条件。** 如果 CTL 线性化回应在 rubric 三个维度中的至少两个上未能以 *p* < .05 优于 ad-hoc 摘要，则反向贡献被驳回。

### CTL-4：跨模型泛化

**主张。** CTL 的解析与生成行为**在前沿模型族上稳定** —— 即槽位 ↔ 层级对应是**模型独立的协议属性**，而非模型特定的偶发现象。

**测量。** 在**至少 5 个**前沿模型族（GPT-5、Claude Sonnet、Gemini、Qwen、DeepSeek）上复制 CTL-1、CTL-2、CTL-3，采用模型中立的解析器 / 生成器实现。

**证伪条件。** 如果 CTL-1、CTL-2 或 CTL-3 在不同模型族间显示统计显著的交互效应（模型族 × CTL-vs-baseline，*p* < .05），则 CTL 必须**退缩为按模型族特化的协议**，跨底物泛化被弱化。

*统计学说明。* 未能拒绝 H0（无交互效应）**不等于**确证了跨模型一致性。要正向确证跨模型泛化，还需要：(i) 每个模型上的 CTL 效应**单独**在 *p* < .05 显著；(ii) 跨模型的效应量方差落在**预先注册的等效区间**之内（TOST 等效性检验程序，Lakens 2017）。**只有三条同时满足** —— 无显著交互、单独显著、等效边界内方差 —— CTL-4 才算被**确证**，而不仅仅是**未被证伪**。

### CTL-5：表面适配器（传输）不变性

**主张。** 给定一份固定的 CFLT 一致输入与一份固定的 apcore Module Registry，CTL 解析器**应当**产出**同一**面向 apcore Registry 的调用 —— 无论该调用最终经由哪个表面适配器（`apcore-mcp`、`apcore-a2a`、`apcore-cli`、框架适配器）送达运行时。

**测量。** 在一份 *N* 条 CFLT 一致请求的基准上、针对**同一份**正典 Registry，于三种投递配置下运行 CTL 解析器：(i) apcore-mcp → MCP 传输；(ii) apcore-a2a → A2A 传输；(iii) apcore-cli → CLI 传输。在一次正典化（normalization）之后，按字节级别**比较**所发出的调用（目标 module ID、已校验输入字典、治理前置条件标志）。

**证伪条件。** 如果正典化后**≥ 5%** 的基准项在不同投递配置间发出的调用**出现分歧**，则 CTL 已**泄漏到传输层**，未严格止步于 apcore 模块层 —— 这与 §2 的底物中立主张相悖，并**驳回** CTL 作为"严格位于 apcore 之上的协议桥"的架构定位。

*为何重要。* 表面适配器不变性是 §5.1 跨底物假设的**运行操作化**。如果在**同一份** CFLT 输入下、CTL 在不同传输下发出**不同**的模块调用，则要么 (a) 解析器条件依赖了它本不该看到的传输特定状态；要么 (b) 槽位 ↔ 层级对应并未**真正归约到** apcore 正典 Module 表示。两种结果都会**证伪** CTL 作为底物中立协议桥的主张。

### CTL-6：跨工具表面外部不变性

**主张。** 槽位 ↔ 层级对应的实证收益是**底物中立的**，即：在**非 apcore** 的结构化工具表面（如裸 MCP 工具定义、OpenAI Function 描述、A2A skill 自由文本）上以等价规则配置 CTL，CTL-1 / CTL-2 的核心效应仍显著。

**测量。** 复刻 CTL-1 / CTL-2 基准到一份**等价规模**的非 apcore 工具集（建议：从公开 MCP Server 中抽取 *M* 个工具，仅保留 name / description / input_schema 三段，**移除** apcore 的 Annotation / ACL / Extension 元数据）；以 CTL 默认槽位 ↔ 层级映射的"无 apcore 元数据"版本（仅 Core 必填，治理 / 扩展信息靠工具描述自由文本兜底）跑同一对比。在每个前沿模型族上对照 CTL-on-apcore vs. CTL-on-raw-MCP 的效应量。

**证伪条件。** 如果在非 apcore 表面上 CTL-1 / CTL-2 的效应量**显著小于** apcore 表面上的效应量（**模型族 × 表面**交互效应 *p* < .05、且效应量差异落在预先注册的非等效区间外），则槽位 ↔ 层级对应的实证收益**底物依赖** —— 即依赖 apcore 自身已优化的元数据分层 —— 而非"底物中立原则"的体现。这会**驳回** §5.1 的跨底物假设。

*为何重要。* CTL-1 至 CTL-5 全部**在 apcore 内**验证；即使全部通过，也只能证明 "CTL 在 apcore 上 work"。CTL-6 是检验**底物中立性**的唯一外部实验。CTL-6 失败不会驳回 CTL 作为 CFLT ↔ apcore 桥的工程价值，但会要求文档把 §5.1 的跨底物主张降格为 "apcore-conditional"。

---

## 7. 研究路线图

CTL 研究计划组织为**多阶段方案**。两端的底物已经独立部署并被验证，是这一研究范围**可信**的前提。下列阶段按**逻辑顺序**呈现；实际执行时间表取决于研究环境（独立研究、工业研究实验室、或研究生项目）与社区参与情况。各阶段**有意设计为解耦的**：任何阶段都可以由感兴趣的研究者**不依赖任何单一贡献者的进度**地独立推进；针对单个子主张（CTL-1 至 CTL-5）的贡献也独立受欢迎。

### 阶段 1 —— 理论形式化 + 基准设计 + 包架构提案

- 把 §3 的槽位 ↔ 层级对应**形式化为类型化映射**，并明确边界行为；映射**做成可配置**（默认表 + 用户覆盖），以适应 §3 "解释性对应" 的强度不对称。
- 设计 CTL-1 / CTL-2 / CTL-3 / CTL-6 基准：组装 *N* 条 CFLT 一致请求语料、*M* 模块 apcore Registry（治理元数据按设计分布）、*M* 模块裸 MCP 对照集、CTL-3 的人评 rubric。
- 公布 **CTL spec 包结构提案**（三包拆分：`ctl-spec` 抽象类型 / `ctl` 编排 + 默认适配器 / `ctl-eval` 评测 harness），明确：
  - **prototype 阶段**：两个适配器（`ctl-adapter-corefirst`、`ctl-adapter-apcore`）住在 CTL 自己的 repo，**不进入 CFLT 或 apcore 任一仓库**，保持 §1 / §10 的"两个项目独立部署"承诺。
  - **stabilization 阶段**：按 `apcore-mcp` / `apcore-a2a` 先例，把原生侧适配器迁移到各自生态（`apcore-ctl` 入 apcore，`corefirst-ctl` 入 corefirst）。迁移**触发条件**：spec 1.0.0 + ≥ 6 个月无 breaking + 至少一条子主张获正面证据 + 出现第二采用方。
- 发表：一篇理论立场论文(目标 venue：*Cognitive Science*、*Topics in Cognitive Science* 或主要 AI 对齐 workshop)。

### 阶段 2 —— 正向原型 + CTL-1、CTL-2、CTL-5 评估

- 把 CTL 正向解析器实现为模型中立库，可从任意 LLM provider 调用；复用 CoreFirst `CFLTTransformer` 作为解析前驱，apcore-typescript `executor.validate()` 作为治理门组合点。
- 在至少 5 个前沿模型族上跑 CTL-1 与 CTL-2 评估。
- **同期交付 CTL-5**：表面适配器不变性 —— 对同一份 CFLT 输入 + 同一份 Registry，比对 `apcore-mcp` / `apcore-a2a` / `apcore-cli` 三种投递路径下 CTL 发出的调用是否字节一致。该项**不依赖 LLM 评测预算**，可作为整个研究计划的第一条早期工程信号。
- 发表：一篇正向性能实证论文(目标 venue：ACL、EMNLP、NAACL 或 NeurIPS Datasets & Benchmarks)。

### 阶段 3 —— 反向原型 + CTL-3、CTL-4 评估

- 实现 CTL 反向生成器，包括 §4.3 的治理解释、同意门、恢复建议流程。
- 跑 CTL-3 人评研究与 CTL-4 跨模型泛化分析。
- 发表：一篇反向理解性实证论文 + 一篇跨模型泛化论文。

### 阶段 4 —— 整合 + 综合

- 整合研究：把 CTL 部署进 CoreFirst 参考应用(支柱 I)，测量 CTL 中介与基线交互下的端到端任务完成率。
- 把阶段 1–3 综合为统一的跨底物研究产出。
- 公开交付物：一份 CTL 规范文档(类比 apcore PROTOCOL_SPEC)，适合独立第三方实现。

---

## 8. 不在范围内

CTL 研究计划**不**致力于交付以下任何一项：

- **工作流引擎**，把多次 CTL 中介调用串成多步计划。归属上游工具（apflow、LangChain、CrewAI）。
- **新传输协议**，与 MCP、A2A、OpenAI Tool Use 竞争。CTL 叠加在 apcore 所采用的任何传输之上。
- **新 LLM**。解析器与生成器组件 LLM 中立；LLM 是可替换的实现之一。
- **产品化的 SaaS 桥接服务。** 与 CFLT 本身一样，CTL 是协议规范；产品化是独立组织的工作。
- **槽位 ↔ 层级对应的自动定理证明器。** 该对应是**经验性辩护的主张**，不是逻辑推导；它的支持来自 CTL-1 至 CTL-5，而非形式证明。

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

**关于 CTL-5 与 CTL-6 的说明。** 在 §6 的六条可证伪子主张中，**CTL-5 与 CTL-6 都不依赖**上述六个 CFLT 子计划：

- **CTL-5**（表面适配器不变性）检验 apcore 侧的**结构性属性** —— 即 CTL 解析器在 apcore 模块层处洁净终止、不向传输层泄漏状态 —— 因此直接对 `apcore-mcp` / `apcore-a2a` / `apcore-cli` 评估。
- **CTL-6**（跨工具表面外部不变性）检验**底物中立假设的外部支撑** —— 即槽位 ↔ 层级对应在非 apcore 工具表面上是否仍带来效应 —— 因此对裸 MCP / OpenAI Tool / A2A skill 评估。

这两条**独立于 CFLT 实证基础**是设计如此：CTL 的"跨底物"主张分两条腿 —— 一条朝 apcore 内部（CTL-5），一条朝 apcore 外部（CTL-6），都与 CTL 在 CFLT 一侧的扎根相互独立。

---

## 10. 状态

本文档描述一个**规划中**的研究计划。**撰写时尚无 CTL 实现。** 两个底物端（CFLT、apcore）已独立部署并对公众开放查阅；CTL 是其桥接，其**规范与实证评估**构成规划中的贡献。执行路径开放：独立研究者、工业团队和研究生**都欢迎**推进本计划 —— **没有任何路径被特权化**。本计划保持**开放**，由有兴趣推进它的任何人共同推进；在任何阶段或任何子主张上的参与都受欢迎。

作者维护本文档、CFLT 框架（cflt.center）、apcore 标准（github.com/aiperceivable）作为**独立的开源工作**（许可宽松）。欢迎就**指导、合作或独立实现**进行问询 —— 可直接邮件（tercel.yi@gmail.com；ORCID [0009-0000-3742-4403](https://orcid.org/0009-0000-3742-4403)），或经 [cflt.center](https://cflt.center) 列出的项目渠道。

**关于代码仓位置。** CTL 实现（含 `ctl-spec`、`ctl`、`ctl-eval`、以及 prototype 阶段的两个适配器 `ctl-adapter-corefirst` 与 `ctl-adapter-apcore`）将住在**独立的第三 repo**，**不进入 CFLT 或 apcore 任一仓库**，以保持两侧"独立部署的开源项目"承诺（见 §1、§5.3）。仅当 spec 1.0.0 稳定（≥ 6 个月无 breaking）、至少一条子主张获正面证据、且出现第二采用方时，才按 `apcore-mcp` 先例把原生侧适配器移交回各自生态。在那之前，CFLT 与 apcore 仓库**对 CTL 零依赖**。

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
- Yi, W. (2026). *Core-First Language Theory (CFLT): A Discourse-Level Linearization Protocol.* Zenodo（归档 DOI 待存档）.

---

*文档版本：1.0.0（内部草案）*
*状态：研究路线图。撰写时尚无 CTL 实现。*
*作者：CFLT 核心团队*
