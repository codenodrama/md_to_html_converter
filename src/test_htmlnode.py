import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_eq_first(self):
        node = HTMLNode("a", "This is a paragraph", ['img', 'link'], {"href": "https://www.google.com", "target": "_blank", })
        node2 = HTMLNode("a", "This is a paragraph", ['img', 'link'], {"href": "https://www.google.com", "target": "_blank", })
        self.assertEqual(node, node2)
    def test_str_first(self):
        node = HTMLNode("a", "This is a paragraph", ['img', 'link'], {"href": "https://www.google.com", "target": "_blank", })
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com" target="_blank"')
    def test_eq_second(self):
        node = HTMLNode("a", "This is a new paragraph", ['img', 'link'], {"href": "https://www.yandex.ru", "target": "_blank", })
        node2 = HTMLNode("a", "This is a new paragraph", ['img', 'link'], {"href": "https://www.yandex.ru", "target": "_blank", })
        self.assertEqual(node, node2)
    def test_str_second(self):
        node = HTMLNode("a", "This is a new paragraph", ['img', 'link'], {"href": "https://www.yandex.ru", "target": "_blank", })
        self.assertEqual(node.props_to_html(), ' href="https://www.yandex.ru" target="_blank"')

if __name__ == "__main__":
    unittest.main()
