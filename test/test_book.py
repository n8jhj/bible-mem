import pytest

from bible_mem.constructs import Book


def test_book():
    # Should not be able to initialize an invalid book of the Bible.
    with pytest.raises(ValueError):
        Book("Joseph")

    # Initialize a valid book for the following tests.
    book = Book("Zephaniah")

    # Check __repr__.
    assert repr(book) == "Book<Zephaniah>"
    assert book.abbreviation == "Zp"
