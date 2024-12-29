import unittest

from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_paragraph_to_html(self):
        leaf = LeafNode(tag="p", value="How are you doing mate?").to_html()
        html = "<p>How are you doing mate?</p>"
        self.assertEqual(leaf, html)

    def test_link_to_html(self):
        leaf = LeafNode(tag="a", value="Download this game now!", props={"href": "whatascam.youfool"}).to_html()
        html = "<a href=\"whatascam.youfool\">Download this game now!</a>"
        self.assertEqual(leaf, html)

    def test_bold_to_html(self):
        leaf = LeafNode(tag="b", value="extremely important message").to_html()
        html = "<b>extremely important message</b>"
        self.assertEqual(leaf, html)
