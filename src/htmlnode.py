class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, attributes=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.attributes = attributes

    def to_html(self):
        raise NotImplementedError

    def attributes_to_html(self):
        if not self.attributes:
            return ""
        props_list = []
        for key in self.attributes:
            props_list.append(f'{key}="{self.attributes[key]}"')

        return f' {" ".join(props_list)}'

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.attributes})"


class LeafNode(HTMLNode):
    def __init__(self, tag, value, attributes=None):
        if attributes is None:  
            attributes = {}
        super().__init__(tag, value, None, attributes)
        
    def to_html(self):
        # Ensure no children
        if self.value is None:
            raise ValueError("LeafNode must have a value")
        if not self.tag:
            return str(self.value)
        return f'<{self.tag}{self.attributes_to_html()}>{self.value}</{self.tag}>'
    
    def __repr__(self):
        if not self.tag:
            return f'LeafNode({self.value})'
        return f'LeafNode(<{self.tag}{self.attributes_to_html()}>{self.value}</{self.tag}>)'


class ParentNode(HTMLNode):
    def __init__(self, tag, children, attributes=None):
        super().__init__(tag, None, children, attributes)

    def to_html(self):
        if not self.tag:
            raise ValueError("ParentNode must have a tag")
        if not self.children:
            raise ValueError("ParentNode must have children")
        
        html = f'<{self.tag}'

        html += self.attributes_to_html() + ">"

        # LOOPY SHENANIGANS TO BUILD UP CHILDREN
        for child in self.children:
            html += child.to_html()

        html += f'</{self.tag}>'

        return html

    def __repr__(self):
        return f'ParentNode({self.tag}, {self.children}, {self.attributes})'    