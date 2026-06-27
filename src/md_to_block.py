

def markdown_to_blocks(markdown):
    """
    Convert markdown text to a list of blocks of Strings
    """
    blocks = []
    subline_block = ""
    for line in markdown.split("\n\n"):
        line = line.strip()
        for subline in line.split("\n"):
            subline = subline.strip()
            if subline:
                if subline_block:
                    subline_block += "\n" + subline
                else:
                    subline_block = subline
        if subline_block:
            blocks.append(subline_block)
            subline_block = ""
            



    return blocks