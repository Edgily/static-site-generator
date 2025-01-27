from enum import Enum
from htmlnode import LeafNode


class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"


class TextNode:
    def __init__(self, text, text_type, url=None):
        if not isinstance(text_type, TextType):
            raise ValueError("TextNode must have a valid TextType")
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        if not isinstance(other, TextNode):
            return False
        return (
            self.text == other.text
            and self.text_type == other.text_type
            and self.url == other.url
        )

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"


def text_node_to_html_node(text_node):
    text = text_node.text
    text_type = text_node.text_type
    url = text_node.url

    match text_type:
        case TextType.TEXT:
            return LeafNode(None, text)
        case TextType.BOLD:
            return LeafNode("b", text)
        case TextType.ITALIC:
            return LeafNode("i", text)
        case TextType.CODE:
            return LeafNode("code", text)
        case TextType.LINK:
            if not text:
                raise ValueError("Link must have text")
            if not url:
                raise ValueError("Link must have URL")
            return LeafNode("a", text, {"href": url})
        case TextType.IMAGE:
            if not url:
                raise ValueError("Image must have URL")
            return LeafNode("img", "", {"src": url, "alt": text})
        case _:
            raise ValueError(f"Invalid text type: {text_type}")
