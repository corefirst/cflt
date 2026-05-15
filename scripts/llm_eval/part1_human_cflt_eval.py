import json
import os
import argparse
from typing import Dict, Any, List, Optional
from utils import (
    call_transformer, 
    validate_cflt_compliance, 
    load_dataset, 
    get_client_and_model, 
    MODELS_CONFIG, 
    LANG_MAP,
    RESULTS_DIR,
    SYSTEM_PROMPT_TEMPLATE
)

REPORT_OUTPUT_PATH = os.path.join(RESULTS_DIR, "part1_eval_report.md")

def run_benchmark(target_model_tag: Optional[str] = None):
    if not os.path.exists(RESULTS_DIR):
        os.makedirs(RESULTS_DIR)

    dataset = load_dataset()
    results = []

    tags_to_test = [target_model_tag] if target_model_tag else MODELS_CONFIG.keys()

    for tag in tags_to_test:
        if tag.startswith("ollama/"): continue # Skip local by default in benchmark unless specified
        
        try:
            client, model_name, config = get_client_and_model(tag)
        except ValueError as e:
            print(f"Skipping {tag}: {e}")
            continue

        print(f"Benchmarking model: {tag}...")
        model_results = {"model": tag, "cases": []}
        
        for case in dataset["test_cases"]:
            res = call_transformer(client, model_name, case["control"])
            metrics = validate_cflt_compliance(res)
            model_results["cases"].append({
                "id": case["id"],
                "input": case["control"],
                "metrics": metrics,
                "response": res
            })
            
        results.append(model_results)

    if results:
        generate_report(results)
    else:
        print("No models available to test.")

def generate_report(results: List[Dict[str, Any]]):
    raw_output_path = os.path.join(RESULTS_DIR, "part1_eval_raw.json")
    with open(raw_output_path, 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    print(f"Raw results saved at {raw_output_path}")

    report = "# CFLT Part I: Logic Transformer Benchmark\n\n"
    report += "## JSON Output Schema Reference\n"
    report += "```json\n"
    report += SYSTEM_PROMPT_TEMPLATE.split("## JSON Output Schema")[-1].strip()
    report += "\n```\n\n"

    for m in results:
        report += f"## Model: {m['model']}\n\n"
        report += "| Case ID | SC (Order) | SR (Subject) | IV (Inference) |\n"
        report += "| :--- | :--- | :--- | :--- |\n"
        for c in m["cases"]:
            report += f"| {c['id']} | {'✅' if c['metrics']['sc'] else '❌'} | {'✅' if c['metrics']['sr'] else '❌'} | {'✅' if c['metrics']['iv'] else '❌'} |\n"
        report += "\n"
    
    with open(REPORT_OUTPUT_PATH, 'w', encoding='utf-8') as f:
        f.write(report)
    print(f"Part I Report generated at {REPORT_OUTPUT_PATH}")

def run_single_input(text: str, model_tag: Optional[str], source: str, target: str):
    source_full = "its original language" if source.lower() == "auto" else LANG_MAP.get(source, source)
    target_full = LANG_MAP.get(target, target)
    
    model_tag = model_tag or "openai/gpt-5"
    
    try:
        client, model_name, config = get_client_and_model(model_tag)
    except ValueError as e:
        print(f"Error: {e}")
        return

    print(f"Processing: '{text}'")
    print(f"Route: {source_full} -> {target_full} (Model: {model_tag})")
    
    res = call_transformer(client, model_name, text, source_full, target_full, target_full)
    
    if "error" in res:
        print(f"Failed: {res['error']}")
    else:
        print("\n--- CFLT Transformation Result ---")
        print(json.dumps(res, indent=2, ensure_ascii=False))
        metrics = validate_cflt_compliance(res)
        print("\n--- Compliance Metrics ---")
        print(f"SC (Order): {'✅' if metrics['sc'] else '❌'}")
        print(f"SR (Subject): {'✅' if metrics['sr'] else '❌'}")
        print(f"IV (Inference): {'✅' if metrics['iv'] else '❌'}")

def main():
    parser = argparse.ArgumentParser(description="CFLT Logic Transformer Evaluator")
    parser.add_argument("--input", type=str, help="Single input text to transform")
    parser.add_argument("--model", type=str, help="Model tag to use (e.g., google/gemini-3.1-flash-lite)")
    parser.add_argument("--source", type=str, default="auto", help="Source language code")
    parser.add_argument("--target", type=str, default="en", help="Target language code")
    parser.add_argument("--benchmark", action="store_true", help="Run the full benchmark suite")

    args = parser.parse_args()

    if args.input:
        run_single_input(args.input, args.model, args.source, args.target)
    elif args.benchmark:
        run_benchmark(args.model)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
