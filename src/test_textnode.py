import unittest

from textnode import Textnode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = Textnode("This is a text node", "bold","12ewq.com")
        node2 = Textnode("This is a text node", "bold", "12ewq.com")
        self.assertEqual(node, node2)


if __name__ == "__main__":
    unittest.main()
