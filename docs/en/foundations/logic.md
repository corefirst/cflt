# Logical Foundations of CFLT/CFLM

> Companion to: [`manifesto.md`](../manifesto.md)
> Read first: [`core-concept.md`](./core-concept.md) — defines "Core" as a salience anchor, not a syntactic predicate.
> Purpose: Show how formal logic, lambda calculus, categorial grammar, speech-act theory, and Relevance Theory motivate CFLM's *early-commitment* principle. **None of these formalisms is the surface form CFLM produces — they are inspirations for why early commitment to the salience anchor is computationally well-formed.**

---

## 1. The Through-Line: Early Commitment to the Salience Anchor

Across multiple formal traditions, the same pattern recurs: **the central commitment of an expression should be made early, and modifiers should attach to it after the commitment is in place.**

- In **predicate logic**, the predicate is the outer functor; arguments are bound after.
- In **lambda calculus**, the function exists before the arguments it consumes.
- In **categorial grammar**, the head functor combines with arguments in a fixed schedule.
- In **speech-act theory**, the illocutionary force is the act being performed; everything else conditions it.
- In **Relevance Theory**, the highest-relevance item should be processed first to maximize cognitive effects per unit effort.

CFLM borrows this convergent pattern and applies it to natural language. The Core (salience anchor) is committed to early; `[Reason] → [Space] → [Time]` modifiers attach afterward. **The output is natural language**, not formal notation — but the conceptual order is the same one formal logic has used for over a century.

> **What this document is not:** This document does not claim that CFLM produces formal-logic notation, that CFLM is verb-first, or that CFLM is predicate-first in the syntactic sense. It claims that the *abstract principle of early commitment*, which formal logic articulates clearly, is one of CFLM's intellectual ancestors — and that the resulting natural-language form is computationally well-formed for the reasons formal logic makes precise.

---

## 2. Predicate Logic (Frege, Russell)

Frege (1879, *Begriffsschrift*) introduced predicate logic precisely to disambiguate natural-language thought. In Frege's notation:

$$
P(a, b, c)
$$

The predicate $P$ — the function symbol — appears outermost; the arguments $a, b, c$ are bound to it. Russell (1905, "On Denoting") later argued that English surface forms systematically disguise this underlying logical structure.

**What CFLM borrows from this tradition:**
- The principle that *the central commitment of a proposition is the function-like component, and arguments are bound to it.*
- The discipline of making the commitment **explicit and early**, rather than letting it emerge implicitly from word order.

**What CFLM does *not* borrow:**
- The **notation** $P(a, b, c)$. CFLM produces "I went out, because it rained, at home, yesterday." — comprehensible English with structured ordering.
- The reduction of "Core" to "predicate symbol." A copular construction ("That girl is my sister") has no obvious "predicate" in the action-verb sense, but it has a clear Core (the identity assertion). CFLM handles this; bare predicate logic does not.

The lesson from Frege/Russell is **structural**, not notational: organize the utterance around its central commitment, then bind the modifiers.

---

## 3. Lambda Calculus and Function Application Order

Church (1936) lambda calculus represents computation as function application. A function $\lambda x.\,f(x)$ is *applied* to arguments — the function exists prior to the arguments it consumes.

In semantic composition, an event $e$ predicated of participants and modifiers is built by successive application:

$$
((((\lambda e. \, \text{COMMIT}(e)) \, a_1) \, a_2) \dots ) \, m_1 \, \dots \, m_k
$$

Here `COMMIT` is the speaker's salience commitment — what the utterance is fundamentally about. The applications $a_i, m_j$ progressively refine the commitment with arguments and modifiers.

**CFLM mapping:** the Core is the outermost commitment; Reason, Space, and Time are successively applied modifiers. Linearizing the application schedule outward-to-inward gives Core-First in surface form.

**Note on generality:** Lambda calculus is type-agnostic — the function $\lambda e.\,\text{COMMIT}(e)$ can wrap an action, a state, an identity, or a speech act. This generality is exactly why the function-application metaphor extends naturally to CFLM's four core types.

---

## 4. Combinatory Categorial Grammar (CCG)

Steedman (2000, *The Syntactic Process*) develops CCG, in which lexical items carry **syntactic categories** (functors and arguments) and combine via formal combinators. A transitive verb has category `(S\NP)/NP` — a function awaiting two NP arguments.

Crucially, CCG admits *multiple equivalent derivations* for the same surface string. Speakers (and parsers) must select one schedule among many.

**CFLM as a CCG schedule choice:** CFLM does not invent a new combinatory grammar. It selects one canonical schedule from CCG's flexible space:

$$
\text{Core} \succ \text{Cause} \succ \text{Place} \succ \text{Time}
$$

This is a **deterministic linearization** — the same combinatory machinery, but with a fixed processing order. The benefit is **predictability**: both human learners and machine parsers know which derivation to expect, reducing planning cost (see `mathematics.md` §7 for the search-space collapse argument).

---

## 5. Speech Act Theory: Illocutionary Force at the Anchor

Austin (1962, *How to Do Things with Words*) and Searle (1969, *Speech Acts*) established that every utterance performs an act — assertion, request, promise, question, etc. — characterized by its **illocutionary force**.

Searle's analysis (1969:30–31) decomposes a speech act into:
1. The **illocutionary force indicator** — what kind of act this is
2. The **propositional content** — what the act is about
3. The **conditions of satisfaction** — when the act has been successfully performed

**CFLM mapping:** the Core, in CFLM, is the linguistic realization of the illocutionary commitment. For each speech-act type:

| Act type | Core takes the form of | Example |
|----------|------------------------|---------|
| Assertion | Action verb / predicate complement | "I went out, because…" |
| Identification | Copular complement | "That girl is my sister, wearing…" |
| Description | Stative predicate | "I'm exhausted, because…" |
| Request | Imperative or modal verb | "Could you help me, because…" |

Note that this list maps directly onto the four core types defined in [`core-concept.md`](./core-concept.md). Speech act theory provides the philosophical grounding for treating these four cases under a single linearization rule: each commits the speaker to a different *kind* of act, but each commits **early**.

---

## 6. Relevance Theory (Sperber & Wilson)

Relevance Theory (Sperber & Wilson 1986/1995) holds that human cognition tends to maximize **relevance** — the ratio of cognitive effects to processing effort.

The Communicative Principle of Relevance:

> Every act of ostensive communication communicates a presumption of its own optimal relevance.

**CFLM as a relevance-maximizing strategy:** placing the Core at position 0 puts the highest-effect token where the listener's attention is greatest. The listener (or LLM, see `llm.md`) can begin computing inferences from the Core onward, rather than waiting through modifiers to discover what the utterance is about.

Native English's end-weight tendency (Quirk et al. 1985) competes with this principle: heavy NPs and given/new structuring often delay the new information. CFLM resolves the tension by treating end-weight as a **stylistic refinement** applied at the polishing stage (the Grammar Overlay in the product implementation), not at the conceptual scaffold stage.

This is consistent with the broader lesson: CFLM optimizes **conceptual order**; native idiom optimizes **surface flow**. The Grammar Overlay layer reconciles them.

---

## 7. Gricean Maxims

Grice (1975) proposed the Cooperative Principle and four maxims:

| Maxim | Statement | CFLM correspondence |
|-------|-----------|---------------------|
| Quantity | Be informative, not over-informative | Four-slot template enforces minimum sufficient information |
| Quality | Be truthful | Orthogonal to CFLM (a content concern) |
| Relation | Be relevant | Core-First places the most relevant token at position 0 |
| **Manner** | **Be clear, brief, orderly** | **CFLM's fixed slot order is the orderliness condition** |

The Maxim of Manner — *"Be orderly"* — explicitly requests predictable linearization. CFLM provides exactly one canonical order, fully satisfying this maxim. This makes CFLM unusually *Gricean-aligned*: native speakers improvise orderliness through context-sensitive heuristics; CFLM provides a single rule that achieves the same goal deterministically.

---

## 8. Discourse Representation Theory (Kamp)

Kamp (1981) introduced Discourse Representation Theory (DRT) to handle **incremental** semantic interpretation: each new clause updates a structured discourse representation, with referents introduced and conditions accumulated over time.

DRT formalizes the intuition that meaning is built **left to right**, with each utterance contributing to a growing representation.

**CFLM mapping:** if the Core is introduced first, it instantly establishes the central discourse referent — the event variable, identity claim, state, or speech act — against which all subsequent contributions are anchored. Modifiers attach to a referent that already exists in the discourse representation, eliminating the temporary ambiguity that would arise if modifiers appeared before their target.

This is exactly the property that modern autoregressive language models (causal/left-to-right) also exploit (see `llm.md`).

---

## 9. Modal and Temporal Logic Under CFLM

The four CFLM slots align with operators in standard logical extensions:

| CFLM slot | Logical operator | Reading |
|-----------|------------------|---------|
| Core | The asserted commitment $C$ | Whatever the speaker fundamentally commits to |
| Condition/Reason | $\Box(\phi \to C)$ or $\text{BECAUSE}(\phi, C)$ | Causal/conditional grounding |
| Space/Context | Spatial operator $\text{AT}_l(C)$ | Spatial location of $C$ |
| Time | Temporal operator $\text{AT}_t(C)$ | Temporal location of $C$ |

This is an **operator-stacking** reading: $C$ is the innermost commitment; reason, space, and time are progressively more "outer" modal-temporal operators wrapping it. Linearizing them outward-from-core gives exactly CFLM's order.

The advantage of this framing is that it works regardless of *what kind* of commitment $C$ is. Whether $C$ is an action ("went out"), a state ("exhausted"), an identity ("is my sister"), or a request ("help me"), the operator stacking is the same.

---

## 10. Honest Limitations

1. **Formal notation is the analogy, not the surface form.** Predicate-logic notation (`P(a,b,c)`), lambda terms, and CCG categories are inspirations for *why early commitment is computationally well-formed*. CFLM's actual output is natural language. A reader concluding "CFLM is formal-logic notation" has misread; see [`core-concept.md`](./core-concept.md).
2. **Logical priority ≠ pragmatic priority.** Formal logic places the function outermost, but human conversation is governed by pragmatics where given information often precedes new (Topic-Comment, Theme-Rheme). CFLM optimizes for *clarity of salience commitment*, which can conflict with native idiomaticity — the Grammar Overlay layer reconciles them.
3. **Categorial flexibility is sacrificed.** CCG explicitly admits multiple equivalent derivations; CFLM picks one canonical schedule. This trades flexibility for predictability — a fair exchange for pedagogy and machine processing, but a real loss for fully native idiomatic production.
4. **Negation and quantifier scope** are underspecified in the four-slot template. Complex utterances (negative existentials, generic statements, counterfactuals) may need slot extensions or escape hatches; this is a known open problem.
5. **Nested speech acts.** Performatives like "I promise to leave tomorrow" embed a verb that *is* the speech act and a complement that *names* a future action. Which slot does each fill? CFLM needs a meta-rule for nested acts — likely the outer act is the Core and the inner content fills the modifier slots.

---

## 11. Cited Works

See [`bibliography.md`](../bibliography.md) for full references.
