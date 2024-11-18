import unittest

from textnode import *
from text_handler import *
from htmlnode import LeafNode

class TestTextHandler(unittest.TestCase):
    def test_first(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        res_nodes = [
                        TextNode("This is text with a ", TextType.TEXT),
                        TextNode("code block", TextType.CODE),
                        TextNode(" word", TextType.TEXT),
                    ]
        i = 0
        for i in range(len(new_nodes)):
            self.assertEqual(new_nodes[i], res_nodes[i])

    def test_second(self):
        node = TextNode("**This** is text with a **code block** word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.CODE)
        res_nodes = [
                        TextNode("This", TextType.BOLD),
                        TextNode(" is text with a ", TextType.TEXT),
                        TextNode("code block", TextType.BOLD),
                        TextNode(" word", TextType.TEXT),
                    ]
        
        i = 0
        for i in range(len(new_nodes)):
            self.assertEqual(new_nodes[i], res_nodes[i])

    def test_third(self):
        node = TextNode("This is text with a code block *word*", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "*", TextType.CODE)
        res_nodes = [
                        TextNode("This is text with a code block ", TextType.TEXT),
                        TextNode("word", TextType.ITALIC),
                    ]
        i = 0
        for i in range(len(new_nodes)):
            self.assertEqual(new_nodes[i], res_nodes[i])

    def test_fourth(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        matches = extract_markdown_images(text)
        another_matches = [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]
        self.assertEqual(matches, another_matches)

    def test_fifth(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        matches = extract_markdown_links(text)
        another_matches = [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")]
        self.assertEqual(matches, another_matches)
    
    def test_sixth(self):
        text = "This is text with a link [](https://www.boot.dev) and [to youtube]()"
        matches = extract_markdown_links(text)
        another_matches = [("", "https://www.boot.dev"), ("to youtube", "")]
        self.assertEqual(matches, another_matches)

    def test_seventh(self):
        nodes = split_nodes_links([TextNode("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)", TextType.TEXT)])
        res_nodes = [
                        TextNode("This is text with a link ", TextType.TEXT),
                        TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
                        TextNode(" and ", TextType.TEXT),
                        TextNode(
                        "to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"
                        ),
                    ]
        i = 0
        for i in range(len(nodes)):
            self.assertEqual(nodes[i], res_nodes[i])

    def test_eightth(self):
        nodes = split_nodes_links([TextNode("[to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)", TextType.TEXT)])
        res_nodes = [
                        TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
                        TextNode(" and ", TextType.TEXT),
                        TextNode(
                        "to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"
                        ),
                    ]
        i = 0
        for i in range(len(nodes)):
            self.assertEqual(nodes[i], res_nodes[i])

    def test_nineth(self):
        nodes = split_nodes_links([TextNode("[to boot dev](https://www.boot.dev)[to youtube](https://www.youtube.com/@bootdotdev)", TextType.TEXT)])
        res_nodes = [
                        TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
                        TextNode(
                        "to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"
                        ),
                    ]
        i = 0
        for i in range(len(nodes)):
            self.assertEqual(nodes[i], res_nodes[i])

    def test_tenth(self):
        text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        nodes = text_to_textnodes(text)

        res_nodes = [
                        TextNode("This is ", TextType.TEXT),
                        TextNode("text", TextType.BOLD),
                        TextNode(" with an ", TextType.TEXT),
                        TextNode("italic", TextType.ITALIC),
                        TextNode(" word and a ", TextType.TEXT),
                        TextNode("code block", TextType.CODE),
                        TextNode(" and an ", TextType.TEXT),
                        TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
                        TextNode(" and a ", TextType.TEXT),
                        TextNode("link", TextType.LINK, "https://boot.dev"),
                    ]
        i = 0
        for i in range(len(nodes)):
            self.assertEqual(nodes[i], res_nodes[i])

    def test_eleventh(self):
        text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg)[link](https://boot.dev)"
        nodes = text_to_textnodes(text)

        res_nodes = [
                        TextNode("This is ", TextType.TEXT),
                        TextNode("text", TextType.BOLD),
                        TextNode(" with an ", TextType.TEXT),
                        TextNode("italic", TextType.ITALIC),
                        TextNode(" word and a ", TextType.TEXT),
                        TextNode("code block", TextType.CODE),
                        TextNode(" and an ", TextType.TEXT),
                        TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
                        TextNode(" and a ", TextType.TEXT),
                        TextNode("link", TextType.LINK, "https://boot.dev"),
                        TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
                        TextNode("link", TextType.LINK, "https://boot.dev"),
                    ]
        i = 0
        for i in range(len(nodes)):
            self.assertEqual(nodes[i], res_nodes[i])

    def test_eleventh(self):
        text = "This is **text** **another bold text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg)[link](https://boot.dev)"
        nodes = text_to_textnodes(text)

        res_nodes = [
                        TextNode("This is ", TextType.TEXT),
                        TextNode("text", TextType.BOLD),
                        TextNode("another bold text", TextType.BOLD),
                        TextNode(" with an ", TextType.TEXT),
                        TextNode("italic", TextType.ITALIC),
                        TextNode(" word and a ", TextType.TEXT),
                        TextNode("code block", TextType.CODE),
                        TextNode(" and an ", TextType.TEXT),
                        TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
                        TextNode(" and a ", TextType.TEXT),
                        TextNode("link", TextType.LINK, "https://boot.dev"),
                        TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
                        TextNode("link", TextType.LINK, "https://boot.dev"),
                    ]
        i = 0
        for i in range(len(nodes)):
            self.assertEqual(nodes[i], res_nodes[i])
    def test_12(self):
        text = """# This is a heading

                This is a paragraph of text. It has some **bold** and *italic* words inside of it.

                * This is the first list item in a list block
                * This is a list item
                * This is another list item"""
        nodes = markdown_to_blocks(text)

        res_nodes = [
                        "# This is a heading",
                        "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
                        """* This is the first list item in a list block\n* This is a list item\n* This is another list item""",
                    ]
        i = 0
        for i in range(len(nodes)):
            self.assertEqual(nodes[i], res_nodes[i])
    
    def test_13(self):
        text = """# This is a heading

                This is a paragraph of text. It has some **bold** and *italic* words inside of it.

                * This is the first list item in a list block
                * This is a list item
                * This is another list item
                
                * This is the first list item in a list block
                * This is a list item"""
        nodes = markdown_to_blocks(text)

        res_nodes = [
                        "# This is a heading",
                        "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
                        """* This is the first list item in a list block\n* This is a list item\n* This is another list item""",
                        """* This is the first list item in a list block\n* This is a list item""",
                    ]
        i = 0
        for i in range(len(nodes)):
            self.assertEqual(nodes[i], res_nodes[i])

    def test_14(self):
        text = """# This is a heading
                # This is a heading

                This is a paragraph of text. It has some **bold** and *italic* words inside of it.

                * This is the first list item in a list block
                * This is a list item
                * This is another list item
                
                * This is the first list item in a list block
                * This is a list item"""
        nodes = markdown_to_blocks(text)

        res_nodes = [
                        """# This is a heading\n# This is a heading""",
                        "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
                        """* This is the first list item in a list block\n* This is a list item\n* This is another list item""",
                        """* This is the first list item in a list block\n* This is a list item""",
                    ]
        i = 0
        for i in range(len(nodes)):
            self.assertEqual(nodes[i], res_nodes[i])

    def test_15(self):
        text = "# This is a heading"
        text_type = block_to_block_type(text)

        res_type = "heading"
        
        self.assertEqual(text_type, res_type)

    def test_16(self):
        text = "```print(text)```"
        text_type = block_to_block_type(text)

        res_type = "code"
        
        self.assertEqual(text_type, res_type)

    def test_17(self):
        text = ">some line\n>another line\n>and one more line"
        text_type = block_to_block_type(text)

        res_type = "quote"
        
        self.assertEqual(text_type, res_type)

    def test_18(self):
        text = "* first\n- second\n* third"
        text_type = block_to_block_type(text)

        res_type = "unordered_list"
        
        self.assertEqual(text_type, res_type)

    def test_19(self):
        text = "88. first\n89. second\n90. third"
        text_type = block_to_block_type(text)

        res_type = "ordered_list"
        
        self.assertEqual(text_type, res_type)
    def test_20(self):
        text = "59745kdnksjbk496ksfn****0000szkkjdsg657"
        text_type = block_to_block_type(text)

        res_type = "paragraph"
        
        self.assertEqual(text_type, res_type)
    def test_21(self):
        text = """# This is a heading

                This is a paragraph of text. It has some **bold** and *italic* words inside of it.

                * This is the first list item in a list block
                * This is a list item
                * This is another list item
                
                88. This is the first list item in a list block
                100. This is a list item
                
                >This is a quote"""

        nodes = markdown_to_html_node(text)

        res_nodes = HTMLNode("div", None, [
        HTMLNode("h1", "This is a heading", None, {}),
        HTMLNode("p", "This is a paragraph of text. It has some **bold** and *italic* words inside of it.", None, {}),
        HTMLNode("ul", None, [
            HTMLNode("li", "This is the first list item in a list block", None, {}),
            HTMLNode("li", "This is a list item", None, {}),
            HTMLNode("li", "This is another list item", None, {}),
        ], {}),
        HTMLNode("ol", None, [
            HTMLNode("li", "This is the first list item in a list block", None, {}),
            HTMLNode("li", "This is a list item", None, {}),
        ], {}),
        HTMLNode("blockquote", "This is a quote", None, {})
        ], {})

        self.assertEqual(nodes, res_nodes)

    def test_22(self):
        text = """##### This is a heading

                This is a paragraph of text. It has some **bold** and *italic* words inside of it.

                * This is the first list item in a list block
                * This is a list item
                * This is another list item
                
                * This is the first list item in a list block
                * This is a list item
                
                >This is a quote"""

        nodes = markdown_to_html_node(text)

        res_nodes = HTMLNode("div", None, [
        HTMLNode("h5", "This is a heading", None, {}),
        HTMLNode("p", "This is a paragraph of text. It has some **bold** and *italic* words inside of it.", None, {}),
        HTMLNode("ul", None, [
            HTMLNode("li", "This is the first list item in a list block", None, {}),
            HTMLNode("li", "This is a list item", None, {}),
            HTMLNode("li", "This is another list item", None, {}),
        ], {}),
        HTMLNode("ul", None, [
            HTMLNode("li", "This is the first list item in a list block", None, {}),
            HTMLNode("li", "This is a list item", None, {}),
        ], {}),
        HTMLNode("blockquote", "This is a quote", None, {})
        ], {})

        self.assertEqual(nodes, res_nodes)

    def test_23(self):
        text = """##### This is a heading

                This is a paragraph of text. It has some **bold** and *italic* words inside of it.

                * This is the first list item in a list block
                * This is a list item
                * This is another list item
                
                * This is the first list item in a list block
                * This is a list item
                
                >This is a quote
                
                ```This is a code block```"""

        nodes = markdown_to_html_node(text)

        res_nodes = HTMLNode("div", None, [
        HTMLNode("h5", "This is a heading", None, {}),
        HTMLNode("p", "This is a paragraph of text. It has some **bold** and *italic* words inside of it.", None, {}),
        HTMLNode("ul", None, [
            HTMLNode("li", "This is the first list item in a list block", None, {}),
            HTMLNode("li", "This is a list item", None, {}),
            HTMLNode("li", "This is another list item", None, {}),
        ], {}),
        HTMLNode("ul", None, [
            HTMLNode("li", "This is the first list item in a list block", None, {}),
            HTMLNode("li", "This is a list item", None, {}),
        ], {}),
        HTMLNode("blockquote", "This is a quote", None, {}),
        HTMLNode("pre", None, [
            HTMLNode("code", "This is a code block", None, {}),
        ], {}),
        ], {})
        
        self.assertEqual(nodes, res_nodes)

    def test_24(self):
        text = """# This is a heading

                This is a paragraph of text. It has some **bold** and *italic* words inside of it.

                * This is the first list item in a list block
                * This is a list item
                * This is another list item
                
                * This is the first list item in a list block
                * This is a list item
                
                >This is a quote
                
                ```This is a code block```"""

        header = extract_title(text)

        res_header = "This is a heading"
        
        self.assertEqual(header, res_header)

    def test_25(self):
        text = """# Hello, this is a heading

                This is a paragraph of text. It has some **bold** and *italic* words inside of it.

                """

        header = extract_title(text)

        res_header = "Hello, this is a heading"
        
        self.assertEqual(header, res_header)

    def test_26(self):
        text = """# Hi-hi-hi, this is a heading

                This is a paragraph of text. It has some **bold** and *italic* words inside of it.

                """

        header = extract_title(text)

        res_header = "Hi-hi-hi, this is a heading"
        
        self.assertEqual(header, res_header)
    
if __name__ == "__main__":
    unittest.main()