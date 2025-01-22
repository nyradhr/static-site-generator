import unittest

from block_to_text import block_to_text

class TestBlockToText(unittest.TestCase):

    def test_paragraph(self):
       block = (
        "Great Scott!\n"
        "This is a paragraph and a half!\n"
        "It's so very long,\n"
        "it seems like it may never end...\n"
        "oh wait we're done."
       )
       text = block_to_text(block, "paragraph")
       self.assertEqual(block, text)

    def test_quote_single_line(self):
        block = "> This is a memorable quote."
        text = block_to_text(block, "quote")
        self.assertEqual(text, "This is a memorable quote.") 
    
    def test_quote_multiple_lines(self):
        block = (
            "> First line\n"
            "> Second line\n"
            "> Third line"
        )
        text = block_to_text(block, "quote")
        expected = (
            "First line\n"
            "Second line\n"
            "Third line"
        )
        self.assertEqual(text, expected) 

    def test_unordered_list_asterisk(self):
        block = (
            "* First\n"
            "* Second\n"
            "* Third"
        )
        text = block_to_text(block, "unordered_list")
        expected = (
            "First\n"
            "Second\n"
            "Third"
        )
        self.assertEqual(text, expected)

    def test_unordered_list_dash(self):
        block = (
            "- First\n"
            "- Second\n"
            "- Third"
        )
        text = block_to_text(block, "unordered_list")
        expected = (
            "First\n"
            "Second\n"
            "Third"
        )
        self.assertEqual(text, expected)

    def test_ordered_list(self):
        block = (
            "1. First\n"
            "2. Second\n"
            "3. Third"
        )
        text = block_to_text(block, "ordered_list")
        expected = (
            "First\n"
            "Second\n"
            "Third"
        )
        self.assertEqual(text, expected)
    
    def test_heading_h1(self):
        block = "# heading 1"
        text = block_to_text(block, "heading")
        expected = "heading 1"
        self.assertEqual(text, expected)
    
    def test_heading_h5(self):
        block = "##### heading 5"
        text = block_to_text(block, "heading")
        expected = "heading 5"
        self.assertEqual(text, expected)
    
    def test_code(self):
        block = (
            "``` x = 12;\n"
            "console.log(x);```"
        )
        text = block_to_text(block, "code")
        expected = (
            " x = 12;\n"
            "console.log(x);"
        )
        self.assertEqual(text, expected)