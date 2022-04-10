from bible_mem.constructs import Book, Reference, Translation, Verse


def test_verse():
    text = "Jesus Christ is the same yesterday and today and forever."
    verse = Verse(
        Reference(Book("Hebrews"), 13, 8),
        Translation("New International Version", 2011),
        text,
    )
    assert repr(verse) == "Verse<He. 13:8 (NIV; 2011)>"
    assert verse.text == text
