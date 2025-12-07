import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_repr(self):
        node = TextNode("print me", TextType.PLAIN)
        self.assertEqual(
            node.__repr__(), f"TextNode({node.text}, {node.text_type.value}, None)"
        )

    def test_types(self):
        node = TextNode("This is a text node", TextType.ITALIC)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_no_link(self):
        node = TextNode("We should have a link", TextType.LINK, None)
        node2 = TextNode("We should have a link", TextType.LINK, "https://dummyurl.com")
        self.assertNotEqual(node, node2)


if __name__ == "__main__":
    unittest.main()
