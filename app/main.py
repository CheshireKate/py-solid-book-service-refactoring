import json
import xml.etree.ElementTree as ET


class Book:
    def __init__(self, title: str, content: str):
        self.title = title
        self.content = content


    def display_console(self) -> None:
        print(self.content)

    def display_reverse(self) -> None:
        print(self.content[::-1])

    def print_book_console(self) -> None:
        print(f"Printing the book: {self.title}...")
        print(self.content)

    def print_book_reverse(self) -> None:
        print(f"Printing the book in reverse: {self.title}...")
        print(self.content[::-1])


    def serialize_json (self) -> str:
        return json.dumps({"title": self.title, "content": self.content})

    def serialize_xml (self) -> str:
        root = ET.Element("book")
        title = ET.SubElement(root, "title")
        title.text = self.title
        content = ET.SubElement(root, "content")
        content.text = self.content
        return ET.tostring(root, encoding="unicode")


def main(book: Book, commands: list[tuple[str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display console":
            book.display_console()
        elif cmd == "display reverse":
            book.display_reverse()
        elif cmd == "print book console":
            book.print_book_console()
        elif cmd == "print book reverse":
            book.print_book_reverse()
        elif cmd == "serialize json":
            return book.serialize_json()
        elif cmd == "serialize xml":
            return book.serialize_xml()


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display console",), ("serialize xml",)]))
