# CFLT 参考实现

> **版本：** 1.0.0 (内部草案)
> **作者：** CFLT 核心团队
> **组织：** [CFLT.center](https://cflt.center)
> **许可：** [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)

本文件记录了实现、嵌入或实质性引用 **Core-First Language Theory (CFLT)** 框架的项目。

CFLT 本身是一套理论和规范 —— 而这些“实现”则是该协议与运行代码相结合的地方。将您的项目添加到此处有助于研究人员和从业者发现工作示例，并避免重复劳动。

---

## 活跃项目

### CoreFirst (第一支柱 —— 人类双语教育)
- **域名：** [corefirst.world](https://corefirst.world)
- **代码库：** [github.com/corefirst/corefirst](https://github.com/corefirst/corefirst)
- **用途：** CFLT 在人类第二语言 (L2) 学习者中的参考实现。这是一个 Next.js Web 应用程序，提供逻辑转换器、AI 课件生成器、带语音评分的语音挑战、游戏化的 CFLT 构建器以及进度分析。
- **目标受众：** 成年 L2 学习者 (v1 初始目标)，计划通过 Visual CFLT 交付模型扩展到所有年龄组。
- **许可：** MIT (代码) / CC BY 4.0 (适用时的应用内教育内容)
- **状态：** 活跃开发中

---

## 计划中项目

### apcore-cflt (第二支柱 —— LLM 协议层)
- **代码库：** 待定 (将存在于 [apcore](https://github.com/apcore) 生态系统中)
- **用途：** 将 CFLT 作为 LLM 和 AI Agent 的标准化推理协议。将提供支持 CFLT 的 MCP 服务器、用于语料库级别 CFLT 转换的 CLI 工具，以及主流语言框架的 SDK。
- **目标受众：** LLM/Agent 开发者、框架构建者。
- **状态：** 尚未开始 —— 参见 [`vision.md`](./vision.md) §3 了解战略案例。

---

## 添加您的实现

欢迎遵循规范 CFLT 协议的项目。请提交 Pull Request，在“活跃项目”下添加一个小节，包含以下信息：

- **项目名称**
- **域名** (如有)
- **代码库 URL**
- **用途** —— 项目提供哪些与 CFLT 相关的功
- **受众** —— 项目的目标群体
- **许可**
- **状态** —— 活跃 (Active) / 计划中 (Planned) / 已归档 (Archived)

### 什么符合“CFLT 实现”的资格？

如果项目满足以下条件之一，则符合资格：

1. 将 CFLT 四元素序列 (`[Core] → [Reason] → [Space] → [Time]`) 作为其功能的结构化组件进行操作化处理，或者
2. 提供明确用于生成、验证或转换符合 CFLT 规范内容的工具，或者
3. 围绕“核心优先序列化 (Core-First sequencing)”原则构建了实质性的教育或分析工作流。

仅将 CFLT 作为背景阅读引用的项目不符合资格；此列表仅用于记录活跃的操作性用途。

---

## 区分 CFLT 与相关工作

请注意，CFLT (**Core-First Language Theory**，本框架) 与关于“**Core First Language Acquisition**” (如 Ambridge & Wagner 2021) 的文献是不同的。两者名称中虽有三个词相同，但探讨的问题不同 —— 详见 `manifesto.md` §4 中的完整区分。
