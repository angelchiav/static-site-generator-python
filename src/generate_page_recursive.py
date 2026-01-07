import os
from pathlib import Path

from generate_page import generate_page

def generate_page_recursive(dir_path_content: str, template_path: str, dest_dir_path: str):
    os.makedirs(dest_dir_path, exist_ok=True)

    for entry in os.listdir(dir_path_content):
        src_path = os.path.join(dir_path_content, entry)

        if os.path.isdir(src_path):
            dest_subdir = os.path.join(dest_dir_path, entry)
            generate_page_recursive(src_path, template_path, dest_subdir)
            continue

        if os.path.isfile(src_path) and entry.endswith(".md"):
            stem = Path(entry).stem

            if stem == "index":
                dest_file_path = os.path.join(dest_dir_path, "index.html")
            else:
                page_dir = os.path.join(dest_dir_path, stem)
                os.makedirs(page_dir, exist_ok=True)
                dest_file_path = os.path.join(page_dir, "index.html")

            generate_page(src_path, template_path, dest_file_path)