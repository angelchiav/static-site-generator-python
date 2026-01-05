import unittest

from htmlnode import ParentNode, LeafNode


class TestParentNode(unittest.TestCase):

    def test_parent_to_html_with_one_child(self):
        child = LeafNode("span", "Hello")
        node = ParentNode("p", [child])
        self.assertEqual(node.to_html(), "<p><span>Hello</span></p>")

    def test_parent_to_html_with_multiple_children(self):
        node = ParentNode(
            "div",
            [
                LeafNode("b", "Bold"),
                LeafNode(None, " and "),
                LeafNode("i", "italic"),
            ],
        )
        self.assertEqual(node.to_html(), "<div><b>Bold</b> and <i>italic</i></div>")

    def test_parent_to_html_with_nested_parent(self):
        inner = ParentNode("p", [LeafNode(None, "Inner")])
        outer = ParentNode("div", [LeafNode(None, "Start "), inner, LeafNode(None, " End")])
        self.assertEqual(outer.to_html(), "<div>Start <p>Inner</p> End</div>")

    def test_parent_to_html_no_tag_raises(self):
        node = ParentNode(None, [LeafNode("p", "x")])
        with self.assertRaises(ValueError):
            node.to_html()

    def test_parent_to_html_no_children_raises(self):
        node = ParentNode("div", None)
        with self.assertRaises(ValueError):
            node.to_html()

    def test_parent_to_html_with_props(self):
        node = ParentNode(
            "a",
            [LeafNode(None, "boot")],
            props={"href": "https://boot.dev", "target": "_blank"},
        )
        self.assertEqual(
            node.to_html(),
            '<a href="https://boot.dev" target="_blank">boot</a>',
        )


if __name__ == "__main__":
    unittest.main()