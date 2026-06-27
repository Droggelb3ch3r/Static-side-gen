from blocks import BlockType, block_to_block_type
from htmlnode import LeafNode, ParentNode
from md_to_block import markdown_to_blocks
from textnode import TextNode, TextType, text_node_to_html_node
from text_to_textnodes import text_to_textnodes
from split_node import split_nodes_delimiter, split_nodes_image, split_nodes_link

def text_to_children(text: str) -> list:
    return [text_node_to_html_node(tn) for tn in text_to_textnodes(text)]


def markdown_to_html_node(markdown):
    blocks_of_md = markdown_to_blocks(markdown)
    block_types = [block_to_block_type(block) for block in blocks_of_md]
    html_nodes = []

    for i, block in enumerate(blocks_of_md):
        if block_types[i] == BlockType.HEADING:
            heading_level = block.count("#", 0, block.index(" "))
            html_nodes.append(ParentNode(f"h{heading_level}", text_to_children(block[heading_level + 1:].strip())))

        elif block_types[i] == BlockType.PARAGRAPH:
            paragraph = " ".join(block.split("\n"))
            html_nodes.append(ParentNode("p", text_to_children(paragraph)))

        elif block_types[i] == BlockType.CODE:
            text = block.strip()
            # die ``` am Anfang/Ende entfernen, aber den inneren Text nicht komplett strippen
            code_content = text[3:-3].lstrip("\n")
            code_node = text_node_to_html_node(TextNode(code_content, TextType.TEXT))
            code = ParentNode("code", [code_node])
            html_nodes.append(ParentNode("pre", [code]))

        elif block_types[i] == BlockType.QUOTE:
            lines = block.split("\n")
            stripped = [line.lstrip(">").strip() for line in lines]
            quote_text = " ".join(stripped)
            html_nodes.append(ParentNode("blockquote", text_to_children(quote_text)))

        elif block_types[i] == BlockType.UNORDERED_LIST:
            list_items = [item[2:].strip() for item in block.split("\n")]
            html_nodes.append(ParentNode("ul", [ParentNode("li", text_to_children(item)) for item in list_items]))

        elif block_types[i] == BlockType.ORDERED_LIST:
            list_items = [item[item.index(".") + 1:].strip() for item in block.split("\n")]
            html_nodes.append(ParentNode("ol", [ParentNode("li", text_to_children(item)) for item in list_items]))

        
    return ParentNode("div", html_nodes)
        