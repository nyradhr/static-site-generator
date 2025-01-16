import unittest
from markdown_to_blocks import markdown_to_blocks

class TestMarkdownToBlocks(unittest.TestCase):

    def test_happy_path(self):
        doc = (
                "# This is a heading\n"
                "\n"
                "This is a paragraph of text. It has some **bold** and *italic* words inside of it.\n"
                "\n"
                "* This is the first list item in a list block\n"
                "* This is a list item\n"
                "* This is another list item"
            )
        blocks = markdown_to_blocks(doc)
        expected = [
            "# This is a heading", 
            "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
            (
                "* This is the first list item in a list block\n"
                "* This is a list item\n"
                "* This is another list item"
            )
        ]
        self.assertEqual(blocks, expected)
        

    def test_excessive_newlines(self):
        doc = "Block 1\n\n\n\n\nBlock 2"
        blocks = markdown_to_blocks(doc)
        expected = ["Block 1", "Block 2"]
        self.assertEqual(blocks, expected)

    def test_empty_doc(self):
        doc = ""
        blocks = markdown_to_blocks(doc)
        expected = []
        self.assertEqual(blocks, expected)
    
    def test_single_block(self):
        doc = "Hello there this is an *example* to see if the function can **correctly** parse a single block"
        blocks = markdown_to_blocks(doc)
        expected = ["Hello there this is an *example* to see if the function can **correctly** parse a single block"]
        self.assertEqual(blocks, expected)
    
    def test_whitespaces_only(self):
        doc = "          "
        blocks = markdown_to_blocks(doc)
        expected = []
        self.assertEqual(blocks, expected)
    
    def test_leading_trailing_whitespaces(self):
        doc = (
                "    1. Nothing wrong with me\n"
                "2. Nothing wrong with me\n"
                "3. Ok that's enough, bye Drowning Pool      \n"
                "\n"
                "     > All my friends are brown and red\n"
                "Spoonman    "
            )
        blocks = markdown_to_blocks(doc)
        expected = [
            (
                "1. Nothing wrong with me\n"
                "2. Nothing wrong with me\n"
                "3. Ok that's enough, bye Drowning Pool"
            ), 
            (
                "> All my friends are brown and red\n"
                "Spoonman"
            )
        ]
        self.assertEqual(blocks, expected)
    