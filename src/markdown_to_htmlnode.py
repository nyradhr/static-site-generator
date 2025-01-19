from htmlnode import HTMLNode
from block_to_blocktype import block_to_blocktype
from markdown_to_blocks import markdown_to_blocks
from blocktype_to_htmlnode import blocktype_to_htmlnode
from text_to_children_nodes import text_to_children_nodes

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    htmlnodes = []
    for block in blocks:
        blocktype = block_to_blocktype(block)
        html = blocktype_to_htmlnode(blocktype)
        children = text_to_children_nodes(block)
        html.children = children
        htmlnodes.append(html)
    root = HTMLNode(tag = "div", children = htmlnodes)
    return root