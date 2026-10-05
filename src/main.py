from textnode import TextType, TextNode


def main() -> None:
    node = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    print(node)


main()