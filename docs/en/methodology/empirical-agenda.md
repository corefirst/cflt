# CFLT Empirical Research Agenda

> **Status:** Draft / Proposal
> **Objective:** To provide a verifiable, falsifiable roadmap for validating the Core-First Language Theory (CFLT) across computational and pedagogical domains.

## 1. Introduction

As a normative protocol for cognitive ergonomics, CFLT makes several high-stakes claims about information processing efficiency and language acquisition speed. To transition from a theoretical framework to an evidence-based science, these claims must be subjected to rigorous empirical testing. This agenda outlines three pillars of research: **Computational Performance**, **Psycholinguistic Validation**, and **SLA (Second Language Acquisition) Outcomes**.

### 1.1 The Cross-Domain Single-Currency Premise

The framework's framing claim — that human L2 production and LLM prompting share a common "linearization cost" that a single protocol can address — is a **load-bearing cross-domain analogy**. We engage it as such, because the analogy is the load-bearing premise of the entire research agenda below, and treating it as self-evident would be intellectually dishonest.

**The challenge.** Guest & Martin (2023, "On Logical Inference over Brains, Behaviour, and Artificial Neural Networks") and the earlier critique tradition (McCloskey 1991) argue that surface analogies between cognitive architectures and neural-network behavior routinely smuggle in unjustified mechanistic identifications. The fact that two systems produce similar surface behavior under similar surface manipulations does **not** entail that the underlying mechanisms are the same. Specifically: the human "Prefrontal Tax" (Levelt's Formulator-stage bottleneck; Kormos 2006) is a working-memory-and-control phenomenon mediated by DLPFC / LIFG / ACC (`foundations/neuroscience.md` §3), while the LLM "Lost in the Middle" curve (Liu et al. 2023) is a softmax-attention-over-positional-encoding phenomenon mediated by causal masking and learned positional priors. These are not the same mechanism in any deep sense.

**Slobin (1996) "Thinking for Speaking"** raises a second, partially-orthogonal challenge: even *within* human cognition, the language-neutral Conceptualizer (Levelt 1989) may be weaker than it appears. Slobin argues that linguistic encoding shapes which conceptual distinctions speakers habitually mark — i.e., the preverbal message is not as language-neutral as the Levelt architecture suggests. If Slobin is right, CFLT's "shared Conceptualizer scaffold" loses some of its load-bearing power: the L1-shaped scaffold may not transfer cleanly to L2 production even with CFLT training.

**CFLT's response — joint, not unitary, currency.**

We accept the Guest & Martin / Slobin critique and revise the framing claim accordingly:

1. **CFLT does *not* claim a single shared mechanism** between human production and LLM prompting. The two systems pay linearization cost in *different mechanistic currencies* — DLPFC metabolic load in one case, attention-distribution-over-positions in the other. The cross-domain claim is not that the mechanisms are identical; it is the weaker claim that **a single normative protocol — Core-first linearization — happens to be a useful intervention in both systems**, for partially distinct reasons.
2. **The "shared currency" is the *intervention*, not the *cost*.** What CFLT actually proposes is a single piece of engineering — the `Core → R → S → T` protocol — and predicts (testably) that it reduces both DLPFC restructuring cost in humans (P3, `core-concept.md` §8.5) *and* attention-drift in LLMs (P2). These are two independent predictions that can be falsified independently. Falsifying one does not falsify the other.
3. **The Slobin challenge is partial.** Slobin's "thinking for speaking" suggests the Conceptualizer is influenced by L1-shaped habits; it does not suggest the Conceptualizer is *fully* L1-determined. The middle-ground reading is that CFLT scaffolds the linearization stage explicitly, which may *attenuate* (not eliminate) L1-shaped Conceptualizer biases. This is testable: a CFLT-trained Mandarin-L1 / English-L2 speaker should show *less* L1-shaped time-fronting than an untrained matched control (P1, `core-concept.md` §8.5).

**Falsification condition for the unification claim.** If both P2 (LLM-side) and P1 (human-side) are individually falsified, the "joint currency" claim collapses — CFLT becomes either a human-side scaffold without LLM benefit, an LLM-side prompt protocol without pedagogical benefit, or neither. The two-pillar structure of this agenda (§2 LLM, §3 human, §4 SLA) is **designed to allow that separation to be observed**: we do not pretend a single experiment can validate the unification; we run independent experiments in each pillar and let the cross-domain claim survive or fall based on their joint result.

This is a deliberately weaker framing than the manifesto's "TCP/IP for thought" metaphor. The metaphor is rhetorically useful; the load-bearing scientific claim is the conjunction of the testable per-pillar predictions, with the single-currency reading retracted to the *strategic positioning* layer.

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

For inquiries regarding data collection via the **CoreFirst** reference project, contact theory@cflt.center.
