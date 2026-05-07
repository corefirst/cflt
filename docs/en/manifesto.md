# Core-First Language Theory (CFLT): Reconstructing Global Bilingual Education from First Principles

> Project home: corefirst.world
> Status: theory layer locked

## 1. Executive Summary

**Core-First Language Theory (CFLT)** is a unified theoretical framework for cross-linguistic communication and bilingual education. It posits a single discourse-level principle — *the cognitive core of an utterance is also its universally-prioritized linear position* — and derives from this principle a teachable, AI-supportable method (**Core-First Language Method, CFLM**) that bridges any two natural languages with minimum cognitive friction.

By identifying the common cognitive "hardware" shared by all humans (Chomsky's Universal Grammar, extended via *core grammar* ↦ *core-first sequencing*) and neutralizing cultural "software" biases (Sapir-Whorf Hypothesis), CFLT leverages AI to create a seamless bridge between any two languages.

**Layered nomenclature:**

| Layer | Name | Role |
|---|---|---|
| Project / Brand | **CoreFirst** (corefirst.world) | Umbrella name covering the theory, the method, and the application |
| Theory | **CFLT — Core-First Language Theory** | Academic claim, citable framework |
| Method | **CFLM — Core-First Language Method** | Pedagogical implementation |

The project ships as a single product also named *CoreFirst* — a deliberate single-brand strategy at this stage. Sub-brands may be introduced if and when additional products diverge.

---

## 2. Theoretical Foundations

> The summaries in §2.1–§2.3 below are deliberately compact. For deep treatments — including honest limitations and citations — see the companion documents:
> - **[`foundations/core-concept.md`](foundations/core-concept.md) — Read this first.** Defines what "Core" means: a salience anchor, not a verb or predicate. Prevents mis-reading the analogies in the other foundation docs.
> - [`foundations/linguistics.md`](foundations/linguistics.md) — UG, information structure, cognitive linguistics, speech production
> - [`foundations/logic.md`](foundations/logic.md) — predicate logic, lambda calculus, CCG, speech acts, Relevance Theory
> - [`foundations/mathematics.md`](foundations/mathematics.md) — information theory, UID, optimal coding, linearization
> - [`foundations/llm.md`](foundations/llm.md) — Transformer attention biases, prompt order, CoT
> - [`bibliography.md`](./bibliography.md) — unified reference list

### 2.1 Universal Grammar and *Core Grammar* (Noam Chomsky)
**Concept:** The human brain possesses an innate, biological "Language Acquisition Device" (LAD). Within Government-Binding theory and the Principles & Parameters framework, Chomsky distinguishes the *core grammar* of a language (universal principles, parametrized) from its *periphery* (idiosyncratic, learned).

**CFLT Extension:** Where Chomsky's *core grammar* is a **static structural** distinction (which rules belong to the core), CFLT introduces a **dynamic linearization** principle: *the cognitive core is also the universally-prioritized utterance-initial position*. CFLT thus extends Chomsky's notion of "core" from a structural category to a sequencing rule. This is the central theoretical contribution of this manifesto.

### 2.2 The Sapir-Whorf Hypothesis (Linguistic Relativity)
**Concept:** The structure of a language shapes its speakers' cognitive processes and worldviews.
**CFLT Application:** Learners from "subject-prominent" or "context-heavy" language backgrounds (e.g., Chinese, Japanese, Korean) face high cognitive friction when switching to "predicate-prominent" languages like English. CFLT defines a **Neutral Buffer Sequence** to eliminate the cost of mental context switching.

### 2.3 Natural Semantic Metalanguage (Anna Wierzbicka)
**Concept:** All complex human meanings can be reduced to a small set of universal concepts known as "Semantic Primes" (e.g., *I, You, Do, Good, Because*).
**CFLT Application:** AI utilizes these primes as an **Atomic Vocabulary** to facilitate the transition from a learner's native language (L1) to the target language (L2) once the Core-First sequence is established.

---

## 3. The Core Framework: Core-First Sequencing Protocol

### 3.1 The Principle: "Core First, Supplement Later"
CFLT mandates a standardized information sequence to unify human expression:

**`[Core Action/Result] → [Condition/Reason] → [Space/Context] → [Time]`**

All four elements are mandatory in the **canonical (unmarked) sequence**. Implementations and teaching materials must preserve this four-element ordering when teaching the default form; partial sequences (e.g., dropping `[Space/Context]`) are **non-conformant** for the canonical form.

> **Important scope clarification.** The four-element canonical sequence defines CFLM's **unmarked default** — the form a fluent speaker produces when no special rhetorical purpose applies. It does **not** prohibit marked deviations (topicalization, fronting, clefts, end-weight repackaging) that mature fluency requires. Every natural language has multiple expressive forms for the same propositional content, and CFLM accommodates this by treating itself as the *baseline* from which deliberate marked deviations are learned later. See [`foundations/core-concept.md`](foundations/core-concept.md) §7 for the full unmarked/marked distinction.

### 3.2 Demonstrating the CFLT Pivot

The Core in CFLM is a **salience anchor**, not a verb (see [`foundations/core-concept.md`](foundations/core-concept.md)). The four examples below illustrate the four kinds of Core that the protocol accommodates.

#### Example 1 — Action Core
**L1 (Chinese, context-heavy order):** *昨天下雨，我在家没出去。* — Time → Reason → Result
**CFLT Reconstruction:** *我没出去，因为下雨，在家，昨天。* — Core → Reason → Space → Time
**English (CFLM-L2):** *I didn't go out, because it rained, at home, yesterday.*

#### Example 2 — Identity / Description Core
**L1 (Chinese):** *那个穿红衣服的女孩是我妹妹。* — Modifier-heavy NP → Identity
**CFLT Reconstruction:** *那个女孩是我妹妹，穿着红衣服，在照片里，去年夏天。* — Core (identity) → Description → Space → Time
**English (CFLM-L2):** *That girl is my sister, wearing a red dress, in the photo, from last summer.*

#### Example 3 — State Core
**L1 (Chinese):** *开了一下午会，我在办公室都累瘫了。* — Cause → Space → State
**CFLT Reconstruction:** *我累瘫了，因为开了一下午会，在办公室，刚才。* — Core (state) → Reason → Space → Time
**English (CFLM-L2):** *I'm exhausted, because of the meeting, in the office, just now.*

#### Example 4 — Request / Speech-Act Core
**L1 (Chinese):** *现在能在桌上帮我递一下盐吗？* — Time → Space → Request
**CFLT Reconstruction:** *能帮我递一下盐吗，请，在桌上，现在？* — Core (request) → Polite marker → Space → Time
**English (CFLM-L2):** *Could you pass the salt, please, on the table, now?*

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
Once functional fluency is achieved via CFLM, the AI introduces culture-specific idioms, metaphors, and advanced stylistic nuances.

---

## 6. Global Vision: Any-to-Any Bilingualism

CFLT is not limited to Chinese-to-English. It is designed as a **Universal Protocol for Human Communication**. By adopting the Core-First sequence as the "Global Interlingua," we can scale bilingual education across any linguistic pair:
*   **Japanese to French:** Using `[Core Action]` as the pivot.
*   **Arabic to Spanish:** Using `[NSM Primes]` as the semantic bridge.

The project home and canonical reference is **corefirst.world**.

---

## 7. Product Implementation: CoreFirst

### 7.1 The "Semantic Lego" Philosophy
Instead of teaching grammar as rigid rules, CoreFirst treats language as a set of functional blocks. The goal is **Maximum Communicative Efficiency** with **Minimum Cognitive Load**.

### 7.2 Implementation of Core Linguistic Elements

#### A. Parts of Speech → Logic Blocks
Grammatical terms (nouns, verbs) are replaced by intuitive functional categories:
*   **`[Who/What]`** (Subject/Object)
*   **`[Action]`** (Predicate)
*   **`[Context]`** (Adverbials of time, place, etc.)

#### B. Tense → Semantic Time Tokens
To solve the complexity of English tenses, CFLM uses "Time Tokens."
*   *Input:* "I eat [Time: Yesterday]"
*   *AI Enhancement:* Automatically refines to "I ate" while validating that the semantic intent (Past) was correctly communicated.

#### C. Complex Structure → Flattened Logic
Avoid nested clauses (e.g., relative clauses). Use linear, additive logic.
*   *Traditional:* "The man who is standing there is my boss."
*   *CFLM Logic:* "That man is my boss, [Description] he is standing there."

### 7.3 Product Logic: Semantic First, Grammar Second
1.  **Semantic Core:** Priority is given to the correct sequence of CFLT logic.
2.  **Grammar Overlay:** AI acts as a non-intrusive "auto-correct" plugin, refining the user's CFLM output into idiomatic L2 without interrupting the flow of thought.

---

## 8. The CFLM Content Ecosystem: Universal Pedagogy

### 8.1 Cross-Age Adaptation
CFLM serves as the foundation for educational content across all age groups:
- **Early Learners:** Focus on "Visual CFLM" using animated icons and a restricted set of ~500 semantic primes to build intuitive concept-to-logic mapping.
- **Adult Learners:** Focus on "Efficiency CFLM" using industry-specific tokens and complex logical connectors for professional scenarios.

### 8.2 Industry-Specific Modules: The Case of "IT English"
The CFLM framework is uniquely suited for technical communication. In the **IT sector**, the logic of "Action-Result First" aligns perfectly with engineering documentation and collaborative coding.
- **Example Tokens:** *deploy, refactor, debug, latency, endpoint, scalability.*
- **Logic Mapping:** Instead of "If we have high latency, we should refactor the code," CFLM encourages: "**Refactor the code**, because of **high latency**, in the **backend**, now."
- **Benefit:** IT professionals can communicate critical technical decisions instantly and accurately across cultures.

The same modular vocabulary-injection pattern extends to medical, financial, technical, and hospitality sectors without altering the underlying cognitive protocol.

### 8.3 Multimodal Delivery (Audio-Visual Synthesis)
- **Audio-Primary:** Voice output is prioritized, with prosody and stress patterns emphasizing the `[Core Action]` of the CFLM block.
- **Visual-Support:** AI-generated images or short clips provide immediate visual feedback for the core concept, bypassing the need for native language translation.

### 8.4 Automated Courseware Generation
Leveraging LLMs, the CFLM framework can autonomously generate entire curricula based on simple prompts (e.g., "Hospital scenarios for an 8-year-old"). This ensures all educational content remains consistent with the "Core First" sequencing principle.

---

## 9. Phonetic Migration: Leveraging Existing Knowledge Systems

### 9.1 The Pinyin-to-IPA Bridge
For Asian learners, particularly those from Chinese-speaking backgrounds, CFLM leverages their existing mastery of **Pinyin** to accelerate pronunciation mastery.
- **Overlapping Sets:** Direct migration of sounds like /b/, /p/, /m/, /f/ (common to both systems).
- **Modification Guidance:** Instead of abstract articulatory descriptions, the system provides "Relative Adjustments." (e.g., "To pronounce the English /v/, start with the Pinyin 'f' muscle position but vibrate your vocal cords.")
- **Zero-to-One Phonemes:** For sounds entirely missing in the native system (like /θ/), AI generates analogies based on related native mouth positions.

### 9.2 Muscular Intelligence
Language learning is a physical skill. By identifying the "Muscle Overlap" between L1 and L2, CFLM reduces the cognitive resistance of learning "new" sounds, treating them as variations of familiar movements. This complements the Core-First sequencing principle: where §3 reduces *syntactic* friction, §9 reduces *articulatory* friction. Both are derived from the same first-principles approach — leverage what the learner's brain and body already encode.

---

## 10. Naming Decision: Why Not "Meta-Language Logic"?

During early framing of this project, the candidate name **"MLL — Meta-Language Logic"** was considered as the umbrella term. It was rejected before publication for three reasons, recorded here so that the choice of CFLT can be evaluated on its merits rather than assumed:

1. **Terminological precision.** "Meta-language" in linguistics and computer science denotes a language used to describe another language (BNF, XML Schema, Tarski-style truth definitions). The framework described in this document is not a meta-language in this technical sense — it is a discourse-sequencing protocol. Adopting "Meta-Language Logic" would have constituted a misuse of established terminology that any peer reviewer with a linguistics or formal-language background would flag.
2. **Same-domain acronym collision.** "MLL" is occupied in adjacent biomedical-AI literature (Mixed Lineage Leukemia); "MLM" is the canonical AI/NLP abbreviation for Masked Language Modeling (BERT and successors). Both collisions would have impaired discoverability and risked mis-classification of this work by search engines and academic indexes in its target domain.
3. **Self-explanatory naming.** "Meta-Language Logic" does not communicate the framework's central operational rule. **Core-First Language Theory** names that rule directly: the core is always first. The §3.1 principle ("Core First, Supplement Later") and the umbrella term now point at the same idea.

This section is preserved as a design-decision record so future contributors do not re-litigate the question.

---

*Created by Chinese2English AI Project, 2026. Project home: corefirst.world.*
