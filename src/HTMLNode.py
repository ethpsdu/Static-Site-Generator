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
# Parent of other Nodes, tree-like architecture
class ParentNode(HTMLNode):
    def __init__(self, tag ,children, props=None):
        super().__init__(tag,None, children, props)
        self.children = children
    # Recursive Function to read Tree of Nodes from Parentnode
    def to_html(self):
        
        if self.tag is None:
            raise ValueError("Tag not provided")
        if self.children is None:
            raise ValueError("Children not provided")
        else:
            tagged_text = ""
            parent_tag = self.tag
            def recursive_stuff(current_node):
                nonlocal tagged_text
                nonlocal parent_tag
                tagged_text += f"<{parent_tag}>"
                for node in current_node:
                    node_vals = node
                    if node.children is None:
                        tagged_text +=f"<{node.to_html()}"
                    else:
                        recursive_stuff(node_vals.children)
                tagged_text += f"</{parent_tag}>"
                return tagged_text
                return recursive_stuff
            return recursive_stuff(self.children)
