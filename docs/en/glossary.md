# Glossary & Acronym Index

> **Version:** 1.0.0 (Internal Draft)
> **Author:** CFLT Core Team
> **Organization:** [CFLT.center](https://cflt.center)
> **License:** [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)

> **Purpose:** A single-point reference for every acronym, technical term, and proper-name shorthand used across the CFLT documentation. When you encounter an unfamiliar abbreviation, look it up here first; cross-references point to the canonical foundations doc for deeper treatment.

---

## 1. CFLT Project Terminology

| Term | Expansion | Definition |
|---|---|---|
| **CFLT** | Core-First Language Theory | The umbrella name for the framework — both the academic theory and the operational protocol. See [`manifesto.md`](./manifesto.md). |
| **CFLT Protocol** | Core-First Language Protocol | The specific operational sequencing rule: `[Core] → [Reason] → [Space] → [Time]`. |
| **CFLT Form** | Core-First Language Form | Output produced under the CFLT Protocol — comprehensible (not yet idiomatic) target-language utterance. |
| **CFLT-L2** | Core-First Language Form in L2 | The CFLT Form rendered in the learner's L2 (target language). |
| **Event Nucleus** | Nucleus of the Event (Structural) | The Core slot's internal structure: predicate + valence-bound participants + manner. See [`foundations/core-concept.md`](./foundations/core-concept.md) §2.1. |
| **Ground Frame** | Circumstantial Ground Frame | The three circumstantial slots (Reason / Space / Time) that frame the event. |
| **Grammar Overlay** | Post-CFLT Idiomatic Layer | The post-CFLT polish layer that converts a CFLT Form into idiomatic L2. |
| **Salience anchor** | Cognitive Salience Anchor | The cognitive object that occupies position 0; what the speaker is "committing to." See [`foundations/core-concept.md`](./foundations/core-concept.md) §1. |
| **L1 / L2** | First / Second Language | L1 = the learner's native language; L2 = the target language being learned. **Both are learner-relative, not English-relative** — for a Chinese-speaking learner of Japanese, L1 = Chinese and L2 = Japanese; English is not in the pair. CFLT supports any-to-any language pairs without requiring English as an intermediate. See [`foundations/core-concept.md`](./foundations/core-concept.md) §2.3 for layer-by-layer universality. |

### Related projects (independent of CFLT itself)

| Term | Status | Definition |
|---|---|---|
| **CoreFirst** ([corefirst.world](https://corefirst.world)) | Official reference experimental project | Next.js application implementing the CFLT Protocol for Pillar I (human bilingual education). Maintained by an organization separate from the CFLT specification body. Other implementations are welcome — see [`reference-implementations.md`](./reference-implementations.md). |
| **apcore** ([github.com/aiperceivable/apcore](https://github.com/aiperceivable/apcore)) | Independent toolchain | Open-source library suite (apcore-mcp, apcore-cli, apcore-sdk, etc.) some teams may use to integrate CFLT into AI assistants, batch-process corpora, or synchronize learning state. **Independent of CFLT** — neither a dependency nor a deliverable. |

### CFLT-defined evaluation metrics

| Term | Expansion | Definition |
|---|---|---|
| **AOL** | Articulation Onset Latency | Time from intent formation to first uttered word. See [`methodology/evaluation-metrics.md`](./methodology/evaluation-metrics.md) §2. |
| **CLI** | Cognitive Load Index | Composite metric for working-memory burden during L2 production. |
| **IPS** | Intent Preservation Score | LLM stability metric — fraction of generations that preserve user intent under prompt variation. |
| **HR** | Hallucination Rate | LLM stability metric — fraction of generations that contradict given context. |

---

## 2. Word-Order Typology

> **S = Subject, V = Verb, O = Object.** These letters describe the default surface order of these three constituents in a transitive declarative clause. See [`foundations/linguistics.md`](./foundations/linguistics.md) §1.1.

| Term | Definition | Example languages |
|---|---|---|
| **SOV** | Subject–Object–Verb | Japanese, Korean, Turkish, Hindi (~45% of world languages) |
| **SVO** | Subject–Verb–Object | English, Mandarin, Spanish, Russian (~42%) |
| **VSO** | Verb–Subject–Object | Welsh, Classical Arabic, Tagalog (~9%) |
| **VOS** | Verb–Object–Subject | Malagasy, some Mayan languages (rare) |
| **OVS** | Object–Verb–Subject | Hixkaryana (very rare) |
| **OSV** | Object–Subject–Verb | Warao, Yoda's English (very rare) |
| **V2** | Verb-Second | The finite verb is always in the second position of a main clause. German, Dutch, Yiddish. |
| **head-final** | Head-Final Construction | Modifier precedes head (e.g., adjective-noun in English: "*red* car"); typical of SOV languages. |
| **head-initial** | Head-Initial Construction | Head precedes modifier (e.g., noun-adjective in French: "voiture *rouge*"); typical of SVO and VSO languages. |
| **topic-prominent** | Topic-Prominent Typology | The clause is structured around topic-comment rather than subject-predicate. Mandarin, Japanese, Korean. (Li & Thompson 1976) |

---

## 3. Linguistic Concepts and Frameworks

| Term | Expansion | Definition |
|---|---|---|
| **UG** | Universal Grammar | Chomsky's hypothesis that humans share an innate language faculty. |
| **LAD** | Language Acquisition Device | The hypothetical innate cognitive module supporting language learning (Chomsky). |
| **NSM** | Natural Semantic Metalanguage | Wierzbicka's set of ~65 universal semantic primes (e.g., I, YOU, THIS, GOOD, BIG, BECAUSE) that all languages can express. |
| **EIC** | Early Immediate Constituents | Hawkins' (1994) parsing efficiency principle: comprehenders prefer constructions where major constituents are recognized as early as possible. |
| **CRD** | Constituent Recognition Domain | The span of words required to identify all immediate constituents of a phrase (Hawkins 1994). |
| **UID** | Uniform Information Density | Hypothesis (Levy & Jaeger 2007) that speakers spread information evenly across a sentence to avoid local processing spikes. |
| **CCG** | Combinatory Categorial Grammar | Steedman's (2000) lexicalist grammar formalism where syntactic categories are types and combination is type composition. |
| **DRT** | Discourse Representation Theory | Kamp's (1981) model of how listeners build a mental representation of unfolding discourse. |
| **SFL** | Systemic Functional Linguistics | Halliday's grammar tradition organized around meaning-making functions (ideational/interpersonal/textual). |
| **CD** | Communicative Dynamism | Prague School concept: degree of "newness" or informational push carried by each clause element (Firbas 1992). |
| **IPA** | International Phonetic Alphabet | The standardized phonetic notation used to represent sounds across languages. |
| **Figure-Ground** | Figure-Ground Perception | Talmy's (2000) cognitive distinction: Figure is the salient/foregrounded entity; Ground is the reference frame. |
| **profile/base** | Profile and Base (Cognitive) | Langacker's (1987) cognitive grammar pair: the *profile* is the entity foregrounded by an expression against its conceptual *base*. |
| **Theme/Rheme** | Theme and Rheme (Functional) | Prague School information structure: Theme is what the message is about; Rheme is what is said about the Theme. |
| **Topic-Comment** | Topic and Comment (Information Structure) | Like Theme/Rheme but specifically applied to topic-prominent languages (Li & Thompson 1976). |
| **illocutionary act** | Illocutionary Act (Speech Act) | Searle's term for what a speaker *does* by uttering — assert, request, promise, etc. |
| **speech act** | Speech Act Theory | Synonym for illocutionary act (Austin, Searle). |

---

## 4. Pedagogy and Second-Language Acquisition

| Term | Expansion | Definition |
|---|---|---|
| **SLA** | Second Language Acquisition | The field studying how non-native languages are learned. |
| **TBLT** | Task-Based Language Teaching | Pedagogical approach using meaningful tasks as the unit of instruction (Long, Ellis, Skehan). |
| **ZPD** | Zone of Proximal Development | Vygotsky's (1978) zone between what a learner can do alone and what they cannot do even with help. |
| ***i+1*** | Input Hypothesis (Krashen) | Krashen's notation for input slightly above the learner's current level *i*. |
| **Affective Filter** | Affective Filter Hypothesis (Krashen) | Krashen's hypothesized emotional barrier (anxiety, low motivation) that blocks input from reaching the LAD. |
| **Monitor Model** | Monitor Model of L2 Acquisition | Krashen's (1982) five-hypothesis model of L2 acquisition: Acquisition-Learning, Monitor, Natural Order, Input, Affective Filter. |
| **Skill Acquisition Theory** | Skill Acquisition Theory (SAT) | DeKeyser's account of L2 mastery as moving from declarative → procedural → automatic knowledge. |
| **Cognitive Load Theory** | Cognitive Load Theory (CLT) | Sweller's (1988, 2011) framework distinguishing intrinsic / extraneous / germane load on working memory. |

---

## 5. Neuroscience

| Term | Expansion | Definition |
|---|---|---|
| **PFC** | Prefrontal Cortex | The brain's "executive control" region; bottlenecks adult L2 production. |
| **DLPFC** | Dorsolateral Prefrontal Cortex | A specific PFC subregion involved in working memory and conflict monitoring. |
| **BG** | Basal Ganglia | Subcortical structures supporting procedural / automatic skill execution. |
| **SN** | Salience Network | A brain network anchored in anterior insula and dACC that detects and prioritizes salient stimuli. |
| **DMN** | Default Mode Network | A brain network active during internally-directed thought (mind-wandering, autobiographical recall). |
| **CEN** | Central Executive Network | A brain network (a.k.a. fronto-parietal control network) supporting goal-directed task focus. |
| **dACC** | Dorsal Anterior Cingulate Cortex | A region central to conflict monitoring and salience detection (part of the SN). |
| **AI** *(in neuroscience)* | Anterior Insula (Neuroscience) | A brain region integrating interoceptive and salience signals (part of the SN). **Not** Artificial Intelligence in this context. |
| **LIFG** | Left Inferior Frontal Gyrus | A region (encompassing Broca's area) central to syntactic processing. |
| **BA** | Brodmann Area | The classical numbered regions of the cerebral cortex (e.g., BA 44, BA 45 = Broca's area). |
| **WM** | Working Memory | Short-term active memory used during cognitive tasks (Baddeley; Cowan). |
| **ERP** | Event-Related Potential | Electrophysiological signal time-locked to a stimulus, measured via EEG. |
| **P600** | Syntactic P600 ERP Component | A specific ERP component peaking ~600 ms after a stimulus, associated with syntactic reanalysis. |

---

## 6. Mathematics and Information Theory

| Term | Expansion | Definition |
|---|---|---|
| **KL divergence** | Kullback-Leibler divergence | An asymmetric measure of difference between two probability distributions. |
| **DAG** | Directed Acyclic Graph | A graph with directed edges and no cycles; used here for semantic structures. |
| **conditional entropy** | $H(Y \mid X)$ | Uncertainty about $Y$ given knowledge of $X$. |
| **Markov chain** | Markov Chain Model | A stochastic process where the next state depends only on the current state. |
| **σ function** | Linearization Sigma Function | The linearization function that maps a semantic graph to a surface order. See [`foundations/mathematics.md`](./foundations/mathematics.md) §1. |

---

## 7. Large Language Models and NLP

| Term | Expansion | Definition |
|---|---|---|
| **LLM** | Large Language Model | A neural network (typically Transformer-based) with billions of parameters trained on text. |
| **NLP** | Natural Language Processing | The field of computational language understanding and generation. |
| **AI** *(in computing)* | Artificial Intelligence | The general field of machine intelligence. (See §5 for the neuroscience meaning of "AI" = Anterior Insula.) |
| **NLU / NLG** | Natural Language Understanding / Generation | Sub-fields of NLP. |
| **GPT** | Generative Pre-trained Transformer | OpenAI's family of autoregressive LLMs. |
| **BERT** | Bidirectional Encoder Representations from Transformers | Google's encoder-only LLM (2018). |
| **MLM** | Masked Language Modeling | Pre-training objective used by BERT (predict masked tokens). |
| **ICL** | In-Context Learning | The ability of LLMs to learn a task from examples placed in the prompt without parameter updates. |
| **RAG** | Retrieval-Augmented Generation | Workflow where an LLM is given retrieved documents as context (Lewis et al. 2020). |
| **Attention Sink** | Attention Sink Mechanism | Phenomenon where initial tokens accumulate disproportionate attention weight (Xiao et al. 2024); fundamental to CFLT's Core-first claim at the LLM level. |
| **Lost-in-the-Middle** | Lost-in-the-Middle Phenomenon | U-shaped accuracy curve in long-context tasks: information at start and end is recovered better than information in the middle (Liu et al. 2023). |
| **Prefix caching** | Prompt Prefix Caching | LLM inference optimization: reusing computation for shared prompt prefixes (vLLM APC, SGLang RadixAttention). |
| **APC** | Automatic Prefix Caching | vLLM's prefix-caching mechanism. |
| **TTFT** | Time To First Token | Latency metric: time from request submission to first generated token. |
| **KV cache** | Key-Value cache | The Transformer attention key/value tensors stored across decoding steps; main target of prefix caching. |
| **TTS** | Text-to-Speech | The synthesis of speech audio from text input. |

### Benchmarks and Conferences (occasional references)

| Term | Definition |
|---|---|
| **MMLU** | Massive Multitask Language Understanding — broad LLM evaluation benchmark (Hendrycks et al. 2021). |
| **TOON** | Token-Optimized Object Notation — a lightweight prompt-encoding format. |
| **DOVE** | Diverse Optimization for the Verbalization Effect — study on prompt-linearization sensitivity (ACL Findings 2025). |
| **ACL** / **NAACL** / **EMNLP** | Major NLP conferences (Association for Computational Linguistics; North American chapter; Empirical Methods in NLP). |
| **ICLR** / **NeurIPS** | Major ML conferences (Int'l Conf. on Learning Representations; Neural Information Processing Systems). |

---

## 8. Author Names & Theory Shortcuts

The documentation cites theorists by surname. Quick-reference for the most frequent ones:

| Surname | First name(s) | Field | Best-known contribution cited in CFLT |
|---|---|---|---|
| **Chomsky** | Noam | Linguistics | Universal Grammar; *core grammar* vs *periphery* |
| **Talmy** | Leonard | Cognitive linguistics | Figure-Ground; Contingency Principle |
| **Langacker** | Ronald | Cognitive grammar | Profile-Base distinction |
| **Hawkins** | John A. | Linguistic typology | EIC, CRD, parsing-efficiency theory |
| **Halliday** | M.A.K. | Functional linguistics | Systemic Functional Grammar; Circumstance roles |
| **Wierzbicka** | Anna | Semantics | NSM, semantic primes |
| **Searle** | John | Philosophy of language | Speech act taxonomy (Representatives, Directives, Commissives, Expressives, Declarations) |
| **Grice** | H. P. | Pragmatics | Cooperative Principle, Maxims, implicature |
| **Sperber & Wilson** | Dan & Deirdre | Pragmatics | Relevance Theory |
| **Kamp** | Hans | Formal semantics | Discourse Representation Theory |
| **Steedman** | Mark | Computational linguistics | Combinatory Categorial Grammar |
| **Levelt** | Willem | Psycholinguistics | Speaking model (Conceptualizer / Formulator / Articulator) |
| **Krashen** | Stephen | SLA | Input Hypothesis, Monitor Model, Affective Filter |
| **Vygotsky** | Lev | Educational psychology | Zone of Proximal Development, scaffolding |
| **Sweller** | John | Cognitive psychology | Cognitive Load Theory |
| **DeKeyser** | Robert | SLA | Skill Acquisition Theory for L2 |
| **Baddeley** | Alan | Cognitive psychology | Working Memory model |
| **Menon & Uddin** | — | Neuroscience | Salience Network as switch between DMN and CEN |
| **Liu et al.** | — | NLP | "Lost in the Middle" (2023) |
| **Xiao et al.** | — | NLP | StreamingLLM, Attention Sinks (2024) |

---

## 9. Cross-References

For full bibliography of cited works, see [`bibliography.md`](./bibliography.md).

For deeper treatment of the canonical concepts:
- **Salience anchor / Core type taxonomy** → [`foundations/core-concept.md`](./foundations/core-concept.md)
- **Figure-Ground, EIC, NSM, profile-base** → [`foundations/linguistics.md`](./foundations/linguistics.md)
- **Speech acts, lambda calculus, CCG, DRT** → [`foundations/logic.md`](./foundations/logic.md)
- **Information theory, entropy, KL** → [`foundations/mathematics.md`](./foundations/mathematics.md)
- **PFC, BG, SN, DMN, CEN, P600** → [`foundations/neuroscience.md`](./foundations/neuroscience.md)
- **Krashen, Vygotsky, Sweller, TBLT** → [`foundations/pedagogy.md`](./foundations/pedagogy.md)
- **Attention Sinks, RAG, prefix caching** → [`foundations/llm.md`](./foundations/llm.md)
- **Slot disambiguation table & decision tree** → [`methodology/slot-disambiguation.md`](./methodology/slot-disambiguation.md)
