from bible_mem.const import BIBLE_BOOKS_FLAT


class Book:
    def __init__(self, name: str):
        if name not in BIBLE_BOOKS_FLAT:
            raise ValueError(f"Invalid book: {name!r}")
        self.name = name
        self.abbreviation = BIBLE_BOOKS_FLAT[name]["abbreviation"]

    def __repr__(self):
        return f"<Book({self.name})>"
