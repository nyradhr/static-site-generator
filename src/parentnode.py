from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag == None:
            raise ValueError("Missing tag")
        if self.children == None or self.children == []:
            raise ValueError("Missing children nodes")
        res = ""
        for child in self.children:
            res += child.to_html()
        return f"<{self.tag}>" + res + f"</{self.tag}>"
