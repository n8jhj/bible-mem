from .book import Book
from .reference import Reference
from .translation import Translation, parse_translation_string
from .verse import Verse


def make_verse(
    text: str, book: str, chapter: int, verse_number: int, translation: str
) -> Verse:
    """Factory function for making a Verse instance."""
    return Verse(
        Reference(Book(book), chapter, verse_number),
        parse_translation_string(translation),
        text,
    )
