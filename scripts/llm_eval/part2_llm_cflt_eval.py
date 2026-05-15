import json
import os
import time
import argparse
from typing import Dict, Any, List, Optional
from utils import (
    get_client_and_model,
    load_dataset,
    compare_json,
    MODELS_CONFIG,
    RESULTS_DIR
)

REPORT_OUTPUT_PATH = os.path.join(RESULTS_DIR, "part2_llm_eval_report.md")

def call_llm_basic(client, model: str, prompt: str, ground_truth: Any = None) -> Dict[str, Any]:
    try:
        system_content = "You are a logical assistant. Output JSON only."
        if isinstance(ground_truth, dict):
            keys = ", ".join(ground_truth.keys())
            system_content += f" Extract information using exactly these keys: {keys}."
            # Provide value hints if ground truth values are simple strings
            hints = [f"'{k}' should be like '{v}'" for k, v in ground_truth.items() if isinstance(v, str) and len(v) < 20]
            # Provide nested structure hints for list-of-dict values
            for k, v in ground_truth.items():
                if isinstance(v, list) and v and isinstance(v[0], dict):
                    nested_keys = ", ".join(v[0].keys())
                    hints.append(f"'{k}' entries should have keys: {nested_keys}")
            if hints:
                system_content += f" Guidance: {'; '.join(hints)}."
            
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": system_content},
                {"role": "user", "content": prompt}
            ],
            response_format={"type": "json_object"}
        )
        usage = response.usage
        
        def to_dict(obj):
            if hasattr(obj, "model_dump"):
                return obj.model_dump()
            return str(obj) if obj else {}

        return {
            "content": json.loads(response.choices[0].message.content),
            "usage": {
                "prompt_tokens": usage.prompt_tokens,
                "completion_tokens": usage.completion_tokens,
                "total_tokens": usage.total_tokens,
                "prompt_details": to_dict(getattr(usage, "prompt_tokens_details", None)),
                "completion_details": to_dict(getattr(usage, "completion_tokens_details", None))
            }
        }
    except Exception as e:
        print(f"  Error calling {model}: {e}")
        return {"error": str(e)}

def run_comparison(client, model_name: str, control_text: str, experimental_text: str, ground_truth: Any):
    # 1. Run Control
    res_control = call_llm_basic(client, model_name, control_text, ground_truth)
    # 2. Run Experimental
    res_cflt = call_llm_basic(client, model_name, experimental_text, ground_truth)
    
    def get_metrics(res):
        if "error" in res:
            return {"accuracy": False, "tokens": 0, "total": 0, "response": None, "error": res["error"]}
        usage = res.get("usage", {})
        accuracy = compare_json(res.get("content"), ground_truth)
        if not accuracy:
            print(f"    [Mismatch] Expected: {ground_truth}, Got: {res.get('content')}")
            
        return {
            "accuracy": accuracy,
            "tokens": usage.get("prompt_tokens", 0),
            "total": usage.get("total_tokens", 0),
            "details": usage,
            "response": res.get("content")
        }

    return {
        "control": get_metrics(res_control),
        "cflt": get_metrics(res_cflt)
    }

def run_benchmark(model_tags: List[str]):
    if not os.path.exists(RESULTS_DIR):
        os.makedirs(RESULTS_DIR)

    dataset = load_dataset()
    results = []

    for tag in model_tags:
        try:
            client, model_name, config = get_client_and_model(tag)
        except ValueError as e:
            print(f"Skipping {tag}: {e}")
            continue

        print(f"Testing model: {tag}...")
        model_results = {"model": tag, "cases": []}
        
        for case in dataset["test_cases"]:
            print(f"  Running Case {case['id']}...")
            metrics = run_comparison(client, model_name, case["control"], case["experimental"], case["ground_truth"])
            metrics["id"] = case["id"]
            metrics["level"] = case["level"]
            metrics["input_control"] = case["control"]
            metrics["input_experimental"] = case["experimental"]
            metrics["ground_truth"] = case["ground_truth"]
            model_results["cases"].append(metrics)
            
        results.append(model_results)

    if results:
        generate_report(results)
    else:
        print("No models available to test.")

def generate_report(results: List[Dict[str, Any]]):
    # Save raw JSON for human audit
    raw_output_path = os.path.join(RESULTS_DIR, "part2_eval_raw.json")
    with open(raw_output_path, 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    print(f"Raw results for human audit saved at {raw_output_path}")

    report = "# CFLT Part II: LLM Logic Verification Report\n\n"
    report += f"**Date:** {time.strftime('%Y-%m-%d %H:%M:%S')}\n\n"

    for model_res in results:
        report += f"## Model: {model_res['model']}\n\n"
        report += "| Case ID | Level | Accuracy (Ctrl/CFLT) | Total Tokens (Ctrl/CFLT) | Gain (%) |\n"
        report += "| :--- | :--- | :--- | :--- | :--- |\n"
        
        for case in model_res["cases"]:
            ctrl_acc = "✅" if case["control"]["accuracy"] else "❌"
            cflt_acc = "✅" if case["cflt"]["accuracy"] else "❌"
            
            ctrl_total = case["control"]["total"]
            cflt_total = case["cflt"]["total"]
            
            if ctrl_total > 0:
                gain = ((ctrl_total - cflt_total) / ctrl_total) * 100
                gain_str = f"{gain:+.1f}%"
            else:
                gain_str = "N/A"
            
            report += f"| {case['id']} | {case['level']} | {ctrl_acc} / {cflt_acc} | {ctrl_total} / {cflt_total} | {gain_str} |\n"
        
        report += "\n---\n\n"

    with open(REPORT_OUTPUT_PATH, 'w', encoding='utf-8') as f:
        f.write(report)
    print(f"Report generated at {REPORT_OUTPUT_PATH}")

def main():
    parser = argparse.ArgumentParser(description="CFLT Phase 2: LLM Verification Evaluator")
    parser.add_argument("--models", type=str, help="Comma-separated model tags (e.g., openai/gpt-5,google/gemini-3.1-pro)")
    parser.add_argument("--file", type=str, help="JSON file containing test cases")
    parser.add_argument("--benchmark", action="store_true", help="Run the full benchmark suite")

    args = parser.parse_args()

    model_tags = args.models.split(",") if args.models else ["openai/gpt-5"]

    if args.file:
        print(f"Feature to run benchmark from {args.file} is not yet implemented.")
    elif args.benchmark or not any(vars(args).values()):
        run_benchmark(model_tags)

if __name__ == "__main__":
    main()
