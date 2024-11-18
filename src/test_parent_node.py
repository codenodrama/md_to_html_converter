import unittest

from htmlnode import *

class TestParentNode(unittest.TestCase):
    def test_eq_first(self):
        node = ParentNode(
            "p", 
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ], 
            )
        node_str = node.to_html()
        res_str = '<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>'
        self.assertEqual(node_str, res_str)

    def test_eq_second(self):
        node = ParentNode(
            "a", 
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ], 
            {"href":"https://www.google.com",}
            )
        node_str = node.to_html()
        res_str = '<a href="https://www.google.com"><b>Bold text</b>Normal text<i>italic text</i>Normal text</a>'
        self.assertEqual(node_str, res_str)

    def test_eq_third(self):
        node = ParentNode(
            "p", 
            [
                ParentNode(
                    "p2",
                    [
                    LeafNode("b2", "Bold text"),
                    LeafNode(None, "Normal text"),
                    LeafNode("i2", "italic text"),
                    LeafNode(None, "Normal text")
                    ] 
                    ),
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ], 
            )
        node_str = node.to_html()
        res_str = '<p><p2><b2>Bold text</b2>Normal text<i2>italic text</i2>Normal text</p2><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>'
        self.assertEqual(node_str, res_str)

if __name__ == "__main__":
    unittest.main()
