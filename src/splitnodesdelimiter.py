from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type == TextType.TEXT:
            parts = node.text.split(delimiter)
            if len(parts) % 2 == 0:
                raise ValueError(f"Incorrectly placed delimiter: '{delimiter}' in text '{node.text}'")
            is_inside_delimiter = False
            for part in parts:
                if part:
                    new_nodes.append(TextNode(part, text_type if is_inside_delimiter else TextType.TEXT))
                is_inside_delimiter = not is_inside_delimiter
        else:
            new_nodes.append(node)
    return new_nodes