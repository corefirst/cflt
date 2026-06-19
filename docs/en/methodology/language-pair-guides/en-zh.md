# English ↔ Chinese: CFLT Operationalization

> **Version:** 1.0.0 (Internal Draft)
> **License:** [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)

> **Audience.** English-speaking learners of Mandarin Chinese (and the reverse direction at moderate scale). Largest learner population worldwide.

---

## 1. Pair-Specific Typological Notes

| Property | English | Chinese (Mandarin) |
|---|---|---|
| **Default word order** | SVO | SVO (with strong topic-prominent overlay) |
| **Tense morphology?** | Yes (-ed, -ing, will, etc.) | No (uses aspect particles 了/过/着 + time adverbs) |
| **Case marking?** | Minimal (only on pronouns: I/me, he/him) | None |
| **Topic-prominent?** | No (subject-prominent) | **Yes (strongly)** |
| **Article system?** | Yes (a/the) | None |
| **Plural marking?** | Yes (-s) | None on nouns; only animate plural with 们 |
| **Pro-drop?** | No (subjects required) | Yes (subjects often dropped) |

**Key implication for CFLT.** Both languages share SVO base order, which makes Core-internal assembly relatively portable. The major friction is that **English requires explicit subjects and tense morphology**, while Chinese encodes both via context + aspect particles. This means CFLT-Chinese can be more compact than CFLT-English; do not force English-style explicitness when rendering in Chinese.

---

## 2. Event-Nucleus Assembly Differences

The same Core "I bought a book yesterday" assembles:

- **English**: *I bought a book* — S + V (with past tense morphology) + O
- **Chinese**: *我买了一本书* — S + V + 了 (perfective) + O — same SVO order, no past tense morphology, perfective marker on verb

Both Cores are SVO; English forces tense, Chinese uses aspect. Both belong **inside Core** (verb morphology / verb-attached particle).

---

## 3. Pair-Specific Edge Cases

### 3.1 Topic-fronting in Chinese without English equivalent

Chinese allows aggressive topicalization that has no neat English equivalent: *这本书我看了三遍* (As-for-this-book, I've-read-it three times). In CFLT-Chinese, the topic can move pre-Core; in CFLT-English, the same idea uses an "as for" construction or stays in default SVO.

**Rule en→zh**: When English uses heavy contrastive focus or *"As for X..."*, render in Chinese with topic-fronting. When English is plain SVO, keep Chinese SVO.

**Rule zh→en**: A pre-Core topic in Chinese typically renders as either an English subject (if simple) or an "as for X" construction (if contrastive).

### 3.2 The Chinese 把 (bǎ) construction

The 把-construction (*我把书看完了*) is Core-internal — it foregrounds a definite patient before the verb. English has no direct equivalent; it surfaces as plain SVO with a definite article: *I finished the book*.

**Rule**: Both stay inside Core. CFLT does not require structural alignment between 把-construction and English SVO; both are valid assembly choices for the same Core slot.

### 3.3 Tense vs aspect

- English forces tense on every finite verb. This stays inside Core (verb morphology).
- Chinese uses aspect (了/过/着) — also stays inside Core. Time adverbs go to the Time slot.

**Pitfall**: When rendering English past-tense sentences in Chinese CFLT, do not add 了 if the time adverb already disambiguates. Native Chinese: *昨天我看书* (yesterday I read book) is fine without 了. Adding 了 may over-mark.

### 3.4 Chinese serial-verb / coverb constructions

*我用刀切肉* (I use knife cut meat) → coverb 用 introduces instrument inside Core. Same as English *I cut the meat with a knife* — instrument inside Core, expressed via coverb (zh) vs preposition (en). No CFLT change between languages.

### 3.5 Chinese resultative compounds

*我吃饱了* (I eat-full PERF) — verb + result complement. This is a **Core-internal** compound predicate. English typically translates as "I am full from eating" or "I ate until full" — same Core, different surface compositionality. Both stay inside Core.

---

## 4. Worked Examples

### Example 1 — basic action with cause and time

- **English raw**: *Yesterday it rained, so I stayed home and didn't go out.*
- **English CFLT**: *I didn't go out, because it rained, at home, yesterday.*
- **Chinese CFLT**: *我没出去，因为下雨，在家，昨天。*

### Example 2 — request with politeness

- **English CFLT**: *Could you please pass the salt, on the table, now?*
- **Chinese CFLT**: *请帮我递一下盐，在桌上，现在。*

Politeness markers (*please* / *请*) are bundled inside the Core (Directive type) at the CFLT teaching layer; in standard speech-act theory (Searle 1975) they operate at the *illocutionary* level rather than the propositional content level — see [`slot-disambiguation.md`](../slot-disambiguation.md) §3 entry 15 for the caveat.

### Example 3 — conditional with future

- **English CFLT**: *I will buy you coffee, if you finish the report, in the office, tomorrow.*
- **Chinese CFLT**: *我请你喝咖啡，如果你完成报告，在办公室，明天。*

Note: Chinese future is implied by 明天 + lack of past marker; no auxiliary verb needed.

### Example 4 — manner + instrument inside Core

- **English CFLT**: *I baked the cake with butter, slowly, for my mom, in the kitchen, yesterday.*
- **Chinese CFLT**: *我用黄油慢慢地为妈妈烤了一个蛋糕，在厨房里，昨天。*

All four (instrument 用黄油/with butter, manner 慢慢地/slowly, beneficiary 为妈妈/for my mom, verb+patient 烤了一个蛋糕/baked the cake) inside Core.

### Example 5 — topic structure preserved

- **English raw**: *As for that book, I read it three times.*
- **English CFLT**: *I read that book three times.* (default SVO)
- **Chinese CFLT (topic-fronted)**: *那本书，我看了三遍。* (topic-fronted, Core-internal)
- **Chinese CFLT (default SVO)**: *我看了那本书三遍。*

Both Chinese variants are valid; choose topic-fronted for emphasis matching the English "as for" construction.

---

## 5. Common Learner Pitfalls

### 5.1 English speakers learning Chinese: over-using subjects

English requires *I*, *you*, *he* in every sentence. Chinese drops them when context permits. CFLT-Chinese should follow Chinese pro-drop conventions — do not force *我* in every Core if the listener can recover the subject.

### 5.2 English speakers learning Chinese: using 是 (be) where Chinese omits it

Chinese identity statements use 是 only as a copula ("X 是 Y"); for adjectival predicates Chinese uses *X 很 Adj* (no copula). English speakers often write *她是漂亮的* (using 是 + 的) instead of *她很漂亮*. CFLT does not control this — it's pure Core-internal Chinese syntax — but be aware that the State Core in Chinese often takes 很 not 是.

### 5.3 Chinese speakers learning English: missing tense

The reverse pitfall. CFLT-English Core must carry tense morphology; rendering *I go yesterday* is ungrammatical. The Time slot's 昨天/yesterday triggers past tense on the English verb (the "backward temporal constraint"; see [`../human-learning.md`](../human-learning.md) §2.1).

### 5.4 Chinese speakers learning English: missing articles

The article system (a/the) has no Chinese equivalent. CFLT does not slot articles — they are Core-internal English noun-phrase syntax. Awareness is required, but it's not a CFLT-protocol issue.

---

## 6. Verification Checklist

1. ☐ Core at position 0; ground frame slots follow in R-S-T order
2. ☐ English Core has explicit subject and tense; Chinese Core may drop subject
3. ☐ Aspect particles (了/过/着) inside Core, not Time slot
4. ☐ Topic-fronting (Chinese) used when English context calls for "as for X"
5. ☐ 把-construction stays inside Core; not aligned mechanically with English structure
6. ☐ Article system (English) handled inside Core's NP, not as a separate slot
