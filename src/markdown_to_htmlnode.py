from htmlnode import HTMLNode
from block_to_blocktype import block_to_blocktype
from markdown_to_blocks import markdown_to_blocks
from blocktype_to_htmlnode import blocktype_to_htmlnode, heading_tag_parser
from text_to_children_nodes import text_to_children_nodes
from block_to_text import block_to_text


def markdown_to_htmlnode(markdown):
    blocks = markdown_to_blocks(markdown)
    htmlnodes = []
    for block in blocks:
        #creating the container/parent htmlnode
        blocktype = block_to_blocktype(block)
        html = blocktype_to_htmlnode(blocktype)
        #handling special cases that needed to analyze the content to determine the right tag
        if blocktype == "heading":
            html.tag = heading_tag_parser(block)
        #BEFORE passing the block as input we need to sanitize it based on the type
        text = block_to_text(block, blocktype)
        #print(f"Block type: {blocktype}, Text: {text}")
        #parsing content into children nodes
        if blocktype in ["ordered_list", "unordered_list"]:
            # Split into li nodes first
            lines = text.split('\n')
            #print(f"List lines: {lines}")
            children = [HTMLNode("li", children=text_to_children_nodes(line)) for line in lines]
        else:
            children = text_to_children_nodes(text)
        #linking children to parent
        if blocktype == "code":
            codenode = html.children[0] #extrapolating code node from pre node
            codenode.children = children #assigning inline content
        else:
            html.children = children
        htmlnodes.append(html)
    #linking all container nodes to the root node
    root = HTMLNode(tag = "div", children = htmlnodes)
    #print(f"Final HTML nodes: {root}")
    return root