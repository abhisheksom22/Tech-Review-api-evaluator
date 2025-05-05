import os
import json
from scripts.utils import read_code_snippets
from scripts.openAI import summarize_with_openai
from scripts.amazonbedrock import summarize_with_claude

OUTPUT_DIR = "results"
TASKS = ["summarization", "documentation", "bug_detection"]

def generate_prompt(code, task):
    if task == "summarization":
        return f"Summarize the code in such a way that it is easy to understand by beginner:\n\n{code}"
    elif task == "documentation":
        return f"Write detailed documentation for the following code:\n\n{code}"
    elif task == "bug_detection":
        return f"Identify and explain possible bugs in this code:\n\n{code}"
    else:
        raise ValueError("Invalid task")

def run_all():
    openai_results = []
    claude_results = []
    snippets = read_code_snippets("code_snippets")

    for snippet in snippets:
        for task in TASKS:
            prompt = generate_prompt(snippet["code"], task)

            print(f"\n▶️ {snippet['filename']} [{snippet['language']}] - {task}")

            try:
                openai_resp = summarize_with_openai(prompt)
            except Exception as e:
                openai_resp = f"Error: {str(e)}"

            try:
                claude_resp = summarize_with_claude(prompt)
            except Exception as e:
                claude_resp = f"Error: {str(e)}"

            openai_results.append({
                "filename": snippet["filename"],
                "language": snippet["language"],
                "task": task,
                "model": "openai",
                "output": openai_resp
            })

            claude_results.append({
                "filename": snippet["filename"],
                "language": snippet["language"],
                "task": task,
                "model": "claude",
                "output": claude_resp
            })

    # Save both results separately
    with open(os.path.join(OUTPUT_DIR, "openai_output.json"), "w") as f:
        json.dump(openai_results, f, indent=2)

    with open(os.path.join(OUTPUT_DIR, "amazon_output.json"), "w") as f:
        json.dump(claude_results, f, indent=2)

    print("\nAll results saved to results/openai_output.json and results/amazon_output.json")

if __name__ == "__main__":
    run_all()
