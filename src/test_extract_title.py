import unittest
from extract_title import extract_title


class TestExtractTitle(unittest.TestCase):
    def test_extract_title_simple(self):
        self.assertEqual(extract_title("# Hello"), "Hello")

    def test_extract_title_strips_whitespace(self):
        self.assertEqual(extract_title("#   Hello world   "), "Hello world")

    def test_extract_title_ignores_non_h1(self):
        md = "## Not H1\n\n# Real Title\n\nText"
        self.assertEqual(extract_title(md), "Real Title")

    def test_extract_title_raises_if_missing(self):
        md = "## Heading\n\nParagraph"
        with self.assertRaises(ValueError):
            extract_title(md)

    def test_extract_title_raises_if_empty(self):
        md = "#   \n\nText"
        with self.assertRaises(ValueError):
            extract_title(md)


if __name__ == "__main__":
    unittest.main()