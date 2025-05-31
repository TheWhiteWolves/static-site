import unittest

from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_repr(self):
        node = LeafNode(None, "test")
        expected = "LeafNode(None, test, None, None)"
        self.assertEqual(str(node), expected)
    
    def test_to_html(self):
        node = LeafNode("a", "Boot.dev", {"href":"https://www.boot.dev/"})
        expected = "<a href=\"https://www.boot.dev/\">Boot.dev</a>"
        self.assertEqual(node.to_html(), expected)

    def test_no_tag(self):
        node = LeafNode(None, "test")
        expected = "test"
        self.assertEqual(node.to_html(), expected)

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        expected = "<p>Hello, world!</p>"
        self.assertEqual(node.to_html(), expected)

    def test_no_value(self):
        node = LeafNode("p", None)
        self.assertRaises(ValueError)

if __name__ == "__main__":
    unittest.main()