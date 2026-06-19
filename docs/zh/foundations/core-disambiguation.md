# 核心消歧：规范性参考

> **版本：** 1.0.0 (内部草案)
> **目的：** 为人类学习者、课程设计者和 LLM 评分系统提供一个明确、可操作的“核心 (Core)”边界定义。

---

## 1. 核心的操作化定义

在 CFLT 中，**核心 (Core)** (槽位 0) 是话语的**显著性锚点 (Salience Anchor)**。它代表了说话者意图断言的主要事件、状态、系属或指令。

**正式边界规则**（规范性分类与 [`core-concept.md`](./core-concept.md) §9 的"为实现者准备的正式定义"一致；本节是其操作性复述）：

核心由以下四组构成：
1.  **谓词**（事件、状态、系属或指令）。
2.  由谓词授权的**价位绑定参与者**（主语、宾语、工具、受益者、接受者、伴随对象）。"*当改变某个论元会改变事件身份时，该论元属于价位绑定*"这一规则是一项 **CFLT 自定义的操作性测试**（即 [`core-concept.md`](./core-concept.md) §2.2 的替换测试），它受到 Levin & Rappaport Hovav (2005) 事件结构理论的启发，但并非由其推导得出；该理论本身并未提供这种基于事件身份的论元判定测试。还需注意，改变一个附加语可能改变所描述的事件 token，却不使其成为动词授权的论元，因此 CFLT 将下文的工具/受益者归类视为一项需按谓词和构式逐一检验的项目约定，而非从来源直接读出的结论：只要动词授权工具和受益者，CFLT 就将它们归类为价位绑定（而非"内部修饰语"）。
3.  **核内 / 核心层方式状语**（动作方式、运动方式）。
4.  以事件为论元的**辖域内算子**：否定、情态、时体、程度。

按 **CFLT 约定**，任何回答 **"如何？"**、**"用什么？"**、**"为/给谁？"**、**"与谁一起？"**、**"以何种情态？"**、**"是否被否定？"** 或 **"到什么程度？"** 的修饰语都归入核心内部（属于上面第 2–4 组）；任何回答 **"为什么？"**、**"在哪里？"** 或 **"何时？"** 的修饰语都被剥离到槽位 1、2 或 3。这种基于提问的划分是一项 **CFLT 自定义的边界**，而非从所引语义学推导出的主张：程度语义学理论（如 Kennedy 1999）解释了程度如何与形容词/谓词进行局部组合，但并未确立程度、方式和事件内部品质构成单一的统一范畴，也未确立它们占据同一个 CFLT 槽位 —— 这一归组是一项 CFLT 操作性定义，需要话语层面的位置检验。

---

## 2. 关键消歧规则

### 2.1 “认识论对冲” vs “报道”规则
*问题案例：* "I think we should leave." (我觉得我们该走了。)

- **规则（认识论对冲）：** 如果“我觉得 (I think)”或“我相信 (I believe)”的作用是软化或限定说话者自己的断言，它被视为**情态修饰语 (Modal Modifier)** 并保留在**核心内部**。
    - *核心：* "I think we should leave"
- **规则（报道）：** 如果句子是在报道他人的心理状态或特定的思考行为，那么该心理动词就是**谓词**。
    - *示例：* "He thinks we should leave." (他觉得我们该走了。)
    - *核心：* "He thinks [that we should leave]" (注：嵌套从句是参与者/宾语)。

### 2.2 “天气与方式”规则
*问题案例：* "It's raining heavily in Tokyo." (东京正下着大雨。)

- **规则（CFLT 约定）：** CFLT 将程度或方式副词（如 *heavily, slightly, quickly*）视为描述事件的内部品质而非外部框架，因而将其置于核心内部。这是一项项目位置约定，而非从程度语义学推导出的结论。
- **决策：** "Heavily" 是方式修饰语 → **在核心内部**。
- **结果：**
    - *核心：* "It's raining heavily"
    - *空间：* "in Tokyo"

### 2.3 “工具 vs 空间”规则
*问题案例：* "I'm working on my laptop in the cafe." (我在咖啡馆用笔记本电脑工作。)

- **规则：** 如果位置是执行动作的*媒介*，它就是**工具**（核内）。如果它是说话者所在的*物理地点*，它就是**空间**（槽位 2）。
- **决策：** "on my laptop" 是工具 → **在核心内部**。"in the cafe" 是地点 → **槽位 2**。
- **结果：**
    - *核心：* "I'm working on my laptop"
    - *空间：* "in the cafe"

---

## 3. 核心边界判定树

请按照以下步骤隔离核心：

1.  **确定主要断言：** 什么是“图形 (Figure)”或“事件”？
2.  **应用“同一事件？”测试：** 如果去掉修饰语，事件的性质或品质会改变吗？
    - *是（例如“慢慢地”、“用黄油”）：* 修饰语在**核心内部**。
    - *否（例如“在下午 5 点”、“在家里”）：* 修饰语在**核心外部（场景框架）**。
3.  **RST 过滤器：** 该修饰语是否回答“为什么 (Why)”、“在哪里 (Where)”或“何时 (When)”？
    - *是：* 移动到槽位 1、2 或 3。
    - *否（且它不是参与者）：* 它作为内部修饰语（方式/工具/情态）属于核心。

---

## 4. 压力测试：20 个边界案例

| # | 句子 | 核心边界 | 逻辑 |
|---|---|---|---|
| 1 | I think it might rain. | *I think it might rain* | 认识论对冲 (情态) + 事件。 |
| 2 | He said he was tired. | *He said he was tired* | 报道言语；"said" 是锚点。 |
| 3 | I'm studying English hard. | *I'm studying English hard* | "Hard" 是方式 (程度)。 |
| 4 | It's boiling hot today. | *It's boiling hot* | "Boiling" 是状态的程度/品质。 |
| 5 | I'll go by car tomorrow. | *I'll go by car* | "By car" 是工具。 |
| 6 | Please sit down here. | *Please sit down* | "Please" 是礼貌标记 (核内)。 |
| 7 | I'm writing via Slack. | *I'm writing via Slack* | "Via Slack" 是媒介 (工具)。 |
| 8 | I'm writing about AI. | *I'm writing about AI* | "About AI" 是动词的论点/宾语。 |
| 9 | I'm exhausted from work. | *I'm exhausted* [理由: from work] | "From work" 是原因 (槽位 1)。 |
| 10 | I baked a cake for you. | *I baked a cake for you* | "For you" 是受益者。 |
| 11 | I read the news on my phone. | *I read the news on my phone* | "On my phone" 是工具。 |
| 12 | It's dark in this room. | *It's dark* [空间: in this room] | "In this room" 是空间 (槽位 2)。 |
| 13 | I'll call you if I can. | *I'll call you* [理由: if I can] | "If I can" 是条件 (槽位 1)。 |
| 14 | She's a doctor in Paris. | *She's a doctor* [空间: in Paris] | 系属核心 + 空间。 |
| 15 | I'm definitely coming. | *I'm definitely coming* | "Definitely" 是情态。 |
| 16 | I haven't eaten yet. | *I haven't eaten* [时间: yet] | "Yet" 是时间 (槽位 3)。 |
| 17 | I'm walking with a cane. | *I'm walking with a cane* | "With a cane" 是工具。 |
| 18 | I'm walking with John. | *I'm walking with John* | "With John" 是伴随。 |
| 19 | I'm working at Google. | *I'm working* [空间: at Google] | "At Google" 是空间 (地点)。 |
| 20 | He's probably joking. | *He's probably joking* | "Probably" 是情态。 |

---

## 5. AI 训练摘要

在生成或验证 CFLT 数据时：
- **默认包含：** 当在“方式”和“空间”之间犹豫不决时，如果修饰语描述的是动词的“如何”（例如 "via API", "on the web"），请将其保留在核心内部。
- **RST 排除：** 仅剥离提供外部框架（理由、空间、时间）的修饰语。
