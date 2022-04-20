from bible_mem.constructs import Book, Reference


def test_reference():
    ref = Reference(Book("Micah"), 6, 8)
    assert repr(ref) == "<Reference(Mc. 6:8)>"

    # Test __eq__.
    assert ref == Reference(Book("Micah"), 6, 8)
    assert ref != Reference(Book("Genesis"), 6, 8)
