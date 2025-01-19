# input: block
# extrapolate INLINE TextNodes
# text_to_textnodes --> list of TextNodes that compose the block
# textnode_to_htmlnode --> list of HTMLNodes
# please note: leafnodes might be used instead of htmlnodes when considering inline elements
def text_to_children_nodes(text):
    return None