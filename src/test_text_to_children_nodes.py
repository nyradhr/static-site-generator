import unittest

from leafnode import LeafNode
from text_to_children_nodes import text_to_children_nodes

class TestTextToChildrenNodes(unittest.TestCase):

    def test_plain_text(self):
        text = (
            "One two three\n"
            "Four five six"
        )
        nodes = text_to_children_nodes(text)
        expected = [LeafNode(tag=None, value="One two three\nFour five six")]
        self.assertEqual(nodes, expected)

    def test_bold_text(self):
        text = (
            "This text is very\n"
            "**bold**"
        )
        nodes = text_to_children_nodes(text)
        expected = [LeafNode(tag=None, value="This text is very\n"), LeafNode(tag="b", value="bold")]
        self.assertEqual(nodes, expected)
    
    def test_italic_text(self):
        text = (
            "*Oh my...*\n"
            "so very *sophisticated*."
        )
        nodes = text_to_children_nodes(text)
        expected = [
            LeafNode(tag="i", value="Oh my..."), 
            LeafNode(tag=None, value="\nso very "), 
            LeafNode(tag="i", value="sophisticated"),
            LeafNode(tag=None, value="."), 
        ]
        self.assertEqual(nodes, expected)

    def test_inline_code(self):
        text = (
            "This string contains a snippet of code:\n"
            "`if (x in arr) {\n"
            "return y\n"
            "}`\n"
            "Neat, right?"
        )
        nodes = text_to_children_nodes(text)
        expected = [
            LeafNode(tag=None, value="This string contains a snippet of code:\n"), 
            LeafNode(tag="code", value="if (x in arr) {\nreturn y\n}"),
            LeafNode(tag=None, value="\nNeat, right?")
        ]
        self.assertEqual(nodes, expected)

    def test_link(self):
        text = "Visit [Boot.dev](https://boot.dev)"
        nodes = text_to_children_nodes(text)
        expected = [
            LeafNode(tag=None, value="Visit "),
            LeafNode(tag="a", value="Boot.dev", props={"href": "https://boot.dev"})
        ]
        self.assertEqual(nodes, expected)

    def test_mixed_inline(self):
        text = "**Bold** with `code` and *italic*"
        nodes = text_to_children_nodes(text)
        expected = [
            LeafNode(tag="b", value="Bold"),
            LeafNode(tag=None, value=" with "),
            LeafNode(tag="code", value="code"),
            LeafNode(tag=None, value=" and "),
            LeafNode(tag="i", value="italic")
        ]
        self.assertEqual(nodes, expected)

    def test_empty_block(self):
        text = ""
        nodes = text_to_children_nodes(text)
        expected = []
        self.assertEqual(nodes, expected)

    def test_image(self):
        text = "Here's a logo: ![Boot.dev](https://boot.dev/logo.png)"
        nodes = text_to_children_nodes(text)
        expected = [
            LeafNode(tag=None, value="Here's a logo: "),
            LeafNode(tag="img", value="", props={"src": "https://boot.dev/logo.png", "alt": "Boot.dev"})
        ]
        self.assertEqual(nodes, expected)