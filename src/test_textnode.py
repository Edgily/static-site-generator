import unittest

from textnode import TextNode, TextType, text_node_to_html_node

from htmlnode import LeafNode


class TestTextNode(unittest.TestCase):
    def test_invalid_text_type_raises_value_error(self):
        with self.assertRaisesRegex(ValueError, "TextNode must have a valid TextType"):
            node = TextNode("some text", "not a valid TextType")

    def test_invalid_text_type_attribute_error(self):
        with self.assertRaises(AttributeError):
            node = TextNode("some text", TextType.INVALID)

    def test_nodes_with_same_text_and_type_are_equal(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
        node3 = TextNode("This is a text node", TextType.LINK, "url")
        node4 = TextNode("This is a text node", TextType.LINK, "url")
        self.assertEqual(node3, node4)

    def test_nodes_with_different_text_or_type_are_not_equal(self):
        node = TextNode("This is a text node", TextType.CODE)
        node2 = TextNode("This is a text node", TextType.TEXT)
        self.assertNotEqual(node, node2)
        node3 = TextNode("This is a text node", TextType.BOLD)
        node4 = TextNode("This is a text", TextType.BOLD)
        self.assertNotEqual(node3, node4)
        node5 = TextNode("This is a text node", TextType.BOLD)
        node6 = TextNode("This is a text node", TextType.IMAGE, "url")
        self.assertNotEqual(node5, node6)
        node7 = TextNode("This is a text node", TextType.BOLD)
        node8 = "This is a text node"
        self.assertNotEqual(node7, node8)


class TestTextNodeToHtmlNode(unittest.TestCase):
    def test_empty_text_results_in_empty_html(self):
        text_node = TextNode("", TextType.TEXT)
        html_node = text_node_to_html_node(text_node)

        self.assertIsInstance(html_node, LeafNode)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "")

    def test_whitespace_text_results_in_whitespace_html(self):
        text_node = TextNode("   ", TextType.TEXT)
        html_node = text_node_to_html_node(text_node)

        self.assertIsInstance(html_node, LeafNode)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "   ")

    def test_nonempty_text_results_in_nonempty_html(self):
        text_node = TextNode("Some text", TextType.BOLD)
        html_node = text_node_to_html_node(text_node)

        self.assertIsInstance(html_node, LeafNode)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "Some text")

    def test_empty_text_results_in_empty_html(self):
        text_node = TextNode("", TextType.BOLD)
        html_node = text_node_to_html_node(text_node)

        self.assertIsInstance(html_node, LeafNode)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "")

    def test_whitespace_text_results_in_whitespace_html(self):
        text_node = TextNode("   ", TextType.BOLD)
        html_node = text_node_to_html_node(text_node)

        self.assertIsInstance(html_node, LeafNode)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "   ")

    def test_italic(self):
        text_node = TextNode("Some italic text", TextType.ITALIC)
        html_node = text_node_to_html_node(text_node)

        self.assertIsInstance(html_node, LeafNode)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "Some italic text")

    def test_italic_empty(self):
        text_node = TextNode("", TextType.ITALIC)
        html_node = text_node_to_html_node(text_node)

        self.assertIsInstance(html_node, LeafNode)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "")

    def test_italic_whitespace(self):
        text_node = TextNode("   ", TextType.ITALIC)
        html_node = text_node_to_html_node(text_node)

        self.assertIsInstance(html_node, LeafNode)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "   ")

    def test_code_node_with_text_results_in_code_html(self):
        text_node = TextNode("Some code text", TextType.CODE)
        html_node = text_node_to_html_node(text_node)

        self.assertIsInstance(html_node, LeafNode)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "Some code text")

    def test_code_node_with_special_characters_results_in_code_html(self):
        text_node = TextNode("Some code text with $p3c!4l$<>{}[]", TextType.CODE)
        html_node = text_node_to_html_node(text_node)

        self.assertIsInstance(html_node, LeafNode)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "Some code text with $p3c!4l$<>{}[]")

    def test_code_node_with_empty_text_results_in_empty_code_html(self):
        text_node = TextNode("", TextType.CODE)
        html_node = text_node_to_html_node(text_node)

        self.assertIsInstance(html_node, LeafNode)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "")

    def test_link_with_valid_text_and_url(self):
        text_node = TextNode('link.com', TextType.LINK, 'https://link.com/%%jflkajsdflkj??9fjasldkfjyes==')
        html_node = text_node_to_html_node(text_node)

        self.assertIsInstance(html_node, LeafNode)
        self.assertEqual(html_node.tag, "a")
        assert html_node.attributes.get("href") == "https://link.com/%%jflkajsdflkj??9fjasldkfjyes=="
        self.assertEqual(html_node.value, "link.com")
    
    def test_link_without_text_raises_value_error(self):
        with self.assertRaisesRegex(ValueError, "Link must have text"):
            text_node = TextNode('', TextType.LINK, 'https://link.com')
            html_node = text_node_to_html_node(text_node)
    
    def test_link_without_url_raises_value_error(self):
        with self.assertRaisesRegex(ValueError, "Link must have URL"):
            text_node = TextNode('Link<><><**FJLSADKFJ text', TextType.LINK, '')
            html_node = text_node_to_html_node(text_node)

    def test_image_node_with_valid_alt_text_and_url_results_in_img(self):
        text_node = TextNode('image alt', TextType.IMAGE, 'https://linktoimage.com/??flkajsdlfk==%%yes')
        html_node = text_node_to_html_node(text_node)

        self.assertIsInstance(html_node, LeafNode)
        self.assertEqual(html_node.tag, "img")
        assert html_node.attributes.get("src") == "https://linktoimage.com/??flkajsdlfk==%%yes"
        assert html_node.attributes.get("alt") == "image alt"
        self.assertEqual(html_node.value, "")
    
    def test_image_node_without_url_raises_value_error(self):
        with self.assertRaisesRegex(ValueError, "Image must have URL"):
            text_node = TextNode('alt text', TextType.IMAGE, '')
            html_node = text_node_to_html_node(text_node)


if __name__ == "__main__":
    unittest.main()

