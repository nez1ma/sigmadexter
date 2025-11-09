from revision.book import Book
from revision.library import Library

def main():
    library = Library("бібліотека1")

    book1 = Book("автор1", "книга1")
    book2 = Book("автор2", "книга2")
    book3 = Book("автор3", "книга3")

    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)

    library.show_books()
    library.remove_book(book2.id)
    library.show_books()

if __name__ == "__main__":
    main()



