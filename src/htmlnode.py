class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        return f'href="{self.props["href"]}" target="{self.props["target"]}"'

    def __eq__(self, other):
        if not isinstance(other, HTMLNode):
            return False
        return (
            self.tag == other.tag and
            self.value == other.value and
            self.children == other.children and
            self.props == other.props
        )

    def __repr__(self):
        return f'''
    HTMLNode:
    tag = {self.tag}
    value = {self.value}
    children = {self.children}
    props = {self.props}
'''
class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        super().__init__(tag=tag, value=value, children=None, props=props)

    def to_html(self):
        if self.value is None:
            raise ValueError("LeafNode must have a value")
        
        if self.tag is None:
            return self.value
        
        props_html = ""
        if self.props:
            props_html = " " + self.props_to_html()

        return f"<{self.tag}{props_html}>{self.value}</{self.tag}>"
        
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, value=None, children=children, props=props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("ParentNode must have a tag")
        
        if self.children is None:
            raise ValueError("ParentNode must have children")
        
        props_html = ""

        if self.props:
            props_html = " " + self.props_to_html()

        children_html = ""
        for child in self.children:
            children_html += child.to_html()
        
        return f"<{self.tag}{props_html}>{children_html}</{self.tag}>"