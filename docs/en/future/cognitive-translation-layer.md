# Cognitive Translation Layer (CTL): A Bidirectional Protocol Between Natural-Language Intent and AI-Perceivable Tool Invocation

> **Version:** 1.0.0 (Internal Draft)
> **Status:** Open research program. No implementation exists at the time of writing. The program is designed so that independent researchers, industry teams, and graduate students can contribute to or extend any phase without coordination overhead.
> **Author:** CFLT Core Team
> **License:** [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)

---

## 1. Why CTL: The Missing Substrate Bridge

CFLT (Core-First Language Theory) and apcore (AI-Perceivable Core) are two independently deployed open-source projects that, on inspection, encode the same organizing principle on disjoint substrates.

- **CFLT** ([cflt.center](https://cflt.center); Zenodo concept DOI: [10.5281/zenodo.20289504](https://doi.org/10.5281/zenodo.20289504)) is a discourse-level linearization protocol. It applies the **Core-then-Frame** principle to natural-language utterances: a mandatory event nucleus (Slot 0) precedes optional framing modifiers (Slots 1–3 — Reason, Space, Time). A reference Pillar I implementation (CoreFirst, Next.js + Electron) is operationally deployed; a 720-trial empirical pilot across five frontier LLMs is reported in the working paper.
- **apcore** ([github.com/aiperceivable](https://github.com/aiperceivable), Apache 2.0, OpenSSF Best Practices certified) is a module standard for AI-invokable tool interfaces. It applies the same Core-then-Frame principle to tool descriptions: a mandatory Core Layer (`input_schema`, `output_schema`, `description`) precedes optional Annotation Layer (`readonly`, `destructive`, `requires_approval`, `idempotent`, `open_world`, `cacheable`, `paginated`) and optional Extension Layer (`x-when-to-use`, `x-preconditions`, `x-postconditions`, `x-common-mistakes`, `x-cost-per-call`). Production SDKs exist for Python, TypeScript, and Rust; third-party adoption is documented.

Both projects, in other words, deploy the same Core-then-Frame layering on different surfaces. What is missing is a **protocol bridge** that maps between them — so that when a human user issues a CFLT-conformant natural-language request and an AI agent fulfills it through apcore-perceivable tool invocations, the cognitive layering is preserved across the substrate boundary, in both directions.

This bridge is the **Cognitive Translation Layer (CTL)**. CTL is the integrative target of the broader cross-substrate research program — open to community contribution.

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
│  apcore module standard (Core / Annotations / Extensions + ACL) │
│  Surface adapters (transparent to CTL):                          │
│    apcore-mcp → MCP / OpenAI Tools                               │
│    apcore-a2a → A2A Agent Cards                                  │
│    apcore-cli, flask-/fastapi-/django-/nestjs-/axum-apcore → ... │
│  Deployed: production SDKs (Python, TypeScript, Rust)            │
└─────────────────────────────────────────────────────────────────┘
```

CTL is not a replacement for existing AI tool-use scaffolding (MCP, OpenAI Function Calling, Anthropic Tool Use, A2A). Those protocols address transport and serialization — *how* a tool description reaches a model. CTL addresses the orthogonal question of **cognitive layering across the substrate boundary** — *which constituents of natural-language intent map to which categories of tool metadata, and how the inverse mapping reconstructs a comprehensible response*.

In apcore's own terms (see [apcore POSITIONING.md](https://github.com/aiperceivable/apcore)), apcore distinguishes a **Cognitive Interface** for AI agents — separate from UI (for humans) and API (for programs). CTL extends that distinction by adding the **human-to-agent translation layer** that the Cognitive Interface presupposes but does not itself provide.

**Transport-agnosticism (precise position).** apcore's POSITIONING explicitly places apcore *beneath* MCP / A2A / CLI / REST as the foundational module standard, with `apcore-mcp`, `apcore-a2a`, `apcore-cli`, and framework adapters (`flask-apcore`, `fastapi-apcore`, `django-apcore`, `nestjs-apcore`, `axum-apcore`) acting as **Surface Adapters** that project the same canonical module definition onto each transport — including the annotation-to-transport-hint mappings (e.g., `destructive` → MCP `destructiveHint`). CTL therefore emits **apcore Registry-targeted invocations**, not transport-specific calls; the surface adapter is downstream of CTL and transparent to it. A single CTL implementation works whether the AI client reaches the module through MCP, A2A, CLI, or REST. The division of labor at the Annotation Layer is correspondingly sharp: CTL handles the **bidirectional natural-language ↔ annotation parsing** (Slot 1 ↔ `destructive` / `requires_approval` / …); the surface adapter handles the **annotation ↔ protocol-hint serialization** (`destructive` ↔ MCP `destructiveHint`, A2A skill descriptors, etc.). These are distinct translations at distinct layers.

**Composition with apcore's 11-step execution pipeline.** apcore's normative pipeline (POSITIONING.md §"11-Step Execution Pipeline"; PROTOCOL_SPEC §runtime) runs: context processing → safety checks → module lookup → ACL enforcement → approval gate → input validation → middleware before → execution → output validation → middleware after → result return. CTL forward direction **terminates at the input to step 3** (module lookup): the parser's output is a Registry-targeted invocation with caller_id, target module, validated inputs, and any consent/approval pre-evidence. CTL reverse direction **begins at the output of step 11** (typed, trace-annotated result). The intervening steps (4–10) are apcore's responsibility and run unmodified — CTL composes with the pipeline, it does not intrude on it. This composition point is what makes CTL implementable as a library above apcore without requiring any change to apcore itself. The apcore SDK already implements this composition point in `Executor.validate()`, which performs dry-run execution of the pure pipeline steps and returns `PreflightResult{ checks, requiresApproval, errors, predictedChanges }` — exactly the "construct a call without executing it" engineering artifact that the CTL forward direction requires. A CTL implementation can consume this API directly; no new apcore surface is needed.

**Symmetry under apcore-a2a multi-agent flows.** The "user utterance" of §4.1 is a placeholder for *any CFLT-conformant linguistic source*. Under `apcore-a2a`, that source can be another agent invoking a skill through an Agent Card, not only a human. CTL applies symmetrically in this case: the calling agent emits a CFLT-conformant request; the receiving agent's CTL instance parses it into an apcore invocation. The slot-to-layer correspondence is invariant under this substitution because CFLT itself is a discourse-level protocol indifferent to whether the producer is human or artificial.

---

## 3. The Slot-to-Layer Correspondence

The empirical pre-condition that makes CTL tractable as a finite research target — rather than open-ended speculation — is a structural correspondence between CFLT's four discourse slots and apcore's three metadata layers. This correspondence is the core insight of the CTL program; verifying that it holds non-trivially across a representative inventory of human intents and module families is itself part of the research.

| CFLT Slot | Linguistic Function | Example Constituent | apcore Layer | apcore Fields | Cross-Substrate Function |
|---|---|---|---|---|---|
| **Slot 0** (Core) | Event nucleus / salience anchor | predicate + valence-bound arguments + manner + scope-internal operators | **Core Layer** | `input_schema`, `output_schema`, `description` | Mandatory functional contract — what the operation *is* |
| **Slot 1** (Reason) | Causal / justification framing | *because*, *in order to*, *so that*, motivational clauses | **Annotation Layer** | `requires_approval`, `destructive`, `idempotent`, `open_world` | Governance — under what conditions the operation may proceed |
| **Slot 2** (Space) | Locative / scope framing | *in X*, *within Y*, *across Z*, scope-restricting clauses | **ACL** | `callers`, `targets`, `conditions`, `default_effect` | Permission boundary — where (in the system) the operation is permitted |
| **Slot 3** (Time) | Temporal / conditional framing | *before*, *after*, *when*, *if*, *whenever*, scheduling clauses | **Extension Layer** | `x-when-to-use`, `x-preconditions`, `x-postconditions`, `x-workflow-hints` | Planning hints — when and in what workflow position the operation belongs |

**Reading the correspondence.** Both column groups describe the same conceptual structure: a mandatory *what* (Core / Slot 0), surrounded by three categories of optional framing — *why* (Reason / governance), *where* (Space / permission), *when* (Time / planning). The claim is not that the mapping is one-to-one and exhaustive — natural language is messier than that — but that the **categorical alignment** is sufficiently strong to support a deterministic-with-fallback parsing strategy.

**Why this is non-trivial.** It would be unremarkable if Slot 0 mapped to the Core Layer and the remaining three slots all mapped to a single "metadata" bucket. The non-trivial observation is that the **three categories of CFLT ground-frame slots (Reason / Space / Time) map distinctly to three categories of apcore non-core metadata (Annotation Layer / ACL / Extension Layer)** — each pair sharing a functional family (governance, permission boundary, planning hints respectively) that pre-existed independently in both projects. This is the structural evidence that the same Core-then-Frame organizing principle is operating on both substrates.

**Correspondence strength is not uniform.** The four entries in the table are **asymmetric in empirical strength** and should be read in tiers:

- **Strong correspondence**: Slot 0 ↔ Core Layer — both are the mandatory functional contract, identical from either linguistic or tool-metadata perspective.
- **Medium correspondence**: Slot 3 ↔ Extension Layer — both concern *when / in what workflow position*, naturally aligned with `x-when-to-use` / `x-preconditions`.
- **Interpretive correspondence**: Slot 1 ↔ Annotation Layer and Slot 2 ↔ ACL — the linguistic Reason slot expresses user *motivation*, whereas Annotation expresses tool *operational properties*; the Space slot expresses event *scope of effect*, whereas ACL expresses *caller-on-target permission boundary*. These pairs sit in a "conceptually adjacent but axis-misaligned" relationship; the binding rests on a CTL-parser-side **category induction** rather than semantic isomorphism.

Engineering implication: the CTL SDK should treat the slot-to-layer mapping as **configurable** (default table + user overrides) rather than as a hard correspondence. A single entry failing on a domain or module family should not invalidate the bridge as a whole; CTL-1 / CTL-2 are accordingly evaluated per correspondence, not as a single composite.

**Convergence with apcore's Cognitive Interface Lifecycle.** apcore's POSITIONING.md decomposes AI-agent module use into a four-stage lifecycle: **Discovery** (description, schema) → **Strategy** (`x-when-to-use`, `x-common-mistakes`) → **Governance** (`requires_approval`, `destructive`, ACL) → **Recovery** (`ai_guidance`, `retryable`). Read against the CFLT slot scheme, this lifecycle factors into the same four functional categories: Discovery = Slot 0 resolution (what); Strategy = Slot 3 binding (when/in-what-workflow); Governance = Slot 1 (why) + Slot 2 (where); Recovery = the reverse-direction frame reconstruction.

**Honest downgrade of the "independent convergence" claim.** The two schemata took shape at **different times in different code bases**, but both are deliberate instantiations of a shared Core-then-Frame prior held by overlapping designers — not the chance convergence of two independent observers. This relationship still constitutes valid engineering evidence that the prior **lands on the tool-metadata substrate independently of the natural-language substrate**, but it should not be invoked as "two independent discoveries coinciding". The principle's double appearance is a design choice; its cross-substrate validity ultimately rests on the empirical sub-claims of §6 — particularly CTL-6, which tests the correspondence against non-apcore tool surfaces.

**Non-invasive extensibility via `Annotations.extra`.** apcore PROTOCOL_SPEC §4.4.1 normatively defines an `Annotations.extra.<namespace>.<name>` extension map for ecosystem-specific metadata (existing namespaces include `mcp.*`, `cli.*`, `a2a.*`). CTL-specific metadata — for example, custom Slot-1 consent phrasing templates or Slot-3 workflow positioning hints — can be carried in `extra.cflt.*` / `extra.ctl.*` without forking apcore or modifying the canonical Annotation surface. The slot-to-layer correspondence is therefore expressible inside apcore's already-deployed conformance envelope.

---

## 4. Bidirectional Mechanism

CTL is bidirectional. The two directions have asymmetric difficulty: forward parsing has a well-formed source representation (CFLT-conformant natural language) but a search space (the module Registry); reverse generation has a well-formed source representation (the structured tool result) but must navigate the constraints of producing fluent CFLT-conformant natural language.

**Risk disclosure for the reverse direction.** The forward direction has the `CFLTTransformer` of the CoreFirst reference implementation (Zod-strict schema + templated system prompt + JSON salvage fallback) as a reusable precursor; the **reverse direction has no existing infrastructure on either substrate side**, and CTL-3 depends on a human-judgment rubric — making it the **single highest-risk component** of the CTL research program. Until Phase 3, design choices for the reverse direction (prompting paradigm, whether to mirror the forward Zod-schema shape, dimensions of the human-judgment rubric) should remain open and be validated via small-scale pilot first.

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

**Note on Registry lookup capability.** The apcore Registry currently offers exact-ID lookup and prefix enumeration (see apcore-typescript `src/registry/registry.ts`: `get / has / list / iter / getDefinition`); it does **not** provide native semantic search. The "Slot 0 → module candidates (affinity match)" step above is implemented by a CTL-internal retrieval layer (embedding recall + LLM re-ranking), with results constrained to module IDs that exist in the Registry (Zod-validated). This layer is part of CTL's implementation responsibility, not an extension request to apcore — and it also means CTL's "LLM-neutral" claim has a known caveat at the embedding-model choice, which should be declared explicitly in SDK design (see §5.3).

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

**What "substrate-neutral" modifies.** To be precise: "substrate-neutral" qualifies the **Core-then-Frame principle itself**, not the CTL implementation. By definition, CTL is the concrete bridge between the **specific pair** of substrates CFLT ↔ apcore; it depends on both sides' concrete protocols. CTL **operationalizes** the substrate-neutral principle by *landing it on this specific substrate pair*, not by being *pluggable across arbitrary tool surfaces*. That CTL depends on apcore is not a counter-argument to the principle, just as HTTP/2 depending on TCP does not refute the abstraction of the transport layer. Bridging to other tool surfaces (raw MCP, A2A, OpenAI Tool Use, …) is the **extension experiment** proposed in §6 CTL-6, not part of the CTL 1.0 surface.

### 5.2 Relation to adjacent traditions

- **Frame Semantics (Fillmore 1982; FrameNet, Baker, Fillmore & Lowe 1998)**: The CFLT four-slot scheme is compatible with — but not identical to — frame-semantic role structures. CTL leverages frame-semantic affinities for Slot 0 → module resolution (Slot 0 carries a predicate; modules are typed by predicate-like functional contracts).
- **Toolformer (Schick et al. 2023)** and the broader LLM-tool-use line: CTL is downstream of this work in that it presupposes the existence of structured tool interfaces; it is upstream in that it addresses the protocol-level question of *which natural-language constituents bind to which tool-metadata categories*, which existing tool-use work treats as solved by ad-hoc prompting.
- **Schema-enforced output (JSON mode, structured outputs)**: CTL extends schema enforcement from the *output* of LLM generation to the *bidirectional translation* between human intent and tool invocation, with governance enforcement at the bridge.

### 5.3 What CTL is not

- **Not a workflow engine.** CTL maps a single intent to a single (or a small disambiguation set of) invocation. Multi-step orchestration belongs to upstream workflow engines (e.g., apflow, LangChain, CrewAI).
- **Not an LLM invocation library.** CTL is LLM-neutral; the LLM is one possible implementation of the parser and generator components, but the protocol does not bind to a specific model.
- **Not a transport protocol.** CTL is layered above the apcore module layer, which in turn is layered above the surface adapters (`apcore-mcp`, `apcore-a2a`, `apcore-cli`, framework adapters) that bridge to MCP, A2A, OpenAI Tool Use, etc.; it addresses the cognitive-layering question that those protocols delegate to ad-hoc prompting.
- **Not a surface adapter.** The `xxx-apcore` adapter family already auto-projects apcore modules onto specific transports — including annotation-to-hint mappings, Agent Card generation, CLI argument parsing, and HTTP route generation. CTL operates strictly above this layer on the natural-language ↔ apcore-module-call boundary; it does not compete with surface adapters.
- **Not a fork of apcore.** CTL-specific metadata is carried in apcore's existing `Annotations.extra.cflt.*` / `extra.ctl.*` namespace per apcore PROTOCOL_SPEC §4.4.1; in apcore-typescript, `extra: Readonly<Record<string, unknown>>` (`src/module.ts`) is the canonical field with defined runtime merge semantics. No spec changes to apcore are required for CTL to be implementable.
- **Not LLM-free.** "LLM-neutral" means **provider-neutral** (OpenAI / Anthropic / Gemini / local models are interchangeable); it does **not** mean LLM-less. Parser, module resolution, and reverse linearization are all LLM-driven. What distinguishes CTL from ad-hoc prompting is the **contract shape** (Zod-strict schema + templated prompt + JSON salvage), not avoiding the LLM. Embedding models (for Slot 0 → module recall) are likewise unavoidable and constitute the acknowledged discount on CTL's "model-neutral" claim.
- **Not a cross-tool-surface universal bridge.** The CTL protocol specification currently defines the CFLT ↔ apcore substrate pair **completely** and no other. Bridging to other tool surfaces (raw MCP, A2A, OpenAI Tool Use, …) is the **extension experiment** of §6 CTL-6, not part of the CTL 1.0 surface — even if CTL-1 through CTL-5 all pass, that only demonstrates "CTL works on apcore"; cross-substrate neutrality must be supported separately by CTL-6.

---

## 6. Falsifiable Sub-Claims

The CTL research program is structured around falsifiable sub-claims, each with a stated falsification condition.

### CTL-1: First-attempt invocation success rate

**Claim.** A CFLT→apcore translation produced by a CTL parser yields higher first-attempt invocation success rates than an LLM-only baseline that lacks the CFLT slot-to-layer correspondence.

**Measurement.** On a benchmark of *N* human-authored CFLT-conformant requests against a Registry of *M* apcore modules with mixed governance metadata, compare first-attempt success (defined as: correct module selected, input_schema satisfied, no governance violation, output validates against output_schema) for CTL-parsed invocations versus baseline.

*On the distinction between "trials" and "requests".* The "720-trial pilot" referenced in the CFLT preprint denotes **24 human-authored CFLT-conformant requests × 5 frontier model families × 6 experimental conditions** (control / CFLT × distractor levels L1–L3). For CTL-1, *N* should be planned as the number of **independent requests** (we recommend *N* ≥ 200 to support *p* < .05 comparison of success rates) and must be **clearly distinguished** in papers and documentation from *trials* (= *N* × model families × conditions), so that readers do not misread "720 trials" as 720 independent requests.

**Falsification condition.** If success rate fails to improve at *p* < .05 across at least three frontier model families, CTL collapses to "ordinary structured-intent parsing" and contributes no protocol-level value beyond existing tool-use scaffolding.

### CTL-2: Over-permission incident reduction

**Claim.** A CTL-mediated invocation flow reduces over-permission incidents (cases where an agent invokes a module with `requires_approval=True` or `destructive=True` without surfacing the consent gate) relative to a baseline that lacks Slot 1 → Annotation Layer binding.

**Measurement.** On a benchmark of intentionally consent-ambiguous requests, count over-permission incidents under CTL versus baseline.

**Falsification condition.** If over-permission incidents fail to decrease in absolute count across at least three frontier model families, the Slot 1 → Annotation Layer correspondence is not protocol-actionable, and the governance contribution of CTL is refuted.

*Why absolute count, not p-value.* Over-permission incidents are rare events with low base rates in any well-constructed benchmark; statistical-significance testing has poor power in this regime. An absolute-count decrease across all evaluated model families is therefore the more conservative falsification criterion. A stronger test using *p* < .05 on a higher-volume, deliberately-skewed benchmark is reserved as a later-phase extension.

### CTL-3: Reverse-direction comprehension preservation

**Claim.** A CFLT-conformant linearization of a structured apcore result yields higher human-judged comprehensibility scores than a raw structured result or an ad-hoc LLM-generated natural-language summary.

**Measurement.** Human judgment study on *K* triplets (raw structured result, ad-hoc summary, CTL-linearized response), with comprehensibility scored on a fixed rubric (does the response surface the answer? does it explain the scope? does it surface the time-validity?).

**Falsification condition.** If CTL-linearized responses do not score higher than ad-hoc summaries on at least two of the three rubric dimensions at *p* < .05, the reverse-direction contribution is refuted.

### CTL-4: Cross-model generalization

**Claim.** CTL parsing and generation behavior is stable across frontier model families — i.e., the slot-to-layer correspondence is a model-independent protocol property rather than a model-specific artifact.

**Measurement.** Replicate CTL-1, CTL-2, CTL-3 across at least five frontier model families (GPT-5, Claude Sonnet, Gemini, Qwen, DeepSeek), using model-neutral parser/generator implementations.

**Falsification condition.** If CTL-1, CTL-2, or CTL-3 results show statistically significant cross-model variance (interaction effect at *p* < .05 between model family and CTL-vs-baseline), CTL must retreat to a per-model-family protocol, weakening the cross-substrate generalization.

*Statistical note.* Failure to reject H0 (no interaction) is **not** the same as confirming cross-model uniformity. For positive confirmation of cross-model generalization we additionally require: (i) each per-model CTL effect to be individually significant at *p* < .05, and (ii) the cross-model effect-size variance to fall within a pre-registered equivalence margin (TOST procedure, Lakens 2017). These three conditions — no significant interaction, individual significance, equivalence-bounded variance — must hold jointly for CTL-4 to be considered confirmed rather than merely not-falsified.

### CTL-5: Surface-adapter (transport) invariance

**Claim.** A CTL parser, given a fixed CFLT-conformant input and a fixed apcore Module Registry, produces the *same* apcore Registry-targeted invocation regardless of which surface adapter (`apcore-mcp`, `apcore-a2a`, `apcore-cli`, framework adapters) ultimately delivers the call to the runtime.

**Measurement.** On a benchmark of *N* CFLT-conformant requests against a single canonical Registry, run the CTL parser under three delivery configurations: (i) apcore-mcp → MCP transport, (ii) apcore-a2a → A2A transport, (iii) apcore-cli → CLI transport. Compare emitted invocations (target module ID, validated input dict, governance precondition flags) for byte-level equivalence after a canonical normalization pass.

**Falsification condition.** If emitted invocations diverge across delivery configurations for ≥ 5% of benchmark items after normalization, CTL is leaking into the transport layer rather than terminating at the apcore module layer, which contradicts the substrate-neutrality claim of §2 and refutes the architectural positioning of CTL as strictly above apcore.

*Why this matters.* Surface-adapter invariance is the operational expression of the cross-substrate hypothesis (§5.1). If CTL emits different module invocations under different transports for the *same* CFLT input, then either (a) the parser is conditioning on transport-specific state it should not see, or (b) the slot-to-layer correspondence does not in fact reduce to the apcore canonical Module representation. Either outcome would falsify CTL's claim to be a substrate-neutral protocol bridge.

### CTL-6: Cross-tool-surface external invariance

**Claim.** The empirical benefit of the slot-to-layer correspondence is **substrate-neutral**: configuring CTL with equivalent rules over a **non-apcore** structured tool surface (e.g., raw MCP tool definitions, OpenAI Function descriptions, A2A skill free-text) still produces the core effects of CTL-1 / CTL-2.

**Measurement.** Replicate the CTL-1 / CTL-2 benchmarks on an **equivalent-scale** non-apcore tool set (suggested construction: select *M* tools from public MCP servers, retaining only `name` / `description` / `input_schema` and **stripping** apcore's Annotation / ACL / Extension metadata); run CTL with a "no-apcore-metadata" version of its default slot-to-layer mapping (Core only mandatory; governance / extension information falls back to the free-text tool description). Compare effect sizes for CTL-on-apcore vs. CTL-on-raw-MCP within each frontier model family.

**Falsification condition.** If on the non-apcore surface CTL-1 / CTL-2 effect sizes are **significantly smaller** than on the apcore surface (**model-family × surface** interaction at *p* < .05, with effect-size difference outside a pre-registered non-equivalence margin), then the empirical benefit of the slot-to-layer correspondence is **substrate-dependent** — driven by apcore's own already-optimized metadata layering rather than by a substrate-neutral principle. This refutes the cross-substrate hypothesis of §5.1.

*Why this matters.* CTL-1 through CTL-5 are all validated **inside apcore**; even if all pass, they only demonstrate that "CTL works on apcore". CTL-6 is the only external experiment that tests **substrate-neutrality**. Failure of CTL-6 does not refute CTL's engineering value as a CFLT ↔ apcore bridge, but it does require the documentation to downgrade the §5.1 cross-substrate claim to "apcore-conditional".

---

## 7. Research Roadmap

The CTL research program is structured as a multi-phase plan. The substrate endpoints (CFLT and apcore) being independently deployed and validated is the precondition that makes this scope credible. The phases below are presented in logical order; the actual execution timeline depends on the institutional setting (independent research, industry research lab, or graduate program) and on community participation. The phases are intentionally decoupled: any phase can be advanced by an interested party without depending on the progress of any single contributor, and contributions to a single sub-claim (CTL-1 through CTL-5) are welcome on their own.

### Phase 1 — Theoretical formalization + benchmark design + package architecture proposal

- Formalize the slot-to-layer correspondence (§3) as a typed mapping with stated edge-case behavior; make the mapping **configurable** (default table + user overrides) to accommodate the strength asymmetry of "interpretive correspondences" identified in §3.
- Design the CTL-1 / CTL-2 / CTL-3 / CTL-6 benchmarks: assemble the *N* CFLT-conformant request corpus, the *M*-module apcore Registry with controlled governance-metadata distributions, the *M*-module raw-MCP control set, and the human-judgment rubric for CTL-3.
- Publish the **CTL spec package-architecture proposal** (three-package split: `ctl-spec` abstract types / `ctl` orchestrator + default adapters / `ctl-eval` evaluation harness), specifying:
  - **Prototype phase**: both adapters (`ctl-adapter-corefirst`, `ctl-adapter-apcore`) live in CTL's own repository, **not** in either the CFLT or the apcore repository, preserving the §1 / §10 commitment that the two endpoint projects remain independently deployed.
  - **Stabilization phase**: follow the `apcore-mcp` / `apcore-a2a` precedent and migrate native-side adapters into their respective ecosystems (`apcore-ctl` joins the apcore family; `corefirst-ctl` joins corefirst). Migration **trigger conditions**: spec 1.0.0 + ≥ 6 months without breaking changes + at least one sub-claim with positive evidence + the appearance of a second adopter.
- Publish: one theoretical position paper (target venues: *Cognitive Science*, *Topics in Cognitive Science*, or a major AI alignment workshop).

### Phase 2 — Forward-direction prototype + CTL-1, CTL-2, CTL-5 evaluation

- Implement the CTL forward-direction parser as a model-neutral library, callable from any LLM provider; reuse the CoreFirst `CFLTTransformer` as the parser precursor and apcore's `Executor.validate()` as the governance-gate composition point.
- Run CTL-1 and CTL-2 evaluations across at least five frontier model families.
- **Deliver CTL-5 in the same phase**: surface-adapter invariance — for a fixed CFLT input and fixed Registry, byte-compare the invocations CTL emits across `apcore-mcp` / `apcore-a2a` / `apcore-cli` delivery configurations. This evaluation **does not depend on LLM-evaluation budget** and can serve as the program's first early engineering signal.
- Publish: one empirical paper on forward-direction performance (target venues: ACL, EMNLP, NAACL, or NeurIPS Datasets & Benchmarks).

### Phase 3 — Reverse-direction prototype + CTL-3, CTL-4 evaluation

- Implement the CTL reverse-direction generator, including the governance-explanation, consent-gating, and recovery-suggestion flows (§4.3).
- Run CTL-3 human-judgment study and CTL-4 cross-model generalization analysis.
- Publish: one empirical paper on reverse-direction comprehensibility + one cross-model generalization paper.

### Phase 4 — Integration + synthesis

- Integration study: deploy CTL in the CoreFirst reference application (Pillar I) and measure end-to-end task completion rates under CTL-mediated versus baseline interaction.
- Synthesize Phases 1–3 into a unified cross-substrate research write-up.
- Public deliverable: a CTL specification document (analogous to the apcore PROTOCOL_SPEC) suitable for independent third-party implementation.

---

## 8. Out of Scope

The CTL research program does not aim to deliver any of the following:

- **A workflow engine** that chains multiple CTL-mediated invocations into multi-step plans. That belongs to upstream tools (apflow, LangChain, CrewAI).
- **A new transport protocol** to compete with MCP, A2A, or OpenAI Tool Use. CTL is layered above whichever transport apcore adopts.
- **A new LLM**. The parser and generator components are LLM-neutral; the LLM is one substitutable implementation.
- **A productized SaaS bridge service.** Like CFLT itself, CTL is a protocol specification; productization is the work of independent organizations.
- **An automated theorem prover for the slot-to-layer correspondence.** The correspondence is an empirically defended claim, not a logical derivation; its support comes from CTL-1 through CTL-5, not from formal proof.

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

**Note on CTL-5 and CTL-6.** Among the six falsifiable sub-claims of §6, **CTL-5 and CTL-6 both** stand outside the six CFLT sub-programs:

- **CTL-5** (surface-adapter invariance) tests an apcore-side **structural property** — that CTL's parser terminates cleanly at the apcore module layer without leaking into transport state — evaluated directly against `apcore-mcp` / `apcore-a2a` / `apcore-cli`.
- **CTL-6** (cross-tool-surface external invariance) tests the **external support for the substrate-neutrality hypothesis** — whether the slot-to-layer correspondence still produces an effect on non-apcore tool surfaces — evaluated against raw MCP tools / OpenAI Function descriptions / A2A skills.

This independence from CFLT empirical foundations is by design: CTL's cross-substrate claim has two legs — one pointing inward to apcore (CTL-5), one outward beyond apcore (CTL-6) — and both are separate from CTL's grounding on the CFLT side.

---

## 10. Status

This document describes a planned research program. **No implementation of CTL exists at the time of writing.** The two substrate endpoints (CFLT, apcore) are independently deployed and publicly inspectable; CTL is the bridge whose specification and empirical evaluation constitute the planned contribution. Execution pathways are open: independent researchers, industry teams, and graduate students are all welcome to advance the program — no pathway is privileged. The program is designed to be advanced by whoever finds it useful; participation at any phase or sub-claim is welcome.

The author maintains this document, the CFLT framework (cflt.center), and the apcore standard (github.com/aiperceivable) as separate open-source efforts under permissive licenses. Inquiries about mentorship, collaboration, or independent implementation are welcome — directly by email (tercel.yi@gmail.com; ORCID [0009-0000-3742-4403](https://orcid.org/0009-0000-3742-4403)) or via the project channels listed at [cflt.center](https://cflt.center).

**On code-repository location.** The CTL implementation (including `ctl-spec`, `ctl`, `ctl-eval`, and the prototype-phase adapters `ctl-adapter-corefirst` and `ctl-adapter-apcore`) will live in a **third, independent repository** — **not** inside either the CFLT or the apcore repository — preserving both projects' "independently deployed open-source projects" commitment (§1, §5.3). Native-side adapters will be handed back to their respective ecosystems (following the `apcore-mcp` precedent) **only** once: spec 1.0.0 has been stable for ≥ 6 months without breaking changes, at least one sub-claim has positive evidence, and a second adopter has appeared. Until then, the CFLT and apcore repositories take **zero dependency** on CTL.

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
- Yi, W. (2026). *Core-First Language Theory (CFLT): A Discourse-Level Linearization Protocol.* Zenodo. https://doi.org/10.5281/zenodo.20289504

---

*Document Version: 1.0.0 (Internal Draft)*
*Status: Research roadmap. No CTL implementation exists at time of writing.*
*Author: CFLT Core Team*
