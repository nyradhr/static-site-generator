import re

def block_to_blocktype(block):
    pattern = re.compile(r"^#{1,6} ")
    if pattern.match(block):
        return "heading"
    if block.startswith("```") and block.endswith("```"):
        return "code"
    if block.startswith(">"):
        lines = block.split("\n")
        for line in lines:
            line = line.strip()
            if not line.startswith(">"):
                return "paragraph"
        return "quote"
    pattern = re.compile(r"[*-] ")
    if pattern.match(block):
        lines = block.split("\n")
        char = block[0]
        for line in lines:
            if not pattern.match(line) or line[0] != char:
                return "paragraph"
        return "unordered_list"
    pattern = re.compile(r"\d+\. ")
    if pattern.match(block) and block.startswith("1"):
        count = 1
        lines = block.split("\n")
        for line in lines:
            if not(pattern.match(line) and line.startswith(f"{count}")):
                return "paragraph"
            count += 1
        return "ordered_list"
    return "paragraph"