from .book import Book


class Reference:
    def __init__(self, book: Book, chapter: int, vern: int):
        self.book = book
        self.chapter = chapter
        self.vern = vern

    @property
    def readout(self):
        return f"{self.book.abbreviation}. {self.chapter}:{self.vern}"

    def __repr__(self):
        return f"<Reference({self.readout})>"
