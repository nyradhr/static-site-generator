import unittest

from parentnode import ParentNode
from leafnode import LeafNode


class TestParentNode(unittest.TestCase):
    def test_many_children_to_html(self):
        many_children = ParentNode(tag="p",children=[LeafNode("b", "Bold text"), LeafNode(None, "Normal text"), LeafNode("i", "italic text"), LeafNode(None, "Normal text")]).to_html()
        expected = "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
        self.assertEqual(many_children, expected)

    def test_empty_list_children_to_html(self):
        empty_children = ParentNode(tag="p", children=[])
        with self.assertRaises(ValueError):
            empty_children.to_html()

    def test_none_children_to_html(self):
        none_children = ParentNode(tag="p", children=None)
        with self.assertRaises(ValueError):
            none_children.to_html()

    def test_none_tag_to_html(self):
        none_tag = ParentNode(tag=None, children=[LeafNode(None, "Normal text")])
        with self.assertRaises(ValueError):
            none_tag.to_html()

    def test_one_children_to_html(self):
        one_children = ParentNode(tag="p", children=[LeafNode(None, "Normal text")]).to_html()
        expected = "<p>Normal text</p>"
        self.assertEqual(one_children, expected)

    def test_nested_parent_one_level_to_html(self):
        nested_parent = ParentNode(tag='b', children=[ParentNode(tag='p', children=[LeafNode("i", "italic text"), LeafNode(None, "Normal text")]),  ParentNode(tag='i', children=[LeafNode("b", "Bold text")])]).to_html()
        expected = "<b><p><i>italic text</i>Normal text</p><i><b>Bold text</b></i></b>"
        self.assertEqual(nested_parent, expected)

    def test_nested_parent_two_levels_to_html(self):
        nested_parent = ParentNode(tag='p', children=[ParentNode(tag='b', children=[ParentNode(tag='i', children=[LeafNode(None, "What a mess")])])]).to_html()
        expected = "<p><b><i>What a mess</i></b></p>"
        self.assertEqual(nested_parent, expected)

    def test_nested_none_children_to_html(self):
        nested_exception = ParentNode(tag='p', children=[ParentNode(tag='b', children=None)])
        with self.assertRaises(ValueError):
            nested_exception.to_html()

    def test_nested_empty_children_to_html(self):
        nested_exception = ParentNode(tag='b', children=[ParentNode(tag='p', children=[])])
        with self.assertRaises(ValueError):
            nested_exception.to_html()