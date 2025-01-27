import unittest

from split_nodes import split_nodes_link
from textnode import TextNode, TextType


class TestSplitNodesLink(unittest.TestCase):
    def test_not_list(self):
        with self.assertRaises(ValueError) as context:
            split_nodes_link("not a list")
        self.assertEqual(str(context.exception), "The provided value is not a list.")

    def test_split_nodes_link_empty_list(self):
        nodes = []
        new_nodes = split_nodes_link(nodes)
        self.assertEqual(len(new_nodes), 0)

    def test_single_list_item(self):
        node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is text with a link ", TextType.TEXT),
                TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
                TextNode(" and ", TextType.TEXT),
                TextNode(
                    "to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"
                ),
            ],
        )

    def test_split_nodes_link_no_links(self):
        nodes = [TextNode("Just plain text", TextType.TEXT)]
        new_nodes = split_nodes_link(nodes)
        self.assertEqual(len(new_nodes), 1)
        self.assertEqual(new_nodes[0].text, "Just plain text")
        self.assertEqual(new_nodes[0].text_type, TextType.TEXT)

    def test_split_nodes_link_multiple_links(self):
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

    def test_split_nodes_link_consecutive(self):
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
