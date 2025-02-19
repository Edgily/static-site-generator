import unittest
from block_to_block_type import BlockType, block_to_block_type


class TestBlockToBlockType(unittest.TestCase):
    def test_paragraph(self):
        self.assertEqual(
            block_to_block_type("text block\ntext block"), BlockType.PARAGRAPH
        )

    def test_heading(self):
        self.assertEqual(
            block_to_block_type("# heading block"), BlockType.HEADING
            )

    def test_code(self):
        self.assertEqual(
            block_to_block_type("```code block\ncode block```"), BlockType.CODE
        )

    def test_quote(self):
        self.assertEqual(
            block_to_block_type("> quote block\n> quote block"), BlockType.QUOTE
        )

    def test_unordered_list(self):
        self.assertEqual(
            block_to_block_type("* unordered list block\n- unordered list block"),
            BlockType.UNORDERED_LIST,
        )

    def test_ordered_list(self):
        self.assertEqual(
            block_to_block_type("1. ordered list block\n2. ordered list block"),
            BlockType.ORDERED_LIST,
        )

    def test_invalid(self):
        with self.assertRaises(ValueError):
            block_to_block_type(None)
            self.assertEqual(
                str(block_to_block_type("string")), "Block must be a string value"
            )


if __name__ == "__main__":
    unittest.main()
