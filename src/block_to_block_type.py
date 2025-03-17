from enum import Enum


class BlockType(Enum):
    PARAGRAPH = ""
    HEADING = "#"
    CODE = "```"
    QUOTE = ">"
    UNORDERED_LIST = "* "
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
    if block[:1] == ">":
        split_lines = block.splitlines()
        all_lines_pass = all(line[:1] == ">" for line in split_lines)
        if all_lines_pass:
            block_type = ">"

    # UNORDERED LIST
    if block[:2] == "* " or block[:2] == "- ":
        split_lines = block.splitlines()
        all_lines_pass = all(
            line[:2] == "* " or line[:2] == "- " for line in split_lines
        )
        if all_lines_pass:
            block_type = "* "

    # ORDERED LIST
    if block[0].isdigit() and block[1] == ".":
        split_lines = block.splitlines()
        all_lines_pass = all(
            line[0].isdigit() and line[1:3] == ". " for line in split_lines
        )
        if all_lines_pass:
            block_type = "1. "

    return BlockType(block_type)
