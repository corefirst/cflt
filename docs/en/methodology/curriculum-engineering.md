# Methodology: Curriculum Engineering (CFLT-Content)

> **Version:** 1.0.0 (Internal Draft)
> **Author:** CFLT Core Team
> **Organization:** [CFLT.center](https://cflt.center)
> **License:** [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)

> **Purpose:** To provide a systematic engineering framework for generating high-quality, CFLT-compliant educational content at scale using Large Language Models.
>
> **Theoretical anchors.** This document operationalizes [`foundations/pedagogy.md`](../foundations/pedagogy.md) §6 (Task-Based Language Teaching) and §8 (bilingual lexical access), and depends on [`foundations/linguistics.md`](../foundations/linguistics.md) §8 (Construction Grammar slot-filling) and §9 (NSM as the slot-filler vocabulary). Token-pack design is the engineering surface of those theoretical commitments.

---

## 1. From Theory to Content: The Modular Approach

Traditional curriculum design is slow and manual. CFLT enables **Programmatic Curriculum Generation** by treating language learning as an assembly of functional blocks and industry-specific tokens.

## 2. The Courseware Generation Pipeline

The generation of a CFLT module (e.g., "English for Backend Engineers") follows a four-step automated process:

### Step 1: Scenario Domain Selection
Identify the high-frequency scenarios for the target audience.
- *Input:* "Backend Engineering"
- *Output:* ["System deployment", "Database troubleshooting", "Code review", "Latency investigation"]

### Step 2: Atomic Token Extraction
Identify the **Salience Anchors (Cores)** and **Contextual Modifiers** specific to the domain.
- *Core Actions:* `deploy`, `refactor`, `debug`, `optimize`.
- *Space Contexts:* `production server`, `local environment`, `staging cluster`.
- *Reason Contexts:* `high latency`, `buffer overflow`, `deprecated API`.

### Step 3: CFLT Template Synthesis
Combine scenarios and tokens into valid `[Core] → [Reason] → [Space] → [Time]` patterns.
- *Example Template:* `[Action: Debug] because [Reason: Error 500] in [Space: Microservice] [Time: Now].`

### Step 4: Multi-Modal Asset Generation
- **Text:** The refined CFLT-L2 form.
- **Audio:** Text-to-Speech (TTS) with emphasis on the Core prosody.
- **Visual:** AI-generated images or icons representing the atomic tokens.

---

## 3. The "IT English" Module Case Study

The IT sector is the primary target for CFLT due to its logical affinity with engineering processes.

### 3.1 Token Taxonomy
| Logic Block | Token Examples |
|---|---|
| **Core** | `merge`, `revert`, `scale`, `containerize` |
| **Reason** | `bottleneck`, `concurrency issue`, `security patch` |
| **Space** | `repo`, `pipeline`, `endpoint`, `firewall` |
| **Time** | `sprint`, `deployment window`, `retroactive` |

### 3.2 Learning Path Engineering
1.  **Level 1 (The Builder):** Drag-and-drop these tokens into the 4-slot UI.
2.  **Level 2 (The Voice):** Speak the sequence: "Scale the database, because of traffic spike, in AWS, tonight."
3.  **Level 3 (The Reflex):** Real-time roleplay responding to an AI "Senior Architect" using strict CFLT.

---

## 4. Validating Content Quality

All AI-generated content must pass the **CFLT Validator**:
- **Constraint Check:** Does the sentence have all mandatory slots?
- **Salience Check:** Is the most important action truly in Position 0?
- **Vocabulary Check:** Does it use the provided industry token pack?

## 5. Scaling: Any-to-Any Content Generation

Because the CFLT logic is universal, once an "IT English" module is engineered, the system can automatically generate an "IT Japanese" or "IT French" module by simply swapping the token pack and the Grammar Overlay configuration. This is the path to **Global Any-to-Any Bilingualism**.

---

## 6. Summary

Curriculum Engineering in CFLT moves from "writing books" to "engineering systems." By automating the synthesis of industry logic and the CFLT protocol, we can provide personalized, relevant, and logically consistent learning material for every industry in the world.
