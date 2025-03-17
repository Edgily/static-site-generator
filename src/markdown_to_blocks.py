import re


def markdown_to_blocks(markdown):
    if markdown == "":
        return []
    strip_whitespace = markdown.strip()
    split_on_two_empty_lines = re.split(r"\n{2,}", strip_whitespace)
    non_empty_lines = []
    for i in split_on_two_empty_lines:
        if i != "":
            non_empty_lines.append(i)

    return non_empty_lines
