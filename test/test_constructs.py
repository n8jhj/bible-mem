from bible_mem.constructs import Book, Reference, Translation, Verse, make_verse


def test_make_verse():
    text = '"Where, O death, is your victory? Where, O death, is your sting?"'
    verse = make_verse(text, "1 Corinthians", 15, 55, "NIV (2011)")
    assert _verses_equal(
        verse,
        Verse(
            Reference(Book("1 Corinthians"), 15, 55),
            Translation("New International Version", 2011),
            text,
        ),
    )


def _verses_equal(v1: Verse, v2: Verse) -> bool:
    return (
        v1.text == v2.text
        and v1.reference.book.name == v2.reference.book.name
        and v1.reference.chapter == v2.reference.chapter
        and v1.reference.vern == v2.reference.vern
        and v1.translation.name == v2.translation.name
        and v1.translation.year_published == v2.translation.year_published
    )
