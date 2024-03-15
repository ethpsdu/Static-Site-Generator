import unittest

from HTMLNode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("This is a text node", "bold", None, {"href": "https://www.google.com", "target": "_blank"})
        node2 = HTMLNode("This is a text node", "bold", None, {"href": "https://www.google.com", "target": "_blank"})

        print(HTMLNode.__repr__(node))
        print("efdsfdsf")
        print(HTMLNode.props_to_html(node2))


if __name__ == "__main__":
    unittest.main()
