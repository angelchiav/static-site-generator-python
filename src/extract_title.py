def extract_title(markdown: str) -> str:
    for line in markdown.split("\n"):
        if line.startswith("# "):
            title = line[2:].strip()
            if title == "":
                raise ValueError("Invalid H1: title is empty")
            return title
        
    raise ValueError("No H1 header found in markdown")