import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_props(self):
        node = HTMLNode(
            "p",
            "testing props to paragraph",
            None,
            {
                "href": "https://www.google.com",
                "target": "_blank",
            },
        )

        self.assertEqual(
            node.props_to_html(), ' href="https://www.google.com" target="_blank"'
        )

    def test_props_empty(self):
        node = HTMLNode("div", "content", None, None)
        self.assertEqual(node.props_to_html(), "")

    def test_props_single(self):
        node = HTMLNode("a", "link", None, {"href": "https://boot.dev"})
        self.assertEqual(node.props_to_html(), ' href="https://boot.dev"')

    def test_repr(self):
        node = HTMLNode("div", "content", None, None)
        self.assertEqual(
            node.__repr__(), f"HTMLNode({node.tag}, {node.value}, None, None)"
        )

    # def test_repr(self):
    #     node = TextNode("print me", TextType.PLAIN)
    #     self.assertEqual(
    #         node.__repr__(), f"TextNode({node.text}, {node.text_type.value}, None)"
    #     )


if __name__ == "__main__":
    unittest.main()
