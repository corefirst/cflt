# Scripts

This directory contains utility scripts for the CFLT project.

## Setup

It is recommended to use a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r scripts/requirements.txt
```

## Configuration

The scripts use environment variables for API authentication. You can create a `.env` file in the project root:

```env
OPENAI_API_KEY=your_key_here
ANTHROPIC_API_KEY=your_key_here
GOOGLE_API_KEY=your_key_here
```

For local models, the scripts expect [Ollama](https://ollama.com/) to be running at `http://localhost:11434`.

---

# LLM Evaluation Scripts (`llm_eval/`)

These scripts benchmark Large Language Models against the CFLT (Core-First) methodology.

## Available Scripts

### 1. Logic Transformer Benchmark (`part1_human_cflt_eval.py`)
Evaluates how well a model can transform source text into the CFLT JSON format while adhering to core protocol rules:
- **Core-First Order**: Subject -> Reason -> Space -> Time.
- **Subject Preservation**: Ensuring the subject is kept in the core slot.
- **Inference Rationale**: Providing valid suggestions when slots are missing.

### 2. LLM Verification (`part2_llm_cflt_eval.py`)
Compares model performance (accuracy and token efficiency) between:
- **Control**: Native language input/output.
- **Experimental**: CFLT-structured input/output.

## Usage

Run the scripts from the project root:

```bash
python scripts/llm_eval/part1_human_cflt_eval.py
python scripts/llm_eval/part2_llm_cflt_eval.py
```

Results will be generated in the `results/` directory.
