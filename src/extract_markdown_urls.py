import re


def extract_markdown_images(markdown):
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", markdown)


def extract_markdown_links(markdown):
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", markdown)
