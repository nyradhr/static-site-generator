import unittest
from block_to_blocktype import block_to_blocktype

class TestBlockToBlockType(unittest.TestCase):

    def test_paragraph(self):
        block = (
            "Robin Hood and Little John\n"
            "Walking through the forest\n"
            "Laughing back and forth at what\n"
            "The other has to say"
        )
        type = block_to_blocktype(block)
        expected = "paragraph"
        self.assertEqual(type, expected)

    def test_empty_string(self):
        block = ""
        type = block_to_blocktype(block)
        expected = "paragraph"
        self.assertEqual(type, expected)
    
    def test_quotes_spaces_between_lines(self):
        block = (
            "> Hi there\n"
            "   > Trying out new things\n"
            "  > This should not work\n"
            "> Probably"
        )
        type = block_to_blocktype(block)
        expected = "quote"
        self.assertEqual(type, expected)
    
    def test_quote_single_line(self):
        block = "> This is a memorable quote"
        type = block_to_blocktype(block)
        expected = "quote"
        self.assertEqual(type, expected)

    def test_quote_many_spaces_after(self):
        block = ">        space!"
        type = block_to_blocktype(block)
        expected = "quote"
        self.assertEqual(type, expected)

    def test_unordered_list_mixed_symbols(self):
        block = (
            "* one\n"
            "- two\n"
            "* three\n"
            "- four"
        )
        type = block_to_blocktype(block)
        expected = "paragraph"
        self.assertEqual(type, expected)

    def test_unordered_list_asterisks(self):
        block = (
            "* First\n"
            "* Second\n"
            "* Third"
        )
        type = block_to_blocktype(block)
        expected = "unordered_list"
        self.assertEqual(type, expected)
    
    def test_unordered_list_dashes(self):
        block = (
            "- First\n"
            "- Second\n"
            "- Third"
        )
        type = block_to_blocktype(block)
        expected = "unordered_list"
        self.assertEqual(type, expected)
    
    def test_unordered_list_malformed(self):
        block = (
            "-This is wrong\n"
            "- This is fine\n"
            "-        This should also be fine"
        )
        type = block_to_blocktype(block)
        expected = "paragraph"
        self.assertEqual(type, expected)
    
    def test_ordered_list_unsorted_numbers(self):
        block = (
            "1. one\n"
            "2. two\n"
            "4. three\n"
            "3. four"
            )
        type = block_to_blocktype(block)
        expected = "paragraph"
        self.assertEqual(type, expected)
    
    def test_ordered_list_correct(self):
        block = (
            "1. one\n"
            "2. two\n"
            "3. three"
        )
        type = block_to_blocktype(block)
        expected = "ordered_list"
        self.assertEqual(type, expected)

    def test_ordered_list_wrong_start(self):
        block = (
            "2. one\n"
            "3. two\n"
            "4. three"
        )
        type = block_to_blocktype(block)
        expected = "paragraph"
        self.assertEqual(type, expected)

    def test_ordered_list_wrong_format(self):
        block = (
            "1.one\n"
            "2.     two\n"
            "4. three"
        )
        type = block_to_blocktype(block)
        expected = "paragraph"
        self.assertEqual(type, expected)

    def test_valid_heading(self):
        block = "### Heading 3"
        type = block_to_blocktype(block)
        expected = "heading"
        self.assertEqual(type, expected)

    def test_invalid_heading(self):
        block = "####### Heading 7"
        type = block_to_blocktype(block)
        expected = "paragraph"
        self.assertEqual(type, expected)

    def test_code_valid(self):
        block = (
            "``` let x = 1;\n"
            " const HI = \"Goodbye\";\n"
            " x += 41;\n"
            " console.log(x)```"
        )
        type = block_to_blocktype(block)
        expected = "code"
        self.assertEqual(type, expected)

    def test_code_no_closing_backticks(self):
        block = (
            "``` class WrongBlock {\n"
            " public static void mistake(Nope[] wrong) {\n"
            " System.out.println(\"we should not do this\")}}"
        )
        type = block_to_blocktype(block)
        expected = "paragraph"
        self.assertEqual(type, expected)
    
    def test_code_wrong_number_backticks(self):
        block = (
            "`` var Var = \"var\" ``"
        )
        type = block_to_blocktype(block)
        expected = "paragraph"
        self.assertEqual(type, expected)
