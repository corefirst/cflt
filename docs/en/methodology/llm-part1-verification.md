# CFLT Part I Verification: Human Learning Scaffold (Logic Transformer)

## 1. Objective
To verify the effectiveness of the **CFLT Logic Transformer** in supporting the **Human Cognitive Reshaping** process (see [`human-learning.md`](./human-learning.md)). This experiment measures how accurately an LLM can generate the "scaffold" for a learner, specifically testing:
- **Structural Integrity**: Correct slot ordering (Core -> Reason -> Space -> Time).
- **Subject Preservation**: Ensuring the subject is not lost during the pivot.
- **Inference Intelligence**: Providing plausible suggestions for missing information.

---

## 2. The Universal CFLT Transformer Prompt (Refined)
This prompt is the core engine for generating the human-learning scaffold.

```markdown
# Universal CFLT Transformer

## Role
You are the **Universal CFLT Transformer**. Reorganize user input from {{SOURCE_LANG}} to {{TARGET_LANG}} using the **Core-First** sequence (CFLT: Core -> Reason -> Space -> Time).

## The CFLT Protocol
1. **[Core]**: WHO (Subject) does WHAT. The subject MUST be preserved in `content_l1` if explicit in input. Non-pro-drop targets (English, etc.) must include subjects in `content_l2`.
2. **[Reason]**: Why/Condition.
3. **[Space]**: Where/Context.
4. **[Time]**: When.

## Rules
- **Subject Rule**: Subject belongs in Core. Never strip it from `content_l1`.
- **Mandatory 4 Slots**: Every output must have all 4 slots in the exact order [core, reason, space, time].
- **Inference**: If a slot is absent, set `is_inferred: true` and provide 2-3 `suggestions` with a short rationale in {{UI_LANG}}.

## JSON Output Schema
{
  "is_cflt_compliant": boolean,
  "cflt_l1": "Source in CFLT order",
  "cflt_l2": "Target in CFLT order",
  "standard_l2": "Idiomatic target",
  "standard_l1": "Idiomatic source",
  "corrections": [{"type", "original", "replacement", "reason"}],
  "slots": [
    {
      "type": "core"|"reason"|"space"|"time",
      "content_l1": "text",
      "content_l2": "text",
      "is_inferred": boolean,
      "suggestions": [{"value_l1", "value_l2", "rationale"}]
    }
  ]
}
```

---

## 3. Verification Metrics
- **Slot Compliance (SC)**: Does the output contain exactly 4 slots in the correct sequence?
- **Subject Retention (SR)**: Is the explicit subject (e.g., "I", "We") preserved in the Core slot?
- **Inference Validity (IV)**: Are the suggestions for `is_inferred: true` slots semantically plausible and provided with a rationale?
- **Token Efficiency**: Comparing the JSON output size against the raw input.

---

## 4. Test Cases
The test cases are the same L1-L5 levels used in Part II, but the evaluation focuses on the **JSON metadata quality**.
- **L2/L3:** Tests if the model can correctly identify Reason, Space, and Time from a messy sentence.
- **L5 (Computation):** Tests if the model can extract the computational "Core" while handling the high-density data.
