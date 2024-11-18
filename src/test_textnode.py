import unittest

from textnode import *
from htmlnode import LeafNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        leaf_node = text_node_to_html_node(node)
        checking_leaf_node = LeafNode("b", node.text)
        self.assertEqual(leaf_node, checking_leaf_node)
    def test_eq_second(self):
        node = TextNode("This is a text node", TextType.ITALIC)
        leaf_node = text_node_to_html_node(node)
        checking_leaf_node = LeafNode("i", node.text)
        self.assertEqual(leaf_node, checking_leaf_node)
    def test_eq_third(self):
        node = TextNode("", TextType.IMAGE, "https://developer.mozilla.org/en-US/docs/Web/HTML/Element", "Some img")
        leaf_node = text_node_to_html_node(node)
        checking_leaf_node = LeafNode("img", "", {"href":node.url, "alt":node.alt})
        self.assertEqual(leaf_node, checking_leaf_node)

if __name__ == "__main__":
    unittest.main()
