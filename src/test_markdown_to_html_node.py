import unittest

from markdown_to_html_node import markdown_to_html_node
from htmlnode import HTMLNode, ParentNode, LeafNode


class TestMarkdownToHTMLNode(unittest.TestCase):
    def test_paragraph_to_html_node(self):
        paragraph_test_input = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with *italic* text and `code` here
"""
        result = markdown_to_html_node(paragraph_test_input)
        self.assertIsInstance(result, ParentNode)
        self.assertEqual(result.tag, "div")
        self.assertEqual(len(result.children), 2)
        self.assertIsInstance(result.children[0], ParentNode)
        self.assertEqual(result.children[0].tag, "p")
        self.assertIsInstance(result.children[1], ParentNode)
        self.assertEqual(result.children[1].tag, "p")

    def test_heading_to_html_node(self):
        heading_test_input = """
# Heading 1

## Heading 2

### Heading 3

#### Heading 4

##### Heading 5

###### Heading 6
"""
        result = markdown_to_html_node(heading_test_input)
        self.assertIsInstance(result, ParentNode)
        self.assertEqual(result.tag, "div")
        self.assertEqual(len(result.children), 6)
        self.assertIsInstance(result.children[0], ParentNode)
        self.assertEqual(result.children[0].tag, "h1")
        self.assertIsInstance(result.children[1], ParentNode)
        self.assertEqual(result.children[1].tag, "h2")
        self.assertIsInstance(result.children[2], ParentNode)
        self.assertEqual(result.children[2].tag, "h3")
        self.assertIsInstance(result.children[3], ParentNode)
        self.assertEqual(result.children[3].tag, "h4")
        self.assertIsInstance(result.children[4], ParentNode)
        self.assertEqual(result.children[4].tag, "h5")
        self.assertIsInstance(result.children[5], ParentNode)
        self.assertEqual(result.children[5].tag, "h6")

    def test_code_block_to_html_node(self):
        code_test_input = """
```
def hello_world():
    print("Hello, world!")
    
# This is a comment
for i in range(5):
    print(i)
```
"""
        result = markdown_to_html_node(code_test_input)
        self.assertIsInstance(result, ParentNode)
        self.assertEqual(result.tag, "div")
        self.assertEqual(len(result.children), 1)
        self.assertIsInstance(result.children[0], ParentNode)
        self.assertEqual(result.children[0].tag, "pre")
        self.assertEqual(result.children[0].children[0].tag, "code")

    def test_quote_to_html_node(self):
        quote_test_input = """
> This is a quote
> with **multiple** lines
> 
> And a blank line in between
"""
        result = markdown_to_html_node(quote_test_input)
        self.assertIsInstance(result, ParentNode)
        self.assertEqual(result.tag, "div")
        self.assertEqual(len(result.children), 1)
        self.assertIsInstance(result.children[0], ParentNode)
        self.assertEqual(result.children[0].tag, "blockquote")
        self.assertEqual(result.children[0].children[0].tag, "p")

    def test_unordered_list_to_html_node(self):
        unorderedlist_test_input = """
* Item 1
- Item 2 with **bold** text
* Item 3 with *italic* words
"""
        result = markdown_to_html_node(unorderedlist_test_input)
        self.assertIsInstance(result, ParentNode)
        self.assertEqual(result.tag, "div")
        self.assertEqual(len(result.children), 1)
        self.assertIsInstance(result.children[0], ParentNode)
        self.assertEqual(result.children[0].tag, "ul")
        li_tags = result.children[0].children
        self.assertEqual(len(li_tags), 3)
        self.assertEqual(li_tags[0].tag, "li")
        self.assertEqual(li_tags[1].tag, "li")
        self.assertEqual(li_tags[2].tag, "li")

    def test_ordered_list_to_html_node(self):
        orderedlist_test_input = """
1. First item
2. Second item
3. Third item
"""
        result = markdown_to_html_node(orderedlist_test_input)
        self.assertIsInstance(result, ParentNode)
        self.assertEqual(result.tag, "div")
        self.assertEqual(len(result.children), 1)
        self.assertIsInstance(result.children[0], ParentNode)
        self.assertEqual(result.children[0].tag, "ol")
        li_tags = result.children[0].children
        self.assertEqual(len(li_tags), 3)
        self.assertEqual(li_tags[0].tag, "li")
        self.assertEqual(li_tags[1].tag, "li")
        self.assertEqual(li_tags[2].tag, "li")

    def test_empty_markdown_input(self):
        empty_input = ""
        result = markdown_to_html_node(empty_input)
        self.assertIsInstance(result, ParentNode)
        self.assertEqual(result.tag, "div")
        self.assertEqual(len(result.children), 0)

    def test_heading_and_paragraph_to_html_node(self):
        heading_and_paragraph_test_input = """
# Heading 1

This is a paragraph with **bold** and *italic* words
"""
        result = markdown_to_html_node(heading_and_paragraph_test_input)
        self.assertIsInstance(result, ParentNode)
        self.assertEqual(result.tag, "div")
        self.assertEqual(len(result.children), 2)
        self.assertIsInstance(result.children[0], ParentNode)
        self.assertEqual(result.children[0].tag, "h1")
        self.assertIsInstance(result.children[1], ParentNode)
        self.assertEqual(result.children[1].tag, "p")
