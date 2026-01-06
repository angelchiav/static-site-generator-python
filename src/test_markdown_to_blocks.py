import unittest
from markdown_to_blocks import markdown_to_blocks


class TestMarkdownToBlocks(unittest.TestCase):
    def test_markdown_to_blocks_basic(self):
        markdown = (
            "# This is a heading\n\n"
            "This is a paragraph of text. It has some **bold** and _italic_ words inside of it.\n\n"
            "- This is the first list item in a list block\n"
            "- This is a list item\n"
            "- This is another list item"
        )

        blocks = markdown_to_blocks(markdown)

        expected = [
            "# This is a heading",
            "This is a paragraph of text. It has some **bold** and _italic_ words inside of it.",
            "- This is the first list item in a list block\n"
            "- This is a list item\n"
            "- This is another list item",
        ]

        self.assertEqual(blocks, expected)

    def test_markdown_to_blocks_extra_newlines(self):
        markdown = (
            "\n\n# Heading\n\n\n"
            "Paragraph\n\n\n\n"
            "- Item 1\n- Item 2\n\n"
        )

        blocks = markdown_to_blocks(markdown)

        expected = [
            "# Heading",
            "Paragraph",
            "- Item 1\n- Item 2",
        ]

        self.assertEqual(blocks, expected)

    def test_markdown_to_blocks_single_block(self):
        markdown = "Just one block of text"
        blocks = markdown_to_blocks(markdown)
        self.assertEqual(blocks, ["Just one block of text"])

    def test_markdown_to_blocks_empty_input(self):
        markdown = "\n\n\n"
        blocks = markdown_to_blocks(markdown)
        self.assertEqual(blocks, [])


if __name__ == "__main__":
    unittest.main()