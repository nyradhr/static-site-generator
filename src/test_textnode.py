import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_url_eq(self):
        node = TextNode("This is a link", TextType.LINK, "example.url")
        node2 = TextNode("This is a link", TextType.LINK, "example.url")
        self.assertEqual(node, node2)

    def test_type_not_eq(self):
        node = TextNode("This is an italic text node", TextType.ITALIC)
        node2 = TextNode("This is an italic text node", TextType.NORMAL)
        self.assertNotEqual(node, node2)

    def test_text_not_eq(self):
        node = TextNode("This is a normal text node", TextType.NORMAL)
        node2 = TextNode("This is a siamese cat", TextType.NORMAL)
        self.assertNotEqual(node, node2)

    def test_url_none_not_eq(self):
        node = TextNode("This is an image", TextType.IMAGE, "image.example")
        node2 = TextNode("This is an image", TextType.IMAGE)
        self.assertNotEqual(node, node2)

    def test_same_url_diff_type_not_eq(self):
        node = TextNode("Dog with a bone", TextType.IMAGE, "example.org")
        node2 = TextNode("Dog with a bone", TextType.LINK, "example.org")


if __name__ == "__main__":
    unittest.main()
