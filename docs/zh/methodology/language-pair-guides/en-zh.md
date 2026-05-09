# 英语 ↔ 汉语：CFLT 操作化

> **版本：** 1.0.0（内部草案）
> **许可：** [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)

> **目标读者。** 英语母语的普通话学习者（以及反向中等规模）。全球最大学习者群体。

---

## 1. 语言对特定的类型学说明

| 属性 | 英语 | 汉语（普通话） |
|---|---|---|
| **默认词序** | SVO | SVO（带强主题优先叠加） |
| **时态形态？** | 是（-ed、-ing、will 等） | 无（用体助词 了/过/着 + 时间副词） |
| **格标？** | 极少（仅在代词上：I/me、he/him） | 无 |
| **主题优先？** | 否（主语优先） | **是（强烈）** |
| **冠词系统？** | 是（a/the） | 无 |
| **复数标记？** | 是（-s） | 名词无；只对有生名词用 们 |
| **省略主语？** | 否（要求主语） | 是（主语常省略） |

**对 CFLT 的关键含义。** 两种语言共享 SVO 基础顺序，使 Core 内部组装相对可移植。主要摩擦在于**英语要求显式主语和时态形态**，而汉语通过语境+体助词编码两者。这意味着 CFLT-汉语可以比 CFLT-英语更紧凑；渲染汉语时不要强加英语式的显式性。

---

## 2. 事件核组装差异

同一个 Core "我昨天买了一本书" 组装为：

- **英语**：*I bought a book* —— S + V（带过去时态形态）+ O
- **汉语**：*我买了一本书* —— S + V + 了（完成体）+ O —— 同样 SVO 顺序，无过去时态形态，动词带完成体标记

两个 Core 都是 SVO；英语强制时态，汉语用体貌。两者都属于 **Core 内部**（动词形态/动词附助词）。

---

## 3. 语言对特定的 edge case

### 3.1 汉语主题前置无英语对应

汉语允许激进的主题化，无英语整齐对应：*这本书我看了三遍*（As-for-this-book, I've-read-it three times）。在 CFLT-汉语中，主题可移到 Core 之前；在 CFLT-英语中，同一思想用 "as for" 结构或保持默认 SVO。

**en→zh 规则**：当英语用强对比焦点或 *"As for X..."* 时，渲染汉语用主题前置。当英语是普通 SVO 时，保持汉语 SVO。

**zh→en 规则**：汉语 Core 之前的主题通常渲染为英语主语（如果简单）或 "as for X" 结构（如果对比）。

### 3.2 汉语 把 (bǎ) 字句

把字句（*我把书看完了*）是 Core 内部 —— 把定指受事前置到动词前。英语无直接对应；它表面为带定冠词的普通 SVO：*I finished the book*。

**规则**：两者都留在 Core 内。CFLT 不要求把字句与英语 SVO 之间的结构对齐；两者都是同一 Core 槽位的有效组装选择。

### 3.3 时态 vs 体貌

- 英语强制每个有限动词带时态。这留在 Core 内（动词形态）。
- 汉语用体貌（了/过/着）—— 也留在 Core 内。时间状语进入时间槽。

**陷阱**：在汉语 CFLT 中渲染英语过去时句子时，如果时间状语已消歧，不要加 了。地道汉语：*昨天我看书*（yesterday I read book）不带 了 即可。加了可能过度标记。

### 3.4 汉语连动词 / 介词类动词构造

*我用刀切肉*（I use knife cut meat）→ 连动词 用 在 Core 内引入工具。与英语 *I cut the meat with a knife* 相同 —— 工具在 Core 内，通过连动词（汉）vs 介词（英）表达。语言之间无 CFLT 变化。

### 3.5 汉语结果补语复合

*我吃饱了*（I eat-full PERF）—— 动词+结果补语。这是一个 **Core 内**复合谓词。英语通常译为 "I am full from eating" 或 "I ate until full" —— 同 Core，不同表面构成性。两者都留在 Core 内。

---

## 4. 完整例句

### 例 1 —— 基本动作带原因和时间

- **英语原始**：*Yesterday it rained, so I stayed home and didn't go out.*
- **英语 CFLT**：*I didn't go out, because it rained, at home, yesterday.*
- **汉语 CFLT**：*我没出去，因为下雨，在家，昨天。*

### 例 2 —— 请求带礼貌

- **英语 CFLT**：*Could you please pass the salt, on the table, now?*
- **汉语 CFLT**：*请帮我递一下盐，在桌上，现在。*

礼貌标记（*please* / *请*）在 CFLT 教学层被打包进 Core（请求型）；在标准言语行为理论（Searle 1975）中它们运作在*施事力*层而非命题内容层 —— 警示参见 [`slot-disambiguation.md`](../slot-disambiguation.md) §3 第 15 条。

### 例 3 —— 条件带未来

- **英语 CFLT**：*I will buy you coffee, if you finish the report, in the office, tomorrow.*
- **汉语 CFLT**：*我请你喝咖啡，如果你完成报告，在办公室，明天。*

注：汉语未来由 明天 + 缺失过去标记暗示；不需要助动词。

### 例 4 —— 方式 + 工具在 Core 内

- **英语 CFLT**：*I baked the cake with butter, slowly, for my mom, in the kitchen, yesterday.*
- **汉语 CFLT**：*我用黄油慢慢地为妈妈烤了一个蛋糕，在厨房里，昨天。*

四者（工具 用黄油/with butter、方式 慢慢地/slowly、受益者 为妈妈/for my mom、动词+受事 烤了一个蛋糕/baked the cake）都在 Core 内。

### 例 5 —— 主题结构保留

- **英语原始**：*As for that book, I read it three times.*
- **英语 CFLT**：*I read that book three times.*（默认 SVO）
- **汉语 CFLT（主题前置）**：*那本书，我看了三遍。*（主题前置，Core 内）
- **汉语 CFLT（默认 SVO）**：*我看了那本书三遍。*

两种汉语变体都有效；为匹配英语 "as for" 结构的强调，选主题前置。

---

## 5. 常见学习者陷阱

### 5.1 英语母语者学汉语：过度使用主语

英语在每句话中都要求 *I*、*you*、*he*。汉语在语境允许时省略它们。CFLT-汉语应遵循汉语省略主语习惯 —— 如果听者能恢复主语，不要在每个 Core 中强制 *我*。

### 5.2 英语母语者学汉语：在汉语省略时使用 是

汉语身份陈述只在 "X 是 Y" 中用 是 作系动词；形容词谓语用 *X 很 形容词*（无系动词）。英语母语者常写 *她是漂亮的*（用 是 + 的）而不是 *她很漂亮*。CFLT 不控制此 —— 这是纯 Core 内汉语句法 —— 但需注意汉语状态型 Core 通常带 很 而非 是。

### 5.3 中文母语者学英语：缺失时态

反向陷阱。CFLT-英语 Core 必须带时态形态；渲染 *I go yesterday* 不合语法。时间槽中的 昨天/yesterday 触发英语动词的过去时（"后向时间约束"；参见 [`../human-learning.md`](../human-learning.md) §2.1）。

### 5.4 中文母语者学英语：缺失冠词

冠词系统（a/the）无汉语对应。CFLT 不为冠词分配槽位 —— 它们是 Core 内的英语名词短语句法。需要意识，但不是 CFLT 协议问题。

---

## 6. 验证清单

1. ☐ Core 在槽位 0；场景框架槽位按 R-S-T 顺序跟随
2. ☐ 英语 Core 有显式主语和时态；汉语 Core 可省略主语
3. ☐ 体助词（了/过/着）在 Core 内，不在时间槽
4. ☐ 当英语语境要求 "as for X" 时，使用主题前置（汉语）
5. ☐ 把字句留在 Core 内；不机械地与英语结构对齐
6. ☐ 冠词系统（英语）在 Core 内的 NP 处理，不作为单独槽位
