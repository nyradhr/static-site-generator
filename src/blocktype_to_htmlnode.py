from textnode import TextNode, TextType
from htmlnode import HTMLNode

def blocktype_to_htmlnode(blocktype):
    if blocktype == "paragraph":
        return HTMLNode(tag="p", children=[])
    elif blocktype == "heading":
        return HTMLNode(tag="h1", children=[])  # TODO: Adjust tag dynamically for h2, h3, etc.
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


# paragraph --> <p>
# heading ---> check for number of # and get corresponding tag (h1, h2, etc)
# code -> <code>
# quote -> <blockquote>
# unordered_list -> <ul> containing <li> tags for every line --> substitute start of lines "* " or "- " with <li>
# ordered_list -> <ol> containing <li> tags for every line --> substitute start of lines "%d. " with <li>