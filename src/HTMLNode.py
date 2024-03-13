# Intermediate Between Markdown and HTML
class HTMLNode():
    def __init__(self, *tag, *value, *children, *props):
        
        if tag is None:
            tag = None
        self.tag = tag
        if value is None:
            value = None
        self.value = value
        if children is None:
            children = None
        self. children = children
        if props is None:
            props = None
        self.props = props
    
    def to_html(self):
        raise NotImplementedError("Not Implemented")
    def props_to_html(self):
            temp_prop = self.props
            
