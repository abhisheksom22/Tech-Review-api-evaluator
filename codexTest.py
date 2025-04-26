import openai
import os
from dotenv import load_dotenv

load_dotenv()


# Paste your API key here
openai.api_key = os.getenv("OPENAI_API_KEY")

# Example Python code to summarize
code_to_summarize = """
def add_numbers(a, b):
    return a + b
"""

# Example Python code to summarize
code_to_summarize = """
def add_numbers(a, b):
    return a + b
"""

prompt = f"Summarize the following code in easy way so that it is understandable by someone has never done coding:\n{code_to_summarize}"

# Updated call using Chat Completions (gpt-3.5 or gpt-4)
response = openai.chat.completions.create(
    model="gpt-4o",  # or "gpt-4", "gpt-3.5-turbo"
    messages=[
        {"role": "system", "content": "You are a helpful assistant that summarizes code."},
        {"role": "user", "content": prompt}
    ],
    temperature=0,
    max_tokens=150
)

print("Summary:\n", response.choices[0].message.content.strip())

