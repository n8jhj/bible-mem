from bible_mem.book import Book
from bible_mem.reference import Reference
from bible_mem.verse import Verse


def test_verse():
    text = "Jesus Christ is the same yesterday and today and forever."
    verse = Verse(Reference(Book("Hebrews"), 13, 8), text)
    assert repr(verse) == "Verse<He. 13:8>"
    assert verse.text == text
