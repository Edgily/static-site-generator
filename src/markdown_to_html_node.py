from htmlnode import HTMLNode, LeafNode, ParentNode
from markdown_to_blocks import markdown_to_blocks
from block_to_block_type import block_to_block_type
from test_text_to_textnodes import text_to_textnodes
from textnode import text_node_to_html_node, TextNode, TextType


def text_to_children(text):
    text_nodes = text_to_textnodes(text)

    html_nodes = []

    for text_node in text_nodes:
        html_node = text_node_to_html_node(text_node)
        html_nodes.append(html_node)

    return html_nodes


def handle_block(block, block_type):
    if block_type == "PARAGRAPH":
        children = text_to_children(block.replace("\n", " "))
        return HTMLNode("p", None, children)
    elif block_type == "HEADING":
        heading_level = block.count("#")
        remove_hashes = block.replace("#", "").strip()
        children = text_to_children(remove_hashes)

        return HTMLNode(f"h{heading_level}", None, children)
    elif block_type == "CODE":
        remove_backticks = block.replace("```", "").strip()
        text_node = TextNode(remove_backticks, TextType.CODE)
        code_node = text_node_to_html_node(text_node)
        pre_node = HTMLNode("pre", None, [code_node], None)

        return pre_node
    elif block_type == "QUOTE":
        lines = block.splitlines()
        processed_lines = []
        for line in lines:
            if line.startswith(">"):
                processed_lines.append(line[1:].strip())
            else:
                processed_lines.append(line)
        join_processed = "\n".join(processed_lines)
        children = text_to_children(join_processed)
        quote_node = HTMLNode("blockquote", None, children, None)
        
        return quote_node
    elif block_type == "UNORDERED_LIST":
        lines = block.splitlines()
        processed_lines = []

        for line in lines:
            if line.startswith("- ") or line.startswith("* "):
                processed_lines.append(line[2:].strip())
            else:
                processed_lines.append(line)

        processed_lines = list(map(lambda x: HTMLNode("li", None, text_to_children(x)), processed_lines))
        ul_node = HTMLNode("ul", None, processed_lines, None)

        return ul_node
    elif block_type == "ORDERED_LIST":
        lines = block.splitlines()
        processed_lines = []
        
        for line in lines:
            if line[0].isdigit() and line[1] == "." and line[2] == " ":
                processed_lines.append(line[3:].strip())
            else:
                processed_lines.append(line)

        processed_lines = list(map(lambda x: HTMLNode("li", None, text_to_children(x)), processed_lines))
        ol_node = HTMLNode("ol", None, processed_lines, None)

        return ol_node

def markdown_to_html_node(md):
    blocks = markdown_to_blocks(md)

    children = []

    for block in blocks:
        block_type = block_to_block_type(block).name
        html_node = handle_block(block, block_type)
        children.append(html_node)

    return HTMLNode("div", None, children)
