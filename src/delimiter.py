from textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []

    for node in old_nodes:
        if len(node.text) == 0:
            continue

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

        if first_section:
            new_nodes.append(TextNode(first_section, TextType.TEXT))
        new_nodes.append(TextNode(middle_section, text_type))
        if end_section:
            new_nodes.extend(
                split_nodes_delimiter(
                    [TextNode(end_section, TextType.TEXT)], delimiter, text_type
                )
            )

    return new_nodes


if __name__ == "__main__":
    print(
        split_nodes_delimiter(
            [
                TextNode(
                    "This *is italic* with more *italic* text.",
                    TextType.TEXT,
                )
            ],
            "*",
            TextType.ITALIC,
        )
    )
    print(
        split_nodes_delimiter(
            [
                TextNode(
                    "This **is bold** with more **bold** text.",
                    TextType.TEXT,
                )
            ],
            "**",
            TextType.BOLD,
        )
    )
    print(
        split_nodes_delimiter(
            [
                TextNode(
                    "This `is code` with more `code` text.",
                    TextType.TEXT,
                )
            ],
            "`",
            TextType.CODE,
        )
    )
