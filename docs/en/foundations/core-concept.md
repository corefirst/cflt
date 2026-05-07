# What "Core" Means in CFLM — Salience, Not Syntax

> Companion to: [`manifesto.md`](../manifesto.md)
> Purpose: Define the operational meaning of "Core" in CFLM precisely. Distinguish it from verb-first, predicate-first, and other syntactic notions that have been informally conflated with it. **This document takes precedence wherever the other foundation documents appear to reduce "Core" to a syntactic category.**

---

## 1. Why this Clarification Matters

A reader skimming the linguistics or logic foundations could come away thinking:

> "CFLM is verb-first / predicate-first."

This is **wrong**, and the misreading would undermine the entire pedagogical and AI-alignment case for CFLM. CFLM is grounded in human cognition and is meant to produce **comprehensible human language**, not formal-logic notation or typologically rare verb-fronting word order.

The corrective principle is simple:

> **Core is the *salience anchor* of an utterance — the constituent the speaker is fundamentally committing to. It is a semantic-pragmatic concept, not a syntactic one.**

The Core may *coincide* with the verb or predicate, but it is not defined by them. CFLM places the Core in linear position 0; what fills position 0 depends on what the speaker is actually asserting.

---

## 2. Distinguishing Core from Adjacent Concepts

| Concept | Tradition | What it picks out | Example |
|---------|-----------|-------------------|---------|
| **Verb / Predicate** | Syntax | A part-of-speech category | "go", "is", "eat" |
| **Topic** | Information structure (Lambrecht 1994) | What the clause is *about* | "As for John, he left" |
| **Theme** | Systemic Functional Grammar (Halliday) | The starting point of the message | "Yesterday, I left" |
| **Figure** | Cognitive semantics (Talmy 2000) | The foregrounded entity/event | "*The cat* is on the mat" |
| **Core (CFLM)** | This project | The salience anchor — the committed assertion | "*I went out*, because it rained" |

These categories overlap in many sentences but are distinct. CFLM's Core is closest to **Figure** and **profile** (Langacker) — both salience-defined, not syntactically defined.

---

## 3. The Four Types of Core

Every well-formed CFLM utterance commits to one of these four core types in position 0:

| Type | Example (CFLM-L2 form) | What's foregrounded |
|------|------------------------|---------------------|
| **Action** | *I didn't go out, because it rained, at home, yesterday.* | An event |
| **State** | *I'm exhausted, because of the meeting, in the office, all afternoon.* | A condition |
| **Identity / Description** | *That girl is my sister, wearing a red dress, in the photo, from last summer.* | An identity assertion |
| **Request / Question** | *Could you pass the salt, please, on the table, now?* | A speech act |

The selection of Core is a **semantic decision** the speaker makes ("what am I really trying to say?"). The placement of Core in position 0 is the **protocol** CFLM enforces.

---

## 4. CFLM Outputs Are Comprehensible Human Language

A common worry: does forcing Core-First produce alien-sounding sentences?

**No, because CFLM does not invert syntactic word order.** Compare:

| Form | Example | Verdict |
|------|---------|---------|
| Strict typological VSO | *Went I to the store yesterday.* | Alien (rare in English; ungrammatical for native readers) |
| Strict formal logic | *GO_OUT(I, ¬, store, yesterday).* | Not language — formal notation |
| **CFLM-L2** | *I didn't go out, because it rained, at home, yesterday.* | Comprehensible English, slightly clipped, parseable by any reader and any modern LLM |
| Idiomatic English (post-Grammar-Overlay) | *Yesterday it rained, so I stayed home and didn't go out.* | Native fluent form, derived from CFLM by the Grammar Overlay |

CFLM-L2 sits between alien constructions and fully idiomatic prose. It's the **scaffold form**: comprehensible and consistent enough to anchor learning and machine processing, while carrying enough native flavor that humans don't reject it.

---

## 5. Why This Works for LLMs

LLMs are trained on **human language corpora**, not on formal-logic notation or VSO-rare patterns. Therefore:

- A formal-logic-style prompt (`P(a,b,c)`) is **off-distribution** for LLMs and produces unstable behavior.
- A typological VSO prompt (*Went I yesterday...*) is **rare in training data** and triggers low-confidence generation.
- A CFLM-L2 prompt (*I went, because... at... yesterday*) is **slightly off-idiomatic but firmly in distribution** — it looks like clipped, structured English that LLMs handle well.

This is the deeper reason CFLM aligns with LLM behavior: not because LLMs love formal logic, but because **CFLM stays inside the human-language manifold while imposing useful structure on it**. The Core-First protocol is a constraint within natural language, not a replacement for it.

---

## 6. Why This Works for Human Learners

The Core-First habit is a **cognitive scaffold for L2 production**, not a destination grammar.

A learner who internalizes "select Core first, then bind modifiers" gains three concrete benefits:

1. **Reduced restructuring cost.** L1 thought no longer needs to be re-parsed into L2 surface order; both languages share the CFLM intermediate scaffold (see `mathematics.md` §8).
2. **Stable parsing anchor.** When listening to L2, the learner expects the Core to appear early, so attention is correctly allocated.
3. **Foundation for stylistic flexibility.** Once the Core-First habit is automatic, learners can deliberately depart from it for rhetorical effect (foregrounding time, hedging, etc.). CFLM is a *base case*, not a ceiling.

The Grammar Overlay layer (in the product) is what polishes CFLM-L2 into native-idiomatic L2 — and over time, the learner internalizes both layers and chooses naturally between them.

---

## 7. Expressive Variability: CFLM Is the Unmarked Default, Not the Only Permitted Form

A natural objection: in any human language, the same propositional content can be expressed in many surface forms — and this is the **norm**, not a defect of language. Compare these expressions of the same proposition:

| Surface form | Information-structural framing |
|--------------|-------------------------------|
| *I didn't go out, because it rained, at home, yesterday.* | Core-First (CFLM-L2): action foregrounded |
| *Yesterday, because of the rain, I stayed home.* | Time topicalized; rain as background |
| *It rained yesterday, so I didn't go out.* | Cause-then-effect narrative flow |
| *The rain kept me home all day yesterday.* | Cause as agent; nominalized rhetoric |
| *Out I never went — the rain wouldn't let up.* | Marked fronting for emphasis |

All of these are perfectly fluent English, encoding the same core proposition. They differ in **information structure, emphasis, register, and rhetorical force**. A native speaker chooses among them based on context, audience, and intent. **This expressive variability is universal across human languages — every language has multiple ways to say the same thing, and that is essential to communication, not a flaw.**

If CFLM proposes a single fixed order, does it conflict with this reality?

### 7.1 The unmarked / marked distinction

In linguistic theory, the **unmarked** form is the default, conventional, neutral expression — what a speaker produces when no special rhetorical purpose applies. **Marked** forms are deliberate deviations from the default, used for emphasis, topicalization, contrast, hedging, or stylistic effect (Greenberg 1966; Croft 1990; Givón 2001).

CFLM proposes Core-First as **the unmarked conceptual default** for its target use cases — not as the only permitted form.

| Form | Status in CFLM | Function |
|------|---------------|----------|
| **CFLM-L2 (Core-First, four slots)** | Unmarked default | Neutral assertion; baseline for learners; consistent format for AI processing |
| Topicalized: *"Yesterday, I went out…"* | Marked | Foreground the temporal frame |
| Causal-fronted: *"Because of the rain, I stayed home."* | Marked | Foreground the reason |
| Cleft: *"It was the rain that kept me home."* | Marked | Contrastive focus |
| Nominalized: *"The rain kept me home."* | Marked | Cause as agent; written-register style |

CFLM does **not prohibit** marked deviations. It says: *if you have no special rhetorical purpose, the default is Core-First. When you do have such a purpose, depart deliberately.*

### 7.2 Why this distinction matters for learners

Native fluency includes **both**:
- A reliable unmarked default that can be produced without conscious effort, and
- A learned inventory of marked deviations chosen for specific rhetorical effects.

Beginners typically lack both. Intermediate learners often have neither a reliable default nor a controlled inventory of deviations — they produce inconsistent, semi-randomly ordered sentences and cannot tell whether a given ordering is appropriate for context.

CFLM accelerates the learner's progression by giving them the unmarked default first, **then** introducing marked deviations as the next learning layer. This is consistent with how native speakers acquire grammar (default first, exceptions later), with skill acquisition theory (declarative→procedural→automatic with deliberate variation), and with cognitive load theory (build a single schema, then specialize).

### 7.3 Three pedagogical stages

Mapping this onto the skill-acquisition framework (see [`pedagogy.md`](./pedagogy.md) §5):

1. **Declarative stage.** Learner explicitly applies CFLM. Output is consistently unmarked Core-First. The default is being installed.
2. **Procedural stage.** CFLM becomes automatic. The learner can produce the unmarked default without thinking. They begin to **recognize** marked deviations in input — *"why did the speaker put 'yesterday' first there?"*
3. **Expressive stage.** Learner has internalized both the default and a growing inventory of marked deviations. Choices among orderings are deliberate stylistic decisions. CFLM becomes a fallback when cognitive load is high (under stress, in unfamiliar topics) or precision is required.

The scaffold is **not the endpoint**. Mastery includes deliberate departure from the scaffold when the rhetorical context calls for it.

### 7.4 Why this is consistent with the rest of CFLT

This view does not weaken CFLM's central claim — it strengthens it:

- The information-theoretic argument (`mathematics.md` §2) for entropy reduction holds for the unmarked case, where the speaker has no specific reason to deviate. Marked deviations are *meant* to be more effortful — that's how they signal emphasis.
- The LLM positional-bias argument (`llm.md` §3) holds for the unmarked prompt format. A user who deliberately wants to draw model attention to time or place can use a marked ordering as a deliberate steering choice.
- The Relevance Theory argument (`logic.md` §6) explicitly accommodates marked deviations: a marked ordering signals that the deviation itself carries information beyond the proposition.

CFLM is therefore best characterized as: **an unmarked default that can be deliberately departed from, with the departure itself becoming meaningful.**

---

## 8. Common Mis-readings, Explicitly Refuted

| Mis-reading | Correct framing |
|-------------|-----------------|
| "CFLM is verb-first." | CFLM is **salience-first**. The Core may be a verb phrase, a copular complement, a state descriptor, or a speech act. |
| "CFLM contradicts language typology." | CFLM makes no descriptive claim about natural-language word order. It is a **pedagogical and computational protocol** that overlays a fixed conceptual order. |
| "CFLM produces alien sentences." | CFLM-L2 is comprehensible (not idiomatic) English. The Grammar Overlay layer handles idiomaticity. |
| "CFLM is formal-logic notation in disguise." | CFLM is **natural language with constrained linearization**. The notation `P(a,b,c)` is an analogy for one direction of the protocol, not the protocol itself. |
| "CFLM only works for action sentences." | CFLM accommodates four core types (action, state, identity, request). The protocol is uniform; what fills position 0 varies. |
| "CFLM bypasses native idiom." | CFLM is a scaffold layer; native idiom is the surface layer that the Grammar Overlay produces. They coexist, they don't compete. |
| "CFLM forbids saying things any other way." | No. CFLM is the **unmarked default**. Marked deviations (topicalization, fronting, clefts) are part of mature fluency and are explicitly accommodated — see §7. |
| "CFLM is the endpoint of language learning." | CFLM is the **scaffold for the unmarked default**. Mastery includes deliberate departures from CFLM when the rhetorical context calls for them. |

---

## 9. Connection to the Other Foundations

This concept of "Core-as-salience" should be read back into the four discipline-specific foundation documents:

- **`linguistics.md`** — Talmy's Figure and Langacker's profile are the right linguistic kin. Surface word-order typology is **not** the right frame for evaluating CFLM, because CFLM does not claim a typological universal.
- **`logic.md`** — Predicate logic notation `P(a,b,c)` is an analogy for *function-application order*, not for the literal surface form CFLM produces. CFLM is a natural-language overlay inspired by this order, not a notational replacement for it.
- **`mathematics.md`** — The information-theoretic case for Core-First (entropy reduction, search-space collapse) does not depend on the Core being a verb. It depends only on the Core being **the most discriminating constituent**, which is the salience definition.
- **`llm.md`** — The "lost in the middle" and primacy-effect arguments hold whether the position-0 token is a verb, a noun, or any salient category. What matters is that it carries the discriminating signal.

---

## 10. Operational Definition (for Implementers)

For the Logic Transformer engine and for any future AI agent extending CFLM:

```
Core(utterance) := the constituent C such that
  ∀ other constituent C':
    removing C destroys the speaker's intended assertion;
    removing C' degrades but does not destroy it.
```

Equivalently, the Core is what survives a maximal-elision test: if you reduced the utterance to one phrase, the Core is the phrase you'd keep.

This definition is **language-agnostic** and **constituent-type-agnostic** — exactly the properties CFLM needs to be both human-pedagogical and LLM-compatible.

---

## 11. Summary

CFLM is **Core-First**, not verb-first, not predicate-first, not formal-logic-first. The Core is a salience anchor selected by the speaker's intent, placed in position 0 by the protocol, and surrounded by `[Reason] → [Space] → [Time]` modifiers.

The resulting form is comprehensible human language — slightly more structured than idiomatic prose — designed to serve both human learners and human-language-trained LLMs. It is polished into native idiom by the Grammar Overlay layer when needed.

Crucially, CFLM is the **unmarked default**, not the only permitted form. Human languages have multiple expressive forms for any meaning, and that variability is essential to communication. CFLM gives learners and machines a reliable default; deliberate marked deviations from that default are the mark of advanced fluency and are explicitly part of the proficiency arc. The scaffold is the start, not the ceiling.
