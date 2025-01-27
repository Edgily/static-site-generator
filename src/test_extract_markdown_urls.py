import unittest

from extract_markdown_urls import extract_markdown_images, extract_markdown_links


class TestMarkdownImagesExtraction(unittest.TestCase):
    def test_single_image(self):
        text = "![alt text](http://example.com/image.jpg)"
        result = extract_markdown_images(text)
        self.assertEqual(result, [("alt text", "http://example.com/image.jpg")])

    def test_multiple_images(self):
        markdown = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        result = extract_markdown_images(markdown)
        self.assertEqual(
            result,
            [
                ("rick roll", "https://i.imgur.com/aKaOqIh.gif"),
                ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg"),
            ],
        )

    def test_no_images(self):
        text = "plain text"
        result = extract_markdown_images(text)
        self.assertEqual(result, [])

    def test_special_characters(self):
        text = """![image with spaces](https://example.com/my%20image.jpg)
        ![image-with-dash](https://example.com/image-2.jpg)
        ![image@with#symbols&](https://example.com/image?id=123&type=png)
        ![émoji 🐻](https://example.com/bear_emoji.png)"""
        expected = [
            ("image with spaces", "https://example.com/my%20image.jpg"),
            ("image-with-dash", "https://example.com/image-2.jpg"),
            ("image@with#symbols&", "https://example.com/image?id=123&type=png"),
            ("émoji 🐻", "https://example.com/bear_emoji.png"),
        ]
        result = extract_markdown_images(text)
        self.assertEqual(result, expected)


class TestMarkdownLinksExtraction(unittest.TestCase):
    def test_single_link(self):
        text = "[Boot.dev](https://boot.dev)"
        result = extract_markdown_links(text)
        self.assertEqual(result, [("Boot.dev", "https://boot.dev")])

    def test_multiple_links(self):
        text = """Here are some links:
        [Python](https://python.org)
        [GitHub](https://github.com)"""

        expected = [("Python", "https://python.org"), ("GitHub", "https://github.com")]
        self.assertEqual(extract_markdown_links(text), expected)

    def test_links_with_special_characters(self):
        text = """
        [Link with spaces](https://example.com/page%20one)
        [Complex URL](https://example.com/search?q=test&page=1)
        [Special &amp; chars](https://example.com/symbols-&-text)
        """

        expected = [
            ("Link with spaces", "https://example.com/page%20one"),
            ("Complex URL", "https://example.com/search?q=test&page=1"),
            ("Special &amp; chars", "https://example.com/symbols-&-text"),
        ]
        self.assertEqual(extract_markdown_links(text), expected)

    def test_no_links(self):
        text = "This is plain text without any links"
        self.assertEqual(extract_markdown_links(text), [])

    def test_not_confused_by_images(self):
        text = """This has both:
        ![image alt](https://example.com/image.jpg)
        [actual link](https://example.com)"""

        expected = [("actual link", "https://example.com")]
        self.assertEqual(extract_markdown_links(text), expected)
