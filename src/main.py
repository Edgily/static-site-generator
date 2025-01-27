from textnode import TextNode, TextType, text_node_to_html_node
from htmlnode import HTMLNode, LeafNode, ParentNode

def main():
    test_node = TextNode("some text", TextType.BOLD, "someurl.woo")
    # print(test_node)

    test_html_node = HTMLNode('p', 'paragraph text', [], {"href": "someurl.url", "target": "_blank"})
    # print(test_html_node.attributes_to_html())

    test_leaf_node = LeafNode("a", "Click here", {"href": "https://example.com"})
    # print(test_leaf_node)

    test_parent_node = ParentNode(
        "div",
        [
            ParentNode(
                "nav",
                [
                    LeafNode("span", "Home", {"class": "nav-item"}),
                    LeafNode("span", "About", {"class": "nav-item active"}),
                    LeafNode("span", "Contact", {"class": "nav-item"}),
                ],
                {"class": "navigation", "role": "navigation"},
            ),
            ParentNode(
                "section",
                [
                    LeafNode("h1", "Welcome!", {"class": "title"}),
                    ParentNode(
                        "div",
                        [
                            LeafNode("p", "This is a test page", {"class": "intro"}),
                            LeafNode("span", "Important note:", {"class": "note"}),
                            LeafNode(
                                "em", "Please read carefully", {"class": "emphasis"}
                            ),
                        ],
                        {"class": "content-wrapper"},
                    ),
                ],
                {"class": "main-content", "id": "main"},
            ),
            LeafNode("span", "Footer text", {"class": "footer-text"}),
        ],
        {"class": "container", "data-theme": "light"},
    )
    # print(test_parent_node.to_html())

    test_text_node = TextNode("VALUE", TextType.LINK, "someurl.woo")
    test_input = text_node_to_html_node(test_text_node)
    test_output = 0
    print("PRINT???", test_input)

if __name__ == "__main__":
    main()
