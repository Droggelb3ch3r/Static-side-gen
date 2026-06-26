from textnode import TextNode, TextType
from extract_markdown_link_image import extract_markdown_images, extract_markdown_links


def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType) -> list[TextNode]:
    new_nodes = []
    
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        if delimiter not in node.text:
            new_nodes.append(node)
            continue
        split_text = node.text.split(delimiter)
        if len(split_text) % 2 == 0:
            raise ValueError("invalid markdown, formatted section not closed")
        for i in range(len(split_text)):
            if split_text[i] == "":
                continue  # leere Strings überspringen
            if i % 2 == 0:
                # gerade Index -> normaler Text
                new_nodes.append(TextNode(split_text[i], node.text_type))
            else:
                # ungerader Index -> formatierter Text (zwischen den Delimitern)
                new_nodes.append(TextNode(split_text[i], text_type))

        
    return new_nodes



def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes = []
    
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        # Suche nach Markdown-Bildsyntax ![alt text](url)
        matches = extract_markdown_images(node.text)

        if not matches:
            new_nodes.append(node)
            continue

        remaining_text = node.text
        for alt_text, url in matches:
            parts = remaining_text.split(f"![{alt_text}]({url})", 1)
            if len(parts) != 2:
                raise ValueError("invalid markdown, image section not closed")

            if parts[0] != "":
                new_nodes.append(TextNode(parts[0], TextType.TEXT))
            new_nodes.append(TextNode(alt_text, TextType.IMAGE, url))
            remaining_text = parts[1]

        if remaining_text != "":
            new_nodes.append(TextNode(remaining_text, TextType.TEXT))

    return new_nodes



def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        # Suche nach Markdown-Linksyntax [alt text](url)
        matches = extract_markdown_links(node.text)

        if not matches:
            new_nodes.append(node)
            continue

        remaining_text = node.text
        for alt_text, url in matches:
            parts = remaining_text.split(f"[{alt_text}]({url})", 1)
            if len(parts) != 2:
                raise ValueError("invalid markdown, link section not closed")

            if parts[0] != "":
                new_nodes.append(TextNode(parts[0], TextType.TEXT))
            new_nodes.append(TextNode(alt_text, TextType.LINK, url))
            remaining_text = parts[1]

        if remaining_text != "":
            new_nodes.append(TextNode(remaining_text, TextType.TEXT))

    return new_nodes