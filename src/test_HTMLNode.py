import unittest

from HTMLNode import HTMLNode
from HTMLNode import LeafNode


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("This is a text node", "bold", None, {"href": "https://www.google.com", "target": "_blank"})
        node2 = HTMLNode("This is a text node", "bold", None, {"href": "https://www.google.com", "target": "_blank"})

        print(HTMLNode.__repr__(node))
        print("efdsfdsf")
        print(HTMLNode.props_to_html(node2))

        node1 = LeafNode("p","ablrjpjmasmd",None, None)

        print(LeafNode.to_html(node1))

if __name__ == "__main__":
    unittest.main()
