# Mathematical Foundations of CFLT/CFLM

> Companion to: [`manifesto.md`](../manifesto.md)
> Read first: [`core-concept.md`](./core-concept.md) — defines "Core" as the salience anchor, not as a verb or predicate.
> Purpose: Frame CFLM in terms of information theory, optimal coding, sequence modeling, and the linearization problem on partial orders.

> **Framing note.** Throughout this document, "Core" refers to the salience anchor of an utterance — the constituent the speaker is fundamentally committing to. The mathematical arguments below depend only on the Core being **the most discriminating constituent** of the utterance, regardless of whether it is realized as an action verb, a copular complement, a state, or a request. The mathematics is therefore agnostic to syntactic category.

---

## 1. The Linearization Problem

A clause's meaning is structurally a **partial order**: certain semantic dependencies must hold (the action depends on its arguments; modifiers depend on the action), but many orderings are possible at the surface. Producing a sentence is therefore a **topological linearization** of a partial-order DAG.

Different languages choose different deterministic linearization functions over the same underlying partial order. CFLM proposes one specific linearization:

$$
L_{\text{CFLM}}(G) = [\,\text{root}(G),\ \text{cause}(G),\ \text{location}(G),\ \text{time}(G)\,]
$$

where $G$ is the semantic DAG and the four functions extract slot fillers.

The mathematical question: among all valid linearizations of $G$, why prefer this one? The answer comes from information theory.

---

## 2. Shannon Information Theory

Shannon (1948) defined the **information content** $I(x) = -\log p(x)$ of an event $x$ with probability $p(x)$, and **entropy** $H(X) = -\sum_x p(x) \log p(x)$ as the average information of a random variable.

In language production, each token contributes information conditional on the preceding tokens:

$$
I(t_n \mid t_1, \dots, t_{n-1}) = -\log p(t_n \mid t_1, \dots, t_{n-1})
$$

A clause is therefore a sequence of conditional informational contributions.

### 2.1 Information Density and the Core
The Core carries the highest information per token: by definition it is the salience anchor — the constituent the speaker is most committed to — and identifying it restricts the space of possible interpretations far more than any single modifier does. Whether the Core is an action ("went out"), a state ("exhausted"), an identity ("is my sister"), or a request ("help me"), it is the maximally discriminating constituent for the listener's interpretation. Placing it first minimizes the **prior uncertainty** under which the listener parses the rest of the clause.

Conditional entropy $H(\text{rest} \mid \text{core})$ is significantly lower than $H(\text{rest})$. Frontloading the core thus front-loads the entropy reduction.

---

## 3. Uniform Information Density Hypothesis (UID)

Levy & Jaeger (2007), Jaeger (2010), and the broader UID literature propose that speakers tend to spread information **uniformly** across the utterance — avoiding spikes and troughs.

This is sometimes presented as a counter-argument to frontloading high-information tokens. We address the tension honestly:

- **For native speakers**, UID predicts that within a fluent utterance, information density is roughly constant. End-focus and end-weight in English distribute heavy NPs to the right precisely to flatten density.
- **For L2 learners and AI agents**, UID is a *production-side* optimization that presupposes the speaker can already plan globally. Learners cannot. CFLM therefore optimizes for **interpretation-side** parsing certainty by frontloading the core, accepting a less-flat density curve.

CFLM is thus not a refutation of UID; it is a **different optimization target** suited to a different speaker population.

---

## 4. Optimal Coding (Source Coding Theorem)

Shannon's source coding theorem (1948) and Huffman coding (1952) tell us that **frequently used or highly informative items should occupy short, easily accessible code positions**.

Translating this to clause linearization:
- The Core Action is the **shortest path to disambiguating the speaker's intent**.
- Putting it in position 1 (the most accessible position) minimizes the listener's expected lookup cost.

This is analogous to placing the most frequently accessed instruction at the entry point of a function — the engineering principle of "front-load the dispatch."

---

## 5. Markov Chains and Sequential Dependence

A clause modeled as a Markov chain $(t_1, t_2, \dots, t_n)$ has joint probability:

$$
p(t_1, \dots, t_n) = \prod_{i=1}^{n} p(t_i \mid t_{i-1}, \dots, t_1)
$$

The **early tokens dominate the conditional distributions** of all later tokens. If $t_1$ encodes the action verb, then $p(t_2 \mid t_1)$ is heavily constrained — possible reasons, locations, and times must be compatible with the action.

For autoregressive language models (the dominant LLM architecture, see `llm.md`), this means:

- A CFLM-prefixed prompt steers all subsequent generation toward action-consistent continuations.
- A non-CFLM prompt (e.g., starting with a temporal adjunct) leaves the action under-determined for many tokens, increasing variance and hallucination risk.

---

## 6. KL Divergence and Prompt Steering

For an autoregressive model with conditional distribution $p_\theta(\cdot \mid \text{prompt})$, the **steering effect** of different prompt orderings can be quantified by the Kullback-Leibler divergence between the resulting distributions:

$$
D_{KL}\!\left(p_\theta(\cdot \mid \text{prompt}_A)\,\Big\|\,p_\theta(\cdot \mid \text{prompt}_B)\right)
$$

Empirical studies (Sclar et al. 2024; Lu et al. 2022 on order sensitivity) consistently find that prompt ordering substantially shifts model output distributions. CFLM is, in this framing, an **engineering choice** to fix the prompt prefix to a high-KL, low-variance ordering.

---

## 7. Combinatorial Bounds on Constructional Flexibility

For a four-slot template with $n_i$ candidate fillers per slot, the size of the productive language is:

$$
|L_{\text{CFLM}}| = \prod_{i=1}^{4} n_i
$$

This is independent of word-order choice — but the **search space at production time** is:

- For free-order natural language: $|L_{\text{CFLM}}| \times 4!$ permutations the speaker must choose among.
- For CFLM-constrained language: $|L_{\text{CFLM}}| \times 1$ — the linearization is fixed.

CFLM thus eliminates a factor of $4! = 24$ from the production search space, reducing planning load by more than an order of magnitude in the linearization sub-task. This is a clear computational argument for pedagogical use.

---

## 8. Information-Theoretic View of L1 → L2 Translation

If $L_1$ and $L_2$ have surface linearizations $\sigma_1, \sigma_2$ over the shared semantic DAG $G$, then producing L2 from L1 thought requires:

$$
\sigma_2 \circ \sigma_1^{-1}(G) = \text{re-linearize}(G \text{ extracted from L1 surface})
$$

This composition has two costs:
1. **Decoding** $\sigma_1^{-1}$: recovering $G$ from L1 surface.
2. **Encoding** $\sigma_2$: re-linearizing $G$ in L2 order.

CFLM short-circuits both by introducing a **canonical intermediate linearization** $\sigma_C$:

$$
\sigma_2 \circ \sigma_C^{-1} \circ \sigma_C \circ \sigma_1^{-1}(G)
$$

This appears longer, but the trick is that $\sigma_C$ is **the same in every language**. Once a learner internalizes $\sigma_C$, both $\sigma_C \circ \sigma_1^{-1}$ and $\sigma_2 \circ \sigma_C^{-1}$ are simple token-level remappings, not structural reorganizations. Mathematically, CFLM converts a structural transformation into a lexical substitution.

---

## 9. Decision-Theoretic Framing for Pedagogy

A learner producing an L2 sentence faces a sequential decision problem at each token position. The total **production cost** can be modeled as:

$$
C(\sigma) = \sum_{i=1}^{n} c_i(\sigma)
$$

where $c_i$ is the cognitive cost of choosing token $i$ given the partial sequence so far. Empirically, $c_i$ scales with the **branching factor** at position $i$: how many continuations are still viable?

By fixing the slot order, CFLM forces the highest-information slot (Core Action) to be filled first, which **collapses branching factor at all later positions**. The overall production cost is bounded above by:

$$
C(\sigma_{\text{CFLM}}) \leq C(\sigma_{\text{free}})
$$

with the gap maximized when the speaker is novice (high baseline branching factor) — exactly the L2 learner case.

---

## 10. Honest Limitations

1. **UID tension.** As noted in §3, native idiomatic English aims for flat information density (often via end-weight); strict CFLM produces lumpy density profiles. Idiomatic polishing must be applied at the surface stage.
2. **Empirical estimation of $c_i$.** The decision-theoretic argument depends on cognitive cost functions that are hard to measure directly; experimental validation is needed (eye tracking, articulation onset latency).
3. **Non-eventive clauses.** The CFLM template assumes an event-denoting clause with a clear core action. Stative descriptions, generic statements, and identification clauses ("This is a chair") fit awkwardly and may need a separate template family.
4. **Long-range dependencies.** When semantic modifiers depend on each other (nested causes, conditional times), the four-slot template flattens what is logically a tree. The Grammar Overlay must reconstruct nesting at the surface level.

---

## 11. Open Mathematical Questions

1. **Optimal slot count.** Why four? Can the cognitive cost function justify exactly four slots, or is this an empirically motivated heuristic?
2. **Slot order proof.** Is `Core → Reason → Space → Time` provably optimal under any natural cost function, or is it one of several local optima?
3. **Recursive CFLM.** When a slot filler is itself a clause, the recursion needs a closure rule; does the recursive variant preserve the linearization-cost theorem?
4. **Cross-linguistic equivalence classes.** Two languages share a "CFLM equivalence class" if their $\sigma$ functions agree under permutation of the four slots. What is the algebraic structure of this equivalence relation?

---

## 12. Cited Works

See [`bibliography.md`](../bibliography.md) for full references.
