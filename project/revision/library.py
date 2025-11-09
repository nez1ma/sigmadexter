from revision.book import Book

class Library:
    def __init__(self, name: str):
        self.name = name
        self.books = []

    def add_book(self, book: Book):
        self.books.append(book)
        print(f"Книга '{book.title}' додана до бібліотеки '{self.name}'.")

    def remove_book(self, book_id: str):
        for book in self.books:
            if book.id == book_id:
                self.books.remove(book)
                print(f"Книга '{book.title}' видалена з бібліотеки '{self.name}'.")
                return
        print(f"Книгу {book_id} не знайдено.")

    def show_books(self):
        if not self.books:
            print("У бібліотеці немає книг.")
        else:
            print(f"\nКниги в бібліотеці '{self.name}':")
            for book in self.books:
                print(f" - {book}")
