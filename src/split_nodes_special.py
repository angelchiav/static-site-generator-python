from textnode import TextNode, TextType
from markdown_extraction import (
    extract_markdown_images,
    extract_markdown_links,
)

def split_nodes_image(old_nodes):
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
            
        text = node.text
        images = extract_markdown_images(text)

        if not images:
            new_nodes.append(node)
            continue

        remaining_text = text

        for alt, url in images:
            markdown = f"![{alt}]({url})"
            parts = remaining_text.split(markdown, 1)

            if len(parts) != 2:
                raise ValueError("Invalid markdown image syntax")
            
            before, after = parts

            if before:
                new_nodes.append(TextNode(before, TextType.TEXT, None))
            
            new_nodes.append(TextNode(alt, TextType.IMAGE, url))

            remaining_text = after

        if remaining_text:
            new_nodes.append(TextNode(remaining_text, TextType.TEXT, None))

    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        text = node.text
        links = extract_markdown_links(text)

        if not links:
            new_nodes.append(node)
            continue

        remaining_text = text

        for anchor, url in links:
            markdown = f"[{anchor}]({url})"
            parts = remaining_text.split(markdown, 1)

            if len(parts) != 2:
                raise ValueError("Invalid markdown link syntax")
            
            before, after = parts

            if before:
                new_nodes.append(TextNode(before, TextType.TEXT, None))
            
            new_nodes.append(TextNode(anchor, TextType.LINK, url))

            remaining_text = after
        
        if remaining_text:
            new_nodes.append(TextNode(remaining_text, TextType.TEXT, None))

    return new_nodes