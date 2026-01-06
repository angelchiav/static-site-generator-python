import unittest

from textnode import TextNode, TextType
from split_nodes_special import split_nodes_image, split_nodes_link


class TestSplitNodesSpecial(unittest.TestCase):
    def test_split_nodes_link_single(self):
        node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev)",
            TextType.TEXT,
        )
        result = split_nodes_link([node])
        expected = [
            TextNode("This is text with a link ", TextType.TEXT, None),
            TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
        ]
        self.assertEqual(result, expected)

    def test_split_nodes_link_multiple(self):
        node = TextNode(
            "Links: [one](https://one.com) and [two](https://two.com)",
            TextType.TEXT,
        )
        result = split_nodes_link([node])
        expected = [
            TextNode("Links: ", TextType.TEXT, None),
            TextNode("one", TextType.LINK, "https://one.com"),
            TextNode(" and ", TextType.TEXT, None),
            TextNode("two", TextType.LINK, "https://two.com"),
        ]
        self.assertEqual(result, expected)

    def test_split_nodes_image_single(self):
        node = TextNode(
            "Here is an image ![cat](https://img.com/cat.png)",
            TextType.TEXT,
        )
        result = split_nodes_image([node])
        expected = [
            TextNode("Here is an image ", TextType.TEXT, None),
            TextNode("cat", TextType.IMAGE, "https://img.com/cat.png"),
        ]
        self.assertEqual(result, expected)

    def test_split_nodes_image_multiple(self):
        node = TextNode(
            "Pics ![one](a.png) and ![two](b.png)",
            TextType.TEXT,
        )
        result = split_nodes_image([node])
        expected = [
            TextNode("Pics ", TextType.TEXT, None),
            TextNode("one", TextType.IMAGE, "a.png"),
            TextNode(" and ", TextType.TEXT, None),
            TextNode("two", TextType.IMAGE, "b.png"),
        ]
        self.assertEqual(result, expected)

    def test_non_text_nodes_unchanged(self):
        node = TextNode("hello", TextType.BOLD, None)
        self.assertEqual(split_nodes_link([node]), [node])
        self.assertEqual(split_nodes_image([node]), [node])


if __name__ == "__main__":
    unittest.main()