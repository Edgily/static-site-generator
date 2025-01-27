from textnode import TextNode, TextType
from extract_markdown_urls import extract_markdown_links

def split_text_link(text):
    extracted_links = extract_markdown_links(text)

    if len(extracted_links) == 0:
        if text == '':
            return []
        return [TextNode(text, TextType.TEXT)]
    
    link_text, url = extracted_links[0]
    parts = text.split(f"[{link_text}]({url})", 1)
    result = []

    if parts[0] != '':
        result.append(TextNode(parts[0], TextType.TEXT))
    result.append(TextNode(link_text, TextType.LINK, url))
    result.extend(split_text_link(parts[1]))

    return result

def split_nodes_link(nodes):
    if not isinstance(nodes, list):
        raise ValueError("The provided value is not a list.")
    new_nodes = []
    for node in nodes:        
        result_nodes = split_text_link(node.text)
        new_nodes.extend(result_nodes)
    return new_nodes


#TODO: Finish split_nodes_images
def split_nodes_images(nodes):
    pass


node = TextNode(
    "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
    TextType.TEXT,
)
new_nodes = split_nodes_link([node])
print(new_nodes)
