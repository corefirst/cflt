# Methodology: Complex Structures & Recursion (CFLT-Complex)

> **Version:** 1.0.0 (Internal Draft)
> **Author:** CFLT Core Team
> **Organization:** [CFLT.center](https://cflt.center)
> **License:** [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)

> **Purpose:** To extend the base CFLT Protocol to handle nested clauses, conditionals, and complex narrative structures without violating the "Core-First" mandate.

---

## 1. The Limits of the Base Protocol

The base CFLT sequence—`[Core Action/Result] → [Condition/Reason] → [Space/Context] → [Time]`—is highly optimized for single, discrete thoughts. It embodies "Flattened Logic." 

However, natural human communication frequently involves **recursion** and **dependency**. What happens when a "Reason" is an entire event itself? What happens when a sentence contains multiple conditional dependencies?

CFLT-Complex provides the rules for **clause stacking** and **recursive slot-filling**.

## 2. Recursive Slot-Filling

The primary rule of CFLT-Complex is that **any slot in the CFLT sequence can contain an embedded CFLT sequence**, provided the inner sequence also obeys the Core-First rule.

### Example: Nested Reason
*Raw Input (Chinese):* 因为如果明天下雨航班会取消，所以我决定今天走。
*(Because if it rains tomorrow the flight will be canceled, so I decided to leave today.)*

**CFLT Decomposition:**
- **Outer Core:** I decided to leave.
- **Outer Time:** today.
- **Outer Reason:** [Because the flight will be canceled, if it rains, tomorrow.] *(This is a nested CFLT block)*

**CFLT-Complex Output:**
> "I decided to leave, today, because [the flight will be canceled, if it rains, tomorrow]."

*Note: In advanced execution, the learner handles the nested block as an independent thought, processing one Core at a time.*

## 3. Clause Stacking (Chronological & Logical Chaining)

When narrating a series of events, forcing everything into a single four-slot sentence causes the "Modifier Trap" to re-emerge. 

**Rule:** Break long narratives into independent CFLT blocks joined by explicit logical connectors (`AND`, `BUT`, `THEN`, `SO`).

### 3.1 Chronological Chaining
*Raw Input:* 昨天我在办公室开了一下午会，然后去餐厅吃了晚饭，最后回家睡觉了。

**CFLT-Complex Output:**
1. "I had a meeting, in the office, all afternoon, yesterday."
2. `THEN` "I ate dinner, at the restaurant."
3. `THEN` "I went to sleep, at home."

### 3.2 Conditional Chaining (If-Then)
Conditionals are inherently tricky because the *condition* (If) often precedes the *result* (Then) in time, but the *result* is usually the semantic Core.

**The CFLT-Complex Rule for Conditionals:** Always assert the **Result (Core)** first, then append the **Condition** in the `[Condition/Reason]` slot. 

*Raw Input:* 如果你完成报告，我明天就在办公室请你喝咖啡。
*(If you finish the report, I will buy you coffee in the office tomorrow.)*

**CFLT-Complex Output:**
> "I will buy you coffee, if you finish the report, in the office, tomorrow."

*Why?* The listener's brain is immediately anchored to the primary reward/action ("buy coffee"). The condition acts as a modifier.

## 4. Multi-Agent Context: The "Context Block"

For LLM Prompting and multi-agent communication, passing massive contexts in the `[Reason]` or `[Space]` slots breaks the efficiency of the parser.

**Rule:** For AI systems, utilize an explicit **[GLOBAL CONTEXT]** block that precedes the CFLT execution array.

```json
{
  "global_context": "The production server went down at 02:00 AM.",
  "cflt_execution_chain": [
    {
      "core": "Restart the database",
      "reason": "to clear the connection pool",
      "space": "in the us-east-1 region",
      "time": "immediately"
    },
    {
      "core": "Notify the on-call engineer",
      "reason": "for secondary verification",
      "space": "via PagerDuty",
      "time": "after the restart"
    }
  ]
}
```

## 5. Honest Limitations

1.  **Idiomaticity ceiling for nested forms.** A nested CFLT block such as *"I decided to leave, today, because [the flight will be canceled, if it rains, tomorrow]"* is the **scaffold form**, not the target idiomatic English. The Grammar Overlay layer is expected to polish this into *"I decided to leave today, because the flight will be canceled if it rains tomorrow."* CFLT-Complex defines the recursion rule, not the surface output.
2.  **Connector inventory is open.** §3 lists `AND / BUT / THEN / SO` as canonical connectors; real chained discourse uses a much wider set (concessive, adversative, temporal-precedence, etc.). The minimal inventory should be treated as a starting point, not a closed set.
3.  **No formal bound on nesting depth.** §2 permits arbitrary recursive embedding, but human working memory and LLM attention both degrade at deep nesting. A practical depth limit (likely 1–2 levels for spoken production, 2–3 for written/agentic use) requires its own empirical bound.
4.  **Tense propagation across blocks.** When chained CFLT blocks share an implicit time frame, the protocol does not yet specify how the Grammar Overlay should propagate tense, aspect, and reference across blocks (e.g., shared subject ellipsis, sequence-of-tenses agreement). This is an open extension.

---

## 6. Summary

CFLT-Complex is not a departure from the Core-First principle; it is its recursive application. By treating complex sentences as **chains of simple CFLT blocks**, learners and models can process theoretically infinite complexity without ever exceeding the working memory limits of a single clause.
