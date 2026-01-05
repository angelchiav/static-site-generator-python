# src/test_htmlnode.py
import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_anchor(self):
        node = HTMLNode(
            tag="a",
            value="boot.dev",
            props={"href": "https://boot.dev", "target": "_blank"},
        )
        self.assertEqual(
            node.props_to_html(),
            'href="https://boot.dev" target="_blank"',
        )

    def test_props_to_html_different_values(self):
        node = HTMLNode(
            tag="a",
            value="google",
            props={"href": "https://google.com", "target": "_self"},
        )
        self.assertEqual(
            node.props_to_html(),
            'href="https://google.com" target="_self"',
        )

    def test_props_to_html_ignores_tag_value_children(self):
        # props_to_html should only depend on props, not on tag/value/children
        child = HTMLNode(tag="b", value="child")
        node = HTMLNode(
            tag="p",
            value="parent",
            children=[child],
            props={"href": "/local", "target": "_top"},
        )
        self.assertEqual(
            node.props_to_html(),
            'href="/local" target="_top"',
        )


if __name__ == "__main__":
    unittest.main()