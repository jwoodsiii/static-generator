from htmlnode import HTMLNode


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag=tag, value=value, props=props)

    def to_html(self):
        # print("DEBUG leaf:", self.tag, self.value, self.props)
        if not self.value:
            raise ValueError
        elif not self.tag:
            return self.value
        else:
            if self.props:
                stitch = f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
                return stitch
            else:
                return f"<{self.tag}>{self.value}</{self.tag}>"
