# src/test_textnode_to_htmlnode.py
import unittest

from textnode import TextNode, TextType
from htmlnode import LeafNode
from textnode_to_htmlnode import text_node_to_html_node  # ajusta el import al nombre real de tu archivo


class TestTextNodeToHTMLNode(unittest.TestCase):

    def test_text_type_text(self):
        tn = TextNode("Hello", TextType.TEXT, url="")
        html = text_node_to_html_node(tn)
        self.assertEqual(html, LeafNode(None, "Hello"))

    def test_text_type_bold(self):
        tn = TextNode("Bold", TextType.BOLD, url="")
        html = text_node_to_html_node(tn)
        self.assertEqual(html, LeafNode("b", "Bold"))

    def test_text_type_italic(self):
        tn = TextNode("Ital", TextType.ITALIC, url="")
        html = text_node_to_html_node(tn)
        self.assertEqual(html, LeafNode("i", "Ital"))

    def test_text_type_code(self):
        tn = TextNode("print('hi')", TextType.CODE, url="")
        html = text_node_to_html_node(tn)
        self.assertEqual(html, LeafNode("code", "print('hi')"))

    def test_text_type_link(self):
        tn = TextNode("Boot.dev", TextType.LINK, "https://boot.dev")
        html = text_node_to_html_node(tn)
        self.assertEqual(html, LeafNode("a", "Boot.dev", {"href": "https://boot.dev"}))

    def test_text_type_image(self):
        tn = TextNode("alt text", TextType.IMAGE, "https://img.com/cat.png")
        html = text_node_to_html_node(tn)
        self.assertEqual(
            html,
            LeafNode("img", "", {"src": "https://img.com/cat.png", "alt": "alt text"}),
        )

    def test_invalid_type_raises(self):
        # Fuerza un tipo inválido para probar el else
        tn = TextNode("x", TextType.TEXT, url="")
        tn.text_type = "not-a-texttype"
        with self.assertRaises(Exception):
            text_node_to_html_node(tn)


if __name__ == "__main__":
    unittest.main()