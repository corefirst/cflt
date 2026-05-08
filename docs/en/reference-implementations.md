# CFLT Reference Implementations

> **Version:** 1.0.0 (Internal Draft)
> **Author:** CFLT Core Team
> **Organization:** [CFLT.center](https://cflt.center)
> **License:** [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)

This document tracks projects that implement, embed, or substantively reference the **Core-First Language Theory** framework.

CFLT itself is theory and specification — the implementations are where the protocol meets running code. Adding your project here helps researchers and practitioners discover working examples and avoid duplicating work.

---

## Active

### CoreFirst (Pillar I — Human Bilingual Education)
- **Domain:** [corefirst.world](https://corefirst.world)
- **Repository:** [github.com/corefirst/corefirst](https://github.com/corefirst/corefirst)
- **Purpose:** Reference implementation of CFLT for human L2 learners. Next.js web application providing a Logic Transformer, AI Courseware Generator, Voice Challenge with phonetic scoring, gamified CFLT Builder, and progress analytics.
- **Audience:** Adult L2 learners (initial v1 target), with planned expansion to all age groups via the Visual CFLT delivery model.
- **License:** MIT (code) / CC BY 4.0 (in-app educational content where applicable)
- **Status:** Active development

---

## Planned

### apcore-cflt (Pillar II — LLM Protocol Layer)
- **Repository:** TBD (will live in the [apcore](https://github.com/apcore) ecosystem)
- **Purpose:** CFLT as a standardized reasoning protocol for LLMs and AI agents. Will provide CFLT-aware MCP server, CLI tooling for corpus-level CFLT transformation, and SDKs for major language frameworks.
- **Audience:** LLM/Agent developers, framework builders.
- **Status:** Not yet started — see [`vision.md`](./vision.md) §3 for the strategic case.

---

## Adding Your Implementation

Implementations following the canonical CFLT protocol are welcome. Open a pull request adding a section under "Active" with:

- **Project name**
- **Domain** (if any)
- **Repository URL**
- **Purpose** — what CFLT-related functionality the project provides
- **Audience** — who the project is for
- **License**
- **Status** — Active / Planned / Archived

### What qualifies as a "CFLT implementation"?

A project qualifies if it:

1. Operationalizes the CFLT four-element sequence (`[Core] → [Reason] → [Space] → [Time]`) as a structural component of its functionality, OR
2. Provides tooling that explicitly produces, validates, or transforms CFLT-conformant content, OR
3. Builds a substantial educational or analytical workflow around the Core-First sequencing principle.

Projects that merely cite CFLT as background reading do not qualify; this list is for active operational use.

---

## Distinguishing CFLT from Adjacent Work

Note that CFLT (Core-First Language **Theory**, this framework) is distinct from the literature on "Core First Language **Acquisition**" (e.g., Ambridge & Wagner 2021). The two share a trigram in their names but address different concerns — see `manifesto.md` §4 for the full distinction.
