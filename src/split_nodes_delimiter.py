# split_nodes_delimiter.py

from textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    if delimiter == "":
        raise ValueError("delimiter cannot be empty")

    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        text = node.text
        if delimiter not in text:
            new_nodes.append(node)
            continue

        parts = text.split(delimiter)
        if len(parts) % 2 == 0:
            raise ValueError(f"Invalid markdown: unmatched delimiter {delimiter!r} in {text!r}")

        for i, part in enumerate(parts):
            if i % 2 == 0:
                if part != "":
                    new_nodes.append(TextNode(part, TextType.TEXT, None))
            else:
                if part == "":
                    raise ValueError(f"Invalid markdown: empty content between {delimiter!r} in {text!r}")
                new_nodes.append(TextNode(part, text_type, None))

    return new_nodes