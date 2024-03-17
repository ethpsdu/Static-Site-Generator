import unittest

from HTMLNode import HTMLNode
from HTMLNode import LeafNode
from HTMLNode import ParentNode


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("l", "bold", "lll", {"href": "https://www.google.com", "target": "_blank"})
        node2 = HTMLNode("b", "bold", "sample", {"href": "https://www.google.com", "target": "_blank"})
        node3 = LeafNode("p", "adsafaa")
        pr_node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )

        #node.to_html()

        print(HTMLNode.__repr__(node))
        print("efdsfdsf")
        print(HTMLNode.props_to_html(node2))

        node1 = LeafNode("p","ablrjpjmasmd",None, None)
        print("------")
        print(node1.to_html())
        print(pr_node.to_html())

if __name__ == "__main__":
    unittest.main()
