import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):
    def test_attributes_to_html_with_one_attribute(self):
        node = HTMLNode("p", "paragraph text", [], {"href": "someurl.url"})
        test_input = node.attributes_to_html()
        test_output = ' href="someurl.url"'
        self.assertEqual(test_input, test_output)

    def test_attributes_to_html_with_multiple_attributes(self):
        node = HTMLNode(
            "p",
            "paragraph text",
            [],
            {"href": "someurl.url", "target": "_blank", "other_prop": "whoops"},
        )
        test_input = node.attributes_to_html()
        test_output = ' href="someurl.url" target="_blank" other_prop="whoops"'
        self.assertEqual(test_input, test_output)

    def test_attributes_to_html_without_attributes(self):
        node = HTMLNode("p", "paragraph text", [])
        test_input = node.attributes_to_html()
        test_output = ""
        self.assertEqual(test_input, test_output)


class TestLeafNode(unittest.TestCase):
    def test_to_html_with_href(self):
        node = LeafNode("a", "Click here", {"href": "https://example.com"})
        test_input = node.to_html()
        test_output = '<a href="https://example.com">Click here</a>'
        self.assertEqual(test_input, test_output)

    def test_to_html_with_multiple_attributes(self):
        node = LeafNode(
            "a",
            "Click here",
            {"href": "someurl.url", "target": "_blank", "other_prop": "whoops"},
        )
        test_input = node.to_html()
        test_output = (
            '<a href="someurl.url" target="_blank" other_prop="whoops">Click here</a>'
        )
        self.assertEqual(test_input, test_output)

    def test_to_html_without_attributes(self):
        node = LeafNode("a", "Click here")
        test_input = node.to_html()
        test_output = "<a>Click here</a>"
        self.assertEqual(test_input, test_output)

    def test_to_html_with_no_value_raises_error(self):
        node = LeafNode("a", None, {"href": "https://example.com"})
        with self.assertRaises(ValueError):
            node.to_html()

    def test_to_html_without_tag_returns_value(self):
        node = LeafNode("", "Click here", {"href": "https://example.com"})
        test_input = node.to_html()
        test_output = "Click here"
        self.assertEqual(test_input, test_output)

    def test_to_html_with_none_tag_returns_value(self):
        node = LeafNode(None, "Click here", {"href": "https://example.com"})
        test_input = node.to_html()
        test_output = "Click here"
        self.assertEqual(test_input, test_output)


class TestParentNode(unittest.TestCase):
    def test_parent_node_must_have_a_tag(self):
        node = ParentNode(
            "",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        with self.assertRaises(ValueError) as context:
            node.to_html()
        self.assertEqual(str(context.exception), "ParentNode must have a tag")

    def test_parent_node_must_have_children(self):
        node = ParentNode(
            "p",
            [],
        )
        with self.assertRaises(ValueError) as context:
            node.to_html()
        self.assertEqual(str(context.exception), "ParentNode must have children")

    def test_parent_node_with_children(self):
        node = ParentNode(
            "div",
            [
                LeafNode("p", "no props"),
                LeafNode("p", "with props", {"class": "test"}),
                ParentNode(
                    "section",
                    [LeafNode("span", "nested")],
                    {"id": "sec1", "class": "main"},
                ),
            ],
            None,
        )

        test_input = node.to_html()
        test_output = '<div><p>no props</p><p class="test">with props</p><section id="sec1" class="main"><span>nested</span></section></div>'
        self.assertEqual(test_input, test_output)

    def test_parent_node_with_deeply_nested_children(self):
        node = ParentNode(
            "div",
            [
                ParentNode(
                    "section",
                    [
                        ParentNode(
                            "article",
                            [LeafNode("p", "Deeply nested")],
                        ),
                    ],
                ),
            ],
        )

        test_input = node.to_html()
        test_output = (
            "<div><section><article><p>Deeply nested</p></article></section></div>"
        )
        self.assertEqual(test_input, test_output)