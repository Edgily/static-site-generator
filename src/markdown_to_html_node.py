from htmlnode import HTMLNode, LeafNode, ParentNode
from markdown_to_blocks import markdown_to_blocks
from block_to_block_type import block_to_block_type
from test_text_to_textnodes import text_to_textnodes
from textnode import text_node_to_html_node, TextNode, TextType


def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    print(text_nodes)

    html_nodes = []

    for text_node in text_nodes:
        html_node = text_node_to_html_node(text_node)
        html_nodes.append(html_node)

    return html_nodes


def handle_block(block, block_type):
    if block_type == "PARAGRAPH":
        children = text_to_children(block)
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
        remove_delimiter = block.replace(">", "").strip()
        children = text_to_children(remove_delimiter)
        quote_node = HTMLNode("blockquote", None, children, None)
        
        return quote_node
    elif block_type == "UNORDERED_LIST":
        # Split the block into lines
        # For each line, remove the "- " or "* " at the beginning
        # Process each line for inline formatting
        # Create an HTMLNode with tag "li" for each processed line
        # Collect all "li" nodes and make them children of an HTMLNode with tag "ul"
        pass
    elif block_type == "ORDERED_LIST":
        # Similar to unordered lists, but remove the "1. ", "2. ", etc. at the beginning
        # Create an HTMLNode with tag "ol" instead of "ul"
        pass


paragraph_test_input = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with *italic* text and `code` here

"""

heading_test_input = """
# Heading 1

## Heading 2

### Heading 3

#### Heading 4

##### Heading 5

###### Heading 6
"""

code_test_input = """
```
def hello_world():
    print("Hello, world!")
    
# This is a comment
for i in range(5):
    print(i)
```
"""

quote_test_input = """
> This is a quote
> with **multiple** lines
> 
> And a blank line in between
"""

def markdown_to_html_node(md):
    blocks = markdown_to_blocks(md)

    children = []

    for block in blocks:
        block_type = block_to_block_type(block).name
        html_node = handle_block(block, block_type)
        children.append(html_node)

    return HTMLNode("div", None, children)


# needs to return:
# "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>"

if __name__ == "__main__":
    print("FINAL:", markdown_to_html_node(quote_test_input))
