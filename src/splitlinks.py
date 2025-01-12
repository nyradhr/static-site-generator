from textnode import TextNode, TextType
from extractlinks import extract_markdown_images, extract_markdown_links

def split_nodes_links(old_nodes):
    new_nodes = []
    for node in old_nodes:
        #maybe check type so that we exclude link and image nodes?
        links = extract_markdown_links(node.text)
        if len(links) == 0:
            new_nodes.append(node)
        else:
            __split_nodes_url(node, new_nodes, links, TextType.LINK)
    return new_nodes

def split_nodes_images(old_nodes):
    new_nodes = []
    for node in old_nodes:
        #maybe check type so that we exclude link and image nodes?
        images = extract_markdown_images(node.text)
        if len(images) == 0:
            new_nodes.append(node)
        else:
            __split_nodes_url(node, new_nodes, images, TextType.IMAGE)
    return new_nodes

def __split_nodes_url(node, new_nodes, elements, type):
    text = node.text
    for element in elements:
        alt = element[0]
        url = element[1]
        if text != "":
            if type == TextType.LINK:
                split_text = text.split(f"[{alt}]({url})", 1)
            else:
                split_text = text.split(f"![{alt}]({url})", 1)
            if split_text[0] != "":
                new_nodes.append(TextNode(split_text[0], TextType.TEXT))
            new_nodes.append(TextNode(alt, type, url))
            text = split_text[1]
    if text != "":
        new_nodes.append(TextNode(text, TextType.TEXT))