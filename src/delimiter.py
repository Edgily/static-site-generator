from textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    pass
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        delimiter_start = node.text.find(delimiter)
        delimiter_end = node.text.find(delimiter, delimiter_start + len(delimiter))

        if delimiter_start == -1:
            new_nodes.append(node)
            continue
        if delimiter_end == -1:
            raise ValueError(f"No closing delimiter {delimiter} found")

        first_section = node.text[:delimiter_start]
        middle_section = node.text[delimiter_start + len(delimiter) : delimiter_end]
        end_section = node.text[delimiter_end + len(delimiter) :]

        new_nodes.append(TextNode(first_section, TextType.TEXT))
        new_nodes.append(TextNode(middle_section, text_type))
        new_nodes.append(TextNode(end_section, TextType.TEXT))

    return new_nodes
