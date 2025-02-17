import unittest
from text_to_textnodes import text_to_textnodes
from textnode import TextNode, TextType


class TestTextToTextNodes(unittest.TestCase):
    def test_text_only(self):
        input_text = "This is a simple text node."
        result = text_to_textnodes(input_text)

        expected_output = [
            TextNode("This is a simple text node.", TextType.TEXT),
        ]

        self.assertEqual(result, expected_output)

    def test_complex_extraction(self):
        input = "*This is italic* with a `code block` with!#&^&$^&@%%%%@@^#$)(@)$(_++_!#+_!#) a [link](link.url) and some **bold text** beside an ![img](img.url) and `more code` and a [link2](link2.url) and **more bold text** with an ![img2](img2.url) ending in *italics again*."
        result = text_to_textnodes(input)

        expected_output = [
            TextNode("This is italic", TextType.ITALIC),
            TextNode(" with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" with!#&^&$^&@%%%%@@^#$)(@)$(_++_!#+_!#) a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "link.url"),
            TextNode(" and some ", TextType.TEXT),
            TextNode("bold text", TextType.BOLD),
            TextNode(" beside an ", TextType.TEXT),
            TextNode("img", TextType.IMAGE, "img.url"),
            TextNode(" and ", TextType.TEXT),
            TextNode("more code", TextType.CODE),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link2", TextType.LINK, "link2.url"),
            TextNode(" and ", TextType.TEXT),
            TextNode("more bold text", TextType.BOLD),
            TextNode(" with an ", TextType.TEXT),
            TextNode("img2", TextType.IMAGE, "img2.url"),
            TextNode(" ending in ", TextType.TEXT),
            TextNode("italics again", TextType.ITALIC),
            TextNode(".", TextType.TEXT),
        ]

        self.assertEqual(result, expected_output)
        zipped = zip(expected_output, result)
        for expected, actual in zipped:
            self.assertEqual(expected.text, actual.text)
            self.assertEqual(expected.text_type, actual.text_type)
            if expected.text_type in [TextType.LINK, TextType.IMAGE]:
                self.assertEqual(expected.url, actual.url)

    def test_leading_trailing_spaces(self):
        input_text = " oh my "
        result = text_to_textnodes(input_text)

        self.assertEqual(
            result,
            [
                TextNode(" oh my ", TextType.TEXT),
            ],
        )

    def test_empty_input(self):
        input_text = ""
        with self.assertRaises(ValueError) as context:
            text_to_textnodes(input_text)

        self.assertEqual(str(context.exception), "The provided node has no text.")

    def test_delimiter_only(self):
        input_text = "****"
        result = text_to_textnodes(input_text)

        self.assertEqual(result, [])


if __name__ == "__main__":
    unittest.main()
