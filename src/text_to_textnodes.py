from textnode import TextNode, TextType
from delimiter import split_nodes_delimiter
from split_nodes import split_nodes_link, split_nodes_image


def text_to_textnodes(text):
    extract_images = split_nodes_image([TextNode(text, TextType.TEXT)])
    extract_links = split_nodes_link(extract_images)
    extract_bold = split_nodes_delimiter(extract_links, "**", TextType.BOLD)
    extract_italic = split_nodes_delimiter(extract_bold, "*", TextType.ITALIC)
    extract_code = split_nodes_delimiter(extract_italic, "`", TextType.CODE)

    return extract_code


if __name__ == "__main__":
    print(
        "RESULT:",
        text_to_textnodes(
            "*This is italic* with a `code block` with a [link](link.url) and some **bold text** beside an ![img](img.url) and `more code` and a [link2](link2.url) and **more bold text** with an ![img2](img2.url) ending in *italics again*."
        ),
    )
    print(
        "RESULT:",
        text_to_textnodes(""),
    )
