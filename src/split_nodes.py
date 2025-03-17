from textnode import TextNode, TextType
from extract_markdown_urls import extract_markdown_links, extract_markdown_images


def split_text_link(text):
    extracted_links = extract_markdown_links(text)

    if len(extracted_links) == 0:
        if text == "":
            return []
        return [TextNode(text, TextType.TEXT)]

    link_text, url = extracted_links[0]
    parts = text.split(f"[{link_text}]({url})", 1)
    result = []

    if parts[0] != "":
        result.append(TextNode(parts[0], TextType.TEXT))
    result.append(TextNode(link_text, TextType.LINK, url))
    result.extend(split_text_link(parts[1]))

    return result


def split_nodes_link(nodes):
    if not isinstance(nodes, list):
        raise ValueError("The provided input is not a list.")

    new_nodes = []

    for node in nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        else:
            if not node.text:
                raise ValueError("The provided node has no text.")
            result_nodes = split_text_link(node.text)
            new_nodes.extend(result_nodes)
    return new_nodes


# LINKS above IMAGES below


def split_text_image(text):
    extracted_images = extract_markdown_images(text)

    if len(extracted_images) == 0:
        if text == "":
            return []
        return [TextNode(text, TextType.TEXT)]

    link_text, url = extracted_images[0]
    parts = text.split(f"![{link_text}]({url})", 1)
    result = []

    if parts[0] != "":
        result.append(TextNode(parts[0], TextType.TEXT))
    result.append(TextNode(link_text, TextType.IMAGE, url))
    result.extend(split_text_image(parts[1]))

    return result


def split_nodes_image(nodes):
    if not isinstance(nodes, list):
        raise ValueError("The provided input is not a list.")

    new_nodes = []

    for node in nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        else:
            if not node.text:
                raise ValueError("The provided node has no text.")
            result_nodes = split_text_image(node.text)
            new_nodes.extend(result_nodes)
    return new_nodes
