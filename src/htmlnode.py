class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    def to_html(self):
        if self.tag == None:
            raise ValueError("Object doesn't have a tag.")
        attr_to_html = '' if self.props == None else ' ' + ' '.join(map(lambda kv: ''.join(f'{kv[0]}="{(kv[1])}"'), self.props.items()))
        res_str = f'<{self.tag}{attr_to_html}>'
        if self.value:
            res_str += self.value
        if self.children:
            for child in self.children:
                res_str += child.to_html()
        res_str += f'</{self.tag}>'
        return res_str
    def props_to_html(self):
        return ' ' + ' '.join(map(lambda kv: ''.join(f'{kv[0]}="{(kv[1])}"'), self.props.items()))
    def __eq__(self, html_node):
        return self.tag == html_node.tag and self.value == html_node.value and self.children == html_node.children and self.props == html_node.props
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"

class LeafNode(HTMLNode):
    def __init__(self, tag, value, attributes=None):
        super().__init__(tag, value)
        self.children = None
        self.attributes = attributes
    def to_html(self):
        if(self.value == None):
            raise ValueError('All leaf nodes must have a value.')
        if(self.tag == None):
            return self.value
        attr_to_html = '' if self.attributes == None else ' ' + ' '.join(map(lambda kv: ''.join(f'{kv[0]}="{(kv[1])}"'), self.attributes.items()))
        return f'<{self.tag}{attr_to_html}>' + self.value + f'</{self.tag}>'

class ParentNode(HTMLNode):
    def __init__(self, tag, children, attributes=None):
        super().__init__(tag)
        self.children = children
        self.attributes = attributes
        self.value = None
    def to_html(self):
        if self.tag == None:
            raise ValueError("Object doesn't have a tag.")
        if not self.children:
            raise ValueError("Object doesn't have children")
        attr_to_html = '' if self.attributes == None else ' ' + ' '.join(map(lambda kv: ''.join(f'{kv[0]}="{(kv[1])}"'), self.attributes.items()))
        res_str = f'<{self.tag}{attr_to_html}>'
        for child in self.children:
            res_str += child.to_html()
        res_str += f'</{self.tag}>'
        return res_str