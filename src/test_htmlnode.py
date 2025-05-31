import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode(None, None, None, {"href":"https://www.boot.dev/", "target":"_blank"})
        html = node.props_to_html()
        expected = " href=\"https://www.boot.dev/\" target=\"_blank\""
        self.assertEqual(html, expected)

    def test_eq_tag(self):
        node1 = HTMLNode("p", "test", None, {"href":"https://www.boot.dev/", "target":"_blank"})
        node2 = HTMLNode("p", "test", None, {"href":"https://www.boot.dev/", "target":"_blank"})
        self.assertEqual(node1.tag, node2.tag)

    def test_eq_value(self):
        node1 = HTMLNode("p", "test", None, {"href":"https://www.boot.dev/", "target":"_blank"})
        node2 = HTMLNode("p", "test", None, {"href":"https://www.boot.dev/", "target":"_blank"})
        self.assertEqual(node1.value, node2.value)
    
    def test_repr(self):
        node = HTMLNode(None, None, None, None)
        expected = f"HTMLNode({node.tag}, {node.value}, {node.children}, {node.props})"
        self.assertEqual(str(node), expected)

if __name__ == "__main__":
    unittest.main()