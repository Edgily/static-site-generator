import unittest

from split_nodes import split_nodes_link, split_nodes_image
from textnode import TextNode, TextType


class TestSplitNodesLink(unittest.TestCase):
    def test_not_list(self):
        with self.assertRaises(ValueError) as context:
            split_nodes_link("not a list")
        self.assertEqual(str(context.exception), "The provided input is not a list.")

    def test_empty_list(self):
        nodes = []
        new_nodes = split_nodes_link(nodes)
        self.assertEqual(len(new_nodes), 0)

    def test_no_text(self):
        nodes = [TextNode("", TextType.TEXT)]
        with self.assertRaises(ValueError) as context:
            split_nodes_link(nodes)
        self.assertEqual(str(context.exception), "The provided node has no text.")

    def test_wrong_node_type(self):
        nodes = [TextNode("Text", TextType.CODE)]
        new_nodes = split_nodes_link(nodes)
        self.assertEqual(new_nodes[0].text, "Text")
        self.assertEqual(new_nodes[0].text_type, TextType.CODE)

    def test_no_link(self):
        nodes = [TextNode("Just plain text", TextType.TEXT)]
        new_nodes = split_nodes_link(nodes)
        self.assertEqual(len(new_nodes), 1)
        self.assertEqual(new_nodes[0].text, "Just plain text")
        self.assertEqual(new_nodes[0].text_type, TextType.TEXT)

    def test_single_link(self):
        node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is text with a link ", TextType.TEXT),
                TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
            ],
        )

    def test_multiple_links(self):
        nodes = [
            TextNode(
                "Click [here](https://boot.dev) or [there](https://youtube.com)",
                TextType.TEXT,
            )
        ]
        new_nodes = split_nodes_link(nodes)
        self.assertEqual(len(new_nodes), 4)
        self.assertEqual(new_nodes[0].text, "Click ")
        self.assertEqual(new_nodes[0].text_type, TextType.TEXT)
        self.assertEqual(new_nodes[1].text, "here")
        self.assertEqual(new_nodes[1].text_type, TextType.LINK)
        self.assertEqual(new_nodes[1].url, "https://boot.dev")
        self.assertEqual(new_nodes[2].text, " or ")
        self.assertEqual(new_nodes[2].text_type, TextType.TEXT)
        self.assertEqual(new_nodes[3].text, "there")
        self.assertEqual(new_nodes[3].text_type, TextType.LINK)
        self.assertEqual(new_nodes[3].url, "https://youtube.com")

    def test_consecutive_links(self):
        nodes = [
            TextNode("[one](https://boot.dev)[two](https://youtube.com)", TextType.TEXT)
        ]
        new_nodes = split_nodes_link(nodes)
        self.assertEqual(len(new_nodes), 2)
        self.assertEqual(new_nodes[0].text, "one")
        self.assertEqual(new_nodes[0].text_type, TextType.LINK)
        self.assertEqual(new_nodes[0].url, "https://boot.dev")
        self.assertEqual(new_nodes[1].text, "two")
        self.assertEqual(new_nodes[1].text_type, TextType.LINK)
        self.assertEqual(new_nodes[1].url, "https://youtube.com")

    def test_mixed_node_types(self):
        nodes = [
            TextNode("Code block", TextType.CODE),
            TextNode("Normal text with ![alt](url)", TextType.TEXT),
            TextNode("Link text", TextType.LINK, "url"),
        ]
        new_nodes = split_nodes_image(nodes)

        self.assertEqual(new_nodes[0].text, "Code block")
        self.assertEqual(new_nodes[0].text_type, TextType.CODE)

        self.assertEqual(new_nodes[1].text, "Normal text with ")
        self.assertEqual(new_nodes[1].text_type, TextType.TEXT)
        self.assertEqual(new_nodes[2].text, "alt")
        self.assertEqual(new_nodes[2].text_type, TextType.IMAGE)

        self.assertEqual(new_nodes[3].text, "Link text")
        self.assertEqual(new_nodes[3].text_type, TextType.LINK)


class TestSplitNodesImage(unittest.TestCase):
    def test_not_list(self):
        with self.assertRaises(ValueError) as context:
            split_nodes_image("not a list")
        self.assertEqual(str(context.exception), "The provided input is not a list.")

    def test_empty_list(self):
        nodes = []
        new_nodes = split_nodes_image(nodes)
        self.assertEqual(len(new_nodes), 0)

    def test_no_text(self):
        nodes = [TextNode("", TextType.TEXT)]
        with self.assertRaises(ValueError) as context:
            split_nodes_image(nodes)
        self.assertEqual(str(context.exception), "The provided node has no text.")

    def test_wrong_node_type(self):
        nodes = [TextNode("Text", TextType.CODE)]
        new_nodes = split_nodes_image(nodes)
        self.assertEqual(new_nodes[0].text, "Text")
        self.assertEqual(new_nodes[0].text_type, TextType.CODE)

    def test_no_image(self):
        nodes = [TextNode("Just plain text", TextType.TEXT)]
        new_nodes = split_nodes_image(nodes)
        self.assertEqual(len(new_nodes), 1)
        self.assertEqual(new_nodes[0].text, "Just plain text")
        self.assertEqual(new_nodes[0].text_type, TextType.TEXT)

    def test_single_image(self):
        node = TextNode(
            "This is text with an image ![img1](https://www.img1.com)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is text with an image ", TextType.TEXT),
                TextNode("img1", TextType.IMAGE, "https://www.img1.com"),
            ],
        )

    def test_single_image_no_text(self):
        node = TextNode(
            "![img1](https://www.img1.com)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertEqual(
            new_nodes,
            [
                TextNode("img1", TextType.IMAGE, "https://www.img1.com"),
            ],
        )

    def test_multiple_images(self):
        nodes = [
            TextNode(
                "Img1 ![img1](https://img1.com) img2 ![img2](https://img2.com)",
                TextType.TEXT,
            )
        ]
        new_nodes = split_nodes_image(nodes)
        self.assertEqual(len(new_nodes), 4)
        self.assertEqual(new_nodes[0].text, "Img1 ")
        self.assertEqual(new_nodes[0].text_type, TextType.TEXT)
        self.assertEqual(new_nodes[1].text, "img1")
        self.assertEqual(new_nodes[1].text_type, TextType.IMAGE)
        self.assertEqual(new_nodes[1].url, "https://img1.com")
        self.assertEqual(new_nodes[2].text, " img2 ")
        self.assertEqual(new_nodes[2].text_type, TextType.TEXT)
        self.assertEqual(new_nodes[3].text, "img2")
        self.assertEqual(new_nodes[3].text_type, TextType.IMAGE)
        self.assertEqual(new_nodes[3].url, "https://img2.com")

    def test_consecutive_images(self):
        nodes = [
            TextNode(
                "![img1](https://img1.com)![img2](https://img2.com)", TextType.TEXT
            )
        ]
        new_nodes = split_nodes_image(nodes)
        self.assertEqual(len(new_nodes), 2)
        self.assertEqual(new_nodes[0].text, "img1")
        self.assertEqual(new_nodes[0].text_type, TextType.IMAGE)
        self.assertEqual(new_nodes[0].url, "https://img1.com")
        self.assertEqual(new_nodes[1].text, "img2")
        self.assertEqual(new_nodes[1].text_type, TextType.IMAGE)
        self.assertEqual(new_nodes[1].url, "https://img2.com")

    def test_mixed_node_types(self):
        nodes = [
            TextNode("Code block", TextType.CODE),
            TextNode("Normal text with ![alt](url)", TextType.TEXT),
            TextNode("Link text", TextType.LINK, "url"),
        ]
        new_nodes = split_nodes_image(nodes)

        self.assertEqual(new_nodes[0].text, "Code block")
        self.assertEqual(new_nodes[0].text_type, TextType.CODE)

        self.assertEqual(new_nodes[1].text, "Normal text with ")
        self.assertEqual(new_nodes[1].text_type, TextType.TEXT)
        self.assertEqual(new_nodes[2].text, "alt")
        self.assertEqual(new_nodes[2].text_type, TextType.IMAGE)

        self.assertEqual(new_nodes[3].text, "Link text")
        self.assertEqual(new_nodes[3].text_type, TextType.LINK)
