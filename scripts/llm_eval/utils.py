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
    "google/gemini-3-flash-preview": {"api_key": os.getenv("GOOGLE_API_KEY"), "base_url": "https://generativelanguage.googleapis.com/v1beta/openai/", "provider": "google"},
    "google/gemini-3-flash": {"api_key": os.getenv("GOOGLE_API_KEY"), "base_url": "https://generativelanguage.googleapis.com/v1beta/openai/", "provider": "google"},
    "ollama/qwen2.5:7b": {"api_key": "ollama", "base_url": "http://localhost:11434/v1", "provider": "ollama"},
    "ollama/qwen3:8b": {"api_key": "ollama", "base_url": "http://localhost:11434/v1", "provider": "ollama"},
    # DeepSeek (OpenAI-compatible). Set DEEPSEEK_API_KEY (https://platform.deepseek.com/api_keys).
    "deepseek/deepseek-chat":     {"api_key": os.getenv("DEEPSEEK_API_KEY"), "base_url": "https://api.deepseek.com/v1", "provider": "deepseek"},
    "deepseek/deepseek-v4-pro": {"api_key": os.getenv("DEEPSEEK_API_KEY"), "base_url": "https://api.deepseek.com/v1", "provider": "deepseek"},
    # Qwen via Alibaba DashScope (OpenAI-compatible). Set QWEN_API_KEY (申请: https://dashscope.console.aliyun.com/apiKey).
    # International endpoint: https://dashscope-intl.aliyuncs.com/compatible-mode/v1
    "qwen/qwen3.6-max": {"api_key": os.getenv("QWEN_API_KEY"), "base_url": "https://dashscope.aliyuncs.com/compatible-mode/v1", "provider": "qwen"},
    "qwen/qwen3.5-plus": {"api_key": os.getenv("QWEN_API_KEY"), "base_url": "https://dashscope.aliyuncs.com/compatible-mode/v1", "provider": "qwen"},
    "qwen/qwen-flash": {"api_key": os.getenv("QWEN_API_KEY"), "base_url": "https://dashscope.aliyuncs.com/compatible-mode/v1", "provider": "qwen"},
    "qwen/qwen-max": {"api_key": os.getenv("QWEN_API_KEY"), "base_url": "https://dashscope.aliyuncs.com/compatible-mode/v1", "provider": "qwen"},
    "qwen/qwen-plus": {"api_key": os.getenv("QWEN_API_KEY"), "base_url": "https://dashscope.aliyuncs.com/compatible-mode/v1", "provider": "qwen"},
    "qwen/qwen-turbo": {"api_key": os.getenv("QWEN_API_KEY"), "base_url": "https://dashscope.aliyuncs.com/compatible-mode/v1", "provider": "qwen"},
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

import re as _re

_PUNCT_STRIP = ".,;:!?。，；：！？\"'`()[]{}（）【】「」"

# Leading determiners / quantifiers that don't change semantic identity.
# "all the lights" ≡ "lights"; "所有备份节点" ≡ "备份节点".
_LEADING_DETERMINERS_EN = ("all the ", "all ", "the ", "a ", "an ", "my ", "our ", "this ", "that ")
_LEADING_DETERMINERS_ZH = ("所有", "那些", "这些", "全部")

# H:00 → H (so "6:00 pm" ≡ "6 pm"). Preserves non-zero minutes (14:15 stays as-is).
_HOUR_ZERO_MINUTE = _re.compile(r"(\b\d{1,2}):00(?!\d)")

# Models sometimes prepend today's ISO date to time fields ("2026-05-16 18:00" ≡ "18:00").
_ISO_DATE_PREFIX = _re.compile(r"^\d{4}-\d{2}-\d{2}[T ]?")

# Collapse spaces between digits and CJK characters (Qwen3 style: "5 楼" → "5楼").
# Non-raw strings so Python processes \uXXXX escapes into the actual Unicode codepoints
# before handing the pattern to the regex engine.
_CJK_DIGIT_SPACE = _re.compile("(\\d)\\s+([一-鿿㐀-䶿豈-﫿])")
_DIGIT_CJK_SPACE = _re.compile("([一-鿿㐀-䶿豈-﫿])\\s+(\\d)")


def _normalize(s: str) -> str:
    if not isinstance(s, str):
        s = str(s)
    s = s.strip().lower()
    # Strip leading ISO date prefix on time-like values BEFORE hyphen→space.
    s = _ISO_DATE_PREFIX.sub("", s)
    # Treat hyphens as spaces: "5th-floor" ≡ "5th floor", "on-call" ≡ "on call".
    s = s.replace("-", " ").replace("—", " ").replace("–", " ")
    # Drop ":00" minute suffix BEFORE punctuation stripping wipes the colon.
    s = _HOUR_ZERO_MINUTE.sub(r"\1", s)
    # Collapse spaces between digits and CJK characters (Qwen3 style):
    # "5 楼" → "5楼", "今晚 7 点" → "今晚7点", "502 号" → "502号"
    s = _CJK_DIGIT_SPACE.sub(r"\1\2", s)
    s = _DIGIT_CJK_SPACE.sub(r"\1\2", s)
    for ch in _PUNCT_STRIP:
        s = s.replace(ch, "")
    s = " ".join(s.split())
    # Strip a single leading determiner/quantifier.
    for d in _LEADING_DETERMINERS_EN:
        if s.startswith(d):
            s = s[len(d):]
            break
    for d in _LEADING_DETERMINERS_ZH:
        if s.startswith(d):
            s = s[len(d):]
            break
    return s


def _resolve_key(canonical_key: str, actual_keys, key_aliases) -> Optional[str]:
    """Find the actual dict key that matches a canonical expected key."""
    if canonical_key in actual_keys:
        return canonical_key
    aliases = key_aliases.get(canonical_key, []) if key_aliases else []
    norm_aliases = {_normalize(a) for a in aliases}
    norm_aliases.add(_normalize(canonical_key))
    for ak in actual_keys:
        if _normalize(ak) in norm_aliases:
            return ak
    return None


def _value_matches(actual_value, canonical_value: str, field: str, value_synonyms) -> bool:
    """Check whether actual_value is an acceptable surface form of canonical_value."""
    if actual_value is None:
        return False
    # Booleans / numbers: stringify and compare via normalized equality.
    if not isinstance(actual_value, str):
        actual_value = str(actual_value)

    accepted = []
    if value_synonyms and field in value_synonyms:
        accepted = list(value_synonyms[field].get(canonical_value, []))
    accepted.append(canonical_value)
    accepted_norm = {_normalize(a) for a in accepted}

    return _normalize(actual_value) in accepted_norm


def compare_extraction(actual, expected, key_aliases=None, value_synonyms=None) -> bool:
    """Compare an extracted JSON object against a ground-truth dict.

    Rules:
      - Every expected key must have a matching key (or alias) in actual.
      - Every expected value must match (after normalization) one of the
        declared synonyms for that (field, canonical_value) pair, or the
        canonical itself.
      - Extra keys in actual are ignored (the model may volunteer more).
      - No fuzzy substring fallback; no string-to-dict coercion.
    """
    if not isinstance(actual, dict) or not isinstance(expected, dict):
        return False
    for canon_key, canon_val in expected.items():
        ak = _resolve_key(canon_key, list(actual.keys()), key_aliases or {})
        if ak is None:
            return False
        if not _value_matches(actual[ak], canon_val, canon_key, value_synonyms or {}):
            return False
    return True


# Back-compat shim: the old name pointed at a recursive compare with hidden
# synonym tables. New callers should use compare_extraction with metadata.
def compare_json(actual: Any, expected: Any) -> bool:
    """Deprecated: strict structural equality only. Use compare_extraction."""
    if isinstance(actual, dict) and isinstance(expected, dict):
        if set(actual.keys()) != set(expected.keys()):
            # Allow extras in actual.
            if not set(expected.keys()).issubset(actual.keys()):
                return False
        return all(compare_json(actual[k], expected[k]) for k in expected)
    if isinstance(actual, list) and isinstance(expected, list):
        return len(actual) == len(expected) and all(
            compare_json(a, e) for a, e in zip(actual, expected)
        )
    if isinstance(actual, str) and isinstance(expected, str):
        return _normalize(actual) == _normalize(expected)
    return actual == expected
