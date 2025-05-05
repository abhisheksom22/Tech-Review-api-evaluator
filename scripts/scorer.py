import os
import json
import csv
import openai
from dotenv import load_dotenv
import utils  # this works since you're in project root when running

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

RESULTS_DIR = "results"
CSV_PATH = os.path.join(RESULTS_DIR, "scores.csv")

def load_outputs(file_name):
    with open(os.path.join(RESULTS_DIR, file_name), "r") as f:
        return json.load(f)

def evaluate_with_gpt(code, task, output):
    prompt = f"""
You are an expert software reviewer. Based on the given code and the model-generated response, evaluate the response for:

1. Accuracy (1-5): Does it correctly describe or handle the code?
2. Clarity (1-5): Is it easy to understand by a beginner?
3. Usefulness (1-5): Does it help a developer understand/debug/improve the code?

Return ONLY the following JSON:
{{"accuracy": 1-5, "clarity": 1-5, "usefulness": 1-5}}

DO NOT include any explanation or prefix.

Code:
```{code}```

Task: {task.upper()}

Model Output:
\"\"\"{output}\"\"\"
"""
    try:
        response = openai.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": prompt}],
            temperature=0
        )
        content = response.choices[0].message.content.strip()

        # Check if response starts with a JSON object
        if not content.startswith("{"):
            raise ValueError(f"Unexpected response format: {content[:60]}...")

        return json.loads(content)

    except Exception as e:
        print(f"❌ GPT evaluation failed: {e}")
        return {"accuracy": 0, "clarity": 0, "usefulness": 0}

def score_outputs(model_name, outputs, snippet_map):
    scored_rows = []
    for item in outputs:
        filename = item["filename"]
        code = snippet_map.get(filename, "")
        task = item["task"]
        output = item["output"]

        scores = evaluate_with_gpt(code, task, output)
        scored_rows.append({
            "filename": filename,
            "language": item["language"],
            "task": task,
            "model": model_name,
            "accuracy": scores["accuracy"],
            "clarity": scores["clarity"],
            "usefulness": scores["usefulness"]
        })

        print(f"Scored {filename} [{task}] → {scores}")
    return scored_rows

def save_to_csv(rows):
    with open(CSV_PATH, "w", newline="") as csvfile:
        fieldnames = ["filename", "language", "task", "model", "accuracy", "clarity", "usefulness"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)

def load_all_code_snippets():
    snippets = utils.read_code_snippets("code_snippets")
    return {s["filename"]: s["code"] for s in snippets}

def main():
    openai_outputs = load_outputs("openai_output.json")
    amazon_outputs = load_outputs("amazon_output.json")
    snippet_map = load_all_code_snippets()

    all_rows = []
    all_rows += score_outputs("openai", openai_outputs, snippet_map)
    all_rows += score_outputs("amazon", amazon_outputs, snippet_map)

    save_to_csv(all_rows)
    print(f"\nAll scores saved to: {CSV_PATH}")

if __name__ == "__main__":
    main()
