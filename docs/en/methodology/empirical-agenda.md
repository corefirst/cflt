# CFLT Empirical Research Agenda

> **Status:** Draft / Proposal
> **Objective:** To provide a verifiable, falsifiable roadmap for validating the Core-First Language Theory (CFLT) across computational and pedagogical domains.

## 1. Introduction

As a normative protocol for cognitive ergonomics, CFLT makes several high-stakes claims about information processing efficiency and language acquisition speed. To transition from a theoretical framework to an evidence-based science, these claims must be subjected to rigorous empirical testing. This agenda outlines three pillars of research: **Computational Performance**, **Psycholinguistic Validation**, and **SLA (Second Language Acquisition) Outcomes**.

---

## 2. Pillar I: Computational Performance (LLM Prompting)

Does the Core-First sequence actually improve Large Language Model (LLM) reasoning and accuracy?

### 2.1 Experiment: The "Instructions-First" Consistency Test
*   **Hypothesis:** Placing core instructions at the beginning of a long context (CFLT order) reduces "middle-loss" phenomena and improves instruction-following accuracy compared to end-of-prompt instructions.
*   **Independent Variable:** Instruction position (CFLT: Core-Modifier vs. Reverse: Modifier-Core).
*   **Dependent Variables:** 
    *   **Accuracy:** Percentage of correctly executed tasks.
    *   **Consistency:** Standard deviation of output format over 100 runs.
    *   **Token Efficiency:** Average token count required to reach a correct solution.
*   **Metric:** LLM-as-a-judge score and deterministic unit tests.

### 2.2 Experiment: Cross-Linguistic Inference Mapping
*   **Hypothesis:** Using CFLT as a "pivot logic" for cross-language reasoning tasks reduces translation-induced logical errors in low-resource language pairs.
*   **Method:** Compare [L1 Prompt → Reasoning → L2 Answer] against [L1 Prompt → CFLT Pivot → Reasoning → L2 Answer].

---

## 3. Pillar II: Psycholinguistic Validation (Human Processing)

Does the human brain process Core-First structures with lower metabolic/cognitive cost?

### 3.1 Experiment: Self-Paced Reading (SPR) & Reaction Time
*   **Hypothesis:** Learners (L2) and Native Speakers (L1) will exhibit shorter reading times for the "Core" segment when it appears in the initial position compared to when it is preceded by multiple circumstantial modifiers.
*   **Metric:** Total Reading Time (TRT) and First Fixation Duration (FFD) via eye-tracking or SPR latency.

### 3.2 Experiment: Cognitive Load via Dual-Task Paradigm
*   **Hypothesis:** Producing an L2 sentence using the CFLT protocol consumes less working memory than producing a traditionally structured L2 sentence.
*   **Method:** Subjects perform a primary task (spoken L2 production) and a secondary task (e.g., tone monitoring). 
*   **Metric:** Reaction time to the secondary task. A faster secondary reaction time indicates lower cognitive load in the primary (CFLT) task.

---

## 4. Pillar III: SLA Outcomes (Pedagogical Efficacy)

Does CFLT training lead to faster fluency and higher accuracy?

### 4.1 Longitudinal A/B Study: The "Fluency Jump"
*   **Hypothesis:** Learners trained with the CFLT scaffold will achieve a higher **Mean Length of Run (MLR)** and fewer "filled pauses" (uh/um) in spontaneous speech than a control group using traditional grammar-first methods.
*   **Participants:** Two groups of A1-level adult learners (n=50 each).
*   **Duration:** 12 weeks of instruction.
*   **Metrics:** 
    *   **Fluency:** WPM (Words Per Minute), MLR.
    *   **Accuracy:** Error-free clauses percentage.
    *   **Complexity:** AS-unit complexity index.

### 4.2 Experiment: The "Fossilization" Check (Skehan's Trade-off)
*   **Goal:** To determine the optimal "fading" point for the CFLT scaffold.
*   **Method:** Compare advanced learners (B2+) who continue strict CFLT usage against those encouraged to use "marked" forms (De-scaffolding).
*   **Metric:** Subjective native-speaker ratings on "naturalness" and "rhetorical effectiveness."

---

## 5. Year 1–2 Research Milestones

| Quarter | Milestone | Deliverable |
|---|---|---|
| **Q3 2026** | Initial LLM Benchmarking | Technical report on "Prompt Order Accuracy" |
| **Q4 2026** | SPR Pilot Study | Psycholinguistic data on [Core-First] processing latency |
| **Q1 2027** | First Longitudinal SLA Trial | Comparative data on A1-to-A2 fluency progression |
| **Q2 2027** | Core-Boundary Disambiguation Dataset | Gold-standard corpus for LLM-as-judge training |

---

## 6. Call for Collaboration

We invite researchers in Cognitive Linguistics, AI, and Applied Linguistics to design and execute these experiments. CFLT is an open framework, and independent verification is the path toward broad academic and engineering adoption as a community standard for cross-linguistic protocol design.

For inquiries regarding data collection via the **CoreFirst** reference project, contact research@cflt.center.
