# scripts/utils.py

import os

def read_code_snippets(root_dir="code_snippets"):
    snippets = []
    for lang in os.listdir(root_dir):
        lang_dir = os.path.join(root_dir, lang)
        if not os.path.isdir(lang_dir):
            continue
        for file in os.listdir(lang_dir):
            if file.endswith(".py") or file.endswith(".cpp"):
                with open(os.path.join(lang_dir, file), "r") as f:
                    code = f.read()
                snippets.append({
                    "filename": file,
                    "language": lang,
                    "code": code
                })
    return snippets
