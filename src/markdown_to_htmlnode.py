from htmlnode import HTMLNode
from block_to_blocktype import block_to_blocktype
from markdown_to_blocks import markdown_to_blocks
from blocktype_to_htmlnode import blocktype_to_htmlnode, heading_tag_parser
from text_to_children_nodes import text_to_children_nodes

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    htmlnodes = []
    for block in blocks:
        #creating the container/parent htmlnode
        blocktype = block_to_blocktype(block)
        html = blocktype_to_htmlnode(blocktype)
        #handling special cases that needed to analyze the content to determine the right tag
        if blocktype == "heading":
            html.tag = heading_tag_parser(block) 
        #parsing content into children nodes
        children = text_to_children_nodes(block)
        #linking children to parent
        html.children = children
        htmlnodes.append(html)
    #linking all container nodes to the root node
    root = HTMLNode(tag = "div", children = htmlnodes)
    return root