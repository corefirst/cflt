# Sociolinguistic Foundations of CFLT

> **Version:** 1.0.0 (Internal Draft)
> **Author:** CFLT Core Team
> **Organization:** [CFLT.center](https://cflt.center)
> **License:** [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)

> Companion to: [`manifesto.md`](../manifesto.md)
> Purpose: Address how the **CFLT Protocol** manages social variables including politeness, honorifics, register, and the tension between "Core Salience" and "Social Face."

---

## 1. The Sociolinguistic Challenge: Face vs. Salience

A potential conflict exists between the **CFLT Protocol** (which mandates early commitment to the semantic Core) and many cultural norms of communication. In "high-context" or "collectivist" cultures, asserting a direct request or result at the start of an utterance can be perceived as aggressive, rude, or "face-threatening" (Brown & Levinson, 1987).

CFLT does not ignore these social realities, but it is explicit about **scope**. The CFLT structure (Core + ground frame) encodes the **propositional–illocutionary skeleton** of an utterance — *what is asserted / requested / asked*. **Politeness, face, and honorifics — and, more broadly, non-literal pragmatic inference such as conversational implicature — sit *outside* that structural scope, as an optional social / pragmatic layer that CFLT does not claim to encode in the Core or the slots.** As a **design choice**, CFLT treats politeness / register as an explicit *wrapper around* the structural skeleton (rather than a force that obscures it) — but the wrapper is a **separate layer, not part of the structural Core**. We flag this as a CFLT strategy, not an empirical claim about politeness in general: cross-linguistically, politeness can also alter syntax, utterance sequence, and discourse strategy, so the "wrapper-without-restructuring" model is a hypothesis to test, not an established property of polite language.

## 2. Politeness as a Logical Wrapper

In the CFLT framework, a "polite" request is modeled as a **Request Core** wrapped in an illocutionary mitigator.

| Element | Direct Form | Polite (CFLT) Form | Logical Role |
|---|---|---|---|
| **Core** | "Give me the salt." | "Could you pass the salt, **please**" | Illocutionary Act (structural Core) + politeness wrapper (mitigator, **outside** the Core) |
| **Reason** | "I need it." | "because I'm seasoning my food" | Contextual Justification |
| **Space** | "On the table." | "on the table" | Spatial Reference |
| **Time** | "Now." | "right now" | Temporal Reference |

**CFLT Strategy:** Place the "Speech-Act Core" (the request) at position 0, and carry politeness as a **social wrapper around** it — the mitigator *Could you … please* — **not** as part of the structural Core. By doing so, the listener receives the "social signal" (politeness) and the "task signal" (the request) simultaneously, without the task being buried in a long preamble.

## 3. Honorifics and Social Indexing (Japanese/Korean)

Languages with complex honorific systems (e.g., Japanese *keigo*) often use verb inflections and specific lexical choices to index the relationship between speaker and hearer.

- **Positioning:** In Japanese (SOV), honorific markers typically cluster at the end of the sentence (the verb). 
- **CFLT Transformation:** When a Japanese speaker uses CFLT to produce L2 English, the "Social Index" is moved to the **Core**. Instead of waiting for a sentence-final verb to signal respect, the learner selects a "High-Register Core" (e.g., "I would appreciate your assistance" instead of "Help me").

This aligns the **Social Salience** (who am I talking to? — a project-internal coinage covering speaker-hearer social relations; cf. Brown & Levinson 1987 *Politeness* on face and social distance) with the **Semantic Salience** (what am I asking for? — the CFLT Core; see [`./core-concept.md`](./core-concept.md) §1 for the *salience anchor* definition). The terms are paired project-internal labels for the two distinct salience-ranking systems CFLT documentation engages with; see [`../glossary.md`](../glossary.md) for the disambiguation between *salience anchor* (CFLT-internal), *Salience Network* (neuroscience import — see [`./neuroscience.md`](./neuroscience.md) §1), and the *Social/Semantic Salience* coinages here.

> **Honest scope: "orthogonal" overstates the relationship.** CFLT documentation sometimes describes the honorific layer as **orthogonal** to the four-slot protocol. The more accurate framing is **partially dissociable**: Momo, Sakai & Sakai (2008, *Brain and Language* 107(1), 81–89) show that Japanese honorification judgment recruits the left inferior frontal gyrus, with activation modulated by individual performance. Cui, Jeong, Okamoto, Takahashi, Kawashima & Sugiura (2022, *Journal of Neurolinguistics* 62, 101041) extend this for socio-pragmatic honorific agreement: lower-status addressee conditions recruit additional bilateral insula and dorsal medial prefrontal cortex (the social-cognitive network) beyond left IFG. Honorific morphology also has known interactions with embedded-clause syntax (e.g., -masu cannot appear in certain embedded contexts; relative clauses host honorifics differently from main clauses). The CFLT pedagogical guidance — apply slot work first, honorific layer second — is *proposed* as a **cognitive workflow** for managing complexity and remains a hypothesis to test, not a validated procedure: the cited neural findings show that honorific processing is complex and interactive, which constrains rather than confirms a clean two-stage separation. It should not be over-claimed as full neural or syntactic independence: the social-cognitive network recruitment is sensitive to addressee status as well as honorific form, and honorific morphology interacts with syntax (above), so partial dissociability is itself bounded.

## 4. Register Scaling: From "Efficiency" to "Elegance"

CFLT methodology defines three levels of **Social Register**:

1.  **Level 1: Minimalist CFLT (Emergency/Technical)** 
    - *Goal:* Maximum speed.
    - *Form:* "Deploy the code, because of the bug, in production, now."
2.  **Level 2: Standard CFLT (Professional/Neutral)**
    - *Goal:* Cooperative communication.
    - *Form:* "I am deploying the code, to fix the bug, on the production server, immediately."
3.  **Level 3: Elegant CFLT (Diplomatic/Formal)**
    - *Goal:* Face-saving and nuance.
    - *Form:* "I would like to inform you that I am deploying a fix, for the critical bug, in the production environment, at this time."

In the CFLT design, across all three levels the **logical sequence is kept identical by construction**; the variable that changes is the **Token Density** and **Lexical Sophistication** within each slot. The intent is to let learners "dial up" politeness without restructuring the underlying protocol. Whether real-world politeness can in fact be scaled this way — without altering order, sequence, or discourse strategy — is a CFLT hypothesis to test, since politeness is not always order-preserving.

## 5. Cultural Relativity and the Social Context Buffer

As discussed in [`linguistics.md`](./linguistics.md), many Asian languages are "Topic-Prominent." Sociolinguistically, this often manifests as "circular communication"—circling the context before hitting the point to avoid appearing blunt.

CFLT addresses this conflict through the **Social Context Buffer**, an optional pragmatic shell that prepends the core protocol: **`[Social Buffer] + [CRST]`**.

- **Function:** The buffer houses greetings, empathy markers, disclaimers, and social framing. It contains no core task logic but serves to "soften" the communication channel.
- **Neural/Cognitive Basis:** This physically separates *emotional labor* (mPFC-driven social indexing) from *logical expression* (CEN-driven task execution).

**Example Transformation:**
- *Pure CRST (Potentially blunt):* "Review this code, because it has bugs, in the main branch, now."
- *With Social Buffer:* "**I know you are super busy today, but** [could you review this code] (Core)..."

CFLT is **proposed** to act as a **Social Buffer** in international professional registers: we hypothesize that the standardized "Global Interlingua" logic creates a neutral context in which directness can be interpreted as **Efficiency** rather than **Rudeness** for speakers from circular-communication backgrounds. This is a register-specific CFLT hypothesis whose outcome is untested; whether CFLT-formatted production is in fact read as Efficiency rather than Rudeness must be measured per register and culture, not assumed. (We make no claim that any specific cross-cultural framework establishes this "directness-as-efficiency" reading — that interpretive outcome is a CFLT prediction, not a cited finding.)

## 6. Honest Limitations

1.  **Cultural Friction:** In extremely traditional or hierarchical settings, strict adherence to Core-First sequencing may still be perceived as culturally "foreign." CFLT is optimized for **Global Functional Fluency**, not for perfect cultural assimilation.
2.  **Irony and Sarcasm:** These complex social signals often rely on violating expected word-order or prosodic patterns. A rigid 4-slot protocol makes "natural" irony difficult to execute.
3.  **Gender and Power Dynamics:** The "Directness" encouraged by CFLT may be socially penalized differently depending on the gender or status of the speaker. This is a broader social issue that a linguistic protocol cannot solve alone.

---

## 7. Cited Works

See [`bibliography.md`](../bibliography.md) (§ Sociolinguistics) for full references. Background works informing this document include Brown & Levinson (1987) on politeness, Hofstede (2001) on broad (and acknowledged-limited) country-level cultural dimensions, and Scollon & Scollon (2001) on intercultural discourse; none is cited as establishing a CFLT-specific outcome.

---

## See Also

- [`linguistics.md`](./linguistics.md) §7 — Linguistic relativity and "thinking-for-speaking," the linguistic backdrop to §5 here.
- [`logic.md`](./logic.md) §5 — Speech-act theory; politeness wrappers as illocutionary mitigators.
- [`core-concept.md`](./core-concept.md) §2 — The Request core type, central to the politeness discussion in §2 here.
- [`../methodology/curriculum-engineering.md`](../methodology/curriculum-engineering.md) — How register levels (§4 here) plug into industry token packs.
