from text_to_textnodes import text_to_textnodes
from text_to_html import text_node_to_html_node

def text_to_children_nodes(block): #block
    textnodes = text_to_textnodes(block)
    htmlnodes = []
    for node in textnodes:
        htmlnodes.append(text_node_to_html_node(node))
    return htmlnodes