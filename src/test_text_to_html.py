import unittest

from text_to_html import text_node_to_html_node
from leafnode import LeafNode
from textnode import TextNode, TextType


class TestTextToHtml(unittest.TestCase):
    def test_text(self):
        node = text_node_to_html_node(TextNode("Just a string of text", TextType.TEXT))
    
        self.assertIsInstance(node, LeafNode)
        self.assertEqual(node.tag, None)
        self.assertEqual(node.value, "Just a string of text")
        self.assertEqual(node.children, None)
        self.assertEqual(node.props, None)

    def test_bold(self):
        node = text_node_to_html_node(TextNode("This string is in bold text", TextType.BOLD))

        self.assertIsInstance(node, LeafNode)
        self.assertEqual(node.tag, "b")
        self.assertEqual(node.value, "This string is in bold text")
        self.assertEqual(node.children, None)
        self.assertEqual(node.props, None)

    def test_italic(self):
        node = text_node_to_html_node(TextNode("This string is in italic text", TextType.ITALIC))

        self.assertIsInstance(node, LeafNode)
        self.assertEqual(node.tag, "i")
        self.assertEqual(node.value, "This string is in italic text")
        self.assertEqual(node.children, None)
        self.assertEqual(node.props, None)
    
    def test_code(self):
        node = text_node_to_html_node(TextNode("x = BigNumber(13214514)", TextType.CODE))

        self.assertIsInstance(node, LeafNode)
        self.assertEqual(node.tag, "code")
        self.assertEqual(node.value, "x = BigNumber(13214514)")
        self.assertEqual(node.children, None)
        self.assertEqual(node.props, None)

    def test_link(self):
        node = text_node_to_html_node(TextNode("This is the one true website", TextType.LINK, "oneringtorulethemall.org"))

        self.assertIsInstance(node, LeafNode)
        self.assertEqual(node.tag, "a")
        self.assertEqual(node.value, "This is the one true website")
        self.assertEqual(node.children, None)
        self.assertEqual(node.props, {"href": "oneringtorulethemall.org"})

    def test_image(self):
        node = text_node_to_html_node(TextNode("Gaze upon the magnificence of the Emperor of Mankind!", TextType.IMAGE, "heresy.png"))

        self.assertIsInstance(node, LeafNode)
        self.assertEqual(node.tag, "img")
        self.assertEqual(node.value, "")
        self.assertEqual(node.children, None)
        self.assertEqual(node.props, {"src": "heresy.png", "alt": "Gaze upon the magnificence of the Emperor of Mankind!"})
    
    def test_invalid_type(self):
        with self.assertRaises(ValueError):
            text_node_to_html_node(TextNode("Just a string of text", "InvalidType"))

    def test_non_text_node(self):
        with self.assertRaises(Exception):
            text_node_to_html_node("This is not a TextNode")

    def test_text_with_url(self):
        node = text_node_to_html_node(TextNode("Just a string of text", TextType.TEXT, "yikes.ohno"))
    
        self.assertIsInstance(node, LeafNode)
        self.assertEqual(node.tag, None)
        self.assertEqual(node.value, "Just a string of text")
        self.assertEqual(node.children, None)
        self.assertEqual(node.props, None)
    
    def test_empty_text(self):
        node = text_node_to_html_node(TextNode("", TextType.TEXT))

        self.assertIsInstance(node, LeafNode)
        self.assertEqual(node.tag, None)
        self.assertEqual(node.value, "")
        self.assertEqual(node.children, None)
        self.assertEqual(node.props, None)

    def test_link_without_url(self):
        with self.assertRaises(ValueError):
            text_node_to_html_node(TextNode("Click here", TextType.LINK))

    def test_image_without_url(self):
        with self.assertRaises(ValueError):
            text_node_to_html_node(TextNode("Alt text", TextType.IMAGE))