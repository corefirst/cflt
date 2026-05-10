# Core Disambiguation: A Normative Reference

> **Version:** 1.0.0 (Internal Draft)
> **Purpose:** To provide an unambiguous, operational definition of the "Core" boundary for human learners, curriculum designers, and LLM-as-a-judge systems.

---

## 1. The Operational Definition of Core

In CFLT, the **Core** (Slot 0) is the **Salience Anchor** of the utterance. It represents the primary event, state, identity, or request the speaker intends to assert. 

**Formal Boundary Rule:** 
The Core consists of:
1.  **The Predicate** (Action, Identity, State, or Request).
2.  **Valence-Bound Participants** (Subject, Object, Indirect Object).
3.  **Internal Modifiers** (Manner, Instrument, Beneficiary, Modal, Negation).

Any modifier that answers **"How?"**, **"With what?"**, or **"To what degree?"** is fused into the Core. Any modifier that answers **"Why?"**, **"Where?"**, or **"When?"** is stripped into Slots 1, 2, or 3.

---

## 2. Key Disambiguation Rules

### 2.1 The "Epistemic Hedge" vs. "Reporting" Rule
*Problem Case:* "I think we should leave."

- **Rule (Epistemic Hedge):** If "I think" or "I believe" functions to soften or qualify the speaker's own assertion, it is treated as a **Modal Modifier** and stays **Inside the Core**.
    - *Core:* "I think we should leave"
- **Rule (Reporting):** If the sentence is reporting someone else's mental state or a specific act of thinking, the mental verb is the **Predicate**.
    - *Example:* "He thinks we should leave." 
    - *Core:* "He thinks [that we should leave]" (Note: the embedded clause is a participant/object).

### 2.2 The "Weather and Manner" Rule
*Problem Case:* "It's raining heavily in Tokyo."

- **Rule:** Adverbs of degree or manner (e.g., *heavily, slightly, quickly*) describe the internal quality of the event, not its external frame.
- **Decision:** "Heavily" is a Manner modifier → **Inside the Core**.
- **Result:**
    - *Core:* "It's raining heavily"
    - *Space:* "in Tokyo"

### 2.3 The "Instrument vs. Space" Rule
*Problem Case:* "I'm working on my laptop in the cafe."

- **Rule:** If the location is the *medium* through which the action is performed, it is an **Instrument** (Inside Core). If it is the *physical site* where the speaker is located, it is **Space** (Slot 2).
- **Decision:** "on my laptop" is the tool (Instrument) → **Inside Core**. "in the cafe" is the site (Space) → **Slot 2**.
- **Result:**
    - *Core:* "I'm working on my laptop"
    - *Space:* "in the cafe"

---

## 3. Core Boundary Decision Tree

Follow these steps to isolate the Core:

1.  **Identify the Primary Assertion:** What is the "Figure" or "Event"?
2.  **Apply the "Same Event?" Test:** If you remove the modifier, does the nature or quality of the event change?
    - *Yes (e.g., "slowly", "with butter"):* The modifier is **Inside Core**.
    - *No (e.g., "at 5pm", "at home"):* The modifier is **Outside Core (Ground Frame)**.
3.  **The RST Filter:** Does the modifier answer Why, Where, or When?
    - *Yes:* Move to Slots 1, 2, or 3.
    - *No (and it's not a participant):* It belongs to the Core as an internal modifier (Manner/Instrument/Modal).

---

## 4. Stress Test: 20 Boundary Cases

| # | Sentence | Core Boundary | Logic |
|---|---|---|---|
| 1 | I think it might rain. | *I think it might rain* | Epistemic hedge (Modal) + Event. |
| 2 | He said he was tired. | *He said he was tired* | Reported speech; "said" is the anchor. |
| 3 | I'm studying English hard. | *I'm studying English hard* | "Hard" is Manner (degree). |
| 4 | It's boiling hot today. | *It's boiling hot* | "Boiling" is degree/quality of the State. |
| 5 | I'll go by car tomorrow. | *I'll go by car* | "By car" is Instrument. |
| 6 | Please sit down here. | *Please sit down* | "Please" is polite marker (Inside Core). |
| 7 | I'm writing via Slack. | *I'm writing via Slack* | "Via Slack" is the medium (Instrument). |
| 8 | I'm writing about AI. | *I'm writing about AI* | "About AI" is the topic/patient of the verb. |
| 9 | I'm exhausted from work. | *I'm exhausted* [Reason: from work] | "From work" is the Cause (Slot 1). |
| 10 | I baked a cake for you. | *I baked a cake for you* | "For you" is Beneficiary. |
| 11 | I read the news on my phone. | *I read the news on my phone* | "On my phone" is the tool (Instrument). |
| 12 | It's dark in this room. | *It's dark* [Space: in this room] | "In this room" is Space (Slot 2). |
| 13 | I'll call you if I can. | *I'll call you* [Reason: if I can] | "If I can" is Condition (Slot 1). |
| 14 | She's a doctor in Paris. | *She's a doctor* [Space: in Paris] | Identity Core + Space. |
| 15 | I'm definitely coming. | *I'm definitely coming* | "Definitely" is Modal. |
| 16 | I haven't eaten yet. | *I haven't eaten* [Time: yet] | "Yet" is Time (Slot 3). |
| 17 | I'm walking with a cane. | *I'm walking with a cane* | "With a cane" is Instrument. |
| 18 | I'm walking with John. | *I'm walking with John* | "With John" is Accompaniment. |
| 19 | I'm working at Google. | *I'm working* [Space: at Google] | "At Google" is Space (Site). |
| 20 | He's probably joking. | *He's probably joking* | "Probably" is Modal. |

---

## 5. Summary for AI Training

When generating or validating CFLT data:
- **Default to Inclusion:** When in doubt between Manner and Space, if the modifier describes the "how" of the verb (e.g., "via API", "on the web"), keep it inside the Core.
- **RST Exclusion:** Only strip out modifiers that provide the external frame (Reason, Space, Time).
