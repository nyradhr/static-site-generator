import unittest

from blocktype_to_htmlnode import blocktype_to_htmlnode, heading_tag_parser

class TestBlockTypeToHTMLNode(unittest.TestCase):

    def test_paragraph(self):
        node = blocktype_to_htmlnode("paragraph")
        self.assertEqual(node.tag, "p")

    def test_heading(self):
        node = blocktype_to_htmlnode("heading")
        self.assertEqual(node.tag, None)

    def test_quote(self):
        node = blocktype_to_htmlnode("quote")
        self.assertEqual(node.tag, "blockquote")

    def test_unordered_list(self):
        node = blocktype_to_htmlnode("unordered_list")
        self.assertEqual(node.tag, "ul")

    def test_ordered_list(self):
        node = blocktype_to_htmlnode("ordered_list")
        self.assertEqual(node.tag, "ol")

    def test_code(self):
        node = blocktype_to_htmlnode("code")
        self.assertEqual(node.tag, "pre")
        self.assertIsNotNone(node.children)
        self.assertEqual(node.children[0].tag, "code")

    def test_unknown_type(self):
        with self.assertRaises(ValueError):
            blocktype_to_htmlnode("strange")

class TestHeadingTagParser(unittest.TestCase):

    def test_heading_level_1(self):
        block = "# heading 1"
        tag = heading_tag_parser(block)
        self.assertEqual(tag, "h1")

    def test_heading_level_2(self):
        block = "## heading 2"
        tag = heading_tag_parser(block)
        self.assertEqual(tag, "h2")

    def test_heading_level_3(self):
        block = "### heading 3"
        tag = heading_tag_parser(block)
        self.assertEqual(tag, "h3")

    def test_heading_level_4(self):
        block = "#### heading 4"
        tag = heading_tag_parser(block)
        self.assertEqual(tag, "h4")

    def test_heading_level_5(self):
        block = "##### heading 5"
        tag = heading_tag_parser(block)
        self.assertEqual(tag, "h5")

    def test_heading_level_6(self):
        block = "###### heading 6"
        tag = heading_tag_parser(block)
        self.assertEqual(tag, "h6")

    def test_heading_no_pound_sign(self):
        block = "heading 0"
        with self.assertRaises(ValueError):
            heading_tag_parser(block)

    def test_heading_level_7_invalid(self):
        block = "####### heading 7"
        with self.assertRaises(ValueError):
            heading_tag_parser(block)

    def test_empty_string(self):
        with self.assertRaises(ValueError):
            heading_tag_parser("")

    def test_none_input(self):
        with self.assertRaises(ValueError):
            heading_tag_parser(None)
    
    def test_no_space_after_pound(self):
        with self.assertRaises(ValueError):
            heading_tag_parser("#heading")

    def test_only_pound_signs(self):
        with self.assertRaises(ValueError):
            heading_tag_parser("###")