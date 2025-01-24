import unittest

from markdown_to_htmlnode import markdown_to_htmlnode

class TestMarkdownToHTMLNode(unittest.TestCase):

    def test_heading_conversion(self):
        markdown = "### This is a heading"
        root_node = markdown_to_htmlnode(markdown)
        heading_node = root_node.children[0]
        self.assertEqual(heading_node.tag, "h3")
        self.assertEqual(heading_node.children[0].tag, None)
        self.assertEqual(heading_node.children[0].value, "This is a heading")


    def test_unordered_list(self):
        markdown = (
            "* First item\n"
            "* Second item\n"
            "* Third item"
        )
        root_node = markdown_to_htmlnode(markdown)
        list_node = root_node.children[0]
        self.assertEqual(list_node.tag, "ul")
        self.assertEqual(len(list_node.children), 3)
        self.assertEqual(list_node.children[0].tag, "li")
        self.assertEqual(list_node.children[0].children[0].tag, None)
        self.assertEqual(list_node.children[0].children[0].value, "First item")
        self.assertEqual(list_node.children[1].tag, "li")
        self.assertEqual(list_node.children[1].children[0].tag, None)
        self.assertEqual(list_node.children[1].children[0].value, "Second item")
        self.assertEqual(list_node.children[2].tag, "li")
        self.assertEqual(list_node.children[2].children[0].tag, None)
        self.assertEqual(list_node.children[2].children[0].value, "Third item")

    def test_multiple_block_types(self):
        markdown = (
            "# Main heading\n\n"
            "This is a paragraph with **bold** text.\n\n"
            "> This is a quote\n\n"
            "* List item 1\n"
            "* List item 2"
        )
        root_node = markdown_to_htmlnode(markdown)
        self.assertEqual(root_node.tag, "div")
        self.assertEqual(len(root_node.children), 4)
        self.assertEqual(root_node.children[0].tag, "h1")
        self.assertEqual(root_node.children[0].children[0].value, "Main heading")
        self.assertEqual(root_node.children[1].tag, "p")
        self.assertEqual(root_node.children[1].children[0].tag, None)
        self.assertEqual(root_node.children[1].children[0].value, "This is a paragraph with ")
        self.assertEqual(root_node.children[1].children[1].tag, "b")
        self.assertEqual(root_node.children[1].children[1].value, "bold")
        self.assertEqual(root_node.children[1].children[2].tag, None)
        self.assertEqual(root_node.children[1].children[2].value, " text.")
        self.assertEqual(root_node.children[2].tag, "blockquote")
        self.assertEqual(root_node.children[2].children[0].tag, None)
        self.assertEqual(root_node.children[2].children[0].value, "This is a quote")
        self.assertEqual(root_node.children[3].tag, "ul")
        self.assertEqual(root_node.children[3].children[0].tag, "li")
        self.assertEqual(root_node.children[3].children[0].children[0].tag, None)
        self.assertEqual(root_node.children[3].children[0].children[0].value, "List item 1")
        self.assertEqual(root_node.children[3].children[1].tag, "li")
        self.assertEqual(root_node.children[3].children[1].children[0].tag, None)
        self.assertEqual(root_node.children[3].children[1].children[0].value, "List item 2")

    def test_ordered_list(self):
        markdown = (
            "1. First ordered item\n"
            "2. Second ordered item with **bold**\n"
            "3. Third ordered item with *italic*"
        )
        root_node = markdown_to_htmlnode(markdown)
        list_node = root_node.children[0]
        self.assertEqual(list_node.tag, "ol")
        self.assertEqual(len(list_node.children), 3)
        self.assertEqual(list_node.children[0].tag, "li")
        self.assertEqual(list_node.children[0].children[0].tag, None)
        self.assertEqual(list_node.children[0].children[0].value, "First ordered item")
        self.assertEqual(list_node.children[1].tag, "li")
        self.assertEqual(list_node.children[1].children[0].tag, None)
        self.assertEqual(list_node.children[1].children[0].value, "Second ordered item with ")
        self.assertEqual(list_node.children[1].children[1].tag, "b")
        self.assertEqual(list_node.children[1].children[1].value, "bold")
        self.assertEqual(list_node.children[2].tag, "li")
        self.assertEqual(list_node.children[2].children[0].tag, None)
        self.assertEqual(list_node.children[2].children[0].value, "Third ordered item with ")
        self.assertEqual(list_node.children[2].children[1].tag, "i")
        self.assertEqual(list_node.children[2].children[1].value, "italic")

    def test_code(self):
        markdown = (
            "```\n"
            "def hello_world():\n"
            "    print(\"Hello World\")\n"
            "```"        
        )
        expected = (
            "\n"
            "def hello_world():\n"
            "    print(\"Hello World\")\n"   
        )
        root_node = markdown_to_htmlnode(markdown)
        code_node = root_node.children[0]
        self.assertEqual(code_node.tag, "pre")
        self.assertEqual(code_node.children[0].tag, "code")
        self.assertEqual(code_node.children[0].children[0].tag, None)
        self.assertEqual(code_node.children[0].children[0].value, expected)

    def test_inline(self):
        markdown = "This is *italic*, this is **bold**, and this is `code`"
        root_node = markdown_to_htmlnode(markdown)
        paragraph_node = root_node.children[0]
        self.assertEqual(paragraph_node.children[0].tag, None)
        self.assertEqual(paragraph_node.children[0].value, "This is ")
        self.assertEqual(paragraph_node.children[1].tag, "i")
        self.assertEqual(paragraph_node.children[1].value, "italic")
        self.assertEqual(paragraph_node.children[2].tag, None)
        self.assertEqual(paragraph_node.children[2].value, ", this is ")
        self.assertEqual(paragraph_node.children[3].tag, "b")
        self.assertEqual(paragraph_node.children[3].value, "bold")
        self.assertEqual(paragraph_node.children[4].tag, None)
        self.assertEqual(paragraph_node.children[4].value, ", and this is ")
        self.assertEqual(paragraph_node.children[5].tag, "code")
        self.assertEqual(paragraph_node.children[5].value, "code")


    def test_quotes(self):
        markdown = (
            "> First quote\n"
            "> Still first quote\n"
            ">\n"
            "> Second quote after empty quote line\n"
        )
        root_node = markdown_to_htmlnode(markdown)
        quote_node = root_node.children[0]
        self.assertEqual(quote_node.tag, "blockquote")
        self.assertEqual(quote_node.children[0].tag, None)
        self.assertEqual(quote_node.children[0].value, "First quote\nStill first quote\n\nSecond quote after empty quote line")

    def test_complex_list(self):
        markdown = (
            "* List with **bold**\n"
            "* List with *italic*\n"
            "* List with `code`\n"
        )
        root_node = markdown_to_htmlnode(markdown)
        list_node = root_node.children[0]
        self.assertEqual(list_node.tag, "ul")
        self.assertEqual(list_node.children[0].tag, "li")
        self.assertEqual(list_node.children[0].children[0].tag, None)
        self.assertEqual(list_node.children[0].children[0].value, "List with ")
        self.assertEqual(list_node.children[0].children[1].tag, "b")
        self.assertEqual(list_node.children[0].children[1].value, "bold")
        self.assertEqual(list_node.children[1].tag, "li")
        self.assertEqual(list_node.children[1].children[0].tag, None)
        self.assertEqual(list_node.children[1].children[0].value, "List with ")
        self.assertEqual(list_node.children[1].children[1].tag, "i")
        self.assertEqual(list_node.children[1].children[1].value, "italic")
        self.assertEqual(list_node.children[2].children[0].tag, None)
        self.assertEqual(list_node.children[2].children[0].value, "List with ")
        self.assertEqual(list_node.children[2].children[1].tag, "code")
        self.assertEqual(list_node.children[2].children[1].value, "code")

    def test_complex_heading(self):
        markdown = (
            "# Main heading with *italic* and **bold**\n\n"
            "## Second heading with `code`"
        )
        root_node = markdown_to_htmlnode(markdown)
        self.assertEqual(root_node.children[0].tag, "h1")
        self.assertEqual(root_node.children[0].children[0].tag, None)
        self.assertEqual(root_node.children[0].children[0].value, "Main heading with ")
        self.assertEqual(root_node.children[0].children[1].tag, "i")
        self.assertEqual(root_node.children[0].children[1].value, "italic")
        self.assertEqual(root_node.children[0].children[2].tag, None)
        self.assertEqual(root_node.children[0].children[2].value, " and ")
        self.assertEqual(root_node.children[0].children[3].tag, "b")
        self.assertEqual(root_node.children[0].children[3].value, "bold")
        self.assertEqual(root_node.children[1].tag, "h2")
        self.assertEqual(root_node.children[1].children[0].tag, None)
        self.assertEqual(root_node.children[1].children[0].value, "Second heading with ")
        self.assertEqual(root_node.children[1].children[1].tag, "code")
        self.assertEqual(root_node.children[1].children[1].value, "code")


    def test_empty_blocks(self):
        markdown = (
            "First paragraph\n\n"
            "\n\n"
            "Second paragraph after 2 newlines\n\n"
            "> A quote\n\n"
            "\n"
            "Another paragraph after quote and 2 newlines"
        )
        root_node = markdown_to_htmlnode(markdown)
        self.assertEqual(root_node.children[0].tag, "p")
        self.assertEqual(root_node.children[0].children[0].tag, None)
        self.assertEqual(root_node.children[0].children[0].value, "First paragraph")
        self.assertEqual(root_node.children[1].tag, "p")
        self.assertEqual(root_node.children[1].children[0].tag, None)
        self.assertEqual(root_node.children[1].children[0].value, "Second paragraph after 2 newlines")
        self.assertEqual(root_node.children[2].tag, "blockquote")
        self.assertEqual(root_node.children[2].children[0].tag, None)
        self.assertEqual(root_node.children[2].children[0].value, "A quote")
        self.assertEqual(root_node.children[3].tag, "p")
        self.assertEqual(root_node.children[3].children[0].tag, None)
        self.assertEqual(root_node.children[3].children[0].value, "Another paragraph after quote and 2 newlines")
