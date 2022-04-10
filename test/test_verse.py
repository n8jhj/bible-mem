from bible_mem.constructs import Book, Reference, Verse


def test_verse():
    text = "Jesus Christ is the same yesterday and today and forever."
    verse = Verse(Reference(Book("Hebrews"), 13, 8), text)
    assert repr(verse) == "Verse<He. 13:8>"
    assert verse.text == text
