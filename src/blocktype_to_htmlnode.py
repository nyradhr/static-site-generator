from htmlnode import HTMLNode

def blocktype_to_htmlnode(blocktype):
    if blocktype == "paragraph":
        return HTMLNode(tag="p", children=[])
    elif blocktype == "heading":
        return HTMLNode(tag=None, children=[]) #tags will be added by the postprocessing function
    elif blocktype == "quote":
        return HTMLNode(tag="blockquote", children=[])
    elif blocktype == "unordered_list":
        return HTMLNode(tag="ul", children=[])
    elif blocktype == "ordered_list":
        return HTMLNode(tag="ol", children=[])
    elif blocktype == "code":
        return HTMLNode(tag="pre", children=[HTMLNode(tag="code", children=[])])
    else:
        raise ValueError(f"Unknown block type: {blocktype}")

def heading_tag_parser(block):
    # Determine header level based on leading '#' characters
    header_level = block.count("#", 0, block.find(" "))
    return f"h{min(header_level, 6)}"