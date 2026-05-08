# Linguistic Foundations of CFLT

> **Version:** 1.0.0 (Internal Draft)
> **Author:** CFLT Core Team
> **Organization:** [CFLT.center](https://cflt.center)
> **License:** [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)

---

## 1. Scope: "Core-First" Is Not "Verb-First"

CFLT defines a normative sequence — `[Core Action/Result] → [Condition/Reason] → [Space/Context] → [Time]` — for both pedagogy and machine reasoning. One disambiguation belongs at the very top of any linguistic discussion of CFLT, because conflating the two concepts leads to wrong predictions about everything that follows.

### 1.1 Two different concepts that are easily confused

| Concept | Level | What it claims | Example |
|---------|-------|---------------|---------|
| **Verb-First (VSO)** | Surface word order | The finite verb precedes subject and object | "Went I to the store" — rare in English; the natural form in Welsh, Classical Arabic |
| **Core-First (CFLT)** | Conceptual linearization | The salience anchor is committed to first | "I went to the store, yesterday" — comprehensible English with a fixed conceptual order |

Verb-First is a **syntactic** category that classifies languages by their default constituent order. Core-First is a **cognitive-pragmatic** principle that orders the speaker's commitments. The two operate at different levels and make different predictions.

The "Core" in CFLT is a **salience anchor** — the constituent the speaker is fundamentally committing to. It may be a verb phrase ("I went out"), a copular complement ("That girl is my sister"), a state ("I'm exhausted"), or a speech act ("Could you help me"). See [`core-concept.md`](./core-concept.md) §1 for the canonical definition; this section adopts that definition without re-stating it.

### 1.2 What this means for the typological literature

Word-order typology (Greenberg 1963; Dryer 2013) — SOV (~45%), SVO (~42%), VSO (~9%) — describes where the *verb* falls in surface word order. This literature is **largely orthogonal to CFLT**. CFLT does not claim a typological universal, does not propose VSO as a target form, and does not predict that natural languages should reorganize their surface syntax. CFLT is a normative conceptual scaffold layered *on top of* whatever surface order the target language uses; the resulting **CFLT Form** is comprehensible natural-language English (or French, Japanese, etc.), not a typologically rare construction.

### 1.3 What the linguistic case actually rests on

1. At the **conceptual** level (pre-verbal message formation; Levelt 1989), the salient event/state/identity/request is cognitively prior — this *is* well-supported.
2. As a **pedagogical scaffold**, surfacing the conceptual core in linear position reduces L1→L2 restructuring cost.
3. As an **AI prompt protocol**, Core-First aligns with documented Transformer attention biases (see `llm.md`) — and crucially, it does so while staying inside the natural-language manifold that LLMs were trained on.

The linguistic case for CFLT is drawn primarily from **cognitive linguistics, information structure, and speech-production theory** — kin notions like Figure (Talmy), profile (Langacker), Topic, and Theme — not from typological generalizations about verb position.

---

## 2. Cognitive Linguistics: Figure-Ground and Profile

### 2.1 Talmy's Figure-Ground in Language
> **Canonical introduction.** This section is the canonical treatment of the Figure-Ground asymmetry in CFLT. Refracted through other lenses in `neuroscience.md` §2 (neural correlates), `core-concept.md` §1 (generalization to "salience anchor"), and `manifesto.md` §2.2 (top-level framing).

Talmy (2000, *Toward a Cognitive Semantics*) argues that linguistic structure systematically reflects the cognitive distinction between **Figure** (the salient, foregrounded entity or event) and **Ground** (the backgrounded reference frame providing context).

> "The Figure is a moving or conceptually movable entity whose path or location is at issue; the Ground is a reference entity with respect to which the Figure's path or location is characterized." (Talmy 2000:312)

**CFLT Protocol mapping:**
- `[Core Action/Result]` = the Figure (what happened)
- `[Condition/Reason] → [Space/Context] → [Time]` = the Ground (under what circumstances)

CFLT thus codifies a **Figure-First** linearization of the Figure-Ground asymmetry. While natural languages distribute Figure and Ground across multiple word-order strategies, the cognitive primacy of the Figure is robust. Talmy's **Contingency Principle** further suggests that humans prioritize the event that is contingent on the frame; in the CFLT Protocol, the Core (contingent event) is placed first, followed by the frame-providing Ground modifiers.

### 2.2 Langacker's Profile-Base Distinction
In Cognitive Grammar (Langacker 1987, 2008), every linguistic expression has a **profile** (the entity or relation foregrounded for attention) against a **base** (the conceptual content presupposed). The profile is what the expression "is about."

**CFLT mapping:** the Core Action *is* the profile of an event-denoting clause. CFLT enforces that the linear utterance opens on the profile, not the base.

---

## 3. Parsing Efficiency: Early Immediate Constituents (EIC)

> **Canonical introduction.** This section is the canonical psycholinguistic statement of EIC in CFLT. Refracted in `mathematics.md` §3 (CRD ratio formalism), `neuroscience.md` §4 (BA 44 / lpSTG dependency-length effects), and `pedagogy.md` §4.1 (the "Modifier Trap" as the pedagogical face of EIC).

Beyond conceptual salience, CFLT is supported by the psycholinguistic requirement for parsing efficiency. John Hawkins (1994, 2004) proposes the **Early Immediate Constituents (EIC)** principle: the human processor prefers word orders that allow it to identify the major building blocks (ICs) of a phrase within the shortest possible window.

### 3.1 Minimizing the Constituent Recognition Domain (CRD)
The CRD is the word-count required to identify all ICs of a phrase. Efficiency is the ratio of ICs to the CRD.

By placing the Core in position 0, CFLT ensures that the "anchoring" constituent of the main clause is identified immediately. This results in an **EIC ratio approaching 100%** for core recognition, drastically reducing the "look-ahead" load on working memory. This is particularly beneficial for L2 learners who have limited cognitive resources for managing incomplete syntactic trees.

### 3.2 Incremental Processing vs. the Modifier Trap
CFLT creates a **head-initial** structure at the discourse level. This enables **incremental processing**: the brain can "attach" details to a known core as they arrive. In contrast, head-final (Topic-First) languages like Chinese often place complex modifiers before the head, forcing the listener to hold a string of descriptors in memory before knowing what is being described — the "modifier trap." CFLT eliminates this trap for the L2 learner.

---

## 4. Information Structure: Theme, Rheme, Given, New

### 4.1 Functional Sentence Perspective (Prague School)
Mathesius (1929), Firbas (1992), and the Prague School developed the concept of **Communicative Dynamism (CD)**: every clause-element carries a degree of "newness" or informational push. The element with the highest CD typically falls toward the end of the clause in English ("end-focus"), but the **thematic** element — what the message is *about* — typically opens the clause.

**Tension with CFLT:** Functional Sentence Perspective predicts that *new and important* information ends a sentence (end-focus, end-weight). CFLT puts the most important information first.

**Resolution:** CFLT is not about packaging information for a hearer who already shares context (where end-focus optimizes); it is about **unambiguously asserting the action as the topic** for a hearer who does not yet share context. CFLT thus aligns with Topic-Comment structures in topic-prominent languages (Li & Thompson 1976) where the topic — here, the core action — anchors the clause.

### 4.2 Givenness Hierarchy and Accessibility
Gundel, Hedberg & Zacharski (1993) and Ariel (1990) describe how speakers manage referent accessibility: more accessible (given) referents take shorter, earlier-mentioned forms. CFLT intersects with accessibility theory in that the Core Action, once fronted, becomes the accessible "given" against which all subsequent modifiers are interpreted.

---

## 5. Speech Production: Levelt's Model

Levelt (1989, *Speaking: From Intention to Articulation*) describes a three-stage production architecture:

1. **Conceptualizer** — generates the *preverbal message* (intent + event structure).
2. **Formulator** — encodes the message into grammatical and phonological form.
3. **Articulator** — produces physical speech.

Crucially, the Conceptualizer's output is **language-neutral**. The semantic core of the intended event exists before any L1- or L2-specific formulation.

**CFLT's pedagogical claim is grounded here:**

> If the preverbal message is language-neutral, then training learners to *linearize the preverbal message* in a fixed Core-First order before entering the Formulator stage decouples conceptual structuring from L1 surface grammar.

Once the message is pre-linearized as `[Core] → [Reason] → [Space] → [Time]`, both L1 and L2 formulation become token-substitution exercises over the same linearized scaffold. This is the cognitive mechanism by which CFLT reduces L1→L2 restructuring cost.

---

## 6. Universal Grammar: Two Different Senses of "Core"

A potential confusion: Chomsky's framework also uses the word "core." It is essential to keep the two senses apart.

| | **Chomsky's *core grammar*** (1981, 1986) | **CFLT's *Core*** |
|---|---------------------------------------|-------------------|
| Domain | Set of grammatical rules | A specific constituent in a specific utterance |
| What it picks out | The universal-principles + parametrized rules of a language | The salience anchor — what the speaker is fundamentally committing to |
| Status | Descriptive linguistic claim | Normative pedagogical/computational protocol |
| Example | "Subject-verb agreement is core; quirky case-marking is periphery." | "In *I went out, because…*, the Core is *went out*." |

These are two different conceptual moves on the word "core":
- **Chomsky's core** is a **classifier on the rule inventory**: which rules belong to the universal core?
- **CFLT's Core** is a **selector on a single utterance**: which constituent is the salience anchor?

CFLT's contribution is orthogonal to Chomsky's core/periphery distinction. CFLT does not classify rules; it specifies a linearization protocol. Chomsky's framework is **compatible with** CFLT (it does not forbid the protocol's linearization rule), but it does not **predict** it either. The two operate at different levels of grammatical theory.

The terminological coincidence is unfortunate but harmless once the distinction is made explicit.

---

## 7. Linguistic Relativity (Sapir-Whorf) and L2 Acquisition Friction

### 7.1 The Strong vs. Weak Hypothesis
The strong Whorfian claim — that language determines thought — is largely rejected (Pinker 1994). The **weak version** — that language influences habitual cognitive patterns — is well-supported (Lucy 1992; Boroditsky 2001).

### 7.2 Application to CFLT
For learners moving between languages with strongly divergent information packaging (e.g., Mandarin's topic-prominent + time-initial structures vs. English's subject-prominent + tense-marked structures), the cognitive friction of restructuring is real and measurable (Slobin 1996, "Thinking for Speaking").

CFLT proposes a **neutral buffer sequence** — the Core-First linearization — that bypasses both L1 and L2 surface idiosyncrasies. Once the learner habitually produces preverbal messages in the buffer order, L2 surface formulation becomes mechanical token substitution.

This is consistent with Slobin's "Thinking for Speaking" framework, which holds that what differs across languages is not deep cognition but the language-specific patterns of *organizing* cognition for verbal expression.

---

## 8. Construction Grammar and Pedagogical Tractability

Goldberg's Construction Grammar (1995, 2006) treats grammar as a learned inventory of form-meaning pairings ("constructions") rather than abstract rules. This is highly compatible with CFLT's pedagogy:

- CFLT treats each `[Core] → [Reason] → [Space] → [Time]` slot as a **construction template**.
- Learners acquire fluency by filling slots, not by deriving sentences from abstract phrase-structure rules.
- Industry-specific token packs (medical, IT, finance) plug into the same constructional slots.

This makes CFLT compatible with the modern, usage-based mainstream of cognitive and constructional linguistics.

---

## 9. Natural Semantic Metalanguage (Wierzbicka)

The NSM program (Wierzbicka 1996; Goddard & Wierzbicka 2002) identifies a small inventory (~65) of **semantic primes** — concepts hypothesized to be lexicalized in all human languages (e.g., I, YOU, DO, GOOD, BECAUSE, BEFORE). NSM uses these primes as a metalanguage for cross-linguistic semantic description.

**CFLT application:** the four-element sequencing protocol corresponds closely to NSM primes:
- `[Core Action]` ↔ DO, HAPPEN, FEEL
- `[Condition/Reason]` ↔ BECAUSE
- `[Space/Context]` ↔ WHERE, IN, AT
- `[Time]` ↔ WHEN, BEFORE, AFTER

NSM thus provides CFLT with a **language-independent vocabulary of slot fillers**. A learner moving between any two languages can use NSM-decomposed thoughts as the bridge.

---

## 10. Honest Limitations

A rigorous foundation must list what CFLT does *not* claim and where its linguistic case is weaker:

1. **CFLT is not a descriptive universal of word order.** Surface word-order typology classifies languages by where the *verb* falls; CFLT does not address verb position. CFLT operates one level up: the salience-defined Core, which may or may not coincide with the verb.
2. **End-focus tension.** In information-packaging terms, English natively places new/heavy information at the end; CFLT inverts this for pedagogical clarity, accepting some loss of native idiomatic feel in early production.
3. **Topic-Comment vs. Subject-Predicate.** CFLT aligns more naturally with topic-prominent languages (Li & Thompson 1976) than with strictly subject-prominent ones. Learners moving from Mandarin to English will find CFLT intuitive on the source side and slightly artificial on the target side until polished by the Grammar Overlay layer.
4. **Idiomaticity.** Idiomatic L2 production requires moving *beyond* the protocol's rigid slots. CFLT is an entry scaffold, not a terminal grammar.

---

## 11. Open Research Questions

1. **Empirical validation.** Does CFLT-trained production measurably reduce L1→L2 restructuring latency? (Suitable for a between-subjects experiment with eye-tracking and articulation-onset measurement.)
2. **Typological generalization.** How does CFLT perform when L1 and L2 are both strongly head-final (e.g., Japanese↔Korean) — does the protocol still help, or is the cognitive overhead already minimal?
3. **Critical period.** Does CFLT benefit adult learners disproportionately compared to children, given that adults are more reliant on explicit conceptual scaffolds?
4. **Idiomaticity ceiling.** At what proficiency level does strict protocol adherence become a hindrance to native-like fluency, and how should the Grammar Overlay layer escalate to relax it?

---

## 12. Cited Works

See [`bibliography.md`](../bibliography.md) for full references.

---

## See Also

- [`core-concept.md`](./core-concept.md) — Canonical disambiguation of "Core" as salience anchor; read first if confused about scope.
- [`phonetics.md`](./phonetics.md) — Phonetic transfer and articulatory bridges, the surface-form complement to syntactic linearization.
- [`sociolinguistics.md`](./sociolinguistics.md) — How register and politeness wrap around the Core without disturbing its position.
- [`pedagogy.md`](./pedagogy.md) §7 — Levelt's speech-production model as the pedagogical hinge for §5 here.
- [`mathematics.md`](./mathematics.md) §3 — EIC re-derived in terms of CRD ratio.
- [`neuroscience.md`](./neuroscience.md) §4 — EIC's neural correlates (BA 44, lpSTG dependency-length effects).
