from textnode import TextNode, TextType
from splitnodesdelimiter import split_nodes_delimiter
from splitlinks import split_nodes_images, split_nodes_links

def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.TEXT)]
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "*", TextType.ITALIC)
    nodes = split_nodes_links(nodes)
    nodes = split_nodes_images(nodes)
    return nodes