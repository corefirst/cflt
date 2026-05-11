# Language-Pair Guides

> **Version:** 1.0.0 (Internal Draft)
> **Author:** CFLT Core Team
> **Organization:** [CFLT.center](https://cflt.center)
> **License:** [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)

> **Purpose:** Operationalize CFLT for specific L1↔L2 pairs. The protocol layer (Core-first, R-S-T order) and slot-semantics layer are universal (see [`../../foundations/core-concept.md`](../../foundations/core-concept.md) §2.3). What is **not** universal is the event-nucleus internal assembly and the language-specific edge cases — those are documented here per pair.

---

## Why This Series Exists

The two-tier model (`core-concept.md` §2.1) decouples:
- the **universal protocol** (slot order, slot semantics) — applies to all language pairs
- the **language-specific assembly** (how the event nucleus is built syntactically) — delegated to native L1/L2 grammar

The protocol works for any language pair, but learners of specific pairs need:
- The list of edge cases that arise when *their* L1 syntax meets *their* L2 syntax
- Worked examples that pivot through CFLT without unnecessary detours
- A list of pitfalls common to that pair

These guides are not duplicates of `slot-disambiguation.md` — that document gives the universal decision tree. These guides give the **pair-specific case law** that supplements the decision tree.

---

## Available Guides

| Pair | Direction | Focus |
|---|---|---|
| [Chinese ↔ Japanese](./zh-ja.md) | bidirectional | The English-independent pivot case — demonstrates that CFLT operates on a non-Indo-European pair without an English intermediate. (Two-family demonstration; the full universality argument is in [`../../foundations/core-concept.md`](../../foundations/core-concept.md) §2.5.) |
| [English ↔ Chinese](./en-zh.md) | bidirectional | Largest learner population worldwide. Topic-prominent vs subject-prominent contrast. |
| [Chinese ↔ English](./zh-en.md) | bidirectional | Most common learner direction (Chinese → English). Highest commercial relevance. |
| [English ↔ Japanese](./en-ja.md) | bidirectional | Classic SVO ↔ SOV typological contrast. Test case for verb-final / particle-rich syntax. |

---

## How To Use a Guide

Each guide is structured as:

1. **Pair-specific notes** — what's typologically distinctive about this pair
2. **Event-nucleus assembly differences** — how the same Core gets built differently in each language
3. **Edge cases** — boundary calls that go differently in this pair vs the universal default
4. **Worked examples** — 5–10 fully decomposed sentences with both languages' surface forms
5. **Common learner pitfalls** — where speakers of L1 typically misapply CFLT when targeting L2

Read the guide for *your specific* L1↔L2 pair. The universal protocol and slot-semantics are in the foundations docs; this guide adds only what's specific to your pair.

---

## Coverage Roadmap

The four current guides cover the most-trafficked pairs in the global L2 market and the typologically-illustrative pairs needed to defend CFLT's universality claim. Future guides may include:

- Korean ↔ Japanese (within-Asian, also SOV-on-SOV with different agglutination strategies)
- Spanish ↔ English (Romance vs Germanic, both SVO)
- Arabic ↔ English (VSO ↔ SVO, root-and-pattern morphology)
- French ↔ Chinese (head-initial Romance vs head-initial isolating)

Contributions welcome — see the [validation process](../slot-disambiguation.md#7-validation-process) for the criteria each guide must satisfy.
