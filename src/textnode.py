from enum import Enum
from htmlnode import LeafNode

class TextType(Enum):
    TEXT = 'text'
    BOLD = 'bold'
    ITALIC = 'italic'
    CODE = 'code'
    LINK = 'link'
    IMAGE = 'image'

class TextNode:
    def __init__(self, text, text_type, url=None, alt=None):
        self.text = text.strip()
        self.text_type = text_type.value
        self.url = url
        self.alt = alt
    def __eq__(self, text_node):
        return self.text == text_node.text and self.text_type == text_node.text_type and self.url == text_node.url and self.alt == text_node.alt
    def __repr__(self):
        return f'TextNode({self.text}, {self.text_type}, {self.url}, {self.alt})'

def text_node_to_html_node(text_node):
    match text_node.text_type:
        case 'text':
            return LeafNode(None, text_node.text)
        case 'bold':
            return LeafNode("b", text_node.text)
        case 'italic':
            return LeafNode("i", text_node.text)
        case 'code':
            return LeafNode("code", text_node.text)
        case 'link':
            return LeafNode("a", text_node.text, {"href":text_node.url,})
        case 'image':
            return LeafNode("img", "", {"href":text_node.url, "alt":text_node.alt})

