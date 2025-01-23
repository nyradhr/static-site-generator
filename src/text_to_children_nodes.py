from text_to_textnodes import text_to_textnodes
from text_to_html import text_node_to_html_node

def text_to_children_nodes(block):
    """Convert a block of markdown text to a list of HTML nodes.

    Takes a string of markdown text, converts it first to TextNodes (handling inline
    markdown like bold, italic, etc), then converts each TextNode to its corresponding
    HTMLNode representation.

    Args:
        block (str): A string of markdown text that may contain inline markdown syntax

    Returns:
        list[HTMLNode]: A list of HTMLNode objects representing the text and any
        inline markdown elements
    """
    textnodes = text_to_textnodes(block)
    htmlnodes = []
    for node in textnodes:
        htmlnodes.append(text_node_to_html_node(node))
    return htmlnodes