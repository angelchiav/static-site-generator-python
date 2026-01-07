from textnode import TextNode, TextType
from htmlnode import LeafNode

def text_node_to_html_node(text_node: TextNode):
    match text_node.text_type:
        case TextType.TEXT:
            return LeafNode(None, text_node.text)
        
        case TextType.BOLD:
            return LeafNode("b", text_node.text)
        
        case TextType.ITALIC:
            return LeafNode("i", text_node.text)
        
        case TextType.LINK:
            if text_node.url is None:
                raise ValueError("Link TextNode must have a URL")
            return LeafNode(
                "a",
                text_node.text,
                props={"href": text_node.url}
            )
        
        case TextType.IMAGE:
            if text_node.url is None:
                raise ValueError("Link TextNode must have a URL")
            return LeafNode(
                "img",
                "",
                props={
                    "src": text_node.url,
                    "alt": text_node.text,
                }
            )
        
        case TextType.CODE:
            return LeafNode("code", text_node.text)

        case _:
            raise Exception(f"Unknown TextType: {text_node.text_type}")