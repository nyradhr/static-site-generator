import unittest

from extract_title import extract_title

class TestExtractTitle(unittest.TestCase):

    def test_header_one(self):
        markdown = "# Hello"
        self.assertEqual(extract_title(markdown), "Hello")
    
    def test_header_two(self):
        markdown = " ##  Hi"
        with self.assertRaises(Exception):
            extract_title(markdown)

    def test_header_one_leading_spaces(self):
        markdown = "   # Nope"
        with self.assertRaises(Exception):
            extract_title(markdown)

    def test_header_one_trailing_spaces(self):
        markdown = "#   Yup"
        self.assertEqual(extract_title(markdown), "Yup")