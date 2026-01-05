import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq_same_values(self):
        node1 = TextNode("This is a text node", TextType.BOLD, url="")
        node2 = TextNode("This is a text node", TextType.BOLD, url="")
        self.assertEqual(node1, node2)

    def test_eq_different_text(self):
        node1 = TextNode("Text one", TextType.BOLD, url="")
        node2 = TextNode("Text two", TextType.BOLD, url="")
        self.assertNotEqual(node1, node2)

    def test_eq_different_type(self):
        node1 = TextNode("Same text", TextType.BOLD, url="")
        node2 = TextNode("Same text", TextType.ITALIC, url="")
        self.assertNotEqual(node1, node2)

    def test_eq_different_url(self):
        node1 = TextNode("Same text", TextType.LINK, url="https://boot.dev")
        node2 = TextNode("Same text", TextType.LINK, url="https://google.com")
        self.assertNotEqual(node1, node2)

    def test_eq_url_none_vs_empty(self):
        node1 = TextNode("Same text", TextType.TEXT, url=None)
        node2 = TextNode("Same text", TextType.TEXT, url="")
        self.assertNotEqual(node1, node2)

    def test_eq_different_object_type(self):
        node = TextNode("Text", TextType.TEXT, url="")
        self.assertNotEqual(node, "TextNode")

if __name__ == "__main__":
    unittest.main()
