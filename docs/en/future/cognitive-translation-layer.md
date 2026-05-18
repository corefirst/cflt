# Cognitive Translation Layer (CTL): A Bidirectional Protocol Between Natural-Language Intent and AI-Perceivable Tool Invocation

> **Version:** 1.0.0 (Internal Draft)
> **Status:** Research program planned for doctoral-level investigation. No implementation exists at the time of writing.
> **Author:** CFLT Core Team
> **License:** [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)

---

## 1. Why CTL: The Missing Substrate Bridge

CFLT (Core-First Language Theory) and apcore (AI-Perceivable Core) are two independently deployed open-source projects that, on inspection, encode the same organizing principle on disjoint substrates.

- **CFLT** ([cflt.center](https://cflt.center); SocArXiv preprint DOI pending moderation, will be linked at [cflt.center](https://cflt.center)) is a discourse-level linearization protocol. It applies the **Core-then-Frame** principle to natural-language utterances: a mandatory event nucleus (Slot 0) precedes optional framing modifiers (Slots 1–3 — Reason, Space, Time). A reference Pillar I implementation (CoreFirst, Next.js + Electron) is operationally deployed; a 720-trial empirical pilot across five frontier LLMs is reported in the preprint.
- **apcore** ([github.com/aiperceivable](https://github.com/aiperceivable), Apache 2.0, OpenSSF Best Practices certified) is a module standard for AI-invokable tool interfaces. It applies the same Core-then-Frame principle to tool descriptions: a mandatory Core Layer (`input_schema`, `output_schema`, `description`) precedes optional Annotation Layer (`readonly`, `destructive`, `requires_approval`, `idempotent`, `open_world`, `cacheable`, `paginated`) and optional Extension Layer (`x-when-to-use`, `x-preconditions`, `x-postconditions`, `x-common-mistakes`, `x-cost-per-call`). Production SDKs exist for Python, TypeScript, and Rust; third-party adoption is documented.

Both projects, in other words, deploy the same Core-then-Frame layering on different surfaces. What is missing is a **protocol bridge** that maps between them — so that when a human user issues a CFLT-conformant natural-language request and an AI agent fulfills it through apcore-perceivable tool invocations, the cognitive layering is preserved across the substrate boundary, in both directions.

This bridge is the **Cognitive Translation Layer (CTL)**. CTL is the integrative target of the broader cross-substrate research program; it is the planned focus of doctoral-level investigation.

---

## 2. Architectural Position

```
┌─────────────────────────────────────────────────────────────────┐
│  Layer 1 — Natural-Language Layer (governed by CFLT)            │
│  Discourse-level linearization protocol for natural language     │
│  Deployed: CoreFirst (Pillar I MVP) + 720-trial LLM pilot        │
└──────────────────────────┬──────────────────────────────────────┘
                           │
                           ▼   (the missing bridge — this document)
                           │
┌─────────────────────────────────────────────────────────────────┐
│  Layer 2 — Cognitive Translation Layer (CTL)   [planned]        │
│  Bidirectional protocol bridge:                                  │
│    Forward:  CFLT-structured intent → apcore-structured call    │
│    Reverse:  apcore-structured result → CFLT-structured reply   │
│    Governance: consent gating, ACL evaluation, error recovery   │
└──────────────────────────┬──────────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────────┐
│  Layer 3 — Tool-Call Layer (governed by apcore)                 │
│  AI-Perceivable module standard for tool invocation              │
│  Deployed: production SDKs (Python, TypeScript, Rust)            │
└─────────────────────────────────────────────────────────────────┘
```

CTL is not a replacement for existing AI tool-use scaffolding (MCP, OpenAI Function Calling, Anthropic Tool Use, A2A). Those protocols address transport and serialization — *how* a tool description reaches a model. CTL addresses the orthogonal question of **cognitive layering across the substrate boundary** — *which constituents of natural-language intent map to which categories of tool metadata, and how the inverse mapping reconstructs a comprehensible response*.

In apcore's own terms (see [apcore POSITIONING.md](https://github.com/aiperceivable/apcore)), apcore distinguishes a **Cognitive Interface** for AI agents — separate from UI (for humans) and API (for programs). CTL extends that distinction by adding the **human-to-agent translation layer** that the Cognitive Interface presupposes but does not itself provide.

---

## 3. The Slot-to-Layer Correspondence

The empirical pre-condition that makes CTL tractable as a finite doctoral target — rather than open-ended speculation — is a structural correspondence between CFLT's four discourse slots and apcore's three metadata layers. This correspondence is the core insight of the CTL program; verifying that it holds non-trivially across a representative inventory of human intents and module families is itself part of the research.

| CFLT Slot | Linguistic Function | Example Constituent | apcore Layer | apcore Fields | Cross-Substrate Function |
|---|---|---|---|---|---|
| **Slot 0** (Core) | Event nucleus / salience anchor | predicate + valence-bound arguments + manner + scope-internal operators | **Core Layer** | `input_schema`, `output_schema`, `description` | Mandatory functional contract — what the operation *is* |
| **Slot 1** (Reason) | Causal / justification framing | *because*, *in order to*, *so that*, motivational clauses | **Annotation Layer** | `requires_approval`, `destructive`, `idempotent`, `open_world` | Governance — under what conditions the operation may proceed |
| **Slot 2** (Space) | Locative / scope framing | *in X*, *within Y*, *across Z*, scope-restricting clauses | **ACL** | `callers`, `targets`, `conditions`, `default_effect` | Permission boundary — where (in the system) the operation is permitted |
| **Slot 3** (Time) | Temporal / conditional framing | *before*, *after*, *when*, *if*, *whenever*, scheduling clauses | **Extension Layer** | `x-when-to-use`, `x-preconditions`, `x-postconditions`, `x-workflow-hints` | Planning hints — when and in what workflow position the operation belongs |

**Reading the correspondence.** Both column groups describe the same conceptual structure: a mandatory *what* (Core / Slot 0), surrounded by three categories of optional framing — *why* (Reason / governance), *where* (Space / permission), *when* (Time / planning). The claim is not that the mapping is one-to-one and exhaustive — natural language is messier than that — but that the **categorical alignment** is sufficiently strong to support a deterministic-with-fallback parsing strategy.

**Why this is non-trivial.** It would be unremarkable if Slot 0 mapped to the Core Layer and the remaining three slots all mapped to a single "metadata" bucket. The non-trivial observation is that the **three categories of CFLT ground-frame slots (Reason / Space / Time) map distinctly to three categories of apcore non-core metadata (Annotation Layer / ACL / Extension Layer)** — each pair sharing a functional family (governance, permission boundary, planning hints respectively) that pre-existed independently in both projects. This is the structural evidence that the same Core-then-Frame organizing principle is operating on both substrates.

---

## 4. Bidirectional Mechanism

CTL is bidirectional. The two directions have asymmetric difficulty: forward parsing has a well-formed source representation (CFLT-conformant natural language) but a search space (the module Registry); reverse generation has a well-formed source representation (the structured tool result) but must navigate the constraints of producing fluent CFLT-conformant natural language.

### 4.1 Forward direction: CFLT intent → apcore invocation

```
User utterance (CFLT-conformant)
  │
  ▼
CFLT parser
  │  produces: { Slot 0: <core>, Slot 1: <reason>, Slot 2: <space>, Slot 3: <time> }
  ▼
Registry resolver
  │  Slot 0 → module candidates (matched against module.description + input_schema affinity)
  │  Slot 1 → governance precondition (e.g., a request framed with "because this can't be undone" → infer destructive=True annotation check)
  │  Slot 2 → ACL scoping (resolve caller_id, target permission match)
  │  Slot 3 → temporal binding (resolve to input_schema time-typed fields or x-preconditions check)
  ▼
Disambiguation (if multiple candidates)
  │  surface candidates to user via CFLT-conformant clarifying question
  ▼
Pre-execution governance gate
  │  apcore Annotation evaluation (consent, destructive, requires_approval)
  │  apcore ACL evaluation
  ▼
apcore invocation
  │
  ▼
Structured result
```

### 4.2 Reverse direction: apcore result → CFLT-conformant response

```
Structured apcore result (typed against output_schema)
  │
  ▼
Salience identification
  │  identify the answer-bearing constituent (= candidate Slot 0 of the response)
  ▼
Frame reconstruction
  │  reason for the operation (← apcore middleware trace, governance decisions)  → Slot 1
  │  scope of effect (← apcore ACL evaluation outcome, side-effect annotations)  → Slot 2
  │  temporal context (← timestamps, validity windows, x-postconditions)         → Slot 3
  ▼
CFLT-conformant linearization
  │  [Core: <answer>] → [Reason: <why this answer>] → [Space: <where it applies>] → [Time: <when valid>]
  ▼
Natural-language response
```

### 4.3 Error and governance flows

Three flows that the CTL bridge must handle natively, since they sit precisely at the substrate boundary where current AI tool-use scaffolding is weakest:

1. **Permission denial.** When apcore ACL evaluation denies an invocation, the denial must be translated into a CFLT-conformant explanation that preserves the user's frame — not "Permission denied (error code 403)" but a Slot 0 + Slot 1 + Slot 2 reconstruction: *what was denied*, *under what governance rule*, *within what scope*.
2. **Consent gating.** When apcore Annotation indicates `requires_approval=True`, CTL must generate a CFLT-conformant confirmation question that surfaces the destructive scope to the user before invocation proceeds. The Core of the question is the operation; the Reason is the destructiveness; the Space is the affected scope; the Time is the time-of-effect.
3. **Recovery suggestion.** When apcore returns an error with `ai_guidance` (per apcore's error recovery convention), CTL must translate that guidance into a CFLT-conformant suggestion that the user can act on. The `ai_guidance` field becomes Slot 0 (the suggested action); `retryable`, `user_fixable`, and the error code feed Slots 1–3 (the reasoning, scope, and timing of the suggestion).

---

## 5. Theoretical Grounding: The Cross-Substrate Hypothesis

The empirical claim that CFLT and apcore share a substrate-neutral organizing principle is itself part of the CTL research program, not a free-standing assumption.

### 5.1 Core-then-Frame as a substrate-neutral ergonomic principle

CFLT's foundation rests on a sequence of cognitive-linguistic and psycholinguistic claims: that the preverbal message (Levelt 1989) admits a salience-anchored decomposition (Talmy 2000, Langacker 1987), that placing the salience anchor at sequence-initial position reduces working-memory load in adult L2 production (Hawkins 2004, Kormos 2006), and that the same intervention reduces order-sensitivity and "Lost in the Middle" effects (Liu et al. 2023) in autoregressive Transformers. These claims jointly motivate Core-then-Frame as a *language-layer* ergonomic principle.

apcore's foundation makes a parallel claim on a different substrate: that AI agents perceiving tool descriptions through context-window-limited attention also benefit from Core-then-Frame structuring — mandatory functional contract preceding optional governance and planning hints — because the same primacy and attention-locality properties operate on tool metadata as on natural-language tokens.

The **cross-substrate hypothesis** is that these are not two independent observations but two consequences of a single substrate-neutral ergonomic principle: that any information-processing system whose throughput is bounded by sequential attention will benefit from Core-then-Frame organization of its input. CTL is the protocol that operationalizes this hypothesis at the bridge between the two substrates.

### 5.2 Relation to adjacent traditions

- **Frame Semantics (Fillmore 1982; FrameNet, Baker, Fillmore & Lowe 1998)**: The CFLT four-slot scheme is compatible with — but not identical to — frame-semantic role structures. CTL leverages frame-semantic affinities for Slot 0 → module resolution (Slot 0 carries a predicate; modules are typed by predicate-like functional contracts).
- **Toolformer (Schick et al. 2023)** and the broader LLM-tool-use line: CTL is downstream of this work in that it presupposes the existence of structured tool interfaces; it is upstream in that it addresses the protocol-level question of *which natural-language constituents bind to which tool-metadata categories*, which existing tool-use work treats as solved by ad-hoc prompting.
- **Schema-enforced output (JSON mode, structured outputs)**: CTL extends schema enforcement from the *output* of LLM generation to the *bidirectional translation* between human intent and tool invocation, with governance enforcement at the bridge.

### 5.3 What CTL is not

- **Not a workflow engine.** CTL maps a single intent to a single (or a small disambiguation set of) invocation. Multi-step orchestration belongs to upstream workflow engines (e.g., apflow, LangChain, CrewAI).
- **Not an LLM invocation library.** CTL is LLM-neutral; the LLM is one possible implementation of the parser and generator components, but the protocol does not bind to a specific model.
- **Not a transport protocol.** CTL is layered above MCP, A2A, OpenAI Tool Use, etc.; it addresses the cognitive-layering question that those protocols delegate to ad-hoc prompting.

---

## 6. Falsifiable Sub-Claims

The CTL research program is structured around falsifiable sub-claims, each with a stated falsification condition.

### CTL-1: First-attempt invocation success rate

**Claim.** A CFLT→apcore translation produced by a CTL parser yields higher first-attempt invocation success rates than an LLM-only baseline that lacks the CFLT slot-to-layer correspondence.

**Measurement.** On a benchmark of *N* human-authored CFLT-conformant requests against a Registry of *M* apcore modules with mixed governance metadata, compare first-attempt success (defined as: correct module selected, input_schema satisfied, no governance violation, output validates against output_schema) for CTL-parsed invocations versus baseline.

**Falsification condition.** If success rate fails to improve at *p* < .05 across at least three frontier model families, CTL collapses to "ordinary structured-intent parsing" and contributes no protocol-level value beyond existing tool-use scaffolding.

### CTL-2: Over-permission incident reduction

**Claim.** A CTL-mediated invocation flow reduces over-permission incidents (cases where an agent invokes a module with `requires_approval=True` or `destructive=True` without surfacing the consent gate) relative to a baseline that lacks Slot 1 → Annotation Layer binding.

**Measurement.** On a benchmark of intentionally consent-ambiguous requests, count over-permission incidents under CTL versus baseline.

**Falsification condition.** If over-permission incidents fail to decrease in absolute count across at least three frontier model families, the Slot 1 → Annotation Layer correspondence is not protocol-actionable, and the governance contribution of CTL is refuted.

*Why absolute count, not p-value.* Over-permission incidents are rare events with low base rates in any well-constructed benchmark; statistical-significance testing has poor power in this regime. An absolute-count decrease across all evaluated model families is therefore the more conservative falsification criterion. A stronger test using *p* < .05 on a higher-volume, deliberately-skewed benchmark is reserved as a Year 3 extension.

### CTL-3: Reverse-direction comprehension preservation

**Claim.** A CFLT-conformant linearization of a structured apcore result yields higher human-judged comprehensibility scores than a raw structured result or an ad-hoc LLM-generated natural-language summary.

**Measurement.** Human judgment study on *K* triplets (raw structured result, ad-hoc summary, CTL-linearized response), with comprehensibility scored on a fixed rubric (does the response surface the answer? does it explain the scope? does it surface the time-validity?).

**Falsification condition.** If CTL-linearized responses do not score higher than ad-hoc summaries on at least two of the three rubric dimensions at *p* < .05, the reverse-direction contribution is refuted.

### CTL-4: Cross-model generalization

**Claim.** CTL parsing and generation behavior is stable across frontier model families — i.e., the slot-to-layer correspondence is a model-independent protocol property rather than a model-specific artifact.

**Measurement.** Replicate CTL-1, CTL-2, CTL-3 across at least five frontier model families (GPT-5, Claude Sonnet, Gemini, Qwen, DeepSeek), using model-neutral parser/generator implementations.

**Falsification condition.** If CTL-1, CTL-2, or CTL-3 results show statistically significant cross-model variance (interaction effect at *p* < .05 between model family and CTL-vs-baseline), CTL must retreat to a per-model-family protocol, weakening the cross-substrate generalization.

*Statistical note.* Failure to reject H0 (no interaction) is **not** the same as confirming cross-model uniformity. For positive confirmation of cross-model generalization we additionally require: (i) each per-model CTL effect to be individually significant at *p* < .05, and (ii) the cross-model effect-size variance to fall within a pre-registered equivalence margin (TOST procedure, Lakens 2017). These three conditions — no significant interaction, individual significance, equivalence-bounded variance — must hold jointly for CTL-4 to be considered confirmed rather than merely not-falsified.

---

## 7. Research Roadmap (Four-Year Doctoral Program)

The CTL research program is structured as a four-year doctoral plan. The substrate endpoints (CFLT and apcore) being independently deployed and validated is the precondition that makes this timeline credible.

### Year 1 — Theoretical formalization + benchmark design

- Formalize the slot-to-layer correspondence (§3) as a typed mapping with stated edge-case behavior.
- Design the CTL-1 / CTL-2 / CTL-3 benchmark: assemble the *N* CFLT-conformant request corpus, the *M*-module apcore Registry with controlled governance-metadata distributions, and the human-judgment rubric for CTL-3.
- Publish: one theoretical position paper (target venues: *Cognitive Science*, *Topics in Cognitive Science*, or a major AI alignment workshop).

### Year 2 — Forward-direction prototype + CTL-1, CTL-2 evaluation

- Implement the CTL forward-direction parser as a model-neutral library, callable from any LLM provider.
- Run CTL-1 and CTL-2 evaluations across at least five frontier model families.
- Publish: one empirical paper on forward-direction performance (target venues: ACL, EMNLP, NAACL, or NeurIPS Datasets & Benchmarks).

### Year 3 — Reverse-direction prototype + CTL-3, CTL-4 evaluation

- Implement the CTL reverse-direction generator, including the governance-explanation, consent-gating, and recovery-suggestion flows (§4.3).
- Run CTL-3 human-judgment study and CTL-4 cross-model generalization analysis.
- Publish: one empirical paper on reverse-direction comprehensibility + one cross-model generalization paper.

### Year 4 — Integration + dissertation

- Integration study: deploy CTL in the CoreFirst reference application (Pillar I) and measure end-to-end task completion rates under CTL-mediated versus baseline interaction.
- Write the doctoral dissertation, integrating Years 1–3 work as a unified cross-substrate research program.
- Public deliverable: a CTL specification document (analogous to the apcore PROTOCOL_SPEC) suitable for independent third-party implementation.

---

## 8. Out of Scope

The CTL research program does not aim to deliver any of the following:

- **A workflow engine** that chains multiple CTL-mediated invocations into multi-step plans. That belongs to upstream tools (apflow, LangChain, CrewAI).
- **A new transport protocol** to compete with MCP, A2A, or OpenAI Tool Use. CTL is layered above whichever transport apcore adopts.
- **A new LLM**. The parser and generator components are LLM-neutral; the LLM is one substitutable implementation.
- **A productized SaaS bridge service.** Like CFLT itself, CTL is a protocol specification; productization is the work of independent organizations.
- **An automated theorem prover for the slot-to-layer correspondence.** The correspondence is an empirically defended claim, not a logical derivation; its support comes from CTL-1 through CTL-4, not from formal proof.

---

## 9. Relation to the CFLT Open Empirical Agenda

CTL is the integrative target (§7.7 in the CFLT OSF preprint) that ties together the six sub-programs of the CFLT open empirical agenda:

- The human-side production fluency program (P1 / §7.1) provides the human-cognitive grounding for the Slot 0 → Core Layer correspondence.
- The typological program (§7.2) determines whether the R-S-T ground-frame ordering is universal or genre-conditional, with direct consequences for the Slot 1/2/3 → Annotation/ACL/Extension mapping.
- The LLM mechanistic program (P2 / §7.3) determines whether Slot 0 → Core Layer correspondence is mechanistically grounded in attention dynamics, or only in protocol-level convention.
- The neural program (P3 / §7.4) provides the bilingual-cognition evidence for the cross-substrate claim's human-side anchor.
- The formal-semantic program (§7.5) determines whether the slot-to-layer correspondence has a compositional-semantic basis.
- The agentic-coordination program (§7.6) provides the multi-turn substrate within which CTL operates.

CTL is therefore not orthogonal to the six sub-programs — it is the protocol that requires them to converge.

---

## 10. Status

This document describes a research program planned for doctoral-level investigation. **No implementation of CTL exists at the time of writing.** The two substrate endpoints (CFLT, apcore) are independently deployed and publicly inspectable; CTL is the bridge whose specification and empirical evaluation constitute the planned doctoral contribution.

The author maintains this document, the CFLT framework (cflt.center), and the apcore standard (github.com/aiperceivable) as separate open-source efforts under permissive licenses. Inquiries about supervision, collaboration, or independent implementation are welcome — directly by email (tercel.yi@gmail.com; ORCID [0009-0000-3742-4403](https://orcid.org/0009-0000-3742-4403)) or via the project channels listed at [cflt.center](https://cflt.center).

---

## References

- Baker, C. F., Fillmore, C. J. & Lowe, J. B. (1998). The Berkeley FrameNet Project. *Proceedings of COLING-ACL '98*, 86–90.
- Fillmore, C. J. (1982). Frame Semantics. In *Linguistics in the Morning Calm*, Linguistic Society of Korea (ed.). Hanshin.
- Hawkins, J. A. (2004). *Efficiency and Complexity in Grammars.* Oxford University Press.
- Kormos, J. (2006). *Speech Production and Second Language Acquisition.* Erlbaum.
- Lakens, D. (2017). Equivalence Tests: A Practical Primer for *t*-tests, Correlations, and Meta-Analyses. *Social Psychological and Personality Science* 8(4), 355–362.
- Langacker, R. W. (1987). *Foundations of Cognitive Grammar, Vol. 1.* Stanford University Press.
- Levelt, W. J. M. (1989). *Speaking: From Intention to Articulation.* MIT Press.
- Liu, N. F. et al. (2023). Lost in the Middle: How Language Models Use Long Contexts. *TACL.*
- Schick, T. et al. (2023). Toolformer: Language Models Can Teach Themselves to Use Tools. *NeurIPS 2023.*
- Talmy, L. (2000). *Toward a Cognitive Semantics, Vol. 1.* MIT Press.
- apcore Project. (2026). *apcore POSITIONING.md.* <https://github.com/aiperceivable>
- Yi, W. (2026). *Core-First Language Theory (CFLT): A Discourse-Level Linearization Protocol.* SocArXiv Preprint.

---

*Document Version: 1.0.0 (Internal Draft)*
*Status: Research roadmap. No CTL implementation exists at time of writing.*
*Author: CFLT Core Team*
