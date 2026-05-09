# 方法论：课程工程 (CFLT-Content)

> **版本：** 1.0.0 (内部草案)
> **作者：** CFLT 核心团队
> **组织：** [CFLT.center](https://cflt.center)
> **许可：** [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)

> **目的：** 提供一个系统的工程框架，利用大语言模型 (LLM) 大规模生成高质量、符合 CFLT 规范的教育内容。
>
> **理论锚点：** 本文件操作化了 [`foundations/pedagogy.md`](../foundations/pedagogy.md) §6（**弱式 TBLT** —— Ellis 2003；CFLT *不*与 Long 强式 TBLT 兼容，诚实定位详见 pedagogy §6）和 §8（双语词汇提取），并依赖于 [`foundations/linguistics.md`](../foundations/linguistics.md) §8（构式语法槽位填充）和 §9（作为槽位填充词汇的自然语义金属语言 NSM）。"令牌包 (Token-pack)"设计是这些理论承诺在工程层面的具体体现。

---

## 1. 从理论到内容：模块化方法

传统的课程设计速度慢且依赖人工。CFLT 将语言学习视为功能块和行业特定令牌 (Token) 的组装，从而实现了 **程序化课程生成 (Programmatic Curriculum Generation)**。

## 2. 课件生成流水线

CFLT 模块 (例如“后端工程师英语”) 的生成遵循一个四步自动化流程：

### 第一步：场景领域选择
识别目标受众的高频场景。
- *输入：* "后端工程"
- *输出：* ["系统部署", "数据库故障排除", "代码审查", "延迟调查"]

### 第二步：原子令牌提取
识别该领域特定的 **显著性锚点 (核心/Cores)** 和 **上下文修饰词**。
- *核心动作 (Core Actions)：* `deploy` (部署), `refactor` (重构), `debug` (调试), `optimize` (优化)。
- *空间上下文 (Space Contexts)：* `production server` (生产服务器), `local environment` (本地环境), `staging cluster` (预发布集群)。
- *原因上下文 (Reason Contexts)：* `high latency` (高延迟), `buffer overflow` (缓冲区溢出), `deprecated API` (已弃用的 API)。

### 第三步：CFLT 模板合成
将场景和令牌组合成有效的 `[核心] → [理由] → [空间] → [时间]` 模式。
- *模板示例：* `[Action: Debug] because [Reason: Error 500] in [Space: Microservice] [Time: Now].`

### 第四步：多模态资产生成
- **文本：** 经过优化的 CFLT-L2 形式。
- **音频：** 文字转语音 (TTS)，强调核心部分的韵律。
- **视觉：** AI 生成的图像或图标，代表原子令牌。

```mermaid
graph TD
    In[行业 / 领域] --> S1[1. 场景选择]
    S1 --> S2[2. 原子令牌提取]
    S2 --> S3[3. CFLT 模板合成]
    S3 --> S4[4. 多模态资产生成]
    
    subgraph "输出资产"
    S4 --> T[文本：CFLT 形式]
    S4 --> A[音频：韵律 TTS]
    S4 --> V[视觉：AI 图标]
    end
```

---

## 3. “IT 英语”模块案例研究

由于 IT 领域与工程流程在逻辑上的高度契合，它是 CFLT 的首要目标。

### 3.1 令牌分类学
| 逻辑块 | 令牌示例 |
|---|---|
| **核心 (Core)** | `merge`, `revert`, `scale`, `containerize` |
| **原因 (Reason)** | `bottleneck`, `concurrency issue`, `security patch` |
| **空间 (Space)** | `repo`, `pipeline`, `endpoint`, `firewall` |
| **时间 (Time)** | `sprint`, `deployment window`, `retroactive` |

### 3.2 学习路径工程
1.  **级别 1 (构建者)：** 将这些令牌拖放到 4 槽位 UI 中。
2.  **级别 2 (发声者)：** 说出序列："Scale the database, because of traffic spike, in AWS, tonight."
3.  **级别 3 (反射者)：** 实时角色扮演，使用严格的 CFLT 逻辑回应 AI “资深架构师”。

```mermaid
graph LR
    L1[级别 1：UI 构建器] -- "槽位填充" --> L2[级别 2：语音挑战]
    L2 -- "韵律反射" --> L3[级别 3：AI 角色扮演]
    L3 -- "流利度" --> Mastery((L2 精通))
    
    style Mastery fill:#f96,stroke:#333,stroke-width:2px
```

---

## 4. 验证内容质量

所有 AI 生成的内容必须通过 **CFLT 验证器 (CFLT Validator)**：
- **约束检查：** 句子是否包含所有必需的槽位？
- **显著性检查：** 最重要的动作是否确实位于位置 0？
- **词汇检查：** 是否使用了提供的行业令牌包？

## 5. 扩展：任意语言对的内容生成

由于 CFLT 逻辑是通用的，一旦工程化了“IT 英语”模块，系统就可以通过简单地更换令牌包和语法覆盖层 (Grammar Overlay) 配置，自动生成“IT 日语”或“IT 法语”模块。这是通往 **全球任意语言对双语能力 (Global Any-to-Any Bilingualism)** 的路径。

```mermaid
graph TD
    Logic["CFLT 通用逻辑：C → R → S → T"]
    
    subgraph "扩展目标"
    Logic --> EN[英语令牌包]
    Logic --> JP[日语令牌包]
    Logic --> FR[法语令牌包]
    end
    
    EN --> M1[英语模块]
    JP --> M2[日语模块]
    FR --> M3[法语模块]
```

---

## 6. 总结

CFLT 中的课程工程从“编写书籍”转向了“工程化系统”。通过自动化行业逻辑与 CFLT 协议的合成，我们可以为世界上每一个行业提供个性化、相关且逻辑一致的学习材料。
