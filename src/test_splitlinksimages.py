import unittest

from textnode import TextNode, TextType
from splitlinks import split_nodes_links, split_nodes_images


class TestSplitLinks(unittest.TestCase):

    def test_split_one_link(self):
        input_node = [TextNode("Let's try one link [hello](url)", TextType.TEXT)]
        split_nodes = split_nodes_links(input_node)
        expected = [TextNode("Let's try one link ", TextType.TEXT), TextNode("hello", TextType.LINK, "url")]
        self.assertEqual(split_nodes, expected)

    def test_split_one_image(self):
        input_node = [TextNode("Let's try one image ![description](img.jpg)", TextType.TEXT)]
        split_nodes = split_nodes_images(input_node)
        expected = [TextNode("Let's try one image ", TextType.TEXT), TextNode("description", TextType.IMAGE, "img.jpg")]
        self.assertEqual(split_nodes, expected)

    def test_split_multiple_links(self):
        input_node = [TextNode("This string contains a [first](link) and even a [second](link)", TextType.TEXT)] 
        split_nodes = split_nodes_links(input_node)
        expected = [TextNode("This string contains a ", TextType.TEXT), TextNode("first", TextType.LINK, "link"), TextNode(" and even a ", TextType.TEXT), TextNode("second", TextType.LINK, "link")]
        self.assertEqual(split_nodes, expected)

    def test_split_multiple_images(self):
        input_node = [TextNode("This string contains a ![first](image) and even a ![second](image)", TextType.TEXT)] 
        split_nodes = split_nodes_images(input_node)
        expected = [TextNode("This string contains a ", TextType.TEXT), TextNode("first", TextType.IMAGE, "image"), TextNode(" and even a ", TextType.TEXT), TextNode("second", TextType.IMAGE, "image")]
        self.assertEqual(split_nodes, expected)

    def test_split_no_link(self):
        input_node = [TextNode("This string does not contain a link", TextType.TEXT)]
        split_nodes = split_nodes_links(input_node)
        expected = [TextNode("This string does not contain a link", TextType.TEXT)]
        self.assertEqual(split_nodes, expected)

    def test_split_no_images(self):
        input_node = [TextNode("This string does not contain an image", TextType.TEXT)]
        split_nodes = split_nodes_images(input_node)
        expected = [TextNode("This string does not contain an image", TextType.TEXT)]
        self.assertEqual(split_nodes, expected)

    def test_split_links_from_string_with_image(self):
        input_node = [TextNode("This string contains a [link](url) and even an ![image](url)", TextType.TEXT)] 
        split_nodes = split_nodes_links(input_node)
        expected = [TextNode("This string contains a ", TextType.TEXT), TextNode("link", TextType.LINK, "url"), TextNode(" and even an ![image](url)", TextType.TEXT)]
        self.assertEqual(split_nodes, expected)

    def test_split_images_from_string_with_link(self):
        input_node = [TextNode("This string contains a [link](url) and even an ![image](url)", TextType.TEXT)] 
        split_nodes = split_nodes_images(input_node)
        expected = [TextNode("This string contains a [link](url) and even an ", TextType.TEXT), TextNode("image", TextType.IMAGE, "url")]
        self.assertEqual(split_nodes, expected)

    def test_split_links_empty_string(self):
        input_node = [TextNode("", TextType.TEXT)]
        split_nodes = split_nodes_links(input_node)
        expected = [TextNode("", TextType.TEXT)]
        self.assertEqual(split_nodes, expected)

    def test_split_images_empty_string(self):
        input_node = [TextNode("", TextType.TEXT)]
        split_nodes = split_nodes_images(input_node)
        expected = [TextNode("", TextType.TEXT)]
        self.assertEqual(split_nodes, expected)
    
    def test_split_links_malformed_markdown(self):
        input_node = [TextNode("[link](url", TextType.TEXT)]
        split_nodes = split_nodes_links(input_node)
        expected = [TextNode("[link](url", TextType.TEXT)]
        self.assertEqual(split_nodes, expected)

    def test_split_images_malformed_markdown(self):
        input_node = [TextNode("![image(url)", TextType.TEXT)]
        split_nodes = split_nodes_images(input_node)
        expected = [TextNode("![image(url)", TextType.TEXT)]
        self.assertEqual(split_nodes, expected)

    def test_split_links_multiple_nodes(self):
        input_node = [TextNode("First node [link](url)", TextType.TEXT), TextNode("Second node ![image](url)", TextType.TEXT)]
        split_nodes = split_nodes_links(input_node)
        expected = [TextNode("First node ", TextType.TEXT), TextNode("link", TextType.LINK, "url"), TextNode("Second node ![image](url)", TextType.TEXT)]
        self.assertEqual(split_nodes, expected)

    def test_split_images_multiple_nodes(self):
        input_node = [TextNode("First node [link](url)", TextType.TEXT), TextNode("Second node ![image](url)", TextType.TEXT)]
        split_nodes = split_nodes_images(input_node)
        expected = [TextNode("First node [link](url)", TextType.TEXT), TextNode("Second node ", TextType.TEXT), TextNode("image", TextType.IMAGE, "url")]
        self.assertEqual(split_nodes, expected)

    def test_split_links_bold_node(self):
        input_node = [TextNode("[link](url)", TextType.BOLD)]
        split_nodes = split_nodes_links(input_node)
        expected = [TextNode("link", TextType.LINK, "url")]
        self.assertEqual(split_nodes, expected)

    def test_split_images_italics_node(self):
        input_node = [TextNode("![alt](url)", TextType.ITALIC)]
        split_nodes = split_nodes_images(input_node)
        expected = [TextNode("alt", TextType.IMAGE, "url")]
        self.assertEqual(split_nodes, expected)

    def test_split_links_url_special_chars_spaces(self):
        input_node = [TextNode("[link](https://example.com/path with spaces)", TextType.TEXT)]
        split_nodes = split_nodes_links(input_node)
        expected = [TextNode("link", TextType.LINK, "https://example.com/path with spaces")]
        self.assertEqual(split_nodes, expected)

    def test_split_images_url_special_chars_spaces(self):
        input_node = [TextNode("![description](https://example.com/path with spaces/image.png)", TextType.TEXT)]
        split_nodes = split_nodes_images(input_node)
        expected = [TextNode("description", TextType.IMAGE, "https://example.com/path with spaces/image.png")]
        self.assertEqual(split_nodes, expected)
    
    def test_split_links_link_node(self):
        input_node = [TextNode("link", TextType.LINK, "url")]
        split_nodes = split_nodes_links(input_node)
        expected = [TextNode("link", TextType.LINK, "url")]
        self.assertEqual(split_nodes, expected)

    def test_split_images_image_node(self):
        input_node = [TextNode("description", TextType.IMAGE, "url")]
        split_nodes = split_nodes_images(input_node)
        expected = [TextNode("description", TextType.IMAGE, "url")]
        self.assertEqual(split_nodes, expected)

    def test_split_links_mixed_malformed_markdown(self):
        input_node = [TextNode("[link1](url [link2](url2)", TextType.TEXT)]
        split_nodes = split_nodes_links(input_node)
        expected = [TextNode("[link1](url ", TextType.TEXT), TextNode("link2", TextType.LINK, "url2")]
        self.assertEqual(split_nodes, expected)
    
    def test_split_images_mixed_malformed_markdown(self):
        input_node = [TextNode("![image1](url ![image2](url2)", TextType.TEXT)]
        split_nodes = split_nodes_images(input_node)
        expected = [TextNode("![image1](url ", TextType.TEXT), TextNode("image2", TextType.IMAGE, "url2")]
        self.assertEqual(split_nodes, expected)
    
    # Nested elements are currently out of the scope of the project

    # def test_split_links_nested_in_alt_text(self):
    #      input_node = [TextNode("[outer [inner](url2)](url1)", TextType.TEXT)]
    #     split_nodes = split_nodes_links(input_node)
    #     expected = [TextNode("[outer ", TextType.TEXT), TextNode("inner", TextType.LINK, "url2"), TextNode("](url1)", TextType.TEXT)]
    #     self.assertEqual(split_nodes, expected)
    
    # def test_split_images_nested_in_alt_text(self):
    #     input_node = [TextNode("![outer ![inner](url2)](url1)", TextType.TEXT)]
    #     split_nodes = split_nodes_images(input_node)
    #     expected = [TextNode("![outer ", TextType.TEXT), TextNode("inner", TextType.IMAGE, "url2"), TextNode("](url1)", TextType.TEXT)]
    #     self.assertEqual(split_nodes, expected)
    
    # def test_split_links_nested_in_url(self):
    #     input_node = [TextNode("[outer]([inner](url2)url1)", TextType.TEXT)]
    #     split_nodes = split_nodes_links(input_node)
    #     expected = [TextNode("[outer](", TextType.TEXT), TextNode("inner", TextType.LINK, "url2"), TextNode("url1)", TextType.TEXT)]
    #     self.assertEqual(split_nodes, expected)
    
    # def test_split_images_nested_in_url(self):
    #     input_node = [TextNode("![outer](![inner](url2)url1)", TextType.TEXT)]
    #     split_nodes = split_nodes_images(input_node)
    #     expected = [TextNode("![outer](", TextType.TEXT), TextNode("inner", TextType.IMAGE, "url2"), TextNode("url1)", TextType.TEXT)]
    #     self.assertEqual(split_nodes, expected)