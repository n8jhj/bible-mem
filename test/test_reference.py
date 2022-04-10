from bible_mem.constructs import Book, Reference


def test_reference():
    ref = Reference(Book("Micah"), 6, 8)
    assert repr(ref) == "Reference<Mc. 6:8>"
