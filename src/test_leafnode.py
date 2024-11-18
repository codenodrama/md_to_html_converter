import unittest

from htmlnode import HTMLNode, LeafNode

class TestLeafNode(unittest.TestCase):
    def test_eq_first(self):
        node = LeafNode("p", "This is a paragraph of text.")
        node2 = LeafNode("p", "This is a paragraph of text.")
        self.assertEqual(node, node2)
    def test_str_first(self):
        node = LeafNode("p", "This is a paragraph of text.")
        node_str_first = node.to_html()
        node_str_second = "<p>This is a paragraph of text.</p>"
        self.assertEqual(node_str_first, node_str_second)
    def test_eq_second(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        node2 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node, node2)
    def test_str_second(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        node_str_first = node.to_html()
        node_str_second = '<a href="https://www.google.com">Click me!</a>'
        self.assertEqual(node_str_first, node_str_second)


if __name__ == "__main__":
    unittest.main()