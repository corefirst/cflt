# Chinese ↔ English: CFLT Operationalization

> **Version:** 1.0.0 (Internal Draft)
> **License:** [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)

> **Audience.** Chinese-speaking learners of English. The largest commercial L2 segment globally, and the canonical target for CFLT-driven SLA.

> **Note.** This guide is the *Chinese-learner-perspective* counterpart to [`en-zh.md`](./en-zh.md). The typological table and examples overlap; what differs is the framing — this guide names pitfalls in the direction Chinese L1 → English L2.

---

## 1. Pair-Specific Notes (Chinese L1 perspective)

For the typological comparison table, see [`en-zh.md`](./en-zh.md) §1.

The key facts a Chinese learner of English needs to internalize:

1. **English has tense; Chinese does not.** Every English finite verb carries past/present/future. CFLT-English Core *must* be tense-marked.
2. **English requires explicit subjects.** Chinese drops subjects freely; English does not. CFLT-English Core needs an overt subject.
3. **English has articles (a/the); Chinese does not.** Article choice is a Core-internal English issue — CFLT does not slot it but cannot ignore it either.
4. **English has plural marking (-s); Chinese only has 们 for animate plurals.** Same as articles: Core-internal English NP detail.
5. **English does not topic-front aggressively.** Many natural Chinese sentences (那本书我看了 / 这件事我处理) need restructuring into SVO when rendered in English.

---

## 2. The "Backward Temporal Constraint" — CFLT's Tense Solution

This is the most important CFLT pedagogical mechanism for this language pair. See [`../human-learning.md`](../human-learning.md) §2.1 for the full account.

**The problem**: A Chinese L1 speaker producing CFLT-English will often say *I go to school yesterday* — correct CFLT order, wrong English tense. They forgot to inflect the verb.

**The CFLT solution**: Train the learner to treat the Time slot's *yesterday* as a **retroactive trigger** that flips the Core's verb form (*go → went*). Initially this happens consciously after the sentence is uttered; with practice, the brain pre-echoes the trigger forward and inflects the verb at production time.

**Operational rule**: After producing a CFLT-English sentence, scan the Time slot. If it contains a past deictic (*yesterday, last week, just now*), check that the Core's verb is past-tensed. If it contains a future deictic (*tomorrow, next year*), check that the Core has *will* or future periphrasis.

CFLT *predicts* this converts a **selection problem** (Chinese L1 has no tense to copy from) into a **bookkeeping rule** (check the Time slot, retro-validate the verb) — a design hypothesis to test, not a demonstrated outcome.

> **Honest scope (Lardiere caveat).** Lardiere's (1998) "Patty" case study (DOI 10.1191/026765898674105303) showed that even an advanced Chinese L1 learner produced English past-tense morphology at only ~6% — the bottleneck is *production*, not *selection*. The cited causes are (a) Mandarin phonotactic constraints (no syllable-final consonant clusters) suppressing *-ed* surface forms; (b) the "Missing Surface Inflection" challenge documented by Hawkins & Liszka (2003 *Prosodic Transfer Hypothesis*) and Goad & White (2006). CFLT *predicts* that the Backward Temporal Constraint addresses the *which-tense* selection problem (a design hypothesis, not yet validated by an intervention study); even on that hypothesis it does **not** address the *how-to-produce-the-inflection* problem. Effective Chinese→English tense pedagogy must combine CFLT's temporal scaffolding with explicit phonological and morphological training.

---

## 3. Pair-Specific Edge Cases (Chinese L1 → English L2)

### 3.1 The 是 ("be") trap

Chinese 是 = English copula *be*, but only in identity statements: 她**是**老师 ↔ She **is** a teacher. For adjectival predicates, Chinese drops 是: 她**很**漂亮 ↔ She **is** beautiful (English keeps *be*).

**Chinese L1 pitfall**: omitting *be* in English adjectival predicates (*She beautiful*).

**Fix**: In CFLT-English, State Cores headed by adjectives always carry *be*. *I'm exhausted* not *I exhausted*.

### 3.2 The aspect ↔ tense mismatch

Chinese 了 ≠ English past tense. 了 marks completion of an event; past tense marks anteriority of the event time. Three rough mappings:

| Chinese | English | Why |
|---|---|---|
| 我吃了 (eat-PERF) | I have eaten / I ate | perfective aspect; English uses present perfect or simple past depending on context |
| 我吃过 (eat-EXP) | I have eaten (before) | experiential — must use present perfect |
| 我在吃 (PROG eat) | I am eating | progressive — both languages have it |

**Rule**: When rendering Chinese 了 in CFLT-English, choose past simple if the time adverb is past-deictic (*yesterday*), choose present perfect if the time is unspecified or experiential.

### 3.3 Chinese measure words → English bare or articulated NPs

Chinese requires a measure word: 一**本**书 (one [classifier] book). English requires either an article or no determiner: *a book* / *books*. There is no clean alignment.

**Rule**: CFLT does not slot measure words / articles — these are Core-internal NP details handled by each language's grammar. Awareness is required, but it's not a CFLT-protocol issue.

### 3.4 Topic-fronted Chinese → SVO English

Chinese learners often try to preserve topic-fronting in English: *That book, I read it three times*. This is grammatical but marked in English (very informal or contrastive). Default English: *I read that book three times*.

**Rule**: When rendering CFLT-Chinese in CFLT-English, default to SVO. Use English topic-fronting only when the original Chinese carries strong contrastive focus.

### 3.5 The relative clause direction reversal

Chinese relative clauses precede the noun: 我看的那本书 (I read [REL] that book). English relative clauses follow: *the book that I read*. This is a Core-internal NP issue (CFLT does not control NP order), but worth flagging because Chinese L1 speakers often produce *I read book* + relative-clause-position errors.

**Rule**: This is pure target-language NP grammar; CFLT delegates fully. The Core slot is satisfied as long as the salience anchor (the action or identity) occupies position 0; how the Core's internal NPs are constructed is target-language business.

---

## 4. Worked Examples (zh L1 → en L2)

### Example 1

- **L1 (raw)**: *昨天我没出去，因为下雨。*
- **CFLT-Chinese**: *我没出去，因为下雨，在家，昨天。*
- **CFLT-English**: *I didn't go out, because it rained, at home, yesterday.*
- ✅ Tense check: *yesterday* triggered *did + not + go out* and *rained* (both past).

### Example 2

- **L1 (raw)**: *我每天早上在公园跑步。*
- **CFLT-Chinese**: *我跑步，在公园，每天早上。*
- **CFLT-English**: *I run, in the park, every morning.*
- Note: present habitual; no past trigger, so *run* (not *ran*).

### Example 3 — common error pattern

- **L1 (raw)**: *昨天他给我打电话。*
- **WRONG CFLT-English (Chinese L1 typical)**: *He call me, yesterday.* (missing tense)
- **CORRECT CFLT-English**: *He called me, yesterday.*

The Time slot *yesterday* must retro-validate *call → called*.

### Example 4 — copula trap

- **L1 (raw)**: *我累了，因为开会。*
- **CFLT-Chinese**: *我累了，因为开会，在办公室，刚才。*
- **WRONG CFLT-English**: *I exhausted, because of the meeting...*
- **CORRECT CFLT-English**: *I'm exhausted, because of the meeting, in the office, just now.*

State Core requires *be*.

### Example 5 — perfective aspect

- **L1 (raw)**: *我看过这本书。*
- **CFLT-Chinese**: *我看过这本书。*
- **CFLT-English**: *I have read this book.*

Chinese 过 → English present perfect.

---

## 5. Common Pitfalls Recap

| Pitfall | Frequency | Fix |
|---|---|---|
| Missing tense on English verb | Very high | Backward temporal constraint — check Time slot |
| Missing copula *be* with State Core | High | Always insert *be* for adjectival/identity predicates |
| Wrong article (a vs the vs ∅) | High | Core-internal NP grammar; not slot-related |
| Over-using topic-fronting in English | Medium | Default to SVO; topicalize only for strong contrast |
| 了 → past tense (instead of perfect) | Medium | Choose tense based on time-adverb deixis |
| Plural -s omission | Medium | Core-internal NP grammar; track countable nouns |

---

## 6. Verification Checklist

1. ☐ Core at position 0; ground frame in R-S-T order
2. ☐ English Core has explicit subject (no pro-drop)
3. ☐ Verb tense matches the Time slot's deixis (backward temporal constraint)
4. ☐ State / Copular Cores have copula *be*
5. ☐ Aspect particles 了/过/着 are NOT translated as adverbs to the Time slot — they trigger English tense/aspect on the verb
6. ☐ Articles and plural marking checked at the Core-internal NP level
