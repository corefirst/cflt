# Core-First Language Theory (CFLT): Reconstructing Global Bilingual Education from First Principles

> **Version:** 1.0.0 (Internal Draft)
> **Author:** CFLT Core Team
> **Organization:** [CFLT.center](https://cflt.center)
> **License:** [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)

## 1. Executive Summary

**Core-First Language Theory (CFLT)** is a unified theoretical and operational framework for cross-linguistic communication and bilingual education. It posits a single discourse-level principle — *the cognitive core of an utterance is also its universally-prioritized linear position* — and defines a teachable, AI-supportable sequencing protocol (**CFLT Protocol**) that bridges any two natural languages with minimum cognitive friction.

### 1.1 The Nature of CFLT: Protocol vs. Description

It is critical to distinguish between two levels of linguistic claim:
1.  **Descriptive Observation:** Languages vary wildly in surface word order (e.g., English SVO vs. Japanese SOV). CFLT does *not* claim that all natural languages are naturally Core-First.
2.  **Normative Protocol:** CFLT is an **engineering protocol for Cognitive Ergonomics**. It defines how information *should* be sequenced to achieve the lowest possible cognitive load during cross-linguistic transfer, L2 acquisition, and AI prompting.

CFLT is to language what **TCP/IP** is to networking: it is a standardized packet-header format for human thought. By adopting a "Core-First" interlanguage protocol, learners bypass the massive metabolic cost of structural restructuring (e.g., waiting for the verb in German or planning a 10-word modifier in Japanese before uttering the noun). It is an **unmarked default**, not a descriptive universal.

By identifying the common cognitive "hardware" shared by all humans (Chomsky's Universal Grammar, extended via *core grammar* ↦ *core-first sequencing*) and neutralizing cultural "software" biases (Sapir-Whorf Hypothesis), CFLT leverages AI to create a seamless bridge between any two languages.

**Nomenclature:**

| Layer | Name | Role |
|---|---|---|
| Framework | **CFLT — Core-First Language Theory** | The unified name for both the academic theory and the operational protocol |
| Implementation | **CFLT Protocol** | The specific `[Core] → [Modifiers]` sequencing rule |

**CFLT** is the primary designation for both its scientific foundations and its practical methods. The term **CFLT Protocol** specifically refers to the operational sequencing rules. **CFLT is an open framework**: any team is welcome to research, implement, or extend it independently. **CoreFirst** ([corefirst.world](https://corefirst.world)) is the official reference experimental project for CFLT, but is not a required dependency or licensing gate — it exists alongside any other implementations the community may build.

---

## 2. Theoretical Foundations

> The summaries in §2.1–§2.5 below are deliberately compact. For deep treatments — including honest limitations and citations — see the companion documents:
> - **[`foundations/core-concept.md`](foundations/core-concept.md) — Read this first.** Defines what "Core" means: a salience anchor, not a verb or predicate. Prevents mis-reading the analogies in the other foundation docs.
> - [`foundations/linguistics.md`](foundations/linguistics.md) — UG, information structure, cognitive linguistics, speech production
> - [`foundations/phonetics.md`](foundations/phonetics.md) — cross-linguistic phonetic transfer, muscular intelligence
> - [`foundations/sociolinguistics.md`](foundations/sociolinguistics.md) — politeness, register, honorifics
> - [`foundations/pedagogy.md`](foundations/pedagogy.md) — Krashen, Vygotsky, Cognitive Load Theory, TBLT, skill acquisition
> - [`foundations/neuroscience.md`](foundations/neuroscience.md) — salience network, PFC metabolic costs, EIC, proceduralization
> - [`foundations/logic.md`](foundations/logic.md) — predicate logic, lambda calculus, CCG, speech acts, Relevance Theory
> - [`foundations/mathematics.md`](foundations/mathematics.md) — information theory, UID, optimal coding, linearization
> - [`foundations/llm.md`](foundations/llm.md) — Transformer attention biases, prompt order, CoT
> - [`bibliography.md`](./bibliography.md) — unified reference list

### 2.1 Universal Grammar and *Core Grammar* (Noam Chomsky)
**Concept:** The human brain possesses an innate, biological "Language Acquisition Device" (LAD). Chomsky distinguishes the *core grammar* (universal principles) from its *periphery* (idiosyncratic, learned).

**CFLT Extension:** Where Chomsky's *core grammar* is a structural category, CFLT introduces a **dynamic linearization** principle: *the cognitive core is also the universally-prioritized utterance-initial position*.

### 2.2 Cognitive Foundations: Figure-Ground and EIC

```mermaid
graph LR
    subgraph "Cognitive Asymmetry (Talmy 2000)"
    F[Figure: Salient/Moving] -- "is located/characterized by" --> G[Ground: Stable/Reference]
    end
    subgraph "CFLT Linearization"
    C[Core] -- "followed by" --> M[Modifiers/Context]
    end
    F -.-> C
    G -.-> M
```

**Figure-Ground (Talmy):** CFLT codifies a **Figure-First** linearization. The Core (Figure) is the salient event, while modifiers (Ground) provide the reference frame. This aligns with the cognitive expectation to locate salient events relative to stable frames.

**Early Immediate Constituents (Hawkins):** CFLT optimizes for **parsing efficiency**. By placing the Core at position 0, it minimizes the "Constituent Recognition Domain," achieving an efficiency ratio near 100% and reducing the look-ahead buffer for both humans and machines.

### 2.3 Computational Foundations: Attention Sinks (Xiao et al.)

```mermaid
graph BT
    subgraph "Transformer Attention Weights"
    P0[Pos 0: Core] --- W0((High Weight))
    P1[Pos 1: Reason] --- W1(.)
    P2[Pos 2: Space] --- W2(.)
    P3[Pos 3: Time] --- W3(.)
    end
    style W0 fill:#f96,stroke:#333,stroke-width:2px
```

**Concept:** Transformer-based LLMs over-attend to the prefix region for two distinct reasons — (1) **Attention Sinks** (Xiao et al. 2024), a softmax-stability artifact in which initial tokens absorb attention regardless of semantic content, and (2) **Primacy / positional bias**, where causal masking compounds the influence of early tokens over later ones.
**CFLT Application:** CFLT exploits (2), not (1). Placing the Core in the high-attention prefix region (typically positions just after `<bos>`) compounds its influence over generation — but this is a primacy argument, not a claim that attention sinks "prefer" semantic content. See [`foundations/llm.md`](foundations/llm.md) §2.3 for the careful disambiguation.

### 2.4 The Sapir-Whorf Hypothesis (Linguistic Relativity)
**Concept:** Language structure influences habitual cognitive patterns.
**CFLT Application:** For learners from "topic-prominent" backgrounds (e.g., Chinese), CFLT provides a **Neutral Buffer Sequence** to eliminate the mental cost of "thinking-for-speaking" in divergent L2 structures.

### 2.5 Natural Semantic Metalanguage (Anna Wierzbicka)
**Concept:** All meanings can be reduced to universal "Semantic Primes."
**CFLT Application:** AI utilizes these primes as an **Atomic Vocabulary** to fill CFLT slots, facilitating any-to-any cross-linguistic translation.

---

## 3. The Core Framework: Core-First Sequencing Protocol

### 3.1 The Principle: "Core First, Supplement Later"
CFLT mandates a standardized information sequence to unify human expression:

**`[Core] → [Reason] → [Space] → [Time]`**

```mermaid
graph LR
    A[Core] --> B[Reason] --> C[Space] --> D[Time]
    style A fill:#f96,stroke:#333,stroke-width:2px
```

All four elements are present in the **canonical (unmarked) sequence**. Implementations and teaching materials should preserve this four-element ordering when teaching the default form; partial sequences (e.g., dropping `[Space]`) are treated as **reduced forms** of the canonical sequence rather than as alternative protocols, and the slot-order rule still applies to whichever slots are present.

> **Coverage scope of the four slots.** The protocol governs only the **ground frame** — the world frame around the event. Modifiers that belong to the event itself (manner *slowly*, instrument *with butter*, beneficiary *for my mom*, accompaniment, modal, negation) live **inside the Core** as part of the event nucleus, not as separate slots. Each language assembles the event nucleus internally using its own native syntax (case marking, prepositions, particles, coverbs); CFLT does not prescribe that internal assembly. The four slots therefore are **not** an exhaustive taxonomy of all modifiers — they are an exhaustive taxonomy of the *circumstantial frame* that the unmarked default places after the Core. See [`foundations/core-concept.md`](foundations/core-concept.md) §2.1–§2.2 for the two-tier model and [`methodology/slot-disambiguation.md`](methodology/slot-disambiguation.md) for the operational decision tree.

> **The role of English in this documentation.** Because English is the most documented L2 and the strongest LLM-supported language, this documentation uses English as the **default illustrative language** and as a **verification anchor** when checking slot assignments across languages. English is **not**, however, a required intermediate hop for cross-language learning (a Mandarin↔Japanese learner does not have to route through English), nor is it the judge of where Core boundaries lie in non-English target languages.
>
> CFLT's universality is a **protocol-layer claim**: the schema (Core-first, R→S→T) and slot-semantics (functional WHY/WHERE/WHEN questions) are language-agnostic. **It is not a claim that English is unnecessary in practice.** The L3 / additional-language acquisition literature (Cenoz 2003; De Angelis 2007) supports the theoretical position that L1↔L2 transfer can be direct, but the *ecological reality* is that English serves as a resource and metalinguistic medium in most learning contexts globally. Specific language-pair courses may legitimately use the learner's existing L2 (often English) as a metalinguistic explanation language without contradicting CFLT's protocol-layer universality. The event-nucleus internal assembly and language-specific edge cases are delegated to each language's native syntax. See [`foundations/core-concept.md`](foundations/core-concept.md) §2.3 for the layer-by-layer breakdown, and the [language-pair guides](methodology/language-pair-guides/index.md) for operationalization in specific pairs.

> **Important scope clarification.** The four-element canonical sequence defines CFLT's **unmarked default** — the form a fluent speaker produces when no special rhetorical purpose applies. It does **not** prohibit marked deviations (topicalization, fronting, clefts, end-weight repackaging) that mature fluency requires, nor does it require every utterance to surface all four slots. Every natural language has multiple expressive forms for the same propositional content, and CFLT accommodates this by treating itself as the *baseline* from which deliberate marked deviations are learned later. See [`foundations/core-concept.md`](foundations/core-concept.md) §6 for the unmarked/marked distinction and §7 for the misreading-refutation matrix.

### 3.2 Demonstrating the CFLT Pivot

The Core in CFLT is a **salience anchor**, not a verb (see [`foundations/core-concept.md`](foundations/core-concept.md)). The four examples below illustrate the four kinds of Core that the protocol accommodates.

#### Example 1 — Action Core
**L1 (Chinese, context-heavy order):** *昨天下雨，我在家没出去。* — Time → Reason → Result
**CFLT Reconstruction:** *我没出去，因为下雨，在家，昨天。* — Core → Reason → Space → Time
**English (CFLT-L2):** *I didn't go out, because it rained, at home, yesterday.*

#### Example 2 — Identity / Description Core
**L1 (Chinese):** *那个穿红衣服的女孩是我妹妹。* — Modifier-heavy NP → Identity
**CFLT Reconstruction:** *那个女孩是我妹妹，穿着红衣服，在照片里，去年夏天。* — Core (identity) → Description → Space → Time
**English (CFLT-L2):** *That girl is my sister, wearing a red dress, in the photo, from last summer.*

#### Example 3 — State Core
**L1 (Chinese):** *开了一下午会，我在办公室都累瘫了。* — Cause → Space → State
**CFLT Reconstruction:** *我累瘫了，因为开了一下午会，在办公室，刚才。* — Core (state) → Reason → Space → Time
**English (CFLT-L2):** *I'm exhausted, because of the meeting, in the office, just now.*

#### Example 4 — Request / Speech-Act Core
**L1 (Chinese):** *现在能在桌上帮我递一下盐吗？* — Time → Space → Request
**CFLT Reconstruction:** *请帮我递一下盐，在桌上，现在。* — Core (request) → Polite marker → Space → Time
**English (CFLT-L2):** *Could you please pass the salt, on the table, now?*

**The CFLT Advantage:** Across all four core types, once the learner adopts Core-First sequencing in their native mind, producing the target language becomes a **token replacement** exercise rather than a structural reorganization. The protocol is uniform; what fills position 0 varies with the speaker's intent.

---

## 4. Distinction from Adjacent Literature

CFLT is to be carefully distinguished from a superficially similar phrase that already appears in the literature:

> Ambridge, B. & Wagner, L. (eds.) (2021). *Testable Theories of Core First Language Acquisition*. Special Issue, *Journal of Child Language*, Vol. 48, Special Issue 5.

**Parsing comparison:**

| | Ambridge & Wagner (2021) | CFLT (this work) |
|---|---|---|
| Constituent structure | `[core] + [first language acquisition]` | `[core-first] + [language theory]` |
| Subject | The **core mechanisms** by which children acquire L1 | The **core-first sequencing** rule for cross-linguistic discourse |
| Population | Children acquiring native language | Bilingual learners producing L2 |
| Domain | Developmental psycholinguistics | Applied linguistics + AI-assisted bilingual pedagogy |

The two strings overlap at the trigram "core first language" but the underlying concepts are unrelated. CFLT does not address L1 acquisition; the Ambridge/Wagner volume does not address bilingual sequencing. Authors writing on CFLT must cite this distinction in any work likely to be retrieved alongside L1 acquisition literature.

---

## 5. AI-Driven Implementation Roadmap

### Phase 1: Cognitive Reshaping (LLM as Logic Tutor)
The AI trains the user to express intentions in their native language using the Core-First sequence. This phase focuses on breaking L1-specific sentence patterns.

### Phase 2: Atomic Mapping (LLM as Token Swapper)
The AI introduces target language "tokens" into the established Core-First framework. Grammar is acquired implicitly through pattern recognition rather than explicit rule memorization.

### Phase 3: Cultural Refinement (Advanced Modules)
Once functional fluency is achieved via CFLT, the AI introduces culture-specific idioms, metaphors, and advanced stylistic nuances.

---

## 6. Global Vision: Any-to-Any Bilingualism

CFLT is not limited to Chinese-to-English. It is designed as a **Universal Protocol for Human Communication**. By adopting the Core-First sequence as the "Global Interlingua," we can scale bilingual education across any linguistic pair:

*   **Japanese (SOV) ↔ German (V2):** 
    - *Japanese habit:* [Modifiers] → [Object] → [Verb]. 
    - *CFLT Pivot (scaffold form):* "Ich esse einen Apfel (Core), weil ich Hunger habe (Reason), im Park (Space), jetzt (Time)." 
    - By forcing the Japanese brain to output the Action (Verb) immediately, we bypass the "waiting for the verb" processing delay in German V2 main clauses. The Grammar Overlay layer subsequently polishes the appended adverbials into idiomatic German positioning.
*   **Arabic (VSO) ↔ Spanish (SVO):**
    - *Arabic habit:* [Verb] → [Subject] → [Object]. 
    - *CFLT Pivot:* "Como una manzana (Core) ... porque tengo hambre (Reason) ... en la cocina (Space)." 
    - CFLT aligns the Arabic V-first tendency with the Spanish SVO core, using **Natural Semantic Metalanguage (NSM) Primes** as the semantic bridge to ensure the *intent* of the verb is preserved across divergent conjugation systems.

The official reference implementation is hosted at **corefirst.world**; the framework itself is open for any team to implement independently.

---

## 7. Reference Implementation: CoreFirst

The section below describes **CoreFirst**, the official reference implementation of CFLT. It illustrates how the protocol can be operationalized as a product; it is **not** a prescription that all CFLT implementations must look this way.

### 7.1 The "Semantic Lego" Philosophy
Instead of teaching grammar as rigid rules, CoreFirst treats language as a set of functional blocks. The goal is **Maximum Communicative Efficiency** with **Minimum Cognitive Load**.

### 7.2 Implementation of Core Linguistic Elements

#### A. Parts of Speech → Logic Blocks
Grammatical terms (nouns, verbs) are replaced by intuitive functional categories:
*   **`[Who/What]`** (Subject/Object)
*   **`[Action]`** (Predicate)
*   **`[Context]`** (Adverbials of time, place, etc.)

> *Note: `[Context]` here is a grouping label used at the teaching layer (textbooks, courseware, and product UI alike), covering CFLT's modifier slots — typically `[Space]` + `[Time]` from §3.1. It is not a fifth CFLT slot.*

#### B. Tense → Semantic Time Tokens
To solve the complexity of English tenses, CFLT uses "Time Tokens."
*   *Input:* "I eat [Time: Yesterday]"
*   *AI Enhancement:* Automatically refines to "I ate" while validating that the semantic intent (Past) was correctly communicated.

#### C. Complex Structure → Flattened Logic
Avoid nested clauses (e.g., relative clauses). Use linear, additive logic.
*   *Traditional:* "The man who is standing there is my boss."
*   *CFLT Logic:* "That man is my boss, [Description] he is standing there."

### 7.3 Product Logic: Semantic First, Grammar Second
1.  **Semantic Core:** Priority is given to the correct sequence of CFLT logic.
2.  **Grammar Overlay:** AI acts as a non-intrusive "auto-correct" plugin, refining the user's CFLT output into idiomatic L2 without interrupting the flow of thought.

---

## 8. The CFLT Content Ecosystem: Universal Pedagogy

### 8.1 Cross-Age Adaptation
CFLT serves as the foundation for educational content across all age groups:
- **Early Learners:** Focus on "Visual CFLT" using animated icons and a restricted set of ~500 semantic primes to build intuitive concept-to-logic mapping.
- **Adult Learners:** Focus on "Efficiency CFLT" using industry-specific tokens and complex logical connectors for professional scenarios.

### 8.2 Industry-Specific Modules: The Case of "IT English"
The CFLT framework is uniquely suited for technical communication. In the **IT sector**, the logic of "Action-Result First" aligns perfectly with engineering documentation and collaborative coding.
- **Example Tokens:** *deploy, refactor, debug, latency, endpoint, scalability.*
- **Logic Mapping:** Instead of "If we have high latency, we should refactor the code," CFLT encourages: "**Refactor the code**, because of **high latency**, in the **backend**, now."
- **Benefit:** IT professionals can communicate critical technical decisions instantly and accurately across cultures.

The same modular vocabulary-injection pattern extends to medical, financial, technical, and hospitality sectors without altering the underlying cognitive protocol.

### 8.3 Multimodal Delivery (Audio-Visual Synthesis)
- **Audio-Primary:** Voice output is prioritized, with prosody and stress patterns emphasizing the `[Core]` of the CFLT block.
- **Visual-Support:** AI-generated images or short clips provide immediate visual feedback for the core concept, bypassing the need for native language translation.

### 8.4 Automated Courseware Generation
Leveraging LLMs, the CFLT framework can autonomously generate entire curricula based on simple prompts (e.g., "Hospital scenarios for an 8-year-old"). This ensures all educational content remains consistent with the "Core First" sequencing principle.

---

## 9. Phonetic Migration: Leveraging Existing Knowledge Systems

### 9.1 The Pinyin-to-IPA Bridge
For Asian learners, particularly those from Chinese-speaking backgrounds, CFLT leverages their existing mastery of **Pinyin** to accelerate pronunciation mastery.
- **Overlapping Sets:** Direct migration of sounds like /b/, /p/, /m/, /f/ (common to both systems).
- **Modification Guidance:** Instead of abstract articulatory descriptions, the system provides "Relative Adjustments." (e.g., "To pronounce the English /v/, start with the Pinyin 'f' muscle position but vibrate your vocal cords.")
- **Zero-to-One Phonemes:** For sounds entirely missing in the native system (like /θ/), AI generates analogies based on related native mouth positions.

### 9.2 Muscular Intelligence
Language learning is a physical skill. By identifying the "Muscle Overlap" between L1 and L2, CFLT reduces the cognitive resistance of learning "new" sounds, treating them as variations of familiar movements. This complements the Core-First sequencing principle: where §3 reduces *syntactic* friction, §9 reduces *articulatory* friction. Both are derived from the same first-principles approach — leverage what the learner's brain and body already encode.

---

## 10. Conclusion: The Unified Protocol for Intelligence

CFLT is not merely a word-order rule; it is a **Neutral Logic Protocol** designed to solve the cognitive heterogeneous gap between the world's linguistic regions.

### 10.1 The Core Discovery
The barrier to global communication is the **Structural Restructuring Tax**. When moving between heterogeneous language families (e.g., Mandarin ↔ English, Japanese ↔ German), the brain spends its finite metabolic resources "re-shaping" the L1 logic template into an L2 surface form. This constant background processing is the root of disfluency in humans and logical variance in AI.

### 10.2 The Solution: An Interlanguage Buffer
CFLT proposes that between L1 and L2, there exists a **language-neutral logic layer**. By mapping raw intent directly to the Core-First sequence, we create a standardized "thought packet" (TCP/IP for Thought). This protocol is:
- **L1-Compatible:** It captures the speaker's intent without premature syntactic commitment.
- **L2-Friendly:** It provides a consistent landing zone for target language tokens.

### 10.3 The Ultimate Benefit: Instant Fluency
By adopting the CFLT Protocol, the task of speaking a second language is transformed from **Complex Restructuring** into **Simple Token Replacement**. 
- **For Humans:** It eliminates the restructuring delay, achieving **Instant Fluency** and reducing speaking anxiety.
- **For AI:** It aligns information density with the transformer's attention architecture, achieving **Lossless Logic Alignment** and deterministic reasoning.

CFLT is the bridge. By standardizing the sequence of thought, we unify human and machine intelligence into a single, high-fidelity communication network.

---

*Authored by the CFLT Core Team, 2026. Project home: cflt.center.*
