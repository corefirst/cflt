# 术语索引与缩写表

> **版本：** 1.0.0（内部草案）
> **作者：** CFLT 核心团队
> **组织：** [CFLT.center](https://cflt.center)
> **许可：** [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)

> **目的：** 为 CFLT 文档中出现的每一个缩写、技术术语、专有名词简称提供单一查阅入口。遇到不熟悉的缩写请先来这里；交叉引用指向相应基础文档作深入处理。

---

## 1. CFLT 项目术语

| 术语 | 展开 | 定义 |
|---|---|---|
| **CFLT** | Core-First Language Theory（核心优先语言理论） | 该框架的伞名 —— 同时涵盖学术理论与操作协议。参见 [`manifesto.md`](./manifesto.md)。 |
| **CFLT 协议** | — | 具体的操作排序规则：`[核心] → [理由] → [空间] → [时间]`。 |
| **CFLT 形式** | — | 在 CFLT 协议下产出的输出 —— 可理解（尚未地道）的目标语言话语。 |
| **CFLT-L2** | — | 用学习者 L2（目标语言）渲染的 CFLT 形式。 |
| **事件核（Event Nucleus）** | — | 核心槽的内部结构：谓词 + 价位绑定参与者 + 方式状语。参见 [`foundations/core-concept.md`](./foundations/core-concept.md) §2.1。 |
| **场景框架（Ground Frame）** | — | 三个情境槽位（理由 / 空间 / 时间），为事件提供框架。 |
| **语法叠加层（Grammar Overlay）** | — | CFLT 之后的润色层，将 CFLT 形式转换为地道 L2。 |
| **显著性锚点（Salience anchor）** | — | 占据位置 0 的认知对象；说话者所"承诺"的内容。参见 [`foundations/core-concept.md`](./foundations/core-concept.md) §1。 |
| **L1 / L2** | First / Second Language | L1 = 学习者的母语；L2 = 正在学习的目标语言。**两者都相对于学习者，不相对于英语** —— 对于母语汉语、目标日语的学习者，L1 = 汉语、L2 = 日语，英语不在该对中。CFLT 支持任意对任意的语言对，不强制英语作为中介。分层普适性参见 [`foundations/core-concept.md`](./foundations/core-concept.md) §2.3。 |

### 相关项目（独立于 CFLT 自身）

| 术语 | 状态 | 定义 |
|---|---|---|
| **CoreFirst**（[corefirst.world](https://corefirst.world)） | 官方参考实验项目 | 实现 CFLT 协议的 Next.js 应用，用于支柱 I（人类双语教育）。由独立于 CFLT 规范机构的组织维护。欢迎其他实现 —— 参见 [`reference-implementations.md`](./reference-implementations.md)。 |
| **apcore**（[github.com/aiperceivable/apcore](https://github.com/aiperceivable/apcore)） | 独立工具链 | 开源库套件（apcore-mcp、apcore-cli、apcore-sdk 等），某些团队可用其把 CFLT 集成进 AI 助手、批量处理语料或同步学习状态。**与 CFLT 独立** —— 既不是依赖也不是交付物。 |

### CFLT 自定义评估指标

| 术语 | 展开 | 定义 |
|---|---|---|
| **AOL** | Articulation Onset Latency（发音启动延迟） | 从意图形成到首词发音的时间。参见 [`methodology/evaluation-metrics.md`](./methodology/evaluation-metrics.md) §2。 |
| **CLI** | Cognitive Load Index（认知负荷指数） | L2 产出过程中工作记忆负担的复合指标。 |
| **IPS** | Intent Preservation Score（意图保留得分） | LLM 稳定性指标 —— 在提示词变体下保留用户意图的生成比例。 |
| **HR** | Hallucination Rate（幻觉率） | LLM 稳定性指标 —— 与给定上下文矛盾的生成比例。 |

---

## 2. 词序类型学

> **S = Subject（主语）、V = Verb（动词）、O = Object（宾语）。** 这些字母描述及物陈述句中三个成分的默认表面语序。参见 [`foundations/linguistics.md`](./foundations/linguistics.md) §1.1。

| 术语 | 定义 | 示例语言 |
|---|---|---|
| **SOV** | 主语–宾语–动词 | 日语、韩语、土耳其语、印地语（约占世界语言 45%） |
| **SVO** | 主语–动词–宾语 | 英语、汉语普通话、西班牙语、俄语（约 42%） |
| **VSO** | 动词–主语–宾语 | 威尔士语、古典阿拉伯语、塔加洛语（约 9%） |
| **VOS** | 动词–宾语–主语 | 马达加斯加语、部分玛雅语（罕见） |
| **OVS** | 宾语–动词–主语 | Hixkaryana 语（极罕见） |
| **OSV** | 宾语–主语–动词 | Warao 语、Yoda 式英语（极罕见） |
| **V2** | 动词第二位（Verb-Second） | 主句中定式动词总位于第二位置。德语、荷兰语、意第绪语。 |
| **head-final（中心语在后）** | — | 修饰语在中心语之前（如英语形容词在名词前："*red* car"）；SOV 语言典型。 |
| **head-initial（中心语在前）** | — | 中心语在修饰语之前（如法语名词在形容词前："voiture *rouge*"）；SVO 与 VSO 语言典型。 |
| **topic-prominent（主题优先）** | — | 子句围绕主题-评论而非主语-谓语组织。汉语普通话、日语、韩语。（Li & Thompson 1976） |

---

## 3. 语言学概念与框架

| 术语 | 展开 | 定义 |
|---|---|---|
| **UG** | Universal Grammar（普遍语法） | 乔姆斯基假说：人类共享天生的语言机能。 |
| **LAD** | Language Acquisition Device（语言习得装置） | 支持语言学习的假设性天生认知模块（乔姆斯基）。 |
| **NSM** | Natural Semantic Metalanguage（自然语义元语言） | Wierzbicka 的 ~65 个普遍语义原语集合（如 I、YOU、THIS、GOOD、BIG、BECAUSE），所有语言都能表达。 |
| **EIC** | Early Immediate Constituents（早期立即成分） | Hawkins (1994) 的解析效率原则：理解者偏好主要成分能尽早被识别的结构。 |
| **CRD** | Constituent Recognition Domain（成分识别域） | 识别短语所有立即成分所需的词跨度（Hawkins 1994）。 |
| **UID** | Uniform Information Density（均匀信息密度） | 假说（Levy & Jaeger 2007）：说话者在句中均匀分配信息以避免局部处理峰值。 |
| **CCG** | Combinatory Categorial Grammar（组合范畴语法） | Steedman (2000) 的词汇化语法形式 —— 句法范畴是类型，组合是类型组合。 |
| **DRT** | Discourse Representation Theory（话语表征理论） | Kamp (1981) 关于听者如何在话语展开过程中构建心理表征的模型。 |
| **SFL** | Systemic Functional Linguistics（系统功能语言学） | Halliday 围绕意义生成功能（概念/人际/语篇）组织的语法传统。 |
| **CD** | Communicative Dynamism（交际动态性） | 布拉格学派概念：每个子句成分携带的"新颖性"或信息推力程度（Firbas 1992）。 |
| **IPA** | International Phonetic Alphabet（国际音标） | 跨语言表示音素的标准化语音符号系统。 |
| **图形-背景（Figure-Ground）** | — | Talmy (2000) 的认知区分：图形是显著/前景化的实体；背景是参考框架。 |
| **profile/base（轮廓/基础）** | — | Langacker (1987) 认知语法的一对：*轮廓*是表达式相对于其概念*基础*所前景化的实体。 |
| **主题/述题（Theme/Rheme）** | — | 布拉格学派信息结构：主题是信息所谈论的对象；述题是关于主题所说的内容。 |
| **主题-评论（Topic-Comment）** | — | 类似主题/述题，但专门用于主题优先语言（Li & Thompson 1976）。 |
| **言外行为（illocutionary act）** | — | Searle 用语 —— 说话者通过话语*所做*的事（断言、请求、承诺等）。 |
| **言语行为（speech act）** | — | 言外行为的同义词（Austin、Searle）。 |

---

## 4. 教学法与第二语言习得

| 术语 | 展开 | 定义 |
|---|---|---|
| **SLA** | Second Language Acquisition（第二语言习得） | 研究非母语如何被学习的领域。 |
| **TBLT** | Task-Based Language Teaching（任务型语言教学） | 以有意义的任务为教学单元的方法（Long、Ellis、Skehan）。 |
| **ZPD** | Zone of Proximal Development（最近发展区） | Vygotsky (1978) 关于学习者独立能做与即便有助也做不到之间的区间。 |
| ***i+1*** | — | Krashen 用以表示略高于学习者当前水平 *i* 的输入。 |
| **情感过滤（Affective Filter）** | — | Krashen 假设的情感屏障（焦虑、低动机），阻止输入到达 LAD。 |
| **监控模型（Monitor Model）** | — | Krashen (1982) 的 L2 习得五假设模型：习得-学习、监控、自然顺序、输入、情感过滤。 |
| **技能习得理论（Skill Acquisition Theory）** | — | DeKeyser 关于 L2 掌握的解释 —— 从陈述性 → 程序性 → 自动化知识的过渡。 |
| **认知负荷理论（Cognitive Load Theory）** | — | Sweller (1988, 2011) 区分内在 / 外在 / 关联负荷的工作记忆框架。 |

---

## 5. 神经科学

| 术语 | 展开 | 定义 |
|---|---|---|
| **PFC** | Prefrontal Cortex（前额叶皮层） | 大脑的"执行控制"区；制约成人 L2 产出。 |
| **DLPFC** | Dorsolateral Prefrontal Cortex（背外侧前额叶皮层） | 涉及工作记忆与冲突监测的特定 PFC 子区。 |
| **BG** | Basal Ganglia（基底神经节） | 支持程序性 / 自动化技能执行的皮层下结构。 |
| **SN** | Salience Network（显著性网络） | 锚定于前岛叶与 dACC 的脑网络，检测并优先处理显著刺激。 |
| **DMN** | Default Mode Network（默认模式网络） | 在内向思维（走神、自传体回忆）期间活跃的脑网络。 |
| **CEN** | Central Executive Network（中央执行网络） | 支持目标导向任务聚焦的脑网络（亦称额顶控制网络）。 |
| **dACC** | Dorsal Anterior Cingulate Cortex（背侧前扣带皮层） | 冲突监测与显著性检测的核心区（SN 的一部分）。 |
| **AI**（神经科学语境下） | Anterior Insula（前岛叶） | 整合内感觉与显著性信号的脑区（SN 的一部分）。**不是**人工智能。 |
| **LIFG** | Left Inferior Frontal Gyrus（左下额回） | 包含 Broca 区、对句法处理至关重要的脑区。 |
| **BA** | Brodmann Area（Brodmann 分区） | 大脑皮层的经典编号分区（如 BA 44、BA 45 = Broca 区）。 |
| **WM** | Working Memory（工作记忆） | 认知任务期间使用的短时活跃记忆（Baddeley；Cowan）。 |
| **ERP** | Event-Related Potential（事件相关电位） | 通过 EEG 测量的、与刺激时间锁定的电生理信号。 |
| **P600** | — | 刺激后约 600 毫秒达到峰值的特定 ERP 成分，与句法重新分析相关。 |

---

## 6. 数学与信息论

| 术语 | 展开 | 定义 |
|---|---|---|
| **KL 散度** | Kullback-Leibler divergence | 两个概率分布之间的非对称差异度量。 |
| **DAG** | Directed Acyclic Graph（有向无环图） | 边有方向且无环的图；本文用于语义结构。 |
| **条件熵** | $H(Y \mid X)$ | 在已知 $X$ 的情况下对 $Y$ 的不确定性。 |
| **马尔可夫链（Markov chain）** | — | 下一状态只依赖于当前状态的随机过程。 |
| **σ 函数** | — | 把语义图映射到表面语序的线性化函数。参见 [`foundations/mathematics.md`](./foundations/mathematics.md) §1。 |

---

## 7. 大语言模型与 NLP

| 术语 | 展开 | 定义 |
|---|---|---|
| **LLM** | Large Language Model（大语言模型） | 通常基于 Transformer、参数量数十亿、用文本训练的神经网络。 |
| **NLP** | Natural Language Processing（自然语言处理） | 计算式语言理解与生成的领域。 |
| **AI**（计算语境下） | Artificial Intelligence（人工智能） | 机器智能的总领域。（神经科学语境下 "AI" = 前岛叶，参见 §5。） |
| **NLU / NLG** | Natural Language Understanding / Generation（自然语言理解 / 生成） | NLP 的子领域。 |
| **GPT** | Generative Pre-trained Transformer（生成式预训练 Transformer） | OpenAI 的自回归 LLM 系列。 |
| **BERT** | Bidirectional Encoder Representations from Transformers | Google 的纯编码器 LLM（2018）。 |
| **MLM** | Masked Language Modeling（掩码语言建模） | BERT 使用的预训练目标（预测被掩盖的 token）。 |
| **ICL** | In-Context Learning（上下文学习） | LLM 通过提示词中的示例学习任务，无需更新参数。 |
| **RAG** | Retrieval-Augmented Generation（检索增强生成） | 将检索得到的文档作为上下文提供给 LLM 的工作流（Lewis et al. 2020）。 |
| **注意力槽（Attention Sink）** | — | 初始 token 累积不成比例的注意力权重（Xiao et al. 2024）；CFLT "核心居首" 主张在 LLM 层的基础。 |
| **Lost-in-the-Middle（迷失在中部）** | — | 长上下文任务中的 U 型准确率曲线：开头与结尾的信息比中间的信息恢复得更好（Liu et al. 2023）。 |
| **前缀缓存（Prefix caching）** | — | LLM 推理优化：复用共享提示词前缀的计算（vLLM APC、SGLang RadixAttention）。 |
| **APC** | Automatic Prefix Caching（自动前缀缓存） | vLLM 的前缀缓存机制。 |
| **TTFT** | Time To First Token（首个 token 时间） | 延迟指标：从请求提交到首个生成 token 的时间。 |
| **KV 缓存** | Key-Value cache | 解码步骤间存储的 Transformer 注意力键 / 值张量；前缀缓存的主要对象。 |
| **TTS** | Text-to-Speech（文本转语音） | 从文本输入合成语音的过程。 |

### 基准与会议（偶尔引用）

| 术语 | 定义 |
|---|---|
| **MMLU** | Massive Multitask Language Understanding —— 广泛的 LLM 评估基准（Hendrycks et al. 2021）。 |
| **TOON** | Token-Optimized Object Notation —— 一种轻量提示词编码格式。 |
| **DOVE** | Diverse Optimization for the Verbalization Effect —— 关于提示词线性化敏感性的研究（ACL Findings 2025）。 |
| **ACL** / **NAACL** / **EMNLP** | 主要 NLP 会议（计算语言学协会；北美分会；自然语言处理实证方法）。 |
| **ICLR** / **NeurIPS** | 主要机器学习会议（国际学习表征会议；神经信息处理系统）。 |

---

## 8. 作者姓名与理论简称

文档以姓氏引用理论家。最常见者的速查：

| 姓氏 | 名 | 领域 | CFLT 中引用的代表贡献 |
|---|---|---|---|
| **Chomsky（乔姆斯基）** | Noam | 语言学 | 普遍语法；*核心语法* vs *边缘* |
| **Talmy** | Leonard | 认知语言学 | 图形-背景；偶然性原则 |
| **Langacker** | Ronald | 认知语法 | 轮廓-基础区分 |
| **Hawkins** | John A. | 语言类型学 | EIC、CRD、解析效率理论 |
| **Halliday** | M.A.K. | 功能语言学 | 系统功能语法；情境角色 |
| **Wierzbicka** | Anna | 语义学 | NSM、语义原语 |
| **Searle（塞尔）** | John | 语言哲学 | 言语行为分类（陈述类、指令类、承诺类、表达类、宣告类） |
| **Grice（格赖斯）** | H. P. | 语用学 | 合作原则、准则、含义 |
| **Sperber & Wilson** | Dan & Deirdre | 语用学 | 关联理论 |
| **Kamp** | Hans | 形式语义学 | 话语表征理论 |
| **Steedman** | Mark | 计算语言学 | 组合范畴语法 |
| **Levelt** | Willem | 心理语言学 | 言语生成模型（概念化器 / 表述器 / 发音器） |
| **Krashen（克拉申）** | Stephen | SLA | 输入假说、监控模型、情感过滤 |
| **Vygotsky（维果茨基）** | Lev | 教育心理学 | 最近发展区、支架 |
| **Sweller** | John | 认知心理学 | 认知负荷理论 |
| **DeKeyser** | Robert | SLA | L2 的技能习得理论 |
| **Baddeley** | Alan | 认知心理学 | 工作记忆模型 |
| **Menon & Uddin** | — | 神经科学 | 显著性网络作为 DMN 与 CEN 之间的开关 |
| **Liu 等** | — | NLP | "Lost in the Middle"（2023） |
| **Xiao 等** | — | NLP | StreamingLLM、注意力槽（2024） |

---

## 9. 交叉引用

完整参考文献参见 [`bibliography.md`](./bibliography.md)。

权威概念的深入处理：
- **显著性锚点 / 核心类型分类** → [`foundations/core-concept.md`](./foundations/core-concept.md)
- **图形-背景、EIC、NSM、轮廓-基础** → [`foundations/linguistics.md`](./foundations/linguistics.md)
- **言语行为、lambda 演算、CCG、DRT** → [`foundations/logic.md`](./foundations/logic.md)
- **信息论、熵、KL** → [`foundations/mathematics.md`](./foundations/mathematics.md)
- **PFC、BG、SN、DMN、CEN、P600** → [`foundations/neuroscience.md`](./foundations/neuroscience.md)
- **Krashen、Vygotsky、Sweller、TBLT** → [`foundations/pedagogy.md`](./foundations/pedagogy.md)
- **注意力槽、RAG、前缀缓存** → [`foundations/llm.md`](./foundations/llm.md)
- **槽位消歧表与判定树** → [`methodology/slot-disambiguation.md`](./methodology/slot-disambiguation.md)
