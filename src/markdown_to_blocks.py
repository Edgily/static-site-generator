import re

input = '''   # This is a heading


This is a paragraph of text. It has some **bold** and *italic* words inside of it.

> Quote line 1
> Quote line 2


```This is some
Code on multiple
Lines```

- List item 1
- Listem item 2

1. ordered list 1
4. ordered list 2


* This is the first list item in a list block
* This is a list item
* This is another list item   '''

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

if __name__ == "__main__":
    print(markdown_to_blocks(input))