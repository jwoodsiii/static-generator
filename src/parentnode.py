from htmlnode import HTMLNode


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, children=children, props=props)

    def to_html(self):
        if not self.tag:
            raise ValueError("no tag provided")
        elif self.children is None:
            raise ValueError("empty children list")
        else:
            out = f"<{self.tag}>"
            for c in self.children:
                out += c.to_html()
            return out + f"</{self.tag}>"
