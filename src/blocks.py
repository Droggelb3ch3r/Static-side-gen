

from enum import Enum


class BlockType(Enum):
    HEADING = "heading"
    PARAGRAPH = "paragraph"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"





def block_to_block_type(block):
    if block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return BlockType.HEADING
    
    elif block.startswith(">"):
        for sub_block in block.split("\n"):
            if not sub_block.startswith(">"):
                return BlockType.PARAGRAPH
        return BlockType.QUOTE
    
    elif block.startswith("- "):
        for sub_block in block.split("\n"):
            if not sub_block.startswith("- "):
                return BlockType.PARAGRAPH
        return BlockType.UNORDERED_LIST
    
    elif block[0].isdigit():
        counter = 1
        for sub_block in block.split("\n"):
            if not sub_block.startswith(f"{counter}. "):
                return BlockType.PARAGRAPH
            counter += 1
        return BlockType.ORDERED_LIST
    
    elif block.startswith("```") and block.endswith("```"):
        return BlockType.CODE

    return BlockType.PARAGRAPH
