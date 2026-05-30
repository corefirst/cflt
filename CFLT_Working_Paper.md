---
title: "Core-First Language Theory (CFLT): A Discourse-Level Linearization Protocol for Cross-Linguistic Communication and LLM Prompting"
author: "Weifeng (Tercel) Yi"
date: "May 2026"
header-includes:
  - \usepackage{titling}
  - \setlength{\droptitle}{-2cm}
  - \posttitle{\par\end{center}\vspace{1.5em}}
---

ORCID: [0009-0000-3742-4403](https://orcid.org/0009-0000-3742-4403) · Independent Researcher · tercel.yi@gmail.com · [cflt.center](https://cflt.center)\
Version: Working paper · 2026-05 snapshot · License: CC BY 4.0

\noindent\rule{\textwidth}{0.4pt}

## Abstract

Second language acquisition (SLA) and Large Language Model (LLM) prompting share a structural bottleneck: the cost of restructuring a multidimensional semantic representation into a sequential string under language-specific linearization rules. Human L2 learners pay this cost as working-memory overhead — particularly in head-final-to-head-initial transitions — while LLMs pay it as semantic drift, order-sensitivity, and "Lost in the Middle" attention degradation (Liu et al. 2023). This paper presents Core-First Language Theory (CFLT), a normative discourse-level linearization protocol that fixes the relative order of two constituent tiers as `[Core] → [Reason] → [Space] → [Time]`. CFLT operates above the morphosyntactic level: each language assembles the event nucleus (Tier 1, Slot 0) — predicate plus valence-bound participants, manner, and scope-internal operators — using its native syntax, while the protocol governs only the ground frame (Tier 2, Slots 1–3) and the boundary between the two. The Core is a *salience anchor* in the sense of Talmy's (2000) Figure / Langacker's (1987) profile, not a verb or a value judgment about "the most important word." A pilot two-part study (24 cases × 4 levels × 2 languages × 5 frontier models × 3 runs = 720 Part II trials) provides preliminary evidence that CFLT-conformant prompts (i) raise extraction accuracy on the specific distractor-heavy condition (Level 3) from a mean of 65.6% to 100% across all five frontier models surveyed (GPT-5, Gemini 3 Flash, Qwen3.5-Plus, DeepSeek V4 Pro, and Claude Sonnet 4.6 via OpenRouter), and (ii) reduce completion-token cost on reasoning-capable models with visible chain-of-thought traces by up to 38%, while showing no token effect on short-output / concealed-reasoning models. A separate buried-decision condition (Level 4) yields a null-to-slightly-negative effect on one model (DeepSeek V4 Pro, −11pp); the other four models saturate L4, so this regression is now best characterized as a model-specific anomaly rather than a general property of CFLT. We report it because it constrains the theory. We position CFLT as a language-neutral interface format for human–AI synchronized reasoning, and outline the empirical agenda required to test it as a falsifiable cognitive and computational claim. Reproducible extraction logic, python evaluation scripts, and raw 720-trial data logs are publicly available at https://github.com/corefirst/cflt.

Keywords: linearization, salience anchor, second language acquisition, prompt engineering, prompt order-sensitivity, Transformer primacy, cognitive ergonomics, discourse protocol

\noindent\rule{\textwidth}{0.4pt}

## 1. Introduction

The gap between thought and speech is bridged by linearization: the mapping of a multidimensional semantic representation onto a sequential string of words. Natural languages adopt different default linearizations — SVO versus SOV, head-initial versus head-final, subject-prominent versus topic-prominent (Greenberg 1963; Li & Thompson 1976; Dryer 2013) — and these defaults are acquired in childhood at no apparent cognitive cost. For an adult learner of an L2 that is typologically distant from her L1, however, the mapping must be performed deliberately, paying what we will call the Prefrontal Tax: the working-memory cost of restructuring an L1-shaped semantic plan into an L2-shaped surface form in real time (Levelt 1989; Hawkins 2004; Kormos 2006).

A structurally analogous problem has appeared in Large Language Model (LLM) prompting. Autoregressive Transformers (Vaswani et al. 2017) exhibit strong sensitivity to prompt linearization: identical semantic content, presented in different surface orders, yields measurably different output distributions (Lu et al. 2022; Sclar et al. 2024). When task-critical information is buried mid-prompt, models exhibit the Lost in the Middle effect (Liu et al. 2023); when prompt order conflicts with the model's positional priors, reasoning traces lengthen and final answers drift.

Both bottlenecks are, at heart, linearization-cost problems. Core-First Language Theory (CFLT), summarized here, is a discourse-level normative protocol designed as a single remedy: it places the speaker's salience anchor (the "Core") at sequence-initial position, and constrains adjunct ordering by a convention motivated by listener-question priority, concreteness, and deictic recoverability. The protocol is intended to be language-neutral at the discourse layer while leaving each language's internal morphosyntax untouched.

### 1.1 A note on the cross-domain framing

The claim that SLA and LLM prompting share a "linearization cost" is a load-bearing cross-domain analogy and deserves an upfront caveat. Guest & Martin (2023) and the earlier critique tradition (McCloskey 1991) rightly warn that surface analogies between cognitive architectures and neural-network behavior routinely smuggle in unjustified mechanistic identifications. We accept the warning and adopt a deliberately weakened framing throughout the paper: CFLT does not claim that the two systems pay linearization cost through the same mechanism. The human "Prefrontal Tax" is a DLPFC/LIFG/ACC phenomenon (Abutalebi & Green 2007); the LLM "Lost in the Middle" curve is a causal-attention-over-positional-encoding phenomenon (Liu et al. 2023). What CFLT *does* claim is that a single normative intervention — Core-first linearization — happens to be useful in both systems for *partially distinct mechanistic reasons*, and that the human-side prediction (P1, §7.1) and the LLM-side prediction (P2, §7.3) are independently falsifiable. The pilot evidence in §6 bears on P2 only.

A second caveat applies on the human side alone. Slobin's (1996) "Thinking for Speaking" thesis is that linguistic encoding shapes which conceptual distinctions speakers habitually mark — i.e., the preverbal message (Levelt 1989's Conceptualizer stage) is not as fully language-neutral as Levelt's architecture suggests. If Slobin is right, CFLT's scaffold cannot fully *eliminate* L1-shaped Conceptualizer biases; it can only attenuate them by externalizing the linearization decision at production time. We accept this consequence and tighten the §7.1 (P1) falsification rider accordingly: the falsification condition for P1 is *attenuation*, not *elimination* — specifically, that CFLT-trained L2 learners should show measurably less L1-shaped time-fronting / topic-fronting than matched controls (a graded, not all-or-nothing, prediction), failing which the human-side claim is refuted. The multi-track structure of §7 (six sub-programs in §7.1–§7.6) is designed to allow the cross-domain claim to be evaluated component-wise rather than as a single up-or-down verdict; the Slobin-tightened P1 is one component of that evaluation.

The paper proceeds as follows. §2 defines the CFLT protocol and the Core/ground-frame partition. §3 motivates the protocol from human parsing and Transformer attention dynamics, with a deliberate primacy-versus-attention-sink disambiguation. §4 motivates the specific Reason → Space → Time adjunct ordering and labels it a convention with rationale, not a derivation. §5 illustrates operationalization across typologically distant languages. §6 reports a pilot two-part empirical evaluation that bears on the LLM-side prediction (P2) only; the human-side predictions (P1, P3) and the typological / formal-semantic / human-AI-synchronization questions are reserved for the falsifiable research agenda in §7. §8 concludes. Readers from a cognitive-linguistic background should treat §6 as the LLM-side component of the broader research program introduced in §1.2; the human-side evidence is intentionally not in this paper, by the framing of §1.1.

The framework described here is maintained as an open commons (CC BY 4.0) at https://cflt.center; this paper is a derivative scholarly summary intended for academic peer engagement, not a substitute for the canonical specification.

### 1.2 CFLT as the natural-language layer of a broader program

This paper documents the natural-language layer of a broader research program built on a single organizing principle — *Core-then-Frame*: schema-enforced primary content preceding optional modifying content. CFLT applies this principle at the discourse layer, governing how human speakers and LLM receivers organize content for low-cost transmission. Whether the same Core-then-Frame ordering also helps carry discourse-level intent into the *structured tool-call interfaces* through which LLM agents act (e.g., MCP-style function schemas) is an open question we flag in §7.6 — not a contribution of this paper. The empirical contribution of this paper is the natural-language layer alone.

\noindent\rule{\textwidth}{0.4pt}

## 2. The CFLT Protocol

A common misreading is that CFLT prescribes "verb-first" word order at the clause level. CFLT is neither verb-first nor predicate-first — it is a discourse-level constraint on the relative order of two tiers of constituents, deliberately silent about the internal grammar of each tier.

### 2.1 Two-tier structure

Every CFLT-conformant utterance is partitioned into two tiers (cf. Van Valin & LaPolla 1997):

- **Tier 1 — Event Nucleus (Slot 0).** The predicate together with its valence-bound participants (subject, object, instrument, beneficiary, recipient, accompaniment), nuclear- and core-level manner adverbials, and scope-internal operators (negation, modality, aspect, degree). Internal order within Tier 1 follows the target language's native syntax: SVO in English, SOV in Japanese, VSO in Modern Standard Arabic. The protocol does not touch Tier 1's internal grammar.

- **Tier 2 — Ground Frame (Slots 1–3).** Circumstantial adjuncts that situate the event in a world frame, ordered:

  `[Reason] > [Space] > [Time]`

The protocol governs only (i) the boundary between Tier 1 and Tier 2, and (ii) the internal order of Tier 2. The choice of morphosyntactic mechanism within each tier — case marking, prepositions, particles, coverbs, do-support, mood — is delegated entirely to the host language.

### 2.2 The "Core" as salience anchor

We define the Core as the salience anchor of the discourse — the constituent that the speaker is fundamentally "committing to" as the primary event, identity, state, or speech act. This characterization aligns the Core with Talmy's (2000) Figure in his Figure-Ground asymmetry (the salient, foregrounded entity whose path or location is at issue) and with Langacker's (1987, 2008) profile in cognitive grammar (the entity foregrounded for attention against a conceptual base). The CFLT Protocol places the Figure / profile at linear position 0 and the Ground / base in the subsequent slots.

Two routine misreadings must be ruled out explicitly:

- **Core ≠ "the most important constituent."** "Important" is a value judgment by the listener; the Core is a structural commitment by the speaker. In *"I went out, because the house was on fire,"* the most newsworthy information is *the house was on fire* — but the Core is *I went out*, because that is the speaker's primary commitment and the anchor against which the ground frame is interpreted. "Important" is not a defined technical term in formal linguistics, cognitive science, or NLP interpretability; adopting it as the CFLT term would conflate four independent dimensions (focus, salience, accessibility, surprisal) that information-structure theory (Krifka 2008; Gundel, Hedberg & Zacharski 1993) deliberately distinguishes.

- **CFLT's Core ≠ Role and Reference Grammar's Nucleus.** RRG (Van Valin & LaPolla 1997; Van Valin 2005) stratifies a clause as a nested hierarchy in which Nucleus (predicate alone) is contained within Core (predicate + arguments), which is contained within the full Clause (Core + Periphery). CFLT's Core aligns with RRG's *Core* layer plus a small portion of the Periphery (manner) and the scope-internal operator hierarchy of Cinque (1999), not with RRG's Nucleus. A reader who silently identifies CFLT's Core with RRG's Nucleus will incorrectly conclude that valence-bound arguments live in the ground frame.

### 2.3 Four types of Core, one protocol slot

Every well-formed CFLT utterance commits to one of four Core types in Slot 0:

| Type | Predicate signature | Example (English CFLT form) | Theoretical anchor |
| :------ | :-------------------------------- | :--------------------------- | :--------------------------- |
| **Action** | λx.λy. *event*(x,y, …), eventive predicate, valence ≥ 1 | *I didn't go out, because …* | Vendler 1957; Dowty 1979; Levin & Rappaport Hovav 2005 |
| **Identity** | λx. *be*(x, P), copular predication | *That girl is my sister, wearing …* | Hengeveld 1992; Higgins 1979 |
| **State** | λx. *state*(x), stative predicate | *I'm exhausted, because …* | Carlson 1977; Maienborn 2005 |
| **Request** | DIR(s, h, P), directive speech act | *Could you pass the salt, please …* | Searle 1969, 1975; Sadock & Zwicky 1985 |

The selection of Core type is a semantic decision by the speaker ("what am I really trying to say?"). The placement of Core in Slot 0 is the protocol CFLT enforces. The four types share a single protocol slot precisely because the protocol is constituent-type-agnostic at the discourse layer; what fills Slot 0 internally is type-specific and language-specific.

### 2.4 Layer-by-layer universality

Whether CFLT is "universal" depends on which layer one looks at. The table below states the canonical position:

| Layer | Content | Universal? | Role of any specific language |
| :--------- | :----------------------------------------------- | :----------------- | :----------------------------------- |
| **L1: Protocol** | Core in Slot 0; ground frame ordered R > S > T | **Yes — protocol-layer universal** | No language is privileged. |
| **L2: Slot semantics** | Which functional question each slot answers (Why / Where / When) | **Yes — functional universal** | These are functional categories, not surface syntax. |
| **L3: Event-nucleus internal assembly** | How predicate + valence + manner are arranged inside the Core | **No — fully language-specific** | Each language uses its own native syntax. |
| **L4: Boundary edge cases** | Whether *"with X"* / *"in X"* / etc. attach inside Core or to a ground-frame slot | **Mostly universal, with language-specific edge cases** | English may serve as a verification anchor but not as judge. |

CFLT's universality claim is restricted to L1 and L2. The other two layers explicitly delegate to language-specific machinery, and that delegation is what makes the universality claim defensible. The position is deliberately weaker than the strong-UG framing of earlier drafts and is compatible with usage-based / construction-grammar accounts (Tomasello 2003; Goldberg 1995, 2006), with the anti-UG critiques of Christiansen & Chater (2008) and Evans & Levinson (2009), and with the typological-functional tradition of Croft (2001) — the central claim is that Levelt's (1989) preverbal message formation is broadly shared across speakers, not that an innate language-specific Universal Grammar is required. The L2 slot-semantics layer (Why / Where / When) corresponds closely to the Natural Semantic Metalanguage primes BECAUSE / WHERE / WHEN (Wierzbicka 1996), which Wierzbicka argues are lexicalized in every documented language — providing an independent typological motivation for treating these three slot-functions as functionally universal even when their surface morphosyntactic realization varies.

### 2.4.1 Typological challenges to the protocol-layer universality

A typologist will rightly object that L1/L2 protocol-layer universality is a strong claim, and that several documented typological patterns appear to contradict it. We engage three of the strongest:

- **Yup'ik discourse-driven fronting (Mithun 1992).** Yup'ik regularly fronts pragmatically salient constituents — newness, topic shift, contrast — rather than event-anchored Cores. The clause-initial position is determined by discourse pragmatics, not by event identification.
- **Evidential-first languages (Aikhenvald 2004).** In Tariana, Tuyuca, Quechua, and Aymara, the obligatory leftmost element is an evidential marker encoding the speaker's information source (visual / non-visual / inferential / reportative / hearsay). Arguably, the evidential is the salience anchor in these languages.
- **Tagalog topic-prominence (Foley & Van Valin 1984).** The *ang*-marked topic is grammatically privileged and need not coincide with the event anchor.

Four points of response, in order of strength:

1. **Scope restriction (already canonical).** CFLT's typological scope is the surveyed range (§2.4 L1/L2 layer applies to Indo-European, Sino-Tibetan, Japonic, Koreanic, Afro-Asiatic). Yup'ik (Eskimo-Aleut), Tariana (Arawakan), Tagalog (Austronesian) are outside it. The universality claim does not extend to them; the rest of this section explains why this is not just retreat.
2. **Salience anchor ≠ event anchor — with an independent operational test, not a tautology.** The CFLT Core is defined constituent-type-agnostically (§2.2; four types: Action, Identity, State, Request). A reasonable concern with this move is that broadening "Core" beyond the action-verb canonical type risks tautological redefinition: if "the salience anchor" is just "whatever is at position 0," CFLT's protocol becomes unfalsifiable (any leftmost element is post-hoc relabeled as the anchor). To prevent this, we pre-commit two independent operational tests for what counts as the salience anchor in a given utterance, both of which are *position-independent*:
   - **(T1) Speaker-commitment substitution test (from §2.2 canonical disambiguation):** the salience anchor is the constituent whose lexical substitution most changes *what proposition the speaker is asserting*, holding the rest of the utterance fixed. Substituting the place adverbial typically yields the same event under a different scene-frame; substituting the salience anchor yields a different propositional commitment.
   - **(T2) Listener-question test:** the salience anchor is the constituent that answers the listener's first natural question after the speaker stops mid-utterance — "what is the speaker doing / asserting / committing to?" — independent of which constituent currently sits at position 0.
   
   Falsification rider. If (T1) and (T2), applied to a corpus of unmarked declaratives in a non-event-prominent language, identify the salience anchor as a constituent other than the one currently at position 0 in that language's default linearization, then either (a) CFLT's protocol-layer prescription is mis-aligned with that language's information packaging and the universality claim is refuted for it, or (b) the language is a candidate for the genre-conditional / fifth-Core-type extension described in point 4 below. The disjunction is not a free escape: case (b) is admissible only if the mismatch is systematic (a recurring information-packaging pattern), not item-by-item rescue. Critically, this means the protocol-layer claim is falsifiable per language: in any L1/L2 candidate language, (T1) and (T2) can be applied to a held-out corpus before any CFLT scaffold is taught, and a systematic mismatch is grounds for restricting the claim, not for redefining the anchor.
3. **Normative protocol vs. descriptive typology.** Even if Yup'ik's *current* default linearization is pragmatically driven, this is a fact about Yup'ik's descriptive grammar, not a verdict on whether a Yup'ik L2 learner of English would benefit from a CFLT scaffold. The L1/L2 universality claim concerns the L2-production scaffold layer, not the L1's descriptive surface grammar.
4. **Terminological mismatch.** The word "Core" has eventive resonance and may mislead readers from non-event-prominent traditions. A possible future expansion of the taxonomy is a fifth Core type — Evidential/Stance Core — to cover the evidential-first languages explicitly. Until that work is done, we restrict the L1/L2 universality claim to the surveyed typological range and treat evidential-first and pragmatically-ordered languages as principled extensions pending empirical investigation, not refuting counterexamples.

This response does not defend CFLT *outside* the surveyed range; it defends the *restricted* version against the *general* refutation. The deeper engagement with the anti-UG opposition (Tomasello 2003; Christiansen & Chater 2008; Evans & Levinson 2009; Newmeyer 2005) and with the Mithun/Aikhenvald typological literature is maintained in the canonical foundations document (cflt.center/foundations/linguistics §6.2).

### 2.5 Disambiguation from adjacent literature

The trigram *"core first language"* also appears in Ambridge & Wagner (eds. 2021), *Testable Theories of Core First Language Acquisition* (*Journal of Child Language*, Special Issue 48/S5). The two works share three words but address different concerns: Ambridge & Wagner parses as `[core] + [first-language-acquisition]` and concerns the core mechanisms by which children acquire their L1; CFLT parses as `[core-first] + [language-theory]` and concerns the core-first sequencing rule for cross-linguistic discourse. We flag the distinction explicitly because retrieval systems will surface both alongside each other.

\noindent\rule{\textwidth}{0.4pt}

## 3. Cognitive and Computational Mechanics

### 3.1 Human parsing: from preverbal message to incremental processing

Levelt's (1989) production architecture distinguishes three stages: Conceptualizer (preverbal message formation, language-neutral), Formulator (grammatical and phonological encoding, language-specific), and Articulator (motor execution). The essential point here is that the Conceptualizer's output is language-neutral — the semantic core of an intended event exists before any L1- or L2-specific surface form.

CFLT's pedagogical claim is grounded here: if the preverbal message is language-neutral, then training the learner to linearize the preverbal message in a fixed Core-First order *before* entering the Formulator stage decouples conceptual structuring from L1 surface grammar. Both L1 and L2 formulation then become token-substitution exercises over the same linearized scaffold, rather than full structural restructuring.

This account is further supported by Hawkins's (1994, 2004) Early Immediate Constituents (EIC) principle — formalized as Minimize Domains — under which the human processor prefers structures that allow the rapid identification of phrasal heads, shortening the Constituent Recognition Domain (CRD). Placing the Core at Slot 0 minimizes the CRD for the anchoring constituent of the discourse, drastically reducing the look-ahead buffer load on working memory. For learners coming from a head-final or modifier-heavy L1 (e.g., Mandarin pre-nominal relative clauses; Japanese clause-final verbs), this inverts the cognitively expensive Modifier Trap at the discourse layer: the learner discharges working-memory contents incrementally, treating subsequent adjuncts as low-priority refinements that can be appended without revising prior commitments.

### 3.2 LLM Transformer attention: primacy, *not* attention sinks

A careful disambiguation is required here, because two distinct mechanisms cause early-position over-attention in Transformer LLMs and they are routinely conflated.

- **Attention sinks (Xiao et al. 2024).** Because the softmax denominator must sum to 1, attention "leaks" into the very first tokens of a sequence regardless of their semantic content. Xiao et al. explicitly note these tokens are *"not being semantically important"* — the sink is a softmax-stability artifact, not a signal of semantic priority. Modern systems typically reserve `<bos>` as a dedicated sink slot.

- **Primacy / positional bias.** Independently, early tokens are attended more heavily by every subsequent token's queries because causal masking compounds early influence over depth. This effect *does* favor semantically rich content placed early. The Lost in the Middle finding of Liu et al. (2023) — a U-shaped accuracy curve in long-context tasks favoring beginning and end over middle — is the document-scale manifestation of this primacy effect.

CFLT exploits primacy, not the sink. When the Core is buried in a prompt, the model's early conditional distribution is high-entropy and downstream tokens inherit that uncertainty — reasoning-capable models lengthen their internal traces because they are, in effect, still searching for the task. Placing the highest-information constituent at the prompt prefix collapses the early branching factor and stabilizes the autoregressive trajectory. The mechanism interacts naturally with Chain-of-Thought prompting (Wei et al. 2022): CFLT contributes stable Slot-0 anchoring for the *task operator*, while CoT contributes the intermediate reasoning structure CFLT does not specify; the two are complementary rather than competing. (This mechanistic claim is predicted, not measured here — the attention-rollout and causal-attribution tests required to verify it are in §7.3.) Putting CFLT's Core at position 0 does *not* "consume" the sink; it occupies the high-attention prefix region immediately after `<bos>`.

A fourth caveat — non-monotonic position bias. The primacy advantage is task-dependent and non-monotonic, not a universal first-position favoritism. Pezeshkpour & Hruschka (2024) show that LLM accuracy on multiple-choice questions varies by tens of percentage points as a function of option order, with the *direction* of the bias differing across models. Berglund et al. (2024, "The Reversal Curse") show that order-sensitivity is structurally entangled with the learned representations themselves, not just with prompt-time formatting. The implications are concrete: (a) the multi-option *buried-decision* condition in §6.5 (L4) shows that CFLT's strict Slot-0 placement can interact with model-specific properties — DeepSeek V4 Pro shows a −11 pp regression while four other surveyed frontier models saturate L4 at or near 100%; the L4 anomaly is therefore best characterized as a model × task-type interaction rather than a general scope limit of CFLT (see §6.5); (b) the stronger CFLT-as-alignment-constraint upgrade (§7.3) faces a harder problem than CFLT-as-prompt-protocol, because the Reversal Curse implies training-time CFLT exposure may not automatically yield inference-time CFLT robustness. The protocol-layer primacy claim is therefore consistent with the five-model data on L3 (universal saturation) and on L4 (four-of-five ceiling); the single-model L4 regression is preserved as informative empirical content rather than reframed as a CFLT-wide scope boundary.

A second caveat: Liu et al.'s (2023) finding is at document scale (information distributed across 10–30 retrieved documents in a long context window). Extrapolating directly to sentence scale (clause ordering within a single utterance) is a cross-scale analogy, not a measured result; the sentence-scale version of the claim is motivated by primacy + sink dynamics rather than proved by Liu et al. We make the analogy explicit and treat the sentence-scale prediction as empirical content that requires its own validation (see §6 and §7.2).

A third caveat: prompt-order sensitivity (Lu et al. 2022; Sclar et al. 2024) and the partial counter-result of Min et al. (2022) — that demonstration *content* matters surprisingly little for in-context learning while *format and order* are first-order variables — together suggest that CFLT's contribution operates on the format-and-order axis, not on content correctness. We treat this as part of the contribution rather than a defect: fixing both the schema and the linear order of the speaker's commitment is the joint discipline.

\noindent\rule{\textwidth}{0.4pt}

## 4. The Adjunct Ordering: Convention with Rationale, Not Derivation

The claim that the Core occupies Slot 0 is supported by multiple convergent strands of evidence (Talmy's Figure-Ground asymmetry; Hawkins's EIC; Levelt's preverbal message; primacy effects in causal-attention Transformers; Gricean Relevance). The claim that the internal order of the ground frame is Reason > Space > Time is a different kind of claim and deserves a separate, more careful framing: it is a convention selected from the 3! = 6 permutations of the three slots, motivated by three rationales — none of which alone constitutes a derivation of R-S-T as the unique optimum.

(i) Listener-question priority (Gricean Relevance). After receiving the Core ("what happened"), the listener's most discourse-coherent next question is "why?" — the cause typically renders the event interpretable. Place and time are scene-locators that the listener can usually defer or infer from context. Reason therefore sits closest to Core.

(ii) Concreteness ladder (with cross-linguistic caveat). Spatial information is more concrete and perceptible than temporal information, which is more deictic and abstract. Working memory benefits from a concrete-to-abstract progression: hearing *where* helps the listener mentally place the event before the more abstract *when* binding closes the scene. This rationale is not culture-neutral: the conceptual-metaphor literature shows that humans recruit spatial structure to talk about time (Lakoff & Johnson 1980), but the *direction* of the mapping is language-specific (Boroditsky 2000 on Mandarin vertical time-axis; Casasanto & Boroditsky 2008 on asymmetric space-to-time priming; Núñez & Sweetser 2006 on Aymara's reversed time deixis). The concreteness rationale therefore generalizes only to languages where the dominant time-talk strategy is spatially-mediated; for languages or registers where time is encoded primarily by grammatical tense/aspect/evidentiality, the rationale weakens. We treat (ii) as provisionally defensible within the surveyed typological range and flag it as a separable open question whether listener-question priority (rationale (i)) alone suffices to motivate R-S-T without (ii).

(iii) Deictic recoverability. In conversational contexts, time often has a recoverable default ("now" or "the time being discussed"); placing it last allows omission without information loss in many contexts. We note explicitly that Levinson (1983) treats speaker / time / place as three primary deictic axes without arguing one is more recoverable than another — the recoverability claim above is a CFLT-internal observation about non-co-present L2 discourse, not a theorem of deixis theory.

These are engineering arguments. The strongest competitor in the discourse-analysis literature is Reinhart (1984), who argues that in narrative discourse, temporal location is the primary structural anchor — readers organize event sequences by *when* before *why*. Under that account, a Core → Time → Reason → Space order would be defensible for narrative-genre production. CFLT selects R-S-T over the alternatives because in its two targeted use cases (L2 conversational/expository pedagogy and LLM prompt stability), the listener-question and concreteness rationales jointly outweigh narrative-temporal-anchoring; narrative L2 production is a recognized boundary case where the R-T-S alternative may perform better and remains an open empirical question (§7.2).

Operational consequence. CFLT's strong claim — *Core in Slot 0* — is supported by the five independent strands of evidence enumerated at the head of this section (Talmy's Figure-Ground asymmetry; Hawkins's EIC; Levelt's preverbal message; primacy effects in causal-attention Transformers; Gricean Relevance) and is non-negotiable. CFLT's weaker claim — *R then S then T* — is a documented convention with stated reasons and may be revised if empirical evaluation shows another permutation outperforms it for a given genre or language pair.

### 4.1 Coverage: how CFLT compresses Halliday's nine circumstance roles

Systemic Functional Linguistics (Halliday & Matthiessen 2014) decomposes circumstantial adjuncts into nine semantic roles. CFLT's three ground-frame slots are a structured compression of this taxonomy:

| Halliday role | CFLT location |
| :-- | :-- |
| Extent (duration, frequency) | Slot 3 [Time] |
| Location: place | Slot 2 [Space] |
| Location: time | Slot 3 [Time] |
| Manner: quality (e.g., *slowly*) | Inside Core (event nucleus) |
| Manner: means (e.g., *by phone*) | Inside Core (instrument) |
| Manner: comparison (e.g., *like X*) | Inside Core (manner sub-type) |
| Cause: reason / purpose / condition / concession | Slot 1 [Reason] |
| Cause: behalf (beneficiary, *for X*) | Inside Core (valence-bound) |
| Accompaniment (*with John*) | Inside Core (valence extension) |
| Matter (*about X*) / Angle (*according to X*) | Slot 2 [Space] (abstract domain) |

The compression follows the two-tier model exactly: roles internal to the event (how, with-what, with-whom, for-whom) collapse into the event nucleus, while roles framing the event (why, where, when, in-what-respect) populate the ground frame. A reader familiar with SFL will rightly object that Halliday treats Matter (*about X*) and Angle (*according to X*) as distinct from Location:place precisely because the abstract/concrete cut is theoretically loaded. The compression we adopt is functional-level: all three (Location:place, Matter, Angle) answer the listener's "in what domain (physical, semantic, perspectival) does this hold?" question. The compression is therefore *functional-level lossless* and *SFL-experiential-level lossy* — a deliberate trade-off because CFLT is a discourse-level production scaffold, not an SFL replacement. A residual edge case (Halliday's *Role*, e.g., *acting as a teacher*) is handled case-by-case in the project's slot-disambiguation reference. The full SFL treatment, including the Matter/Angle classification basis, is maintained at cflt.center/foundations/linguistics §4.4.1.

\noindent\rule{\textwidth}{0.4pt}

## 5. Operationalization

CFLT is a normative scaffold, not a descriptive claim about natural-language defaults. Its operational value is that it converts structural transformations into lexical substitutions: the learner or prompt author no longer chooses *where to place* a constituent, only *what to place* in each protocol slot.

Example A — Mandarin (topic-time-first L1) to English (head-initial L2):
- L1 default: 昨天（Time）下雨（Reason），我没出去（Core）。
- CFLT pivot: [Core: 我没出去] → [Reason: 因为下雨] → [Space: 在家] → [Time: 昨天]
- L2 output: *"I didn't go out, because it was raining, at home, yesterday."*

Tier 1 (*I didn't go out*) is assembled by English's native morphosyntax — do-support, SVO order, post-verbal negation; the speaker no longer has to *decide* whether to front time or topicalize reason. The protocol fixes that choice.

Example B — Same pivot to Japanese (head-final L2):
- CFLT pivot: identical
- L2 output (spoken / right-dislocated register): 出かけなかった、雨が降ったから、家で、昨日。

Japanese's Tier 1 internal order (SOV) is preserved by its native syntax; only the boundary between Tier 1 and Tier 2 and the order within Tier 2 are governed by the protocol. The protocol survives the typological change even though the surface order of Tier 1's internal arguments does not.

Example C — Human-to-LLM prompt (English):
- Natural prose: *"Yesterday, at the cafe across from the station, because the wifi was unstable, please summarize the attached document into three bullet points."*
- CFLT-reordered: *"Please summarize the attached document into three bullet points, because the wifi was unstable, at the cafe across from the station, yesterday."*

The semantic content is identical; the second form positions the Core directive (*summarize ... three bullet points*) at the prompt prefix, where it benefits from primacy attention.

A worked five-language demonstration (English, Mandarin, Japanese, Korean, Modern Standard Arabic) spanning Indo-European, Sino-Tibetan, Japonic, Koreanic, and Afro-Asiatic typologies, with the native morphosyntactic mechanism (negation, aspect, argument marking) explicitly identified for each, is given in the project's canonical core-concept reference. The key observation is that the protocol-layer order is invariant across the five languages even though each assembles its event nucleus with a completely different morphosyntactic toolkit.

The protocol has been implemented operationally as a human-bilingual-education application (Next.js + Electron, Apache 2.0; see Data and Code Availability) providing four surfaces: a Logic Transformer that restructures natural-language input into CFLT JSON, scenario-based course generation for English↔Mandarin adult learners, multi-turn roleplay with per-turn CFLT-compliance feedback, and progress analytics over local learning logs. The Logic Transformer surface corresponds operationally to the Part I benchmark in §6.4 — the same task, on the same dataset schema, packaged for end-user interaction.

\noindent\rule{\textwidth}{0.4pt}

## 6. Pilot Empirical Evaluation

To assess CFLT's computational claim — that Core-initial linearization stabilizes LLM behavior — we conducted a controlled two-part study (May 2026). All prompts, raw API responses, scoring scripts, and aggregate reports are released alongside this paper (see Data Availability) and are reproducible from a single command. This is a pilot study; its limitations are made explicit in §6.5, and we frame the results as suggestive rather than confirmatory.

### 6.1 Design

The study uses a single shared dataset of 24 cases distributed as 4 difficulty levels × 2 languages × 3 scenarios (12 English + 12 Mandarin items). Each case provides:

- `utterance_control` — natural-prose phrasing, typically reason-first or topic-first;
- `utterance_cflt` — the **same lexical content** reordered as `Core → Reason → Space → Time`; no markup tokens, no compression;
- `ground_truth` — canonical extraction in a fixed schema (`action / target / location / time`).

Levels were designed to probe distinct properties:

| Level | Probe |
| :---- | :------------------------------------------------------------------------------------------------------------------------------ |
| L1 | Single action, 2 fields — ceiling probe; both arms expected to saturate. |
| L2 | Action + location + time, 4 fields — moderate load. |
| L3 | L2 plus *distractor* clauses (red herrings, ongoing context) — primary test of "Lost in the Middle" mitigation. |
| L4 | Multiple candidate actions, the *decided* action buried at end-of-utterance in control — primary buried-decision primacy test. |

Part I — Logic Transformer Benchmark asks whether the CFLT transformation can be performed *by an LLM*. Each case's `utterance_control` is fed to a transformer LLM under a fixed system prompt (no ground-truth values, only the output schema). Three structural-compliance metrics are scored automatically — SC (slot order Core→Reason→Space→Time), SR (Core slot retains the subject), IV (inferred slots carry justifying suggestions) — and a DX metric measures downstream extraction accuracy when the transformer's output is fed back to a separate extractor LLM.

Part II — Control vs. CFLT Extraction is the primary ablation. Each case's `utterance_control` and `utterance_cflt` are fed independently to the same extractor LLM with the same schema-only system prompt. The two arms differ only in clause order. Each arm is repeated N=3 times at `temperature=0` (provider defaults where the API rejects the parameter), giving 24 cases × 2 arms × 3 runs = 144 API calls per model.

Methodological guardrails enforced by the evaluation harness:

- No ground-truth leakage: the system prompt declares only the schema (`action / target / location / time`), never the canonical values.
- The two arms share identical lexical content; the manipulation is **order only**.
- Per-case variance is reported (mean ± std across the 3 runs).
- `prompt_tokens` and `completion_tokens` are reported separately, never merged into a single "gain" number, because they respond to different mechanisms.
- Surface-form synonyms (e.g., `"6 PM today"` ≡ `"today 6 PM"`; *5 楼* ≡ *5楼*) are dataset-driven and auditable, not hidden in scoring code.

Five current-generation models were evaluated in Part II, spanning four distinct output regimes: `openai/gpt-5` (concealed reasoning), `google/gemini-3-flash-preview` (short output), `qwen/qwen3.5-plus` (visible chain-of-thought), `deepseek/deepseek-v4-pro` (visible chain-of-thought), and `anthropic/claude-sonnet-4-6` (short output, routed via OpenRouter as Anthropic's direct API is not OpenAI-compatible). The five models come from five different commercial providers; the cross-provider coverage strengthens the generalizability of the resulting cross-model pattern.

### 6.2 Part II Results — Accuracy

We report non-ceiling Δ-accuracy: the accuracy delta restricted to levels where the control arm has not already saturated (≥ 90%), because on saturated levels CFLT has no headroom and including them dilutes the verdict.

| Model | Informative levels | Non-ceiling Control | Non-ceiling CFLT | Δ |
| :-- | :-- | :-- | :-- | :-- |
| GPT-5 | L3 | 61% | 100% | **+38.9 pp** |
| Gemini 3 Flash | L3 | 78% | 100% | **+22.2 pp** |
| Qwen3.5-Plus | L2, L3 | 75% | 97% | **+22.2 pp** |
| DeepSeek V4 Pro | L3, L4 | 69% | 86% | **+16.7 pp** |
| Claude Sonnet 4.6 | L2, L3 | 78% | 89% | **+11.1 pp** (L3 alone: +28pp; L2 −6pp noise drags aggregate) |

The Level-3 (distractor-heavy) effect is consistent and large across all five models: control accuracy ranges from 56% to 78% (mean 65.6%), CFLT accuracy saturates at exactly 100% for every model. The five-model L3 universality is the primary finding of the study: the primacy advantage is observed across four distinct output regimes (concealed reasoning, visible chain-of-thought, two short-output non-reasoning models) and five different commercial providers.

The Level-4 (buried-decision) effect is sharply characterized by the five-model data: four of the five models show L4 at or near ceiling under both arms (GPT-5 100%/100%, Gemini 94%/94%, Qwen 94%/92%, Claude 100%/100%); only DeepSeek V4 Pro shows the −11 pp regression (83% → 72%). The L4 cases place multiple candidate actions before a final decision; the control's natural narrative sequence (alternatives → final choice) provides a potential reasoning scaffold that CFLT front-loading removes. The five-model evidence now strongly suggests this is a DeepSeek-specific model × task-type interaction, not a general property of CFLT-on-buried-decisions. We retain the result in §6.5 because it is the cleanest informative deviation in the L4 condition and because reporting single-model anomalies is intrinsic to the falsifiability discipline (§7.3).

### 6.3 Part II Results — Token Cost

Token effects split cleanly along the reasoning-versus-non-reasoning axis:

| Model | Prompt tokens Δ | Completion tokens Δ | Reasoning trace? |
| :-------------- | :--------------- | :------------------- | :---------------------------------- |
| GPT-5 | −1.5% | +0.7% | concealed (no exposed trace) |
| Gemini 3 Flash | −1.4% | +1.4% | no |
| Claude Sonnet 4.6 | −1.2% | +0.9% | no |
| Qwen3.5-Plus | −1.1% | **−38.4%** | yes (visible chain-of-thought) |
| DeepSeek V4 Pro | −1.1% | **−12.5%** | yes (visible chain-of-thought) |

Prompt tokens move trivially in either direction (≤ 1.5%), as expected when both arms carry identical lexical content. Across the five models, the cluster structure is unambiguous: completion tokens drop substantially only on the two models with visible reasoning traces (Qwen, DeepSeek), while the three short-output or concealed-reasoning models (GPT-5, Gemini Flash, Claude Sonnet 4.6) all show completion-token Δ within ±1.5% (pure noise). This clean two-cluster split is consistent with the §3.2 prediction that an early Core constraint collapses the branching factor of the model's internal search — *which can only show a token effect when that search is externalized in the visible completion stream*. An illustrative case: Qwen's `ZH_L3_03` arm shows the control trace at 17,092 completion tokens (long confused reasoning, wrong final answer) versus the CFLT trace at 2,821 tokens (focused reasoning, correct) — a 6× reduction on a single case. The three short-output / concealed-reasoning models show no meaningful completion-token effect, which is neither evidence for nor against the protocol's claim, because no externalized internal search is being shortened.

A clarifying note: the original CFLT documentation projected a 30–50% prompt-token savings under a "compressed CFLT" formulation with explicit slot labels and `NULL` fillers. The current dataset uses lexically identical content in both arms (the manipulation is purely order), so prompt compression is not testable by design. To test the prompt-economy claim directly, a third "compressed CFLT" arm is required; this is reserved for the registered confirmatory study (§7).

### 6.4 Part I Results — Logic Transformer Feasibility

Part I (using `deepseek/deepseek-v4-pro` as the transformer and `openai/gpt-5` as the downstream extractor, N=1):

- Structural compliance: SC = SR = IV = **100%** across all 24 cases. The transformer reliably produces well-formed CFLT JSON with correct slot order, subject preservation, and inference suggestions.
- Downstream extraction accuracy (DX): L1 = 100%, L2 = 83%, L3 = 67%, L4 = 100%; overall = 88%.
- The L3 DX (67%) is comparable to the Part II L3 control baseline (61–78%) but well below the human-authored CFLT ceiling (100% in Part II). On inspection, the three L3 DX failures are stochastic (N=1) rather than systematic; a v3 snapshot of the same prompt achieved 23/24 = 96%.

Implication. CFLT is currently a usable preprocessing protocol when authored by a human, and a *structurally* implementable protocol when authored by an LLM — but LLM-authored CFLT does not yet preserve enough content fidelity at L3 to recover the full Part II accuracy gain. Closing this gap (e.g., by fine-tuning a Logic Transformer on CFLT-conformant data) is a concrete research-agenda item (§7.3).

### 6.5 Limitations

We enumerate limitations explicitly because the headline number — 100% accuracy on L3 across all five models — is larger than is plausible for a mature evaluation and reflects properties of the pilot set as much as a real ceiling.

- **Sample size.** 24 cases × 3 runs × 2 conditions × 5 models = 720 Part II trials is adequate for descriptive cross-model comparison and is the empirical base for the five-model L3 universality claim, but it is still below the threshold for confirmatory mixed-effects inference at the per-case level. A pre-registered larger-scale evaluation (N ≥ 10 runs per case; per-case-author replication) is the next step in §7.
- **Ceiling saturation.** L1 control accuracy is at ceiling for all five models; L2 saturates for three (GPT-5, Gemini, DeepSeek), shows mild positive noise on Qwen (+6 pp), and is informative-with-negative-noise on Claude (−6 pp, see next bullet); L4 saturates for four of five models, with only DeepSeek showing the −11 pp regression discussed below. L3 is the only level that is reliably informative across all five models. Future case design must target the regions where current frontier models actually fail.
- **Claude L2 noise observation.** Claude Sonnet 4.6 is the only model where L2 became informative with a non-zero aggregate direction (83% control → 78% CFLT, −6 pp). Per-case inspection shows this is sampling noise, not a stable effect: one case (ZH_L2_01) went from 0% control to 100% CFLT (+100 pp), one case (ZH_L2_02) went the opposite direction (100% → 0%, −100 pp), and one case (EN_L2_03) showed a mild negative (−33 pp); the remaining three L2 cases were saturated on both arms. The aggregate −6 pp is the algebraic residual after these cases mostly cancel. At N=3 runs per arm, this aggregate sits within sampling noise and we do not interpret it as a real CFLT regression on Claude L2. A confirmatory study with N ≥ 10 per case is required to resolve the direction.
- **L4 null/negative result.** Of the five models, only DeepSeek V4 Pro shows an informative L4 regression (−11 pp); the other four are at or near ceiling on L4 under both arms (GPT-5 100%/100%, Gemini 94%/94%, Qwen 94%/92%, Claude 100%/100%). We assess three competing readings of this anomaly against the cross-model evidence:

  Reading (a) — Primacy is over-strong as a unified explanation. *Status: weakly supported.* Under this reading, the L3-vs-L4 reversal would be predicted to replicate across multiple models — the L4 regression should appear whenever L4 is informative. With four of five models showing no L4 regression at all (three at exact ceiling, one near-ceiling noise), the prediction does not generalize. The primacy advantage at Slot 0 is not violated in the majority of frontier models. *Surviving form*: a weaker version of reading (a) might claim that primacy advantage can be locally overridden when the natural narrative order is itself a strong reasoning scaffold — but the evidence base for this is thin (N = 1 model out of 5).

  Reading (b) — DeepSeek-specific model × item-type interaction. *Status: most consistent with the data.* The reading-(b) concern is its textbook ad-hoc-rescue shape: "if it doesn't generalize, blame the items." With four of five models showing no L4 issue and only DeepSeek diverging, the interaction-with-model is the most likely interpretation of the −11 pp signal. We pre-commit anti-rescue criteria for a confirmatory study so this reading does not slide into unfalsifiability: (i) the redesigned L4 set must keep embedding-distance between the buried-decision and distractor options above a pre-registered threshold; (ii) the decision must be syntactically anchored (e.g., "我决定", "I decide", "I'll take") not merely positioned last; (iii) the L4 items must be re-authored by ≥ 2 independent annotators. If the redesigned L4 still shows DeepSeek-specific −11 pp regression under these constraints, reading (b) is locked in as model × item interaction. If the regression disappears under any of the constraints, reading (b) is refuted and we revisit (a).

  Reading (c) — Reasoning-capable models compensate for buried decisions through internal search. *Status: not supported by current data.* Reading (c) predicts that the L4 regression should correlate with reasoning-trace visibility — long-trace reasoning models should show more regression, short-output models should show less. The five-model data does not bear this out: Qwen (the model with the longest reasoning traces — control mean 5,368 completion tokens on L3) shows L4 noise (−3 pp); DeepSeek (shorter traces, ~283 tokens) shows the −11 pp regression; Claude (no visible reasoning trace, ~50 tokens) shows zero L4 effect. Reading (c)'s predicted monotonic relationship between trace length and L4 regression is absent. The reading is not refuted (N=5 is small for cross-model regression), but it is not supported by current data and we deprioritize it.

  Synthesis. The L4 anomaly is best characterized as a DeepSeek-V4-Pro-specific model × task-type interaction with a pre-registered redesign protocol that would falsify or confirm it. The primacy-driven mechanism (§3.2) remains consistent with the five-model L3 universality and with the four-of-five L4 saturation. Reporting the DeepSeek regression remains valuable as an operational note: deployments on DeepSeek for multi-option decision tasks should A/B-test CFLT before committing.
- **Model coverage.** Five models across five commercial providers is the cross-provider base for the L3 universality claim; the four-of-five L4 saturation result is also drawn from this set. Stronger generalization claims (and tighter resolution of the DeepSeek L4 anomaly) require ≥ 8 frontier models including at least one from each major architecture family, with a planned re-run when checkpoints update. The OpenRouter routing used for Claude in this iteration generalizes to other gateway-routed models, lowering the cost of future expansion.
- **Construct validity of "distractor density."** L1–L4 difficulty was operationalized at case-construction time by a single author. A principled, embedding-distance-based difficulty metric should replace this in the confirmatory study.
- **Statistical inference.** With N = 24 cases per condition we report descriptive statistics and per-case mean ± std only. Bootstrap CIs, mixed-effects modeling with case and language as random effects, and pre-registered hypothesis tests are deferred to the confirmatory study.
- **Language coverage.** The dataset is bilingual (English + Mandarin), which is a strict improvement on the English-only baseline implicit in much prompt-engineering work; but it is still a thin sample of the world's typological space. Extending to head-final languages (Japanese, Korean) and to a VSO language (Arabic) is a near-term priority.
- **Model-version drift.** Frontier LLMs update on month-scale timescales; the May 2026 checkpoints may not replicate on subsequent releases. The released code re-runs the entire study in a single command for verification.
- **Scoring is automated, not human-rated.** Binary extraction was scored programmatically against a dataset-driven synonym table; we did not manually verify a held-out sample for inter-rater agreement against the automated judge. This is a future-work item.

We therefore characterize these results as suggestive — with one informative null result (L4) that should constrain the next iteration of the theory — rather than as confirmatory evidence for CFLT-in-general.

\noindent\rule{\textwidth}{0.4pt}

## 7. Open Questions and Research Agenda

CFLT's value as a theoretical claim rests on whether it makes falsifiable predictions across cognitive, typological, and computational dimensions. We enumerate the open questions that, in our view, define a multi-phase research program. (The canonical formulation is in the project's empirical-agenda reference; this section summarizes and re-orders for this paper's scope.)

### 7.1 Psycholinguistic — Production-speed advantage under L2 conditions (P1)

Claim. Adult L2 learners taught the CFLT unmarked default will produce sentences with higher fluency (words per minute) and lower hesitation rate than learners taught a free-order baseline, controlled for vocabulary and grammar coverage.

Methodology. Between-subjects intervention; two groups of intermediate L2 learners receive identical lexical/grammatical content for N weeks; one group additionally drills the CFLT four-slot template. Measure words per minute in elicited monologue, hesitation pauses ≥ 250 ms (Pawley & Syder 1983), and error rate.

Falsification condition. Two graded criteria, both must hold for the claim to survive: (i) the CFLT-trained group shows a statistically significant fluency advantage at *p* < .05 across at least two replication sites; and (ii) the CFLT-trained group shows measurably reduced L1-shaped fronting (e.g., for Mandarin-L1 / English-L2, reduced rate of unmarked time-initial declaratives relative to matched controls) — this is the Slobin-tightened criterion (§1.1), and reflects that CFLT is predicted to *attenuate*, not eliminate, L1-shaped Conceptualizer biases. If (i) holds but (ii) does not, the fluency benefit is real but not attributable to L1-bias attenuation; if (ii) holds but (i) does not, the bias is reduced without translating to production-time benefit; either single failure refutes the joint P1 claim as stated.

Adjacent evidence. VanPatten's (1996, 2004) Processing Instruction work supports the existence of a "default schema" benefit methodologically, though not directly for CFLT. Kormos (2006) places the L2 production bottleneck at the Formulator stage, predicting a CFLT effect mechanistically. DeKeyser (2007) provides the declarative-to-procedural skill-acquisition curves into which CFLT should fit. Slobin (1996) defines the upper bound on the predicted effect — CFLT attenuates rather than eliminates the L1 bias.

### 7.2 Typological — Is R > S > T the unique optimum?

The R-S-T inner order is a convention (§4), not a derivation. Two extensions are needed:

(a) Quantitative corpus work across at least one language per major family (Mandarin, Japanese, Arabic, Swahili, Quechua). *Falsification condition*: in unmarked declaratives with ≥ 2 ground-frame adjuncts co-occurring, the relative-order frequencies (R-S, R-T, S-T pairs) should show R preceding S, R preceding T, and S preceding T in ≥ 60% of attested co-occurrences in ≥ 4 of the 5 families. If the frequency floor is missed in ≥ 2 families, the unmarked-default claim of R>S>T is refuted as a cross-linguistic generalization within the surveyed typology, and CFLT should retreat to a per-language convention.

(b) A registered narrative-genre test of Reinhart's (1984) competing Time-first hypothesis, with the falsification condition that if Time-first reliably outperforms R-S-T for narrative L2 production across ≥ 2 languages (measured by fluency, hesitation rate, and listener comprehension at *p* < .05), CFLT should adopt a genre-conditional protocol — R-S-T for expository/conversational registers, R-T-S for narrative.

### 7.3 Computational — LLM attention concentration and protocol-vs-alignment (P2)

Pilot status. The pilot study (§6) treats CFLT as a prompt-time intervention; the L3 finding (100% accuracy across all five models) is suggestive but not yet confirmed under a pre-registered larger-N protocol.

Strong test. When an LLM receives a CFLT-formatted prompt versus a semantically identical scrambled-order prompt, attention weights to Slot 0 should be higher in the CFLT condition (measurable via attention rollout, Abnar & Zuidema 2020; or via causal attribution, Vig 2019), and downstream task accuracy should be higher for tasks where the Core constituent is the answer-bearing element. Across ≥ 3 model families.

Falsification condition. If across ≥ 3 frontier model families the CFLT-formatted prompt shows neither attention-weight concentration at position 0 nor task-accuracy advantage, the LLM-side claim is refuted.

Stronger version — protocol vs. alignment constraint. The pilot tests CFLT at prompt-time. A stronger claim is that training-time exposure to CFLT-conformant data would reduce LLM *intrinsic* order-sensitivity. A small-scale fine-tuning experiment — models fine-tuned on CFLT-reordered versus naturally ordered instruction data, evaluated under prompt-order perturbation — would distinguish CFLT-as-prompt-protocol from CFLT-as-alignment-constraint. The latter is the more substantial contribution to AI alignment.

### 7.4 Neural — Bilingual PFC cost reduction (P3)

Claim. Bilingual speakers trained on a CFLT intermediate scaffold will show reduced prefrontal cortex activation during L1→L2 production tasks compared to bilinguals using ad-hoc surface restructuring (Abutalebi & Green 2007, 2016), as measured by fMRI or fNIRS.

Methodology. Within-subjects design with CFLT-trained vs. untrained translation conditions; measure BOLD signal in dorsolateral PFC and the dorsal anterior cingulate (Salience Network nodes, Seeley et al. 2007); align with the word-order-processing paradigm reported by Hashimoto, Yokoyama & Kawashima (2012), whose preliminary findings on cross-linguistic word-order modulation of brain response were presented as a conference abstract by the same lab in 2006 (Yokoyama, Fukushima, Riera & Kawashima 2006, *NeuroImage* OHBM abstract). The 2012 paper is published in *The Open Medical Imaging Journal* (Bentham Open); the methodology used there is standard fMRI block design and the imaging protocol is replicable, but the publication venue is acknowledged to have weaker peer-review scrutiny than the canonical neuroimaging journals — the prudent reading is to treat Hashimoto et al. 2012 as a *methodological reference*, not as an evidential anchor on its own, and to require the present study's contrast to replicate against an independent imaging cohort before drawing strong conclusions.

Falsification condition. If trained CFLT speakers show equal or greater PFC activation than untrained controls, the cognitive-cost-reduction claim is refuted.

### 7.5 Formal-semantic — CFLT at the syntax–semantics interface (Exploratory)

*This subsection identifies a research direction rather than a single falsifiable claim, and is labeled exploratory accordingly.*

Can the Tier 1 / Tier 2 partition be characterized formally as a constraint at the syntax-semantics interface — for example, as a principled cut in scope-taking behavior, with Tier 2 adjuncts functioning as world-restricting modifiers? Engagement with the formal-semantic tradition would convert CFLT from an engineering heuristic into a testable claim about the architecture of meaning composition. The natural reference points are Heim & Kratzer (1998) on compositional semantics for the Tier 1 / Tier 2 cut itself; Kratzer (1991, 2012) on modality and conditionals for the Tier 2 Reason / Condition slot as a world-restricting modifier in the sense of restrictor / nuclear-scope partition; and Krifka (1989, 1998) on event composition and the origins of telicity for the Tier 1 event nucleus, its participants, and its aspectual closure. A concrete first-stage falsifiable sub-claim within this program: the Tier 2 adjunct ordering should correspond to scope-nesting in compositional semantics, with Reason scoping over Space scoping over Time, such that swapping the surface order without re-bracketing produces ill-formed or differently-truth-conditioned readings. If a corpus / native-speaker judgment study across the surveyed five-language range shows that scope-nesting is order-invariant for these adjunct classes, the formal-semantic embedding of CFLT collapses to "discourse convention" and the interface-economy reading is refuted.

### 7.6 Human–AI synchronized reasoning (Exploratory)

*This subsection is labeled exploratory because the operationalization of "drift" is not yet pre-committed.*

If both human prompt authors and LLM responders are CFLT-conformant, does multi-turn agentic reasoning exhibit lower drift than under unconstrained protocols? Concrete first-stage operationalization: on the SWE-bench (or GAIA) benchmark, agents instructed under a CFLT system prompt should show (a) higher per-turn task-relevant-token ratio, and (b) lower across-turn topic-divergence (measured as cosine distance between consecutive turn embeddings) than agents under a matched unconstrained-protocol baseline, across ≥ 3 frontier model families. Falsification condition: if neither (a) nor (b) improves at *p* < .05 across the model families, the human-AI synchronization claim is refuted at the agent-workflow scale. Stronger versions of the claim — that human-side CFLT training plus LLM-side CFLT prompting compose multiplicatively rather than additively — are deferred until single-side claims are independently confirmed.

A concrete agentic special case — whether CFLT-ordered intent improves first-attempt tool-call success and reduces over-permission incidents when an agent acts through structured tool-call interfaces (e.g., MCP-style function schemas) — is continuous with this test. We flag it as an open question, not a separate contribution, and make no claim that a dedicated translation layer is required beyond existing LLM tool-use scaffolding.

\noindent\rule{\textwidth}{0.4pt}

## 8. Conclusion

We have argued that linearization cost is the shared currency of two superficially distant problems — adult L2 production and human-to-LLM prompting — and that a single normative discourse-level protocol can pay that cost in both currencies. The protocol fixes the relative order of two tiers (`[Core] → [Reason] → [Space] → [Time]`) while leaving each language's internal morphosyntax intact, and it leaves the contents of each slot to the speaker.

We have been careful to mark several things this paper does *not* claim:

- CFLT is **not** a descriptive universal of natural-language word order; it is a normative protocol that operates one level up from surface syntax.
- CFLT does **not** depend on strong Universal Grammar; the core motivation is Levelt's (1989) preverbal message formation, which is compatible with usage-based, constructionist, and anti-UG positions.
- The **R-S-T inner order is a convention with rationale**, not a derivation; it may be revised under empirical evaluation, particularly for narrative-genre production.
- CFLT exploits **primacy**, not the attention-sink artifact (Xiao et al. 2024); the two mechanisms are distinct and should not be conflated.
- The pilot evidence (§6) is **suggestive, not confirmatory**, and includes one informative null/negative result (L4 buried-decision condition on one model) that constrains rather than supports the theory.

CFLT is best read not as a finished theory but as a research scaffold whose value will be determined by the open questions of §7 — across psycholinguistics, typology, LLM mechanistic interpretability, neuroscience, formal semantics, and human-AI interaction. Whether the specific protocol we have proposed is the correct one is, ultimately, an empirical question; what we hope this paper establishes is that the question is worth asking, and that the falsification conditions for asking it well are now on the table.

The empirical agenda enumerated in §7 — six sub-programs (§7.1–§7.6) spanning psycholinguistic production, cross-linguistic corpus work, LLM mechanistic interpretability, bilingual neuroimaging, formal-semantic embedding, and human-AI multi-turn coordination — is intended as a coherent multi-phase open research program. Whether a single Core-then-Frame ordering can additionally carry intent into the structured tool-call interfaces through which LLM agents act is flagged as an open question in §7.6, not a contribution of this paper. The author is independently developing this program at <https://cflt.center> and welcomes correspondence from researchers whose work intersects any of the open sub-areas.

\noindent\rule{\textwidth}{0.4pt}

## Data and Code Availability

Prompt templates, raw API responses, the dataset (`dataset.json` v2.0.0; 24 cases × 4 levels × 2 languages), the evaluation scripts (`scripts/llm_eval/`), and the May 2026 report archive (`experiment-history/2026-05-17/`) are deposited at https://cflt.center. The full ablation reproduces in a single command (`python scripts/llm_eval/part2_llm_cflt_eval.py --runs 3`). A pre-registered protocol for the confirmatory study described in §7 will be filed at a public pre-registration registry prior to data collection.

A reference implementation (human bilingual education) is independently maintained as an open-source application (Next.js + Electron) at https://github.com/corefirst/corefirst (Apache 2.0). It runs fully locally given a valid LLM API key. The pilot empirical evaluation in §6 is independent of this implementation and relies only on the standalone scripts in `scripts/llm_eval/`; the implementation is referenced here as concrete evidence that the protocol is operationally deployable, not as part of §6's empirical evidence base.

## Conflict of Interest

The author maintains the cflt.center project repository, which serves as the open materials site for this work and as the canonical specification of the CFLT framework. The framework itself is licensed CC BY 4.0 and is not a commercial product. The author declares no financial conflicts of interest.

## Funding

No external funding was received for this work. All API costs for the pilot empirical evaluation (§6) were borne by the author personally.

## Ethics

This study involved no human or animal subjects. The pilot empirical evaluation (§6) consisted entirely of commercial Large Language Model API queries against publicly accessible model endpoints; no personal data, user-generated content, or identifiable information was processed. The bilingual test items in `scripts/llm_eval/dataset.json` were authored by the project lead for benchmark purposes and contain no personal or sensitive content. No ethics board approval was sought, as no human-subjects research was conducted; this paper reports a purely computational ablation.

## AI Use Disclosure

This paper's AI-assisted workflow is disclosed in accordance with the 2025–2026 standards adopted by major academic venues.

The author, a non-native English speaker, conducted all core theoretical development, experimental design, and data analysis independently. AI tools (Claude, Gemini) were employed exclusively for grammatical copy-editing, stylistic refinement, and academic register optimization of the author's original English drafts. All output was rigorously reviewed and revised by the human author to ensure conceptual accuracy. The author maintains full accountability for the entirety of this work.

## Acknowledgments

This paper summarizes work developed within the CFLT framework (cflt.center). The framework integrates research across cognitive linguistics, formal semantics, psycholinguistics, second-language acquisition, neuroscience, and NLP; the full canonical specification, with bibliography of approximately 150 entries, is maintained at the project site. The author thanks the maintainers of the five frontier LLM platforms evaluated in this work, and OpenRouter for the gateway access used to route Anthropic's Claude. Any errors of theoretical framing or empirical interpretation remain the author's own.

## How to cite

For the framework as a whole: *CFLT Core Team. (2026). Core-First Language Theory (CFLT): Reconstructing Global Bilingual Education from First Principles. https://cflt.center.*

For this paper: *Yi, W. (2026). Core-First Language Theory (CFLT): A Discourse-Level Linearization Protocol for Cross-Linguistic Communication and LLM Prompting. Manuscript, https://cflt.center.*

\noindent\rule{\textwidth}{0.4pt}

## References

- Abnar, S. & Zuidema, W. (2020). Quantifying Attention Flow in Transformers. *ACL 2020*.
- Abutalebi, J. & Green, D. W. (2007). Bilingual Language Production: The Neurocognition of Language Representation and Control. *Journal of Neurolinguistics* 20(3), 242–275.
- Abutalebi, J. & Green, D. W. (2016). Neuroimaging of Language Control in Bilinguals: Neural Adaptation and Reserve. *Bilingualism: Language and Cognition* 19(4), 689–698.
- Aikhenvald, A. Y. (2004). *Evidentiality.* Oxford University Press.
- Ambridge, B. & Wagner, L. (eds.) (2021). *Testable Theories of Core First Language Acquisition.* Special Issue, *Journal of Child Language* 48(S5).
- Berglund, L., Tong, M., Kaufmann, M., Balesni, M., Stickland, A. C., Korbak, T. & Evans, O. (2024). The Reversal Curse: LLMs Trained on "A is B" Fail to Learn "B is A." *ICLR 2024.*
- Boroditsky, L. (2000). Metaphoric Structuring: Understanding Time Through Spatial Metaphors. *Cognition* 75(1), 1–28.
- Carlson, G. N. (1977). *Reference to Kinds in English.* PhD dissertation, University of Massachusetts Amherst.
- Casasanto, D. & Boroditsky, L. (2008). Time in the Mind: Using Space to Think About Time. *Cognition* 106(2), 579–593.
- Christiansen, M. H. & Chater, N. (2008). Language as Shaped by the Brain. *Behavioral and Brain Sciences* 31(5), 489–509.
- Cinque, G. (1999). *Adverbs and Functional Heads: A Cross-Linguistic Perspective.* Oxford University Press.
- Croft, W. (2001). *Radical Construction Grammar: Syntactic Theory in Typological Perspective.* Oxford University Press.
- DeKeyser, R. M. (2007). *Practice in a Second Language: Perspectives from Applied Linguistics and Cognitive Psychology.* Cambridge University Press.
- Dowty, D. R. (1979). *Word Meaning and Montague Grammar.* Reidel.
- Dryer, M. S. (2013). In *The World Atlas of Language Structures Online*, Dryer & Haspelmath (eds.).
- Evans, N. & Levinson, S. C. (2009). The Myth of Language Universals. *Behavioral and Brain Sciences* 32(5), 429–448.
- Foley, W. A. & Van Valin, R. D. Jr. (1984). *Functional Syntax and Universal Grammar.* Cambridge University Press.
- Goldberg, A. E. (1995). *Constructions: A Construction Grammar Approach to Argument Structure.* University of Chicago Press.
- Goldberg, A. E. (2006). *Constructions at Work.* Oxford University Press.
- Greenberg, J. H. (1963). Some Universals of Grammar with Particular Reference to the Order of Meaningful Elements. In *Universals of Language*, Greenberg (ed.), MIT Press.
- Guest, O. & Martin, A. E. (2023). On Logical Inference over Brains, Behaviour, and Artificial Neural Networks. *Computational Brain & Behavior* 6, 213–227.
- Gundel, J. K., Hedberg, N. & Zacharski, R. (1993). Cognitive Status and the Form of Referring Expressions in Discourse. *Language* 69(2), 274–307.
- Halliday, M. A. K. & Matthiessen, C. M. I. M. (2014). *Halliday's Introduction to Functional Grammar* (4th ed.). Routledge.
- Hashimoto, Y., Yokoyama, S. & Kawashima, R. (2012). Neuro-typology of sentence comprehension. *The Open Medical Imaging Journal* 6, 62–69.
- Hawkins, J. A. (1994). *A Performance Theory of Order and Constituency.* Cambridge University Press.
- Hawkins, J. A. (2004). *Efficiency and Complexity in Grammars.* Oxford University Press.
- Heim, I. & Kratzer, A. (1998). *Semantics in Generative Grammar.* Blackwell.
- Kratzer, A. (1991). Modality. In *Semantics: An International Handbook of Contemporary Research*, von Stechow & Wunderlich (eds.). De Gruyter, 639–650.
- Kratzer, A. (2012). *Modals and Conditionals: New and Revised Perspectives.* Oxford University Press.
- Krifka, M. (1989). Nominal Reference, Temporal Constitution and Quantification in Event Semantics. In *Semantics and Contextual Expression*, Bartsch, van Benthem & van Emde Boas (eds.). Foris, 75–115.
- Krifka, M. (1998). The Origins of Telicity. In *Events and Grammar*, Rothstein (ed.). Kluwer, 197–235.
- Hengeveld, K. (1992). *Non-verbal Predication: Theory, Typology, Diachrony.* Mouton de Gruyter.
- Higgins, F. R. (1979). *The Pseudo-cleft Construction in English.* Garland.
- Kormos, J. (2006). *Speech Production and Second Language Acquisition.* Erlbaum.
- Krifka, M. (2008). Basic Notions of Information Structure. *Acta Linguistica Hungarica* 55(3–4), 243–276.
- Lakoff, G. & Johnson, M. (1980). *Metaphors We Live By.* University of Chicago Press.
- Langacker, R. W. (1987). *Foundations of Cognitive Grammar, Vol. 1: Theoretical Prerequisites.* Stanford University Press.
- Langacker, R. W. (2008). *Cognitive Grammar: A Basic Introduction.* Oxford University Press.
- Levelt, W. J. M. (1989). *Speaking: From Intention to Articulation.* MIT Press.
- Levin, B. & Rappaport Hovav, M. (2005). *Argument Realization.* Cambridge University Press.
- Levinson, S. C. (1983). *Pragmatics.* Cambridge University Press.
- Li, C. N. & Thompson, S. A. (1976). Subject and Topic: A New Typology of Language. In *Subject and Topic*, Li (ed.), Academic Press.
- Liu, N. F., Lin, K., Hewitt, J., Paranjape, A., Bevilacqua, M., Petroni, F. & Liang, P. (2023). Lost in the Middle: How Language Models Use Long Contexts. *Transactions of the Association for Computational Linguistics.*
- Lu, Y., Bartolo, M., Moore, A., Riedel, S. & Stenetorp, P. (2022). Fantastically Ordered Prompts and Where to Find Them: Overcoming Few-Shot Prompt Order Sensitivity. *ACL 2022.*
- Maienborn, C. (2005). On the Limits of the Davidsonian Approach: The Case of Copula Sentences. *Theoretical Linguistics* 31(3), 275–316.
- McCloskey, M. (1991). Networks and Theories: The Place of Connectionism in Cognitive Science. *Psychological Science* 2(6), 387–395.
- Min, S., Lyu, X., Holtzman, A., Artetxe, M., Lewis, M., Hajishirzi, H. & Zettlemoyer, L. (2022). Rethinking the Role of Demonstrations: What Makes In-Context Learning Work? *EMNLP 2022.*
- Mithun, M. (1992). Is Basic Word Order Universal? In *Pragmatics of Word Order Flexibility*, Payne (ed.), John Benjamins, 15–61.
- Newmeyer, F. J. (2005). *Possible and Probable Languages: A Generative Perspective on Linguistic Typology.* Oxford University Press.
- Núñez, R. E. & Sweetser, E. (2006). With the Future Behind Them: Convergent Evidence From Aymara Language and Gesture in the Crosslinguistic Comparison of Spatial Construals of Time. *Cognitive Science* 30(3), 401–450.
- Pawley, A. & Syder, F. H. (1983). Two Puzzles for Linguistic Theory: Nativelike Selection and Nativelike Fluency. In *Language and Communication*, Richards & Schmidt (eds.), Longman.
- Pezeshkpour, P. & Hruschka, E. (2024). Large Language Models Sensitivity to the Order of Options in Multiple-Choice Questions. *Findings of NAACL 2024.*
- Reinhart, T. (1984). Principles of Gestalt Perception in the Temporal Organization of Narrative Texts. *Linguistics* 22(6), 779–809.
- Sadock, J. M. & Zwicky, A. M. (1985). Speech Act Distinctions in Syntax. In *Language Typology and Syntactic Description*, Shopen (ed.), Vol. 1, Cambridge University Press.
- Sclar, M., Choi, Y., Tsvetkov, Y. & Suhr, A. (2024). Quantifying Language Models' Sensitivity to Spurious Features in Prompt Design. *ICLR 2024.*
- Searle, J. R. (1969). *Speech Acts: An Essay in the Philosophy of Language.* Cambridge University Press.
- Searle, J. R. (1975). A Taxonomy of Illocutionary Acts. In *Language, Mind and Knowledge*, Gunderson (ed.), University of Minnesota Press.
- Seeley, W. W., Menon, V., Schatzberg, A. F., Keller, J., Glover, G. H., Kenna, H., Reiss, A. L. & Greicius, M. D. (2007). Dissociable Intrinsic Connectivity Networks for Salience Processing and Executive Control. *The Journal of Neuroscience* 27(9), 2349–2356.
- Slobin, D. I. (1996). From "Thought and Language" to "Thinking for Speaking." In *Rethinking Linguistic Relativity*, Gumperz & Levinson (eds.), Cambridge University Press.
- Talmy, L. (2000). *Toward a Cognitive Semantics, Vol. 1: Concept Structuring Systems.* MIT Press.
- Tomasello, M. (2003). *Constructing a Language: A Usage-Based Theory of Language Acquisition.* Harvard University Press.
- Van Valin, R. D. Jr. & LaPolla, R. J. (1997). *Syntax: Structure, Meaning, and Function.* Cambridge University Press.
- Van Valin, R. D. Jr. (2005). *Exploring the Syntax-Semantics Interface.* Cambridge University Press.
- VanPatten, B. (1996). *Input Processing and Grammar Instruction in Second Language Acquisition.* Ablex.
- VanPatten, B. (ed.) (2004). *Processing Instruction: Theory, Research, and Commentary.* Erlbaum.
- Vaswani, A. et al. (2017). Attention Is All You Need. *NeurIPS 2017.*
- Vendler, Z. (1957). Verbs and Times. *The Philosophical Review* 66(2), 143–160.
- Vig, J. (2019). A Multiscale Visualization of Attention in the Transformer Model. *ACL 2019 System Demonstrations.*
- Wei, J. et al. (2022). Chain-of-Thought Prompting Elicits Reasoning in Large Language Models. *NeurIPS 2022.*
- Wierzbicka, A. (1996). *Semantics: Primes and Universals.* Oxford University Press.
- Xiao, G., Tian, Y., Chen, B., Han, S. & Lewis, M. (2024). Efficient Streaming Language Models with Attention Sinks. *ICLR 2024.*
- Yokoyama, S., Fukushima, A., Riera, J. & Kawashima, R. (2006). Is There a Difference in the Brain Activation Patterns Between SVO and SOV Languages? *NeuroImage* 31(S1), S159 (OHBM conference abstract).

A complete bibliography of approximately 150 entries spanning all eight foundational disciplines is maintained at https://cflt.center/bibliography.
