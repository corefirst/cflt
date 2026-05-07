# LLM Foundations of CFLT/CFLM

> Companion to: [`manifesto.md`](../manifesto.md)
> Read first: [`core-concept.md`](./core-concept.md) — defines "Core" as the salience anchor (action, state, identity, or request), not as a syntactic predicate.
> Purpose: Connect CFLM's Core-First sequencing claim to documented behaviors of Transformer-based language models — attention biases, position effects, autoregressive dynamics, and chain-of-thought reasoning.

> **Why LLMs handle CFLM gracefully.** LLMs are trained on human-language corpora, not on formal-logic notation or typologically rare constructions. CFLM-L2 outputs (e.g., "I went out, because it rained, at home, yesterday") are slightly non-idiomatic but firmly inside the natural-language manifold the model was trained on. This is the deeper reason CFLM and LLM behavior are aligned — CFLM stays in the same distribution the model has learned, while imposing a fixed-order constraint that exploits the model's known positional biases.

---

## 1. Why LLMs Care About Order

CFLM's pedagogical claim is about humans. Its **second strategic pillar** (see [`../vision.md`](../vision.md)) is that the same Core-First protocol benefits LLMs. This document substantiates that pillar.

The mechanism is concrete: **modern LLMs are autoregressive Transformers with positional biases**. Where information appears in the prompt or generated sequence has measurable effects on model behavior. CFLM's slot order is a deliberate engineering choice to align prompts with these biases.

---

## 2. Transformer Attention Mechanics

### 2.1 The Original Architecture
Vaswani et al. (2017, "Attention Is All You Need") introduced the Transformer: a stack of self-attention layers in which every token attends to every other token via learned key/query/value projections.

In the **decoder-only autoregressive variant** (GPT family, Llama, Gemini, Claude), attention is **causally masked** — token $t_n$ can attend to $t_1, \dots, t_{n-1}$ but not to future tokens. This has two consequences directly relevant to CFLM:

1. **Earlier tokens influence more downstream computation.** Token $t_1$ is in the receptive field of *every* subsequent token; $t_n$ influences nothing.
2. **Generation is conditioned on the prefix.** The prompt's opening tokens steer the generative trajectory more than its closing tokens.

### 2.2 Positional Encodings
Whether absolute (Vaswani 2017), relative (Shaw et al. 2018), or rotary (Su et al. 2021, RoPE), positional encodings inject order information into the otherwise position-agnostic attention. Empirical analyses consistently find that:

- Absolute position 0 receives disproportionate attention ("attention sinks", Xiao et al. 2024).
- Distant tokens are attended to less effectively, especially in the middle of long contexts.

CFLM exploits this: **the Core Action at position 0 is over-attended by construction**, biasing the model's early state toward the asserted event.

---

## 3. The Lost-in-the-Middle Phenomenon

Liu et al. (2023, "Lost in the Middle: How Language Models Use Long Contexts") showed empirically that LLMs disproportionately attend to information at the **beginning** and **end** of long contexts, with substantial degradation in the middle.

**CFLM implication:** placing the Core Action at the start of a clause is not just stylistic — it places the most discriminating information in the **highest-attention region** of the model's context window. Subsequent modifiers (Reason, Space, Time) ride on the strong attention anchor established by the core.

For multi-clause CFLM-formatted prompts, this also suggests a meta-rule: the highest-stakes core action of the entire conversation should appear in the system prompt or the first user turn, not buried in turn 7.

---

## 4. Primacy Effects in In-Context Learning

Lu et al. (2022, "Fantastically Ordered Prompts and Where to Find Them") demonstrated that few-shot prompt **ordering can change accuracy by 30+ percentage points** on the same task. The phenomenon is reproducible across model families.

Min et al. (2022, "Rethinking the Role of Demonstrations") showed that the *format* and *order* of demonstrations often matter more than the *correctness* of their labels.

**CFLM implication:** if order alone causes massive variance in model behavior, then a **fixed canonical order** is an obvious mitigation. CFLM provides exactly this: a deterministic schedule that makes prompt behavior more predictable across tasks, prompts, and model versions.

---

## 5. Chain-of-Thought and Structured Reasoning

Wei et al. (2022, "Chain-of-Thought Prompting Elicits Reasoning in Large Language Models") showed that prompting models to generate intermediate reasoning steps dramatically improves performance on multi-step tasks. This effect emerges at sufficient model scale.

Subsequent work (Kojima et al. 2022, *zero-shot CoT*; Yao et al. 2023, *Tree of Thoughts*) generalized the principle: **explicit, structured reasoning surfaces underused capability**.

**CFLM as CoT format:** the four-slot CFLM template is itself a minimal chain-of-thought structure for declarative statements. Rather than freeform reasoning, CFLM provides:

1. State the action (commit to the event).
2. Justify (why it happened).
3. Localize (where).
4. Anchor in time.

Each slot is a discrete reasoning step with a clear semantic question. This is amenable to **prompt-engineered CoT** that asks the model to fill CFLM slots one at a time before committing to a final fluent sentence.

---

## 6. Instruction Tuning and System Prompt Anchoring

Modern instruction-tuned models (Ouyang et al. 2022; the Llama 2/3 chat lineage; the Claude/Gemini/GPT-4 systems) place the **system prompt** at the very start of the context. The training signal teaches the model to treat this prefix as a high-priority constraint.

CFLM aligns with this convention at two levels:

1. **System prompt level.** The Logic Transformer's system prompt (`src/core/system_prompt.md`) declares the CFLM protocol up front, before any user content. This anchors the model in CFLM-compliant generation mode.
2. **User-turn level.** Within each user message, the same Core-First principle applies — the action verb of the user's intent should be near the start.

When both levels reinforce each other, the model is over-determined toward CFLM-compliant outputs, reducing variance.

---

## 7. Hallucination Reduction via Early Commitment

A documented failure mode of LLMs is **late drift**: a generation trajectory that begins coherently but loses logical commitment over many tokens, eventually contradicting earlier claims (Maynez et al. 2020 on summarization hallucination; Zhang et al. 2023 on long-form generation).

The CFLM diagnosis: when the action commitment is *implicit* or *delayed* in the surface form, the model's internal state remains under-determined, leaving room for downstream tokens to wander.

**CFLM remedy:** by forcing the action commitment into position 0 (or as close to it as syntactically possible), the autoregressive trajectory is **anchored** before any modifiers are generated. The space of viable continuations is narrowed early.

This is consistent with empirical findings on **constrained decoding** (Hokamp & Liu 2017; Post & Vilar 2018) — committing to a structural anchor reduces generation variance.

---

## 8. Cross-Agent Communication and Protocol Cost

In multi-agent systems where two LLMs exchange messages (e.g., agentic workflows, MCP-mediated communication, or AI-to-AI coordination), each agent must:

1. Parse the incoming message into an internal representation.
2. Plan a response.
3. Linearize the response back into a message.

Each parse/produce cycle is lossy when surface forms are inconsistent. If both agents adhere to CFLM:

- The parser knows the action will be at position 0 → faster, lower-variance parsing.
- The producer knows where to put the action → consistent surface forms.

CFLM thus functions as a **shared linearization protocol** — analogous to a wire format in distributed systems. The strategic case for this is the second pillar of the vision document.

---

## 9. Empirical Evaluation Hooks

To test whether CFLM-formatted prompts measurably improve LLM behavior, the following experiments are concrete and tractable:

1. **Order-variance reduction.** For a fixed task, generate $N$ prompts where slot order is permuted. Measure output variance (BLEU/ROUGE/embedding distance) for CFLM-fixed vs. free-order. Hypothesis: CFLM-fixed produces lower variance.
2. **Long-context retrieval.** Place a key fact in different slot positions across a long context, and ask the model to retrieve it. Hypothesis: CFLM-position-0 placement yields higher retrieval accuracy than middle positions, consistent with Liu et al. 2023.
3. **Hallucination rate.** On long-form generation, compare hallucination rates for prompts that begin with the action vs. prompts that begin with a temporal/spatial adjunct. Hypothesis: action-first prompts hallucinate less.
4. **Cross-model transfer.** If CFLM aligns with attention biases shared across models (GPT, Claude, Gemini, Llama), then a CFLM-tuned prompt should transfer better across families than a freeform prompt.

These are testable claims, not assertions. The CoreFirst implementation can serve as the first empirical platform.

---

## 10. Honest Limitations

1. **Architecture-specific.** The arguments above are tightly bound to autoregressive Transformers with positional encoding biases. Future architectures (state-space models, diffusion-LM, retrieval-only systems) may not exhibit the same primacy/middle-loss patterns. CFLM's LLM justification is not architecture-agnostic.
2. **Tokenization coupling.** "Position 0" is a token-level claim, but CFLM operates at the slot level. The mapping from CFLM slots to token positions depends on the tokenizer; one slot may be many tokens. The benefit is approximate, not exact.
3. **Trained behavior, not architectural law.** Most positional biases (attention sinks, primacy) are emergent properties of trained models, not architectural guarantees. They can be reduced or eliminated by specific training regimes (Xiao et al. 2024 on attention-sink mitigation). Future models may not exhibit them.
4. **Empirical claims still need testing.** This document outlines hypotheses derived from the literature; they are not yet validated in CoreFirst's own experiments. The §9 evaluation hooks are the next step.
5. **Scale dependence.** Many CoT and primacy effects emerge only at scale. Small models may not benefit from CFLM formatting.

---

## 11. Cited Works

See [`bibliography.md`](../bibliography.md) for full references.
