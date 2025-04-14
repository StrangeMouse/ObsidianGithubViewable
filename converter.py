import os
import re
from urllib.parse import quote
from pathlib import Path
import shutil

SOURCE_DIR = "."
TARGET_DIR = "converted"

def convert_wikilinks(content):
    # Handle embeds: ![[path/to/file|optional]]
    def embed_repl(match):
        path = match.group(1).strip()
        if "|" in path:
            path = path.split("|")[0].strip()
        path = path.replace(" ", "_")
        encoded_path = quote(path) + ".md"
        return f"![file]({encoded_path})"

    # Handle normal wikilinks: [[path/to/file|Display]]
    def link_repl(match):
        full = match.group(1).strip()
        parts = full.split("|")
        path = parts[0].strip().replace(" ", "_")
        display = parts[1].strip() if len(parts) > 1 else path.split("/")[-1]
        encoded_path = quote(path) + ".md"
        return f"[{display}]({encoded_path})"

    content = re.sub(r'!\[\[([^\]]+)\]\]', embed_repl, content)
    content = re.sub(r'\[\[([^\]]+)\]\]', link_repl, content)
    return content

def add_newline_before_latex(content):
    return re.sub(r'(?<!\n)(\$\$)', r'\n\1', content)

def escape_backslashes_in_latex(content):
    # Replace \\ with \\\\ inside $$ blocks
    def replacer(match):
        latex = match.group(0)
        return latex.replace("\\\\", "\\\\\\\\")
    return re.sub(r'\$\$(.*?)\$\$', replacer, content, flags=re.DOTALL)

def process_file(source_path, target_path):
    with open(source_path, 'r', encoding='utf-8') as f:
        content = f.read()

    content = convert_wikilinks(content)
    content = add_newline_before_latex(content)
    content = escape_backslashes_in_latex(content)

    os.makedirs(os.path.dirname(target_path), exist_ok=True)
    with open(target_path, 'w', encoding='utf-8') as f:
        f.write(content)

def rename_path_with_underscores(path):
    new_parts = [p.replace(" ", "_") for p in Path(path).parts]
    return os.path.join(*new_parts)

# Clean old converted dir if it exists
if os.path.exists(TARGET_DIR):
    shutil.rmtree(TARGET_DIR)

for root, _, files in os.walk(SOURCE_DIR):
    if root.startswith(TARGET_DIR) or ".git" in root or ".github" in root:
        continue

    for name in files:
        source_path = os.path.join(root, name)
        rel_path = os.path.relpath(source_path, SOURCE_DIR)

        # Skip this script and non-Obsidian files
        if os.path.abspath(source_path) == os.path.abspath(__file__):
            continue

        renamed_rel_path = rename_path_with_underscores(rel_path)
        target_path = os.path.join(TARGET_DIR, renamed_rel_path)

        if name.endswith(".md"):
            process_file(source_path, target_path)
        else:
            os.makedirs(os.path.dirname(target_path), exist_ok=True)
            shutil.copy2(source_path, target_path)
