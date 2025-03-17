import unittest
from extract_title import extract_title


class TestExtractTitle(unittest.TestCase):
    def test_extract_title(self):
        input = "# Heading\n\nThis is a paragraph."
        self.assertEqual(extract_title(input), "Heading")

    def test_value_error_on_no_heading(self):
        with self.assertRaises(ValueError):
            extract_title("This is a paragraph without a heading")


if __name__ == "__main__":
    unittest.main()
