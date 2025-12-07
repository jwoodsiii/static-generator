from textnode import TextNode, TextType


def main():
    tmp = TextNode("Here is an anchor text", TextType.LINK, "https://www.boot.dev")
    print(tmp)


if __name__ == "__main__":
    main()
