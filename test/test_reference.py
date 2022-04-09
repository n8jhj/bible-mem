from bible_mem.book import Book
from bible_mem.reference import Reference


def test_reference():
    ref = Reference(Book("Micah"), 6, 8)
    assert repr(ref) == "Reference<Mc. 6:8>"
