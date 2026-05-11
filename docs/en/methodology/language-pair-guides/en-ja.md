# English ↔ Japanese: CFLT Operationalization

> **Version:** 1.0.0 (Internal Draft)
> **License:** [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)

> **Audience.** English-speaking learners of Japanese, and Japanese-speaking learners of English. The classic SVO ↔ SOV typological contrast.

---

> **See also**: [`zh-ja.md`](./zh-ja.md) for the no-English-bridge Chinese↔Japanese perspective, and [`zh-en.md`](./zh-en.md) for the Chinese L1 → English L2 perspective.

## 1. Pair-Specific Typological Notes

| Property | English | Japanese |
|---|---|---|
| **Default word order** | SVO | SOV |
| **Head direction** | head-initial (V before O, P before NP) | head-final (O before V, NP before P) |
| **Case marking?** | Minimal (only on pronouns) | Rich (が, を, に, で, と, から, へ) |
| **Tense morphology?** | Yes | Yes |
| **Topic-prominent?** | Weak | Strong (with explicit は marker) |
| **Pro-drop?** | No | Yes |
| **Honorific system?** | None | Pervasive (敬語: respectful, humble, polite forms) |

**Key implication for CFLT.** This pair maximally stresses the two-tier model: the protocol layer is identical for both languages, but the event-nucleus internal assembly is **inverted** (SVO vs SOV). Without CFLT's two-tier separation, learners conflate these layers and either keep English SVO inside Japanese sentences (ungrammatical) or struggle to organize discourse before the verb arrives.

CFLT's contribution: separating "what comes after Core" (universal R-S-T order) from "how Core is internally structured" (Japanese SOV with case marking) makes this pair learnable in a way that pure imitation cannot.

---

## 2. Event-Nucleus Assembly: Maximum Divergence

The same Core "I bought a book at the bookstore yesterday" assembles:

- **English**: *I bought a book* — S V O (SVO, head-initial)
- **Japanese**: *私は本を買った* — S は O を V (SOV, head-final, case-marked)

These are **maximum-typological-divergence Cores** — every structural property is mirrored. CFLT does not align them; each language assembles its own Core natively.

**What CFLT does**: place that whole Core block at slot 0, then apply the universal R-S-T frame.

---

## 3. Pair-Specific Edge Cases

### 3.1 Verb-final discipline (English L1 → Japanese L2)

The hardest hurdle: English speakers must hold the verb in working memory while uttering all the modifiers, since Japanese verbs come last.

**CFLT mitigation**: Although the Japanese Core ends with the verb, the Core block itself still occupies slot 0. The English speaker plans the Core mentally first (using English verb-medial intuition), then verbalizes it in Japanese SOV order. The R-S-T ground frame follows in canonical order regardless.

**Concrete drill**:
1. Mentally select the Core action (e.g., "buy the book")
2. Build the Japanese Core: 本を買う (book + を + buy)
3. Append politeness/aspect: 本を買いました
4. Apply ground frame: 本を買いました、本屋で、昨日 (Core, Space, Time)

### 3.2 は (topic) vs が (subject)

> **Pedagogical simplification notice.** Kuno (1973) distinguishes *thematic* vs *contrastive* uses of は, and *neutral-description* vs *exhaustive-listing* uses of が — four distinct functions, not two. Heycock (2008) and Kuroda (2005) further document edge cases (embedded clauses cannot host thematic-は; contrastive-は has falling intonation; etc.). The five rules below cover the dominant **thematic-は ↔ exhaustive-が** mapping for the unmarked default and are sufficient for most CFLT teaching contexts; they do not handle all four uses. For mature mastery, see Kuno 1973 (Ch. 2), Heycock 2008 (Oxford Handbook of Japanese Linguistics), Kuroda 2005 (J. East Asian Linguistics 14:1–58).

Japanese distinguishes topic-marked subject (は) from focus-marked subject (が). English has no morphological mark for this; it surfaces via word order, contrastive stress, or lexical choice (*as for X*).

**Rule en→ja**:
- Default English subjects → Japanese は (when establishing topic) or が (when introducing new info)
- English contrastive stress on subject → Japanese は with falling intonation, or が emphatic
- "As for X..." → topic-fronted X-は

**Rule ja→en**:
- は → English default subject in SVO; if contrastive, may add "as for"
- が in non-emphatic context → default English subject
- が in focus context (e.g., 私が書いた "It is I who wrote it") → cleft sentence in English

### 3.3 Japanese aspect: -ている, -てある, -ておく

Japanese has rich verbal periphrasis encoding aspect/result/preparation. These all stay **inside Core** (verb morphology), not in any ground-frame slot.

| Japanese | Function | English equivalent |
|---|---|---|
| -ている | progressive or stative resultant | *is V-ing* or *has V-ed* (depending on verb class) |
| -てある | resultant from intentional action | *has been V-ed* |
| -ておく | preparatory action | *V in advance* |
| -てしまう | completion / regret | *finish V-ing* / *unfortunately V* |

**Rule**: keep these Core-internal in both languages; do not let them leak into the Time slot.

### 3.4 Honorifics (敬語) — partially dissociable from CFLT

Japanese honorifics modify the entire utterance morphologically. English has no direct equivalent; politeness is achieved lexically (*could you*, *would you mind*) or modally.

**Rule**: Honorifics are **partially dissociable** from the four-slot protocol — they do not change Core or ground-frame *assignments*, but neuroimaging shows Japanese-honorific processing engages the left IFG (Momo, Sakai & Sakai 2008, *Brain and Language* 107(1), 81–89) and, in socio-pragmatic agreement contexts, additionally recruits bilateral insula and dorsal medial prefrontal cortex when the addressee status varies (Cui, Jeong, Okamoto, Takahashi, Kawashima & Sugiura 2022, *Journal of Neurolinguistics* 62, 101041). The CFLT teaching guidance — apply slot work first, honorific layer second — is therefore valid as a *cognitive workflow* but should not be over-claimed as full neural independence; the social-cognitive network recruitment is sensitive to addressee status as well as form. See [`../../foundations/sociolinguistics.md`](../../foundations/sociolinguistics.md) for the full discussion.


For learners: keep CFLT slot work and honorific work as separate cognitive tasks. CFLT structure first, honorific layer second.

### 3.5 Particles で, に, と — multiple slot candidates

A single Japanese particle can map to multiple CFLT slots:

| Particle | Possible CFLT location | Disambiguation |
|---|---|---|
| で (instrument) | inside Core | *ペンで書く* — instrument |
| で (location of action) | Slot 2 [Space] | *公園で会う* — location |
| に (recipient/dative) | inside Core (beneficiary) | *母にあげる* — recipient |
| に (location of existence) | Slot 2 [Space] | *京都に住む* — location |
| に (time point) | Slot 3 [Time] | *3時に来る* — time |
| と (accompaniment) | inside Core | *友達と行く* — accompaniment |
| と (quotation marker) | not a slot — Core-internal | *「来る」と言った* |

**Rule**: Apply the universal substitution test (`slot-disambiguation.md` §2). The particle does not determine the slot; the **functional question** answered does.

### 3.6 No subject? Track who's missing

Japanese drops subjects freely; English does not. CFLT-English Core needs explicit subjects; CFLT-Japanese Core may omit them.

**Rule en→ja**: It's safe to drop English subject pronouns when rendering CFLT-Japanese, as long as context recovers them.

**Rule ja→en**: Subjects must be reconstructed for CFLT-English. Default to *I* for first-person diary-like contexts; otherwise use discourse context.

---

## 4. Worked Examples

### Example 1 — basic action

- **English CFLT**: *I didn't go out, because it rained, at home, yesterday.*
- **Japanese CFLT**: *出かけなかった、雨が降ったから、家で、昨日。*

Note: Japanese drops "I" (pro-drop); English doesn't.

### Example 2 — request with politeness

- **English CFLT**: *Could you please pass the salt, on the table, now?*
- **Japanese CFLT (polite)**: *塩を渡してくれませんか、テーブルの上で、今。*
- **Japanese CFLT (humble polite)**: *塩を渡していただけませんか、テーブルの上で、今。*

The English politeness layer (*could you ... please*) maps to multiple Japanese honorific options; CFLT does not slot them.

### Example 3 — instrument inside Core

- **English CFLT**: *I cut the meat with a knife, in the kitchen, just now.*
- **Japanese CFLT**: *ナイフで肉を切った、台所で、さっき。*

Instrument *with a knife* / *ナイフで* stays inside Core in both languages, despite radically different syntax.

### Example 4 — full Core with all valence

- **English CFLT**: *I baked the cake with butter, slowly, for my mom, in the kitchen, yesterday.*
- **Japanese CFLT**: *母のためにバターでゆっくりケーキを焼いた、台所で、昨日。*

Note: Japanese arranges beneficiary-に → instrument-で → manner → object-を → verb (all SOV-internal); English arranges S-V-O + instrument + manner + beneficiary (all SVO-internal). Both occupy Core slot 0; both are followed by Space + Time. The Japanese example here also drops Reason ("because it was her birthday"); for the 4-slot version with Reason included, see [`slot-disambiguation.md`](../slot-disambiguation.md) §5.2.

### Example 5 — identity + description

- **English CFLT**: *That girl is my sister, wearing a red dress, in the photo, from last summer.*
- **Japanese CFLT**: *あの女の子は私の妹だ、赤い服を着て、写真の中で、去年の夏。*

The は-marked subject *あの女の子* mirrors English *that girl* topic.

---

## 5. Common Learner Pitfalls

### 5.1 English speakers learning Japanese

- **Forgetting verb-final**: producing *I bought yesterday a book* SOV-fragmented Japanese
- **Misusing は vs が**: applying は to grammatical subjects without topic context
- **Over-explicit subjects**: not dropping pronouns when context permits
- **Honorific level mismatch**: applying CFLT correctly but using wrong honorific level for the social context

### 5.2 Japanese speakers learning English

- **SOV bleeding into English**: producing *I yesterday book bought* by literal slot translation
- **Missing tense**: similar to Chinese L1 → English (use the backward temporal constraint)
- **Missing articles**: no Japanese equivalent
- **Direct は → "is"**: confusing topic marker with copula
- **Missing subject**: leaving the English Core subject-less

---

## 6. Verification Checklist

1. ☐ Core at position 0; ground frame in R-S-T order
2. ☐ English Core: SVO + tense; Japanese Core: SOV + case marking + verb-final
3. ☐ Aspect/tense morphology stays inside Core (not in Time slot)
4. ☐ は/が usage matches topic vs focus distinction (when going en→ja)
5. ☐ Subjects reconstructed for English; allowed to drop for Japanese
6. ☐ Honorifics applied as partially-dissociable layer; do not affect slot assignments
7. ☐ で / に / と particle-to-slot mapping verified by substitution test, not particle identity

---

## 7. Open Issues for This Pair

1. **Japanese sentence-final particles** (ね, よ, か, わ, ぞ) — utterance-level, do not fit any slot
2. **Honorific cascading** — when using 敬語 throughout, every verb in every CFLT block must be marked; this is heavy cognitive load orthogonal to CFLT
3. **Quotation in Japanese** uses と as a quotative — quoted material may itself form a nested CFLT block; see [`../complex-structures.md`](../complex-structures.md)
