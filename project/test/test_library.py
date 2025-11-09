import pytest
from revision.book import Book
from revision.library import Library

@pytest.fixture
def sample_library():
    lib = Library("тестова бібліотека")
    book1 = Book("автор1", "книга1")
    book2 = Book("автор2", "книга2")
    book3 = Book("автор3", "книга3")
    lib.add_book(book1)
    lib.add_book(book2)
    lib.add_book(book3)
    return lib, [book1, book2, book3]

class TestLibrary:

    def test_add_book(self):
        lib = Library("бібліотека")
        book = Book("автор", "назва")
        lib.add_book(book)
        assert book in lib.books

    def test_remove_book_existing(self, sample_library):
        lib, books = sample_library
        book_to_remove = books[1]
        lib.remove_book(book_to_remove.id)
        assert book_to_remove not in lib.books

    def test_remove_book_nonexistent(self, sample_library):
        lib, _ = sample_library
        fake_id = "1234"
        lib.remove_book(fake_id)
        assert len(lib.books) == 3

@pytest.mark.parametrize(
    "author,title",
    [
        ("авторA", "книгаA"),
        ("авторB", "книгаB"),
        ("авторC", "книгаC"),
    ]
)
def test_book_str(author, title):
    book = Book(author, title)
    s = str(book)
    assert author in s
    assert title in s
    assert len(book.id) > 0
