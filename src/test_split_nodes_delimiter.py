import unittest

from textnode import TextNode, TextType
from split_nodes_delimiter import split_nodes_delimiter


class TestSplitNodesDelimiter(unittest.TestCase):
    def test_split_code_single(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        result = split_nodes_delimiter([node], "`", TextType.CODE)
        expected = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT),
        ]
        self.assertEqual(result, expected)

    def test_split_bold_single(self):
        node = TextNode("a **bold** b", TextType.TEXT)
        result = split_nodes_delimiter([node], "**", TextType.BOLD)
        expected = [
            TextNode("a ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" b", TextType.TEXT),
        ]
        self.assertEqual(result, expected)

    def test_split_italic_single(self):
        node = TextNode("a _italic_ b", TextType.TEXT)
        result = split_nodes_delimiter([node], "_", TextType.ITALIC)
        expected = [
            TextNode("a ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" b", TextType.TEXT),
        ]
        self.assertEqual(result, expected)

    def test_multiple_delimited_sections(self):
        node = TextNode("a `one` b `two` c", TextType.TEXT)
        result = split_nodes_delimiter([node], "`", TextType.CODE)
        expected = [
            TextNode("a ", TextType.TEXT),
            TextNode("one", TextType.CODE),
            TextNode(" b ", TextType.TEXT),
            TextNode("two", TextType.CODE),
            TextNode(" c", TextType.TEXT),
        ]
        self.assertEqual(result, expected)

    def test_does_not_split_non_text_nodes(self):
        nodes = [
            TextNode("Hello ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" world", TextType.TEXT),
        ]
        result = split_nodes_delimiter(nodes, "`", TextType.CODE)
        self.assertEqual(result, nodes)  # unchanged (no backticks)

    def test_unmatched_delimiter_raises(self):
        node = TextNode("This is `broken markdown", TextType.TEXT)
        with self.assertRaises(ValueError):
            split_nodes_delimiter([node], "`", TextType.CODE)

    def test_empty_delimited_content_raises(self):
        node = TextNode("This is `` broken", TextType.TEXT)
        with self.assertRaises(ValueError):
            split_nodes_delimiter([node], "`", TextType.CODE)

    def test_no_delimiter_returns_same_node(self):
        node = TextNode("Just plain text", TextType.TEXT)
        result = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(result, [node])


if __name__ == "__main__":
    unittest.main()