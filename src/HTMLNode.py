# Intermediate Between Markdown and HTML
class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
         self.tag = tag
         self.value = value
         self.children = children
         self.props = props
    # Return String of object
    def __repr__(self):
        return f"Textnode({self.tag}, {self.value}, {self.children}, {self.props})"
    # Temporary, raises Error
    def to_html(self):
        raise NotImplementedError("Not Implemented")
    # return props in html format
    def props_to_html(self):
            return f"href={self.props["href"]} target={self.props["target"]}"

class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None,children=None, props=None):
        super().__init__(tag, value, None, props)
        
    def to_html(self):
        if self.value is None:
            raise ValueError("LeafNode has no Parameter Value")
        if self.tag is None:
            return self.value
        else:
            return f"<{self.tag}>{self.value}</{self.tag}>"
class ParentNode(HTMLNode):
    def __init__(self, tag ,children, props=None):
        super().__init__(tag,None, children, props)
        self.children = children
    def to_html(self):
        if self.tag is None:
            raise ValueError("Tag not provided")
        if self.children is None:
            raise ValueError("Children not provided")
        else:
            pass