from parentnode import ParentNode

def blocktype_to_htmlnode(blocktype):
    """Convert a markdown block type to its corresponding HTMLNode.

    Args:
        blocktype (str): The type of markdown block.

    Returns:
        HTMLNode: A new HTMLNode object with the appropriate tag.
        For code blocks, returns a pre node containing a code node.
        For heading blocks, returns a node with tag=None (to be set later by heading_tag_parser).

    Raises:
        ValueError: If blocktype is not one of the valid types.
    """
    if blocktype == "paragraph":
        return ParentNode(tag="p", children=None)
    elif blocktype == "heading":
        return ParentNode(tag=None, children=None)
    elif blocktype == "quote":
        return ParentNode(tag="blockquote", children=None)
    elif blocktype == "unordered_list":
        return ParentNode(tag="ul", children=None)
    elif blocktype == "ordered_list":
        return ParentNode(tag="ol", children=None)
    elif blocktype == "code":
        return ParentNode(tag="pre", children=[ParentNode(tag="code", children=None)])
    else:
        raise ValueError(f"Unknown block type: {blocktype}")

def heading_tag_parser(block):
    """Convert a markdown heading block to its HTML tag.
        
        Args:
            block (str): A markdown heading block starting with '#' characters
            
        Returns:
            str: HTML heading tag (h1-h6)
            
        Raises:
            ValueError: If block is not a valid heading
    """ 
    if not block or not isinstance(block, str):
        raise ValueError("Block must be a non-empty string")
        
    content_start = 0
    while content_start < len(block) and block[content_start] == '#':
        content_start += 1
        if content_start > 6:
            raise ValueError("Too many #'s: maximum heading level is 6")
            
    if content_start == 0 or content_start >= len(block) or block[content_start] != ' ':
        raise ValueError("Invalid heading format: must start with # followed by space")
        
    return f"h{content_start}"