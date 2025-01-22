import re

def block_to_text(block, blocktype):
    if blocktype == "quote":
        lines = block.split('\n')
        lines = [line[1:].lstrip() for line in lines]
        return '\n'.join(lines)
    elif blocktype == "unordered_list":
        lines = block.split('\n')
        lines = [line[2:] for line in lines]
        return '\n'.join(lines)
    elif blocktype == "ordered_list":
        lines = block.split('\n')
        lines = [re.sub(r"\d+\. ", "", line) for line in lines]
        return '\n'.join(lines)
    elif blocktype == "heading":
        header_level = block.count("#", 0, block.find(" "))
        return block[header_level+1:]
    elif blocktype == "code":
        return block[3:-3]
    #paragraph
    return block