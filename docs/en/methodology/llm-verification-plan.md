# CFLT Experimental Verification Plan: LLM Accuracy & Efficiency

> **Version:** 1.0.0  
> **Target:** Verification of Core-First Language Theory (CFLT) on Large Language Models.  
> **Status:** Finalized Draft.

---

## 1. Objective & Scope
This plan details a rigorous empirical framework to validate the **Core-First Language Theory (CFLT)** protocol within the context of Large Language Models (LLMs). The goal is to prove that anchoring the speaker's primary commitment (the "Core") at Position 0 significantly enhances model performance while optimizing computational costs.

---

## 2. The Verification Matrix (Tiered Difficulty)
To ensure robustness, the verification suite is divided into five levels of increasing information density and logical complexity. Each test case compares a **Native Language Expression (Control)** against a **CFLT-Structured Expression (Experimental)**.

### Level 1: Simple Intent (Low Density)
*   **Description:** Single action, single modifier.
*   **Control (Native):** "Please close the window because it is raining outside."
*   **CFLT:** "[CORE] Close window, [REASON] because raining."
*   **Expected JSON:** `{"action": "close", "target": "window"}`

### Level 2: Parameter-Heavy (Medium Density)
*   **Description:** Single action with specific Space, Time, and Reason slots.
*   **Control (Native):** "Since the meeting has concluded, please turn off all the lights in the grand conference room on the 5th floor at 6:00 PM today."
*   **CFLT:** "[CORE] Turn off lights, [REASON] meeting concluded, [SPACE] 5F Grand Conference Room, [TIME] Today 18:00."
*   **Expected JSON:** `{"action": "off", "target": "lights", "location": "5F_conference_room", "time": "18:00"}`

### Level 3: High Density / Noisy Context (High Difficulty)
*   **Description:** Core action buried in a paragraph of background info and irrelevant details (Tests Middle-Loss).
*   **Control (Native):** A narrative describing server room maintenance and temperature fluctuations, ending with a request to shut down backup nodes.
*   **CFLT:** "[CORE] Shutdown backup nodes, [REASON] prevent hardware damage, [SPACE] East Wing Server Room, [TIME] 14:15."
*   **Expected JSON:** `{"action": "shutdown", "target": "backup_nodes", "priority": "high"}`

### Level 4: Complex Salience / Intent Extraction (Extreme Difficulty)
*   **Description:** Multiple potential actions mentioned; model must identify the *primary* commitment.
*   **Control (Native):** "I thought about calling the police, but I decided to stay home and organize evidence tonight instead of going to the insurance company tomorrow."
*   **CFLT:** "[CORE] Organize evidence, [REASON] avoid escalation, [SPACE] home, [TIME] tonight."
*   **Expected JSON:** `{"primary_action": "document_evidence", "status": "decided"}`

### Level 5: High-Density Data & Multi-Step Logic (Computational/Extreme)
*   **Description:** Raw unformatted log extraction + multi-step arithmetic + conditional logic constraints.
*   **Control (Native):** A raw server log snippet followed by a complex request to calculate average CPU usage and filter entries meeting specific CPU/Error/Memory thresholds.
*   **CFLT:** "[CORE] Calculate avg CPU & extract high-load error logs, [REASON] prevent memory melting (Limit:30GB), [SPACE] Log Data, [TIME] past hour."
*   **Expected JSON:** Summarized metrics including `avg_cpu`, `high_load_errors`, and a boolean `melting_point_triggered`.

---

## 3. Evaluation Models & Hardware Standards

### Category A: Local Open-Source Models (24-32G RAM Accessibility)
*Goal: Ensure the experiment is reproduced by the community on standard consumer hardware (e.g., RTX 3090/4090 or 32GB Mac).*
*   **Meta-Llama-3-8B-Instruct** (The global ecosystem baseline)
*   **Qwen2-7B-Instruct** (Leading Chinese/Logic open-source model)
*   **DeepSeek-V2-Lite-Chat / DeepSeek-Coder-V2-Lite** (Highly efficient MoE architecture)
*   **Gemma-2-9B-It** (Google's latest state-of-the-art open weights)
*   *Quantization: 4-bit (AWQ/GGUF) or 8-bit (FP8) to fit 16GB-24GB VRAM.*

### Category B: Frontier Closed-Source Models (2025-2026 State-of-the-Art)
*   **OpenAI:** `gpt-5.5-pro`, `gpt-5.4-mini`
*   **Anthropic:** `claude-opus-4-7`, `claude-sonnet-4-6`
*   **Google:** `gemini-3.1-pro-preview`, `gemini-3-flash`

---

## 4. Verification Indicators (Data-Driven Comparison)

The evaluation is based on a direct comparison of the **API Response Metadata** and **Generated Content**.

### Metric 1: Accuracy (JSON Hit Rate)
*   **Mechanism:** Compare model output directly against the **Expected JSON Ground Truth**.
*   **Success Criteria:** Exact match of keys and values (Binary 1 or 0).
*   **Goal:** Prove CFLT has a higher hit rate, especially in Level 3–5 cases.

### Metric 2: Input Efficiency (Prompt Token Consumption)
*   **Mechanism:** Extract `usage.prompt_tokens` from the API response.
*   **Goal:** Demonstrate that the CFLT protocol reduces "syntactic fluff," leading to lower per-request costs.

### Metric 3: Output Quality (Completion Token Waste)
*   **Mechanism:** Extract `usage.completion_tokens`.
*   **Goal:** Prove that the structural clarity of CFLT prevents "model rambling," resulting in concise, straight-to-the-point JSON responses.

---

## 5. Parameter Settings (Universal)
*   **Temperature:** `0.0` (Deterministic output)
*   **Response Format:** `json_object` (Mandatory)
*   **Max Tokens:** `512`
*   **Top_P:** `1.0`

---

## 6. Execution Workflow
1.  **Dataset Preparation:** Generate 50+ paired samples for each of the 5 difficulty levels.
2.  **Sequential Execution:** Run the prompts through the target models individually (no concurrent stress test).
3.  **Comparative Analysis:** Generate a report comparing the Hit Rate and Token usage across all difficulty levels and model categories.
