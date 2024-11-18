import unittest

from textnode import *
from text_handler import *

class TestSplitLink(unittest.TestCase):
    def first_test(self):
        nodes = split_nodes_links(TextNode( "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)", TextType.TEXT))
        res_nodes = [
                        TextNode("This is text with a link ", TextType.TEXT),
                        TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
                        TextNode(" and ", TextType.TEXT),
                        TextNode(
                        "to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"
                        ),
                    ]
        print(len(res_nodes))
        i = 0
        for i in range(len(nodes)):
            self.assertEqual(nodes[i], res_nodes[i])

    def second_test(self):
        node = TextNode( "This is text with a link [to new boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)", TextType.TEXT)
        res_nodes = [
                        TextNode("This is text with a link ", TextType.TEXT),
                        TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
                        TextNode(" and ", TextType.TEXT),
                        TextNode(
                        "to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"
                        ),
                    ]
        i = 0
        for i in range(len(new_nodes)):
            self.assertEqual(new_nodes[i], res_nodes[i])


if __name__ == "__main__":
    unittest.main()