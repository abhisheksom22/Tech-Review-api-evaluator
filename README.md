# Tech Review: Comparing OpenAI and Amazon Bedrock APIs

This project evaluates and compares the performance of **OpenAI GPT-4o** and **Amazon Bedrock Claude 3 Sonnet** for three important software development tasks:

- Code Summarization  
- Code Documentation  
- Bug Detection  

We use 20 Python and C++ code snippets across different difficulty levels and evaluate responses using both **manual** and **LLM-based (GPT-4o)** scoring.

---

## Setup Instructions

### Create Virtual Environment

```bash
python3 -m venv codex_env
source codex_env/bin/activate
```

---

### Install Required Packages

```bash
pip install openai boto3 matplotlib pandas python-dotenv
```

---

### Configure API Keys

Create a `.env` file in the root directory and add the following:

```dotenv
# OpenAI
OPENAI_API_KEY=your_openai_api_key_here

# AWS Bedrock
AWS_ACCESS_KEY_ID=your_aws_access_key
AWS_SECRET_ACCESS_KEY=your_aws_secret_key
AWS_REGION=us-east-1
```

You can also configure AWS CLI for Bedrock (optional):

```bash
aws configure
# Enter access key, secret key, and region
```

---

## How to Run the Project

### Step 1: Run API Evaluation Script

```bash
python runner.py
```

This runs both OpenAI and Amazon Bedrock APIs for all Python and C++ snippets and saves results to:
- `results/openAI_output.json`
- `results/amazon_output.json`

---

### Step 2: Score Responses Using GPT-4o

```bash
python scripts/scorer.py
```

This uses GPT-4o to score each output on `accuracy`, `clarity`, and `usefulness`. It produces:
- `results/scores.csv`

---

### Step 3: Generate Comparison Graphs

```bash
python scripts/plot_scores.py
```

This generates visual bar graphs for:
- `results/summarization_comparison.png`
- `results/documentation_comparison.png`
- `results/bug_detection_comparison.png`

---

## Script Overview

| File | Description |
|------|-------------|
| `runner.py` | Main driver script that calls OpenAI and Bedrock APIs |
| `scripts/openAI.py` | Sends code + task to OpenAI GPT-4o |
| `scripts/amazonbedrock.py` | Sends code + task to Claude 3 Sonnet on Amazon Bedrock |
| `scripts/utils.py` | Helper for reading code snippets from `code_snippets/` folder |
| `scripts/scorer.py` | Uses GPT-4o to evaluate API responses and produce scores |
| `scripts/plot_scores.py` | Uses scores to generate visual graphs comparing models |

---

## Evaluation Details

We used a hybrid strategy for evaluation:

- **Manual Evaluation:** Scored by humans on 1–5 scale for:
  - Accuracy
  - Clarity
  - Usefulness

- **LLM Evaluation:** GPT-4o was used to simulate unbiased LLM-based scoring using structured prompts.

Final scores were averaged and stored in `scores.csv`.

---

## Output Format

Each result in the JSON output files contains:

```json
{
  "filename": "sum.cpp",
  "language": "cpp",
  "task": "documentation",
  "model": "openai",
  "output": "The sum.cpp file defines..."
}
```

---

## Project Repository

All code, graphs, data, and report available at:

[https://github.com/abhisheksom22/Tech-Review-api-evaluator.git](https://github.com/abhisheksom22/Tech-Review-api-evaluator.git)

---

## 👥 Authors

- **Abhishek Som** — [asom2@illinois.edu]  
- **Neel Harip** — [nhari7@illinois.edu]
