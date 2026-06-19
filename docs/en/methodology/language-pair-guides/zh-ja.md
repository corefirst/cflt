# Chinese ↔ Japanese: CFLT Without the English Bridge

> **Version:** 1.0.0 (Internal Draft)
> **License:** [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)

> **Why this guide matters.** Some Chinese learners of Japanese (and vice versa) detour through English: 中文 → 英语 → 日语, a 2-hop translation. CFLT *hypothesizes* that such a detour adds layers of friction and error accumulation, and that pivoting **directly** through the protocol layer (no English required) reduces them — but the prevalence of the English detour and its comparative cost are not yet established by evidence; treat this as a motivation, not a measured result. What this guide does demonstrate is feasibility: that CFLT operates on a non-Indo-European pair without an English intermediate. The *full universality argument* — five languages, four families with reference-grammar citations — is in [`../../foundations/core-concept.md`](../../foundations/core-concept.md) §2.5. The narrower English-independence (feasibility) claim is what the zh↔ja pair actually demonstrates; an English-independence *learning advantage* remains a hypothesis to test.

---

> **See also**: [`en-ja.md`](./en-ja.md) for the English-bridged perspective on the Japanese side, and [`en-zh.md`](./en-zh.md) for the English-bridged perspective on the Chinese side.

## 1. Pair-Specific Typological Notes

| Property | Chinese (Mandarin) | Japanese |
|---|---|---|
| **Default word order** | SVO (subject–verb–object) | SOV (subject–object–verb) |
| **Head direction** | mostly head-initial (V-O, P-NP), with head-final NP modifiers | head-final throughout (O-V, NP-P, modifier-noun) |
| **Topic-prominent?** | Yes (strongly) | Yes (with explicit topic marker は) |
| **Case marking?** | None (relies on word order + coverbs) | Rich (が ga, を o, に ni, で de, と to, から kara, へ e) |
| **Tense morphology?** | None (relies on aspect particles 了, 过, 着 + time adverbs) | Rich (-た past, -る non-past, -ている progressive) |
| **Pro-drop?** | Yes (subject often omitted) | Yes (subject often omitted, sometimes object too) |

**Key implication for CFLT.** The two languages share *topic-prominence* (a major facilitating overlap) but diverge sharply in *event-nucleus assembly* (verb-final vs verb-medial, case-marked vs case-less). The CFLT protocol layer (Core-first, R-S-T) is identical for both; the event nucleus is built using each language's own machinery; where a slot filler is hard to map directly, CFLT proposes paraphrasing its meaning through a controlled semantic metalanguage inspired by NSM (Wierzbicka 1996) — NSM-style explication, not token-by-token translation (NSM primes are meanings, not directly substitutable tokens).

---

## 2. Event-Nucleus Assembly Differences

The same Core "I bought a book with money for my mom" assembles differently:

### Chinese assembly
- Word order: Subject–coverb–instrument–benefactive coverb–beneficiary–verb–object
- *我用钱为妈妈买了一本书*
  - 我 (S) — 用 (coverb: with) — 钱 (instrument) — 为 (coverb: for) — 妈妈 (beneficiary) — 买 (V) — 了 (perfective) — 一本书 (O)

### Japanese assembly
- Word order: Subject–instrument-で–beneficiary-に–object-を–verb
- *私はお金で母に本を買った*
  - 私 (S) — は (topic) — お金 (instrument) — で (case: instrument) — 母 (beneficiary) — に (case: dative) — 本 (O) — を (case: accusative) — 買った (V + past)

**What CFLT prescribes**: both nuclei occupy slot 0 as a single salience unit. The internal arrangement (coverbs in Chinese, postpositional case in Japanese) is **not CFLT's business** — each language's hardware handles it.

**What CFLT does prescribe**: after the nucleus closes, the ground frame slots (Reason, Space, Time) follow in canonical order, attached using each language's native subordinator/particle.

---

## 3. Pair-Specific Edge Cases

These are the boundary calls that go differently in the zh-ja pair than the project-standard defaults in `slot-disambiguation.md`.

> **Scope note.** The 把 construction, は/が, topic, contrast, grammatical subject, and focus are **context-dependent correspondences, not direct equivalents**. wa/ga selection in particular involves complex interactions among topic, contrast, focus, exhaustiveness, prosody, and clause type (Kuno 1973; Kuroda 2005; Heycock 2008), so a 把-patient, a topic, or a focused subject does not map onto a single Japanese or Chinese form by rule. Read the arrows below as default starting hypotheses to confirm against context and native-speaker judgment, not deterministic mappings.

### 3.1 Chinese 把 (bǎ) construction → Japanese topicalization

The Chinese **把** construction fronts a definite object before the verb: *我把书买了*. Surface order: S-把-O-V. Functionally, this foregrounds the *patient* relative to the action. This is **inside Core** in CFLT terms — it's part of how the event nucleus is built in Chinese.

The functional Japanese equivalent often uses topic marking: *本は私が買った* (literally "the book, I bought"). Same Core-internal foregrounding, achieved with は marker.

**Default for zh→ja** (context-dependent, confirm against context): If the Chinese 把-construction patient is the topical/given referent, は is often the natural rendering in Japanese; if it's contrastive focus, が or the default を-marked object may fit better. These are tendencies, not a one-to-one rule.

### 3.2 Japanese は (topic) vs が (subject) → Chinese topicalization vs SVO

Japanese systematically distinguishes topic (は) from grammatical subject (が). Chinese has no morphological mark for this distinction — it relies on word order (topicalized referents move to clause-initial position).

- 日: *この本は私が読んだ* (As for this book, I read it)
- 中: *这本书我读了* (literal topic-fronting)
- 中: *我读了这本书* (default SVO; less topical)

**Default for ja→zh** (context-dependent, confirm against context): は-marked subjects often render as Chinese topic-fronted forms (frequently pre-Core); が-marked subjects often render in default SVO position. These are tendencies, not equivalences — selection still depends on topic/contrast/focus in context. **Caution**: do not blindly translate は as 是 (the copula) — they are unrelated.

### 3.3 Chinese 因为/所以 vs Japanese から/ので/から (Reason slot)

Chinese typically marks the reason explicitly with 因为 X, 所以 Y or postposed 因为 X. Japanese has multiple reason particles (から causal, ので explanatory, ため purpose). The CFLT [Reason] slot accommodates all of them, but the choice of particle in Japanese carries pragmatic weight.

- 中: *我没出去, 因为下雨, 在家, 昨天* (CFLT form)
- 日: *出かけなかった、雨が降ったから、家で、昨日* (CFLT form)

**Rule**: when rendering a Chinese 因为-clause in Japanese CFLT, choose から for raw causal reasoning, ので when the listener should accept the cause as given, ため when it's purposive.

### 3.4 Time and aspect: 了/过/着 ↔ -た/-ている/-てある

Chinese uses **aspect particles** (no tense morphology). Japanese uses **tense + aspect morphology** on the verb. Both belong **inside Core** (attached to the predicate), not the Time slot. The Time slot carries adverbial time references only.

- 中: *昨天* + V + *了* (yesterday + verb + perfective)
- 日: V + *-た* + *昨日* (verb-past + yesterday)

**Rule**: aspect/tense markers stay inside Core (on the verb); deictic time words go in the Time slot.

### 3.5 No subject? No problem — but track who's missing

Both languages drop subjects freely. CFLT does not penalize pro-drop: if the subject is recoverable from context, the Core can start with the predicate.

- 中: *买了书* (bought-PERF book)
- 日: *本を買った* (book-ACC bought)
- Both still satisfy "Core is the salience anchor" — the predicate carries the salience even without explicit subject.

---

## 4. Worked Examples (No English)

### Example 1 — simple action with reason

**Chinese (default conversational):** *昨天下雨，我没出去。*

**Step 1 — Identify Core (substitution test)**: 我没出去 (I didn't go out) is the salient event. 下雨 is the cause.

**Step 2 — CFLT decomposition (language-neutral)**:
- Core: 我没出去 / 出かけなかった
- Reason: 因为下雨 / 雨が降ったから
- Space: 在家 / 家で
- Time: 昨天 / 昨日

**Step 3 — Render in Chinese CFLT**: *我没出去，因为下雨，在家，昨天。*

**Step 4 — Render in Japanese CFLT**: *出かけなかった、雨が降ったから、家で、昨日。*

No English at any step.

### Example 2 — request with politeness layer

**Chinese:** *现在能在桌上帮我递一下盐吗？*

**CFLT decomposition**:
- Core (Directive): 帮我递一下盐 / 塩を渡してくれ
- Politeness: 能…吗 / -てくれませんか
- Space: 在桌上 / テーブルの上で
- Time: 现在 / 今

**Chinese CFLT**: *请帮我递一下盐，在桌上，现在。*

**Japanese CFLT**: *塩を渡してくれませんか、テーブルの上で、今。*

The politeness markers (能…吗 in Chinese, -てくれませんか in Japanese) attach inside Core (Directive type). They are not a separate slot.

### Example 3 — identity statement with description

**Chinese:** *那个穿红衣服的女孩是我妹妹。*

**CFLT decomposition**:
- Core (Copular): 那个女孩是我妹妹 / あの女の子は私の妹だ
- Description (inside Core, manner-like): 穿着红衣服 / 赤い服を着ている
- Space: 在照片里 / 写真の中で
- Time: 去年夏天 / 去年の夏

**Chinese CFLT**: *那个女孩是我妹妹，穿着红衣服，在照片里，去年夏天。*

**Japanese CFLT**: *あの女の子は私の妹だ、赤い服を着て、写真の中で、去年の夏。*

The description "wearing a red dress" in both languages stays inside Core as a participial modifier of the identity claim.

### Example 4 — instrument + manner + beneficiary all inside Core

**Chinese:** *他用筷子在厨房里慢慢地为妈妈做了一道菜，昨天，因为是她生日。*

**CFLT decomposition**:
- Core (Event, fully assembled): 他用筷子慢慢地为妈妈做了一道菜 / 彼は箸でゆっくり母のために料理を作った
- Reason: 因为是她生日 / 母の誕生日だったから
- Space: 在厨房里 / 台所で
- Time: 昨天 / 昨日

**Chinese CFLT**: *他用筷子慢慢地为妈妈做了一道菜，因为是她生日，在厨房里，昨天。*

**Japanese CFLT**: *彼は箸でゆっくり母のために料理を作った、母の誕生日だったから、台所で、昨日。*

All four "inside Core" elements (instrument 用筷子/箸で, manner 慢慢/ゆっくり, beneficiary 为妈妈/母のために, action+aspect 做了/作った) live in Core. Three ground-frame slots follow in canonical order.

### Example 5 — conditional core (CFLT-Complex)

**Chinese:** *如果你完成报告，我明天就在办公室请你喝咖啡。*

**CFLT decomposition**:
- Core (Event): 我请你喝咖啡 / コーヒーをおごる
- Reason (condition): 如果你完成报告 / 報告書を仕上げたら
- Space: 在办公室 / オフィスで
- Time: 明天 / 明日

**Chinese CFLT**: *我请你喝咖啡，如果你完成报告，在办公室，明天。*

**Japanese CFLT**: *コーヒーをおごる、報告書を仕上げたら、オフィスで、明日。*

The condition (functional WHY-class) sits in [Reason] slot in both languages, marked by 如果/たら/ば.

---

## 5. Common Learner Pitfalls

### 5.1 Chinese learner of Japanese: forgetting verb-final discipline

A Chinese learner producing CFLT-Japanese sometimes leaves Chinese SVO order intact and just appends は/が/を after each Chinese word. Result: ungrammatical Japanese.

**Diagnosis**: The CFLT protocol is satisfied (Core slot at position 0), but the **internal assembly** of Core is wrong — Japanese requires verb-final inside Core. CFLT does not override that requirement.

**Fix**: Always check that the Core's internal verb is at the end of the Core block before applying the ground frame. CFLT only governs the boundary between Core and the ground frame, not the internal order.

### 5.2 Japanese learner of Chinese: keeping は/が awareness when Chinese drops it

Japanese learners producing CFLT-Chinese sometimes try to preserve は/が distinction by inserting 是 ("is") or by overusing topic-fronting. Result: 中文 sounds stilted.

**Fix**: When the Japanese sentence has は (topic), front the topic in Chinese (move it before the Core). When it has が (subject focus or new info), keep default SVO order. Never use 是 to mark topic.

### 5.3 Both directions: forcing one ground-frame slot when the source language combines them

Japanese で can mark instrument *or* location depending on context; Chinese 在 marks location while 用 marks instrument. A Japanese で can correspond to Chinese 在 (Space) or 用 (inside Core, instrument). Translating mechanically loses the slot distinction.

**Diagnosis**: This is exactly the kind of edge case the universal decision tree handles correctly (substitution test: change the で-NP — does the event change? If yes → instrument, inside Core; if no → location, Space slot).

**Fix**: Run the decision tree from `slot-disambiguation.md` §2 even when both source and target are non-English. The tree is language-agnostic.

### 5.4 Aspect markers leaking into the Time slot

A common mistake: putting the perfective 了 / -た in the Time slot. They are not adverbial time references — they're verb morphology, attached to the predicate inside Core.

**Rule**: 了, 过, 着, -た, -ている, -ていた all stay inside Core. The Time slot carries 昨天 / 今 / 来年 type adverbials only.

---

## 6. Verification Checklist

For any zh→ja or ja→zh CFLT rendering, verify:

1. ☐ Core at position 0 contains the salient predicate + valence + manner (substitution test passes)
2. ☐ Internal Core order respects the target language's syntax (verb-final for Japanese, verb-medial for Chinese)
3. ☐ Particles/coverbs/case markers are correctly applied within Core
4. ☐ Ground frame follows in canonical order: Reason → Space → Time
5. ☐ Aspect/tense markers are inside Core, not in the Time slot
6. ☐ Topic structure (は/topic-fronting) is preserved across languages where present
7. ☐ Politeness layer is intact (especially for Japanese, where omission can be impolite)

If all 7 pass, the CFLT rendering is correct in this language pair — and importantly, you got there **without translating through English at any step**.

---

## 7. Open Issues for This Pair

1. **Honorific morphology in Japanese** is heavy and pervades the entire utterance. CFLT does not slot it; it's a layer orthogonal to the four slots (see [`../../foundations/sociolinguistics.md`](../../foundations/sociolinguistics.md)).
2. **Discourse particles** (Chinese 吧/呢/啊, Japanese ね/よ/か) are utterance-level and don't fit any slot. Both languages use them heavily; CFLT-rendered output should append them at the utterance boundary, not inside any slot.
3. **Classifiers / counters** (Chinese 一**本**书, Japanese 本一**冊**) are part of NP-internal syntax, fully delegated to language-native machinery; CFLT does not address them.
