# openAI.py

import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def summarize_with_openai(prompt):
    response = openai.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that explains code."},
            {"role": "user", "content": prompt}
        ],
        temperature=0,
        max_tokens=300
    )
    return response.choices[0].message.content.strip()
