import unittest

from textnode import TextNode, TextType
from text_to_textnodes import text_to_textnodes

class TestTextToTextNodes(unittest.TestCase):

    def test_text_to_textnodes_happy_path(self):
        text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        nodes = text_to_textnodes(text)
        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.TEXT),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev")
        ]
        self.assertEqual(nodes, expected)

    def test_text_to_textnodes_empty_string(self):
        text = ""
        nodes = text_to_textnodes(text)
        expected = []
        self.assertEqual(nodes, expected)

    def test_text_to_textnodes_image_inside_bold_text(self):
        text = "This string contains **bold text with a [link](url) inside** of it"
        nodes = text_to_textnodes(text)
        expected = [
            TextNode("This string contains ", TextType.TEXT),
            TextNode("bold text with a ", TextType.BOLD),
            TextNode("link", TextType.LINK, "url"),
            TextNode(" inside", TextType.BOLD),
            TextNode(" of it", TextType.TEXT)
        ]
        self.assertEqual(nodes, expected)

    def test_text_to_textnodes_only_normal_text(self):
        text = "This string of text does not contain any special markdown character"
        nodes = text_to_textnodes(text)
        expected = [TextNode(text, TextType.TEXT)]
        self.assertEqual(nodes, expected)