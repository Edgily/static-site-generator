import unittest

from markdown_to_blocks import markdown_to_blocks


class TestMarkdownToBlocks(unittest.TestCase):
    def test_extraction(self):
        input = '''   # This is a heading


This is a paragraph of text. It has some **bold** and *italic* words inside of it.







* This is the first list item in a list block
* This is a list item
* This is another list item   '''
        result = markdown_to_blocks(input)

        self.assertEqual(
            result,
            ['# This is a heading', 'This is a paragraph of text. It has some **bold** and *italic* words inside of it.', '* This is the first list item in a list block\n* This is a list item\n* This is another list item'],
        )
    
    def test_extraction_other_order(self):
        input = '''   # This is a heading





* This is the first list item in a list block
* This is a list item
* This is another list item




This is a paragraph of text. It has some **bold** and *italic* words inside of it.



'''
        result = markdown_to_blocks(input)

        self.assertEqual(
            result,
            ['# This is a heading', '* This is the first list item in a list block\n* This is a list item\n* This is another list item', 'This is a paragraph of text. It has some **bold** and *italic* words inside of it.'],
        )

    def test_empty_input(self):
        input_text = ""    
        result = markdown_to_blocks(input_text)

        self.assertEqual(result, [])