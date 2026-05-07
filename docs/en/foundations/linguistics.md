# Linguistic Foundations of CFLT/CFLM

> Companion to: [`manifesto.md`](../manifesto.md)
> Purpose: Establish which linguistic traditions support the Core-First sequencing claim, and honestly acknowledge where typological reality diverges from CFLM's normative protocol.

---

## 1. Scope: "Core-First" Is Not "Verb-First"

CFLM proposes a normative sequence — `[Core Action/Result] → [Condition/Reason] → [Space/Context] → [Time]` — for both pedagogy and machine reasoning. One disambiguation belongs at the very top of any linguistic discussion of CFLM, because conflating the two concepts leads to wrong predictions about everything that follows.

### 1.1 Two different concepts that are easily confused

| Concept | Level | What it claims | Example |
|---------|-------|---------------|---------|
| **Verb-First (VSO)** | Surface word order | The finite verb precedes subject and object | "Went I to the store" — rare in English; the natural form in Welsh, Classical Arabic |
| **Core-First (CFLM)** | Conceptual linearization | The salience anchor is committed to first | "I went to the store, yesterday" — comprehensible English with a fixed conceptual order |

Verb-First is a **syntactic** category that classifies languages by their default constituent order. Core-First is a **cognitive-pragmatic** principle that orders the speaker's commitments. The two operate at different levels and make different predictions.

The "Core" in CFLM is a **salience anchor** — the constituent the speaker is fundamentally committing to. It may be a verb phrase ("I went out"), a copular complement ("That girl is my sister"), a state ("I'm exhausted"), or a speech act ("Could you help me"). See [`core-concept.md`](./core-concept.md) for the precise definition.

### 1.2 What this means for the typological literature

Word-order typology (Greenberg 1963; Dryer 2013) — SOV (~45%), SVO (~42%), VSO (~9%) — describes where the *verb* falls in surface word order. This literature is **largely orthogonal to CFLM**. CFLM does not claim a typological universal, does not propose VSO as a target form, and does not predict that natural languages should reorganize their surface syntax. CFLM is a normative conceptual scaffold layered *on top of* whatever surface order the target language uses; the resulting CFLM-L2 form is comprehensible natural-language English (or French, Japanese, etc.), not a typologically rare construction.

### 1.3 What the linguistic case actually rests on

1. At the **conceptual** level (pre-verbal message formation; Levelt 1989), the salient event/state/identity/request is cognitively prior — this *is* well-supported.
2. As a **pedagogical scaffold**, surfacing the conceptual core in linear position reduces L1→L2 restructuring cost.
3. As an **AI prompt protocol**, Core-First aligns with documented Transformer attention biases (see `llm.md`) — and crucially, it does so while staying inside the natural-language manifold that LLMs were trained on.

The linguistic case for CFLM is drawn primarily from **cognitive linguistics, information structure, and speech-production theory** — kin notions like Figure (Talmy), profile (Langacker), Topic, and Theme — not from typological generalizations about verb position.

---

## 2. Cognitive Linguistics: Figure-Ground Asymmetry

### 2.1 Talmy's Figure-Ground in Language
Talmy (2000, *Toward a Cognitive Semantics*) argues that linguistic structure systematically reflects the cognitive distinction between **Figure** (the salient, foregrounded entity or event) and **Ground** (the backgrounded reference frame providing context).

> "The Figure is a moving or conceptually movable entity whose path or location is at issue; the Ground is a reference entity with respect to which the Figure's path or location is characterized." (Talmy 2000:312)

**CFLM mapping:**
- `[Core Action/Result]` = the Figure (what happened)
- `[Condition/Reason] → [Space/Context] → [Time]` = the Ground (under what circumstances)

CFLM thus codifies a **Figure-First** linearization of the Figure-Ground asymmetry. While natural languages distribute Figure and Ground across multiple word-order strategies, the cognitive primacy of the Figure is robust.

### 2.2 Langacker's Profile-Base Distinction
In Cognitive Grammar (Langacker 1987, 2008), every linguistic expression has a **profile** (the entity or relation foregrounded for attention) against a **base** (the conceptual content presupposed). The profile is what the expression "is about."

**CFLM mapping:** the Core Action *is* the profile of an event-denoting clause. CFLM enforces that the linear utterance opens on the profile, not the base.

---

## 3. Information Structure: Theme, Rheme, Given, New

### 3.1 Functional Sentence Perspective (Prague School)
Mathesius (1929), Firbas (1992), and the Prague School developed the concept of **Communicative Dynamism (CD)**: every clause-element carries a degree of "newness" or informational push. The element with the highest CD typically falls toward the end of the clause in English ("end-focus"), but the **thematic** element — what the message is *about* — typically opens the clause.

**Tension with CFLM:** Functional Sentence Perspective predicts that *new and important* information ends a sentence (end-focus, end-weight). CFLM puts the most important information first.

**Resolution:** CFLM is not about packaging information for a hearer who already shares context (where end-focus optimizes); it is about **unambiguously asserting the action as the topic** for a hearer who does not yet share context. CFLM thus aligns with Topic-Comment structures in topic-prominent languages (Li & Thompson 1976) where the topic — here, the core action — anchors the clause.

### 3.2 Givenness Hierarchy and Accessibility
Gundel, Hedberg & Zacharski (1993) and Ariel (1990) describe how speakers manage referent accessibility: more accessible (given) referents take shorter, earlier-mentioned forms. CFLM intersects with accessibility theory in that the Core Action, once fronted, becomes the accessible "given" against which all subsequent modifiers are interpreted.

---

## 4. Speech Production: Levelt's Model

Levelt (1989, *Speaking: From Intention to Articulation*) describes a three-stage production architecture:

1. **Conceptualizer** — generates the *preverbal message* (intent + event structure).
2. **Formulator** — encodes the message into grammatical and phonological form.
3. **Articulator** — produces physical speech.

Crucially, the Conceptualizer's output is **language-neutral**. The semantic core of the intended event exists before any L1- or L2-specific formulation.

**CFLM's pedagogical claim is grounded here:**

> If the preverbal message is language-neutral, then training learners to *linearize the preverbal message* in a fixed Core-First order before entering the Formulator stage decouples conceptual structuring from L1 surface grammar.

Once the message is pre-linearized as `[Core] → [Reason] → [Space] → [Time]`, both L1 and L2 formulation become token-substitution exercises over the same linearized scaffold. This is the cognitive mechanism by which CFLM reduces L1→L2 restructuring cost.

---

## 5. Universal Grammar: Two Different Senses of "Core"

A potential confusion: Chomsky's framework also uses the word "core." It is essential to keep the two senses apart.

| | **Chomsky's *core grammar*** (1981, 1986) | **CFLM's *Core*** |
|---|---------------------------------------|-------------------|
| Domain | Set of grammatical rules | A specific constituent in a specific utterance |
| What it picks out | The universal-principles + parametrized rules of a language | The salience anchor — what the speaker is fundamentally committing to |
| Status | Descriptive linguistic claim | Normative pedagogical/computational protocol |
| Example | "Subject-verb agreement is core; quirky case-marking is periphery." | "In *I went out, because…*, the Core is *went out*." |

These are two different conceptual moves on the word "core":
- **Chomsky's core** is a **classifier on the rule inventory**: which rules belong to the universal core?
- **CFLM's Core** is a **selector on a single utterance**: which constituent is the salience anchor?

CFLT's contribution is orthogonal to Chomsky's core/periphery distinction. CFLT does not classify rules; it specifies a linearization protocol. Chomsky's framework is **compatible with** CFLM (it does not forbid CFLM's linearization rule), but it does not **predict** it either. The two operate at different levels of grammatical theory.

The terminological coincidence is unfortunate but harmless once the distinction is made explicit.

---

## 6. Linguistic Relativity (Sapir-Whorf) and L2 Acquisition Friction

### 6.1 The Strong vs. Weak Hypothesis
The strong Whorfian claim — that language determines thought — is largely rejected (Pinker 1994). The **weak version** — that language influences habitual cognitive patterns — is well-supported (Lucy 1992; Boroditsky 2001).

### 6.2 Application to CFLM
For learners moving between languages with strongly divergent information packaging (e.g., Mandarin's topic-prominent + time-initial structures vs. English's subject-prominent + tense-marked structures), the cognitive friction of restructuring is real and measurable (Slobin 1996, "Thinking for Speaking").

CFLM proposes a **neutral buffer sequence** — the Core-First linearization — that bypasses both L1 and L2 surface idiosyncrasies. Once the learner habitually produces preverbal messages in the buffer order, L2 surface formulation becomes mechanical token substitution.

This is consistent with Slobin's "Thinking for Speaking" framework, which holds that what differs across languages is not deep cognition but the language-specific patterns of *organizing* cognition for verbal expression.

---

## 7. Construction Grammar and Pedagogical Tractability

Goldberg's Construction Grammar (1995, 2006) treats grammar as a learned inventory of form-meaning pairings ("constructions") rather than abstract rules. This is highly compatible with CFLM's pedagogy:

- CFLM treats each `[Core] → [Reason] → [Space] → [Time]` slot as a **construction template**.
- Learners acquire fluency by filling slots, not by deriving sentences from abstract phrase-structure rules.
- Industry-specific token packs (medical, IT, finance) plug into the same constructional slots.

This makes CFLM compatible with the modern, usage-based mainstream of cognitive and constructional linguistics.

---

## 8. Natural Semantic Metalanguage (Wierzbicka)

The NSM program (Wierzbicka 1996; Goddard & Wierzbicka 2002) identifies a small inventory (~65) of **semantic primes** — concepts hypothesized to be lexicalized in all human languages (e.g., I, YOU, DO, GOOD, BECAUSE, BEFORE). NSM uses these primes as a metalanguage for cross-linguistic semantic description.

**CFLM application:** the four-element CFLM sequence corresponds closely to NSM primes:
- `[Core Action]` ↔ DO, HAPPEN, FEEL
- `[Condition/Reason]` ↔ BECAUSE
- `[Space/Context]` ↔ WHERE, IN, AT
- `[Time]` ↔ WHEN, BEFORE, AFTER

NSM thus provides CFLM with a **language-independent vocabulary of slot fillers**. A learner moving between any two languages can use NSM-decomposed thoughts as the bridge.

---

## 9. Honest Limitations

A rigorous foundation must list what CFLM does *not* claim and where its linguistic case is weaker:

1. **CFLM is not a descriptive universal of word order.** Surface word-order typology classifies languages by where the *verb* falls; CFLM does not address verb position. CFLM operates one level up: the salience-defined Core, which may or may not coincide with the verb.
2. **End-focus tension.** In information-packaging terms, English natively places new/heavy information at the end; CFLM inverts this for pedagogical clarity, accepting some loss of native idiomatic feel in early production.
3. **Topic-Comment vs. Subject-Predicate.** CFLM aligns more naturally with topic-prominent languages (Li & Thompson 1976) than with strictly subject-prominent ones. Learners moving from Mandarin to English will find CFLM intuitive on the source side and slightly artificial on the target side until polished by the Grammar Overlay layer.
4. **Idiomaticity.** Idiomatic L2 production requires moving *beyond* CFLM's rigid slots. CFLM is an entry scaffold, not a terminal grammar.

---

## 10. Open Research Questions

1. **Empirical validation.** Does CFLM-trained production measurably reduce L1→L2 restructuring latency? (Suitable for a between-subjects experiment with eye-tracking and articulation-onset measurement.)
2. **Typological generalization.** How does CFLM perform when L1 and L2 are both strongly head-final (e.g., Japanese↔Korean) — does the protocol still help, or is the cognitive overhead already minimal?
3. **Critical period.** Does CFLM benefit adult learners disproportionately compared to children, given that adults are more reliant on explicit conceptual scaffolds?
4. **Idiomaticity ceiling.** At what proficiency level does strict CFLM adherence become a hindrance to native-like fluency, and how should the Grammar Overlay layer escalate to relax it?

---

## 11. Cited Works

See [`bibliography.md`](../bibliography.md) for full references.
