import unittest

from textnode import TextNode, TextType
from splitnodesdelimiter import split_nodes_delimiter

class TestSplitNodesDelimiter(unittest.TestCase):

    def test_end_of_string_delimiter(self):
        test = TextNode("Hello this is an *italics string*", TextType.TEXT)
        nodes = split_nodes_delimiter([test], "`", TextType.CODE)
        nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
        nodes = split_nodes_delimiter(nodes, "*", TextType.ITALIC)
        expected = [TextNode("Hello this is an ", TextType.TEXT), TextNode("italics string", TextType.ITALIC)]
        self.assertEqual(nodes, expected)

    def test_start_of_string_delimiter(self):
        test = TextNode("**Starting the** string with a delimiter", TextType.TEXT)
        nodes = split_nodes_delimiter([test], "`", TextType.CODE)
        nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
        nodes = split_nodes_delimiter(nodes, "*", TextType.ITALIC)
        expected = [TextNode("Starting the", TextType.BOLD), TextNode(" string with a delimiter", TextType.TEXT)]
        self.assertEqual(nodes, expected)
    
    def test_consecutive_empty_delimiters(self):
        test = TextNode("Trying out many `codeblocks ``` one after the other", TextType.TEXT)
        nodes = split_nodes_delimiter([test], "`", TextType.CODE)
        nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
        nodes = split_nodes_delimiter(nodes, "*", TextType.ITALIC)
        expected = [TextNode("Trying out many ", TextType.TEXT), TextNode("codeblocks ", TextType.CODE), TextNode(" one after the other", TextType.TEXT)]
        self.assertEqual(nodes, expected)

    def test_consecutive_delimiters_with_content(self):
        test = TextNode("This time **we have stuff ****inside the next** bit", TextType.TEXT)
        nodes = split_nodes_delimiter([test], "`", TextType.CODE)
        nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
        nodes = split_nodes_delimiter(nodes, "*", TextType.ITALIC)
        expected = [TextNode("This time ", TextType.TEXT), TextNode("we have stuff ", TextType.BOLD), TextNode("inside the next", TextType.BOLD), TextNode(" bit", TextType.TEXT)]
        self.assertEqual(nodes, expected)
    
    def test_multiple_nodes_with_and_without_delimiter(self):
        test = TextNode("This is a node without a delimiter", TextType.TEXT)
        test_2 = TextNode("This is a node with **an actual** delimiter", TextType.TEXT)
        nodes = split_nodes_delimiter([test, test_2], "`", TextType.CODE)
        nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
        nodes = split_nodes_delimiter(nodes, "*", TextType.ITALIC)
        expected = [TextNode("This is a node without a delimiter", TextType.TEXT), TextNode("This is a node with ", TextType.TEXT), TextNode("an actual", TextType.BOLD), TextNode(" delimiter", TextType.TEXT)]
        self.assertEqual(nodes, expected)

    def test_string_with_only_one_delimiter(self):
        test = TextNode("This string only has **one delimiter", TextType.TEXT)
        with self.assertRaises(ValueError):
            split_nodes_delimiter([test], "**", TextType.BOLD)

    def test_mixed_delimiters(self):
        test = TextNode("This node has *italics* and **bold text** in one sentence", TextType.TEXT)
        nodes = split_nodes_delimiter([test], "`", TextType.CODE)
        nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
        nodes = split_nodes_delimiter(nodes, "*", TextType.ITALIC)
        expected = [TextNode("This node has ", TextType.TEXT), TextNode("italics", TextType.ITALIC), TextNode(" and ", TextType.TEXT), TextNode("bold text", TextType.BOLD), TextNode(" in one sentence", TextType.TEXT)]
        self.assertEqual(nodes, expected)