<div align="center">
  <img src="./docs/assets/cflt-logo.svg" alt="CFLT" width="200"/>
</div>

# CFLT — Core-First Language Theory

> **A unified theoretical framework for cross-linguistic communication, second-language pedagogy, and human-AI cognitive alignment.**
>
> Project home: [cflt.center](https://cflt.center) · Archival: [Zenodo · DOI 10.5281/zenodo.20289504](https://doi.org/10.5281/zenodo.20289504) · License: CC BY 4.0
>
> *中文版: [README.zh.md](./README.zh.md)*

---

## How to Cite

If you use CFLT theory, methodology, or code in academic work or derivative projects, please cite:

```
Yi, W. (2026). Core-First Language Theory (CFLT): A Discourse-Level
Linearization Protocol for Cross-Linguistic Communication and LLM
Prompting. Zenodo. https://doi.org/10.5281/zenodo.20289504
```

## License

- **Theoretical documentation, research notes, and figures** — [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) (see [`LICENSE`](./LICENSE))
- **Source code in sibling reference-implementation repos** (e.g. [CoreFirst](https://github.com/corefirst/corefirst)) — see each project's own `LICENSE` file (Apache 2.0 / MIT)

Both license families permit reuse, adaptation, and redistribution provided that proper attribution is given to the original author.

For collaboration, dataset access, or extended use beyond standard citation: tercel.yi@gmail.com

## AI Use Disclosure

The author is a non-native English speaker. AI tools (Claude, Gemini) were used for English translation, copy-editing, and reference formatting in the preparation of written materials. All theoretical claims, research design, empirical pilot data, and substantive arguments are the author's original work.

---

## Quick links

| Resource | Status |
|---|---|
| **[cflt.center](https://cflt.center)** — full documentation site (mkdocs) | Live |
| **[Zenodo archival](https://doi.org/10.5281/zenodo.20289504)** — *CFLT: A Discourse-Level Linearization Protocol for Cross-Linguistic Communication and LLM Prompting* | Archived; concept DOI: [10.5281/zenodo.20289504](https://doi.org/10.5281/zenodo.20289504) |
| **[CoreFirst](https://github.com/corefirst/corefirst)** ([corefirst.world](https://corefirst.world)) — Pillar I MVP, Next.js + Electron, Apache 2.0 | Deployed |

---

## What is CFLT?

**Core-First Language Theory (CFLT)** is a discourse-level normative protocol that fixes the relative order of two constituent tiers as:

```
[Core] → [Reason] → [Space] → [Time]
```

CFLT operates *above* the morphosyntactic level: each language assembles the **event nucleus** (Slot 0 — predicate + valence-bound participants + manner + scope-internal operators) using its native syntax, while the protocol governs only the **ground frame** (Slots 1–3) and the boundary between the two.

The Core is a **salience anchor** in the sense of Talmy's (2000) Figure / Langacker's (1987) profile — *not* a verb, *not* a value judgment about "the most important word."

CFLT addresses a shared bottleneck: adult L2 production pays this restructuring cost as DLPFC working-memory overhead; LLM prompting pays it as semantic drift, order-sensitivity, and "Lost in the Middle" attention degradation. A single normative intervention — Core-first linearization — is useful in both systems for partially distinct mechanistic reasons.

CFLT is **theory + method**, not a product. The theory belongs to the open commons (CC BY 4.0). Reference implementations live in independent projects.

---

## The two-pillar framing

CFLT applies a single *Core-then-Frame* organizing principle on the natural-language layer, in two processing contexts:

| Pillar | Context | Engineering deliverable | Status |
|---|---|---|---|
| **Pillar I** — Human Bilingual Education | Natural-language (human side) | [CoreFirst app](https://github.com/corefirst/corefirst) (Logic-First, Grammar-Second pedagogy) | MVP deployed |
| **Pillar II** — Machine Alignment | Natural-language (LLM side) | CFLT as standardized prompt protocol | Pilot validated (see §6 of preprint) |

Whether the same Core-First ordering of natural-language intent also helps when the downstream task is agentic tool use (e.g., MCP-style tool-call interfaces) is an open question — a special case of Pillar II, not a separate substrate. CFLT's linearization-cost mechanism applies to sequentially processed language, not to structured tool-call schemas; we therefore treat the human–agent tool-call boundary as a research question within Pillar II.

---

## Empirical status

A pilot two-part study (720 trials: 24 cases × 4 levels × 2 languages × 5 frontier models × 3 runs) provides preliminary evidence for the LLM-side prediction:

- **Level 3 (distractor-heavy):** CFLT-conformant prompts raise extraction accuracy from a mean of **65.6% to 100%** across **all five** frontier models surveyed (GPT-5, Gemini 3 Flash, Qwen3.5-Plus, DeepSeek V4 Pro, Claude Sonnet 4.6).
- **Token cost:** CFLT reduces completion-token cost on reasoning-capable models with visible chain-of-thought traces by up to **38%**, while showing no token effect on short-output / concealed-reasoning models.
- **Level 4 (buried-decision):** a null-to-slightly-negative effect on one model (DeepSeek V4 Pro, −11pp); the other four models saturate L4, so this regression is characterized as a model-specific anomaly rather than a general property of CFLT.

The pilot evidence is **suggestive, not confirmatory** — see preprint §6 for full results and §7 for the falsifiable research agenda (six sub-programs, §7.1–§7.6).

Raw data, prompts, and evaluation scripts at release tag `osf-pilot-2026-05`. The full ablation reproduces in a single command:

```bash
python scripts/llm_eval/part2_llm_cflt_eval.py --runs 3
```

---

## Reading order

For first-time readers:

1. **[`docs/en/manifesto.md`](./docs/en/manifesto.md)** — Start here. The canonical theoretical statement: what CFLT claims, why, and how the four-element Core-First sequence is operationalized as CFLT.

2. **[`docs/en/foundations/core-concept.md`](./docs/en/foundations/core-concept.md)** — Read this *immediately after the manifesto*. It defines what "Core" means (a salience anchor — action, state, identity, or request — **not** a verb or predicate) and refutes the most common misreadings. Also explains how CFLT is the unmarked default, not the only permitted form.

3. **[`docs/en/vision.md`](./docs/en/vision.md)** — Cross-project strategic roadmap: the two-pillar mission (Pillar I human education, Pillar II LLM protocol).

4. **Pick the foundation closest to your background:**
   - **[`pedagogy.md`](./docs/en/foundations/pedagogy.md)** — Krashen, Vygotsky's ZPD, Cognitive Load Theory, DeKeyser's Skill Acquisition, TBLT, Kroll's bilingual lexical access. For educators and SLA researchers.
   - **[`linguistics.md`](./docs/en/foundations/linguistics.md)** — UG, information structure (Theme-Rheme), cognitive linguistics (Talmy / Langacker), Levelt's speech production, NSM. Distinguishes Core-First from VSO word order.
   - **[`neuroscience.md`](./docs/en/foundations/neuroscience.md)** — Salience Network, PFC metabolic costs, EIC, Attention Sinks vs. Primal Tokens, proceduralization.
   - **[`logic.md`](./docs/en/foundations/logic.md)** — Predicate logic, lambda calculus, CCG, speech-act theory, Relevance Theory, Gricean maxims, DRT.
   - **[`mathematics.md`](./docs/en/foundations/mathematics.md)** — Information theory, UID, optimal coding, KL divergence, linearization on partial orders.
   - **[`llm.md`](./docs/en/foundations/llm.md)** — Transformer attention, positional biases, lost-in-the-middle, prompt-order variance, hallucination dynamics.

5. **[`docs/en/methodology/empirical-agenda.md`](./docs/en/methodology/empirical-agenda.md)** — The three empirical tracks: Computational (LLM), Psycholinguistic (human), SLA (pedagogy).

6. **[`docs/en/bibliography.md`](./docs/en/bibliography.md)** — Unified citations (~150 references across linguistics, philosophy of language, mathematics, LLM/NLP, SLA pedagogy).

---

## Reference implementations

CFLT itself is theory and specification. Concrete implementations live in independent projects — see [`docs/en/reference-implementations.md`](./docs/en/reference-implementations.md) for the up-to-date list.

- **[CoreFirst](https://github.com/corefirst/corefirst)** ([corefirst.world](https://corefirst.world)) — first reference implementation for Pillar I (human bilingual education). Next.js + Electron, Apache 2.0.

---

## Editorial posture

The theory documents follow four rules:

1. **Cite real scholarship.** Every named author and work is verifiable.
2. **Acknowledge limits.** Each foundation document contains an "Honest Limitations" section. CFLT is partly normative (a pedagogical/computational protocol), not purely descriptive — and we say so.
3. **Connect explicitly to CFLT claims.** Theory exists to support specific operational claims, not to decorate them.
4. **Keep "Core" defined consistently.** Core = salience anchor (action / state / identity / request). Not a verb. Not a predicate symbol.

The preprint adds two further commitments:

- **Cross-domain analogy framing.** The claim that SLA and LLM prompting share a "linearization cost" is treated as a load-bearing analogy, with the human-side and LLM-side predictions held to be **independently falsifiable** (preprint §1.1).
- **Suggestive, not confirmatory.** The §6 pilot is reported as suggestive evidence with one informative null result (L4 buried-decision on one model). The strong claims are deferred to the falsifiable research agenda in §7.

---

## How to cite

For the framework as a whole:

> CFLT Core Team. (2026). *Core-First Language Theory (CFLT): Reconstructing Global Bilingual Education from First Principles.* [https://cflt.center](https://cflt.center)

For the archived preprint (once Zenodo DOI is issued):

> Yi, W. (2026). *Core-First Language Theory (CFLT): A Discourse-Level Linearization Protocol for Cross-Linguistic Communication and LLM Prompting.* Zenodo. https://doi.org/10.5281/zenodo.20289504

Specific foundation documents may be cited as:

> CFLT Core Team. (2026). *Pedagogical Foundations of CFLT.* In *Core-First Language Theory.* [https://cflt.center/foundations/pedagogy](https://cflt.center/foundations/pedagogy)

---

## Contributing

Contributions are welcome — open an issue or pull request:

- Refinements to the foundations (additional citations, counter-arguments, new disciplines)
- Translations of any document to other languages
- New entries to `reference-implementations.md` for projects that adopt CFLT
- Empirical evidence supporting or challenging CFLT's claims, particularly on the sub-programs of the §7 agenda

---

## Author

**Tercel Yi** · Independent Researcher · ORCID [0009-0000-3742-4403](https://orcid.org/0009-0000-3742-4403) · [tercel.yi@gmail.com](mailto:tercel.yi@gmail.com)

Sole maintainer of CFLT and [CoreFirst](https://github.com/corefirst/corefirst). The author welcomes correspondence on supervision, collaboration, and independent implementation.

---

## License

The theoretical content in this repository is licensed under [Creative Commons Attribution 4.0 International (CC BY 4.0)](./LICENSE). You are free to share and adapt the material for any purpose, including commercially, provided you give appropriate credit.
