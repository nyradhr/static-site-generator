def markdown_to_blocks(document):
    block_list = document.split("\n\n")
    result = []
    for block in block_list:
        block = block.strip()
        if len(block) > 0:
            result.append(block)
    return result