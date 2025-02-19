"""
We will support 6 types of markdown blocks:

paragraph
heading
code
quote
unordered_list
ordered_list

We need a way to inspect a block of markdown text and determine what type of block it is.

Assignment
Create a BlockType enum with the above markdown block types. ✅

Create a block_to_block_type function that takes a single block of markdown text as input and returns the BlockType representing the type of block it is. You can assume all leading and trailing whitespace was already stripped (we did that in a previous lesson).

Headings start with 1-6 # characters, followed by a space and then the heading text.

Code blocks must start with 3 backticks and end with 3 backticks.

Every line in a quote block must start with a > character.

Every line in an unordered list block must start with a * or - character, followed by a space.

Every line in an ordered list block must start with a number followed by a . character and a space. The number must start at 1 and increment by 1 for each line.

If none of the above conditions are met, the block is a normal paragraph.
"""

from enum import Enum


class BlockType(Enum):
    PARAGRAPH = ""
    HEADING = "#"
    CODE = "```"
    QUOTE = "> "
    UNORDERED_LIST = "* " or "- "
    ORDERED_LIST = "1. "


def block_to_block_type(block):
    if not isinstance(block, str):
        raise ValueError("Block must be a string value")

    # PARAGRAPH default case
    block_type = ""

    # HEADING
    if block[0] == "#":
        block_type = "#"

    # CODE
    if block[:3] == "```" and block[-3:] == "```":
        block_type = "```"

    # QUOTE
    if block[:2] == "> ":
        split_lines = block.splitlines()
        all_lines_pass = all(line[:2] == "> " for line in split_lines)
        if all_lines_pass:
            block_type = "> "

    # UNORDERED LIST
    if block[:2] == "* " or block[:2] == "- ":
        split_lines = block.splitlines()
        all_lines_pass = all(
            line[:2] == "* " or line[:2] == "- " for line in split_lines
        )
        if all_lines_pass:
            block_type = block[:2]

    # ORDERED LIST
    if block[0].isdigit() and block[1] == ".":
        split_lines = block.splitlines()
        all_lines_pass = all(
            line[0].isdigit() and line[1:3] == ". " for line in split_lines
        )
        if all_lines_pass:
            block_type = "1. "

    return BlockType(block_type)


if __name__ == "__main__":
    print(block_to_block_type("This is a paragraph"))
    print(block_to_block_type("# This is a heading"))
    print(block_to_block_type("```This is a code block```"))
    print(block_to_block_type("> Quote line 1\n> Quote line 2"))
    print(block_to_block_type("* List item 1\n- List item 2"))
    print(block_to_block_type("5. List item 1\n3. List item 2"))
