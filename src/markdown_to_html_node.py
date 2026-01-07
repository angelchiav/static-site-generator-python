from htmlnode import ParentNode, LeafNode

from markdown_to_blocks import markdown_to_blocks
from block_to_block_type import block_to_block_type
from blocktype import BlockType
from text_to_textnodes import text_to_textnodes
from textnode_to_htmlnode import text_node_to_html_node


def text_to_children(text: str):
    return [text_node_to_html_node(n) for n in text_to_textnodes(text)]


def count_heading_level(block: str) -> int:
    count = 0
    for ch in block:
        if ch == "#":
            count += 1
        else:
            break
    return count


def markdown_to_html_node(markdown: str):
    blocks = markdown_to_blocks(markdown)
    html_children = []

    for block in blocks:
        block_type = block_to_block_type(block)

        match block_type:
            case BlockType.HEADING:
                level = count_heading_level(block)
                text = block[level + 1 :]  # remove "# "
                children = text_to_children(text)
                html_children.append(ParentNode(f"h{level}", children))

            case BlockType.PARAGRAPH:
                children = text_to_children(block)
                html_children.append(ParentNode("p", children))

            case BlockType.BLOCKQUOTE:
                lines = block.split("\n")
                cleaned = []
                for line in lines:
                    s = line.lstrip()
                    if s.startswith(">"):
                        s = s[1:]
                        if s.startswith(" "):
                            s = s[1:]
                    cleaned.append(s)
                quote_text = "\n".join(cleaned).strip()

                html_children.append(ParentNode("blockquote", [LeafNode(None, quote_text)]))

            case BlockType.CODE:
                # block looks like: ```\n...\n```
                code = block[4:-3]
                html_children.append(ParentNode("pre", [LeafNode("code", code)]))

            case BlockType.QUOTE:
                lines = block.split("\n")
                cleaned = []
                for line in lines:
                    s = line.lstrip()
                    if s.startswith(">"):
                        s = s[1:]
                        if s.startswith(" "):
                            s = s[1:]
                    cleaned.append(s)
                quote_text = "\n".join(cleaned).strip()

                # Render blockquote content directly (no extra <p> wrapper)
                html_children.append(ParentNode("blockquote", [LeafNode(None, quote_text)]))

            case BlockType.UNORDERED_LIST:
                items = block.split("\n")
                li_nodes = []
                for item in items:
                    text = item[2:]  # remove "- "
                    children = text_to_children(text)
                    li_nodes.append(ParentNode("li", children))
                html_children.append(ParentNode("ul", li_nodes))

            case BlockType.ORDERED_LIST:
                items = block.split("\n")
                li_nodes = []
                for item in items:
                    # item looks like "1. something"
                    text = item.split(". ", 1)[1]
                    children = text_to_children(text)
                    li_nodes.append(ParentNode("li", children))
                html_children.append(ParentNode("ol", li_nodes))

    return ParentNode("div", html_children)