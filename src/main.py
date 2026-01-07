import sys

from copy_static import copy_static
from generate_page_recursive import generate_page_recursive

def normalize_base_path(basepath: str) -> str:
    if not basepath:
        return "/"
    if not basepath.startswith("/"):
        basepath = "/" + basepath
    if not basepath.endswith("/"):
        basepath = basepath + "/"
    return basepath

def main():
    basepath = sys.argv[1] if len(sys.argv) > 1 else "/"
    basepath = normalize_base_path(basepath)

    output_dir = "docs"
    copy_static("static", output_dir)
    generate_page_recursive("content", "template.html", output_dir, basepath)

if __name__ == "__main__":
    main()