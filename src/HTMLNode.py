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