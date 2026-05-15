import json
import os
from typing import Dict, Any, List, Optional
from dotenv import load_dotenv

try:
    from openai import OpenAI
except ImportError:
    print("Error: 'openai' library not found. Please install it using 'pip install openai'.")
    exit(1)

load_dotenv()

# --- Shared Configuration ---
DATASET_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "dataset.json"))
RESULTS_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../results"))

LANG_MAP = {
    "en": "English",
    "zh": "Chinese",
    "ja": "Japanese",
    "ko": "Korean",
    "fr": "French",
    "de": "German",
    "es": "Spanish"
}

# Unified Model Registry
# Format: provider/model-name
MODELS_CONFIG = {
    "openai/gpt-5": {"api_key": os.getenv("OPENAI_API_KEY"), "base_url": "https://api.openai.com/v1", "provider": "openai"},
    "openai/gpt-5-mini": {"api_key": os.getenv("OPENAI_API_KEY"), "base_url": "https://api.openai.com/v1", "provider": "openai"},
    "anthropic/claude-4-sonnet": {"api_key": os.getenv("ANTHROPIC_API_KEY"), "base_url": "https://api.anthropic.com", "provider": "anthropic"},
    "google/gemini-1.5-flash": {"api_key": os.getenv("GOOGLE_API_KEY"), "base_url": "https://generativelanguage.googleapis.com/v1beta/openai/", "provider": "google"},
    "google/gemini-1.5-pro": {"api_key": os.getenv("GOOGLE_API_KEY"), "base_url": "https://generativelanguage.googleapis.com/v1beta/openai/", "provider": "google"},
    "google/gemini-3.1-flash-lite": {"api_key": os.getenv("GOOGLE_API_KEY"), "base_url": "https://generativelanguage.googleapis.com/v1beta/openai/", "provider": "google"},
    "google/gemini-3.1-pro": {"api_key": os.getenv("GOOGLE_API_KEY"), "base_url": "https://generativelanguage.googleapis.com/v1beta/openai/", "provider": "google"},
    "ollama/qwen2.5:7b": {"api_key": "ollama", "base_url": "http://localhost:11434/v1", "provider": "ollama"},
}

SYSTEM_PROMPT_TEMPLATE = """
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
"""

def get_client_and_model(model_tag: str):
    if "/" not in model_tag:
        # Fallback for old style or raw names
        config = MODELS_CONFIG.get(f"openai/{model_tag}") or {"api_key": os.getenv("OPENAI_API_KEY"), "base_url": "https://api.openai.com/v1", "provider": "openai"}
        actual_model = model_tag
    else:
        provider, actual_model = model_tag.split("/", 1)
        config = MODELS_CONFIG.get(model_tag)
        if not config:
            raise ValueError(f"Model tag '{model_tag}' not found in registry.")

    if not config["api_key"] and config["provider"] != "ollama":
        raise ValueError(f"API key for {model_tag} is not set in environment.")

    # For Google provider, models usually need the 'models/' prefix in the OpenAI-compatible endpoint
    if config["provider"] == "google" and not actual_model.startswith("models/"):
        actual_model = f"models/{actual_model}"

    client = OpenAI(api_key=config["api_key"] or "none", base_url=config["base_url"])
    return client, actual_model, config

def call_transformer(client: OpenAI, model: str, input_text: str, source_lang: str = "English", target_lang: str = "English", ui_lang: str = "English") -> Dict[str, Any]:
    try:
        prompt = SYSTEM_PROMPT_TEMPLATE.replace("{{SOURCE_LANG}}", source_lang) \
                                     .replace("{{TARGET_LANG}}", target_lang) \
                                     .replace("{{UI_LANG}}", ui_lang)
        
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": prompt},
                {"role": "user", "content": input_text}
            ],
            response_format={"type": "json_object"}
        )
        return json.loads(response.choices[0].message.content)
    except Exception as e:
        return {"error": str(e)}

def validate_cflt_compliance(res: Dict[str, Any]) -> Dict[str, bool]:
    slots = res.get("slots", [])
    slot_types = [s.get("type") for s in slots]
    
    # SC (Order): Core -> Reason -> Space -> Time
    order_map = {"core": 0, "reason": 1, "space": 2, "time": 3}
    indices = [order_map.get(t) for t in slot_types if t in order_map]
    sc = indices == sorted(indices) and len(indices) >= 1

    # SR (Subject): Core slot should not be empty
    sr = any(s.get("type") == "core" and s.get("content_l1") for s in slots)

    # IV (Inference): Inferred slots must have suggestions
    iv = all(not s.get("is_inferred") or (s.get("suggestions") and len(s.get("suggestions")) > 0) for s in slots)

    return {"sc": sc, "sr": sr, "iv": iv}

def load_dataset():
    with open(DATASET_PATH, 'r', encoding='utf-8') as f:
        return json.load(f)

def compare_json(actual: Any, expected: Any) -> bool:
    """Recursively compare two JSON objects for structural and semantic equality."""
    if isinstance(actual, dict) and isinstance(expected, dict):
        # Key semantic mapping
        key_synonyms = {
            "error": ["error_type", "err", "type"],
            "mem": ["peak_memory", "mem_peak", "memory"],
            "time": ["timestamp", "at"]
        }
        
        # Check if expected keys exist in actual (or their synonyms)
        for ek, ev in expected.items():
            found_key = ek
            if ek not in actual:
                # Try synonyms
                if ek in key_synonyms:
                    for syn in key_synonyms[ek]:
                        if syn in actual:
                            found_key = syn
                            break
                if found_key == ek: # Still not found
                    return False
            
            if not compare_json(actual[found_key], ev):
                return False
        return True
    elif isinstance(actual, list) and isinstance(expected, list):
        if len(actual) != len(expected): return False
        return all(compare_json(a, e) for a, e in zip(actual, expected))
    else:
        if isinstance(actual, str) and isinstance(expected, str):
            a_clean = actual.strip().lower()
            e_clean = expected.strip().lower()
            if a_clean == e_clean: return True
            
            # ID prefix removal (e.g., "ID:001" matches "001")
            if a_clean.replace("id:", "").strip() == e_clean.replace("id:", "").strip():
                return True
            
            # Semantic mapping for common evaluation values
            synonyms = {
                "off": ["turn off", "shutdown", "关", "关闭", "power off", "关掉"],
                "on": ["turn on", "start", "开", "开启", "power on", "打开"],
                "close": ["shut", "关", "关闭", "关上"],
                "window": ["windows", "窗户", "窗"],
                "lights": ["light", "灯", "电灯"],
                "5f_conference_room": ["5楼大会议室", "grand conference room on the 5th floor", "5f grand conference room", "5f_grand_conference_room", "5f_large_conference_room"],
                "document_evidence": ["organize_evidence", "collect_evidence", "整理证据", "整理所有证据"],
                "error": ["error_type", "err", "error", "错误类型"],
                "mem": ["peak_memory", "mem_peak", "memory", "内存峰值", "峰值内存"]
            }
            if e_clean in synonyms and a_clean in synonyms[e_clean]:
                return True
            # Also check reverse mapping for symmetric synonyms
            for canon, syns in synonyms.items():
                if a_clean == canon and e_clean in syns:
                    return True

            # Partial match for longer values (e.g., "5f grand conference room" matches "5f conference room")
            if len(e_clean) > 5 and (e_clean in a_clean or a_clean in e_clean):
                return True
            
            # Key-based synonym check for lists of dicts
            # (handled by recursive call if keys match, but sometimes keys themselves are synonyms)
            # This is handled in the dict comparison above but for values here.
                
        return actual == expected
