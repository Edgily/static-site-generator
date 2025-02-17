import unittest

from textnode import TextNode, TextType

from delimiter import split_nodes_delimiter


class TestSplitNodesDelimiter(unittest.TestCase):
    def test_multiple_bold(self):
        node = TextNode("This is **bold** and more **bold text**.", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)

        self.assertEqual(len(new_nodes), 5)

        self.assertEqual(new_nodes[0].text, "This is ")
        self.assertEqual(new_nodes[0].text_type, TextType.TEXT)

        self.assertEqual(new_nodes[1].text, "bold")
        self.assertEqual(new_nodes[1].text_type, TextType.BOLD)

        self.assertEqual(new_nodes[2].text, " and more ")
        self.assertEqual(new_nodes[2].text_type, TextType.TEXT)

        self.assertEqual(new_nodes[3].text, "bold text")
        self.assertEqual(new_nodes[3].text_type, TextType.BOLD)

        self.assertEqual(new_nodes[4].text, ".")
        self.assertEqual(new_nodes[4].text_type, TextType.TEXT)

    def test_multiple_italic(self):
        node = TextNode("This is *italic* and more *italic text*.", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "*", TextType.ITALIC)

        self.assertEqual(len(new_nodes), 5)

        self.assertEqual(new_nodes[0].text, "This is ")
        self.assertEqual(new_nodes[0].text_type, TextType.TEXT)

        self.assertEqual(new_nodes[1].text, "italic")
        self.assertEqual(new_nodes[1].text_type, TextType.ITALIC)

        self.assertEqual(new_nodes[2].text, " and more ")
        self.assertEqual(new_nodes[2].text_type, TextType.TEXT)

        self.assertEqual(new_nodes[3].text, "italic text")
        self.assertEqual(new_nodes[3].text_type, TextType.ITALIC)

        self.assertEqual(new_nodes[4].text, ".")
        self.assertEqual(new_nodes[4].text_type, TextType.TEXT)

    def test_multiple_code(self):
        node = TextNode("This is `code` and more `code text`.", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)

        self.assertEqual(len(new_nodes), 5)

        self.assertEqual(new_nodes[0].text, "This is ")
        self.assertEqual(new_nodes[0].text_type, TextType.TEXT)

        self.assertEqual(new_nodes[1].text, "code")
        self.assertEqual(new_nodes[1].text_type, TextType.CODE)

        self.assertEqual(new_nodes[2].text, " and more ")
        self.assertEqual(new_nodes[2].text_type, TextType.TEXT)

        self.assertEqual(new_nodes[3].text, "code text")
        self.assertEqual(new_nodes[3].text_type, TextType.CODE)

        self.assertEqual(new_nodes[4].text, ".")
        self.assertEqual(new_nodes[4].text_type, TextType.TEXT)

    def test_no_normal_text(self):
        node = TextNode("`code`", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(len(new_nodes), 1)
        self.assertEqual(new_nodes[0].text_type, TextType.CODE)

    def test_empty_text(self):
        node = TextNode("", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(len(new_nodes), 0)

    def test_no_delimiters(self):
        node = TextNode("This is plain text", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)

        self.assertEqual(len(new_nodes), 1)
        self.assertEqual(new_nodes[0].text, "This is plain text")
        self.assertEqual(new_nodes[0].text_type, TextType.TEXT)

    def test_unclosed_delimiter(self):
        node = TextNode("This is **unclosed*", TextType.TEXT)

        with self.assertRaises(ValueError) as context:
            split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(str(context.exception), "No closing delimiter ** found")
