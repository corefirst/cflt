# CFLT — Core-First Language Theory

> **A unified theoretical framework for cross-linguistic communication, second-language pedagogy, and human-AI cognitive alignment.**
>
> Project home: [cflt.center](https://cflt.center)
>
> *中文版: [README.zh.md](./README.zh.md)*

---

## What is CFLT?

**Core-First Language Theory (CFLT)** proposes a single discourse-level principle:

> *The cognitive core of an utterance is also its universally-prioritized linear position.*

From this principle, the **Core-First Language Method (CFLM)** derives a four-element sequencing rule that bridges any two natural languages with minimum cognitive friction, while also serving as a structured prompt protocol for Large Language Models:

```
[Core Action/Result] → [Condition/Reason] → [Space/Context] → [Time]
```

CFLT is **theory + method**, not a product. The theory belongs to the open commons (CC BY 4.0). Reference implementations live in separate projects — see [reference-implementations.md](./docs/en/reference-implementations.md).

---

## Reading Order

For first-time readers:

1. **[`docs/en/manifesto.md`](./docs/en/manifesto.md)** — Start here. The canonical theoretical statement: what CFLT claims, why, and how the four-element Core-First sequence is operationalized as CFLM.

2. **[`docs/en/foundations/core-concept.md`](./docs/en/foundations/core-concept.md)** — Read this *immediately after the manifesto*. It defines what "Core" means in CFLM (a salience anchor — action, state, identity, or request — **not** a verb or predicate) and refutes the most common mis-readings. Also addresses how CFLM is the unmarked default, not the only permitted form. Without this, the formal-logic and information-theoretic analogies in the other foundation docs can be misread.

3. **Pick the foundation closest to your background:**
   - **[`docs/en/foundations/pedagogy.md`](./docs/en/foundations/pedagogy.md)** — Krashen's Input Hypothesis, Vygotsky's ZPD, Cognitive Load Theory, Skill Acquisition Theory, Task-Based Language Teaching, Kroll's bilingual lexical access, motor-skill transfer in phonetics. Most directly relevant for educators and SLA researchers.
   - **[`docs/en/foundations/linguistics.md`](./docs/en/foundations/linguistics.md)** — Universal Grammar, information structure (Theme-Rheme, Topic-Comment), cognitive linguistics (Talmy's Figure, Langacker's profile), speech production (Levelt), Natural Semantic Metalanguage. Explicitly distinguishes Core-First from VSO word order.
   - **[`docs/en/foundations/logic.md`](./docs/en/foundations/logic.md)** — Predicate logic, lambda calculus, CCG, speech-act theory, Relevance Theory, Gricean maxims, DRT. Frames these as inspirations for the *early-commitment principle*, not as the surface form CFLM emits.
   - **[`docs/en/foundations/mathematics.md`](./docs/en/foundations/mathematics.md)** — Information theory, Uniform Information Density, optimal coding, Markov chains, KL divergence, the linearization problem on partial orders, search-space reduction in production planning.
   - **[`docs/en/foundations/llm.md`](./docs/en/foundations/llm.md)** — Transformer attention, positional biases, lost-in-the-middle, prompt-order variance, chain-of-thought, hallucination dynamics. Why CFLM aligns with LLM behavior precisely because it stays inside the natural-language manifold the model was trained on.

4. **[`docs/en/bibliography.md`](./docs/en/bibliography.md)** — Unified citations (~80 references across linguistics, philosophy of language, mathematics, LLM/NLP research, and SLA pedagogy).

5. **[`docs/en/vision.md`](./docs/en/vision.md)** — Cross-project strategic roadmap: the dual mission of CFLT across human bilingual education (Pillar I) and LLM protocol standardization (Pillar II).

## Reading Map

```
                           manifesto.md
                       (the central thesis)
                                │
                                ▼
                  foundations/core-concept.md
                (Core = salience anchor; not verb;
                 unmarked default; comprehensible
                 human language manifold)
                                │
            ┌───────────┬───────┼────────┬───────────┐
            ▼           ▼       ▼        ▼           ▼
        pedagogy   linguistics  logic   math       llm
       (SLA, ZPD,  (cognitive  (formal  (info-     (transformer
       cognitive   linguistics, logic   theory,    biases, prompt
       load,       information  inspires linearization) engineering)
       skill       structure,  early-
       acquisition, speech     commit-
       TBLT)       production) ment)
            └───────────┴───────┴────────┴───────────┘
                                │
                                ▼
                         bibliography.md
                      (full reference list)
```

---

## Reference Implementations

CFLT itself is theory and specification. Concrete implementations live in independent projects. See [`docs/en/reference-implementations.md`](./docs/en/reference-implementations.md) for the up-to-date list.

The first reference implementation is [**CoreFirst**](https://github.com/corefirst/corefirst) ([corefirst.world](https://corefirst.world)) — an open-source Next.js application implementing CFLM for human L2 learners (Pillar I).

---

## Editorial Posture

The theory documents follow four rules:

1. **Cite real scholarship.** Every named author and work is verifiable.
2. **Acknowledge limits.** Each foundation document contains an "Honest Limitations" section. CFLT is partly normative (a pedagogical/computational protocol), not purely descriptive — and we say so.
3. **Connect explicitly to CFLM claims.** Theory exists to support specific operational claims, not to decorate them.
4. **Keep "Core" defined consistently.** Core = salience anchor (action / state / identity / request). Not a verb. Not a predicate symbol. The core-concept document is the canonical reference.

---

## How to Cite

If you cite CFLT in academic or technical writing, please use:

> CFLT Core Team. (2026). *Core-First Language Theory (CFLT): Reconstructing Global Bilingual Education from First Principles.* Retrieved from https://cflt.center

Specific foundation documents may be cited as:

> CFLT Core Team. (2026). *Pedagogical Foundations of CFLT/CFLM.* In *Core-First Language Theory.* https://cflt.center/foundations/pedagogy

---

## Contributing

Contributions are welcome — open an issue or pull request:

- Refinements to the foundations (additional citations, counter-arguments, new disciplines)
- Translations of any document to other languages
- New entries to `reference-implementations.md` for projects that adopt CFLM
- Empirical evidence supporting or challenging CFLM's claims

---

## License

The theoretical content in this repository is licensed under [Creative Commons Attribution 4.0 International (CC BY 4.0)](./LICENSE). You are free to share and adapt the material for any purpose, including commercially, provided you give appropriate credit.
