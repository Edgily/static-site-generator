def extract_title(md):
    split_lines = md.splitlines()
    for line in split_lines:
        if line.startswith("# "):
            return line[2:].strip()
    else:
        raise ValueError("No heading")