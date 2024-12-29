
import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_raw_text(self):
        html = HTMLNode(None, "Hello").props_to_html()
        text = ""
        self.assertEqual(html, text)

    def test_props_to_html_paragraph(self):
        html = HTMLNode(tag="p", value="This is a paragraph").props_to_html()
        text = ""
        self.assertEqual(html, text)

    def test_props_to_html_link(self):
        html = HTMLNode(tag="a", value="Click here to win!", props={"href": "click2win.yay"}).props_to_html()
        text = " href=\"click2win.yay\""
        self.assertEqual(html, text)
