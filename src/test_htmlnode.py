import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):
    def test1(self):
        node = HTMLNode("p", "paragraph text", [], {"href": "someurl.url"})
        test_input = node.attributes_to_html()
        test_output = ' href="someurl.url"'
        self.assertEqual(test_input, test_output)

    def test2(self):
        node = HTMLNode(
            "p",
            "paragraph text",
            [],
            {"href": "someurl.url", "target": "_blank", "other_prop": "whoops"},
        )
        test_input = node.attributes_to_html()
        test_output = ' href="someurl.url" target="_blank" other_prop="whoops"'
        self.assertEqual(test_input, test_output)

    def test3(self):
        node = HTMLNode("p", "paragraph text", [])
        test_input = node.attributes_to_html()
        test_output = ""
        self.assertEqual(test_input, test_output)

class TestLeafNode(unittest.TestCase):
    def test1(self):
        node = LeafNode("a", "Click here", {"href": "https://example.com"})
        test_input = node.to_html()
        test_output = '<a href="https://example.com">Click here</a>'
        self.assertEqual(test_input, test_output)

    def test2(self):
        node = LeafNode("a", "Click here", {"href": "someurl.url", "target": "_blank", "other_prop": "whoops"})
        test_input = node.to_html()
        test_output = '<a href="someurl.url" target="_blank" other_prop="whoops">Click here</a>'
        self.assertEqual(test_input, test_output)

    def test3(self):
        node = LeafNode("a", "Click here")
        test_input = node.to_html()
        test_output = '<a>Click here</a>'
        self.assertEqual(test_input, test_output)

    def test4(self):
        node = LeafNode("a", None, {"href": "https://example.com"})
        with self.assertRaises(ValueError):
            node.to_html()

    def test5(self):
        node = LeafNode("", "Click here", {"href": "https://example.com"})
        test_input = node.to_html()
        test_output = "Click here"
        self.assertEqual(test_input, test_output)

    def test6(self):
        node = LeafNode(None, "Click here", {"href": "https://example.com"})
        test_input = node.to_html()
        test_output = "Click here"
        self.assertEqual(test_input, test_output)


class TestParentNode(unittest.TestCase):
    def test1(self):
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

    def test2(self):
        node = ParentNode(
            "p",
            [] ,
        )
        with self.assertRaises(ValueError) as context:
            node.to_html()
        self.assertEqual(str(context.exception), "ParentNode must have children")

    def test3(self):
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

    def test4(self):
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
        test_output = "<div><section><article><p>Deeply nested</p></article></section></div>"
        self.assertEqual(test_input, test_output)


if __name__ == "__main__":
    unittest.main()
