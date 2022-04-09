from bible_mem import const


def test_books():
    # Tests that the JSON file is set up so there are no duplicate abbreviations.
    assert len(_set_of_book_abbreviations()) == const.BIBLE_BOOK_COUNT_TOTAL


def _set_of_book_abbreviations():
    abbreviations = set()
    for testament, books in const.BIBLE_BOOKS.items():
        for name, data in books.items():
            abbreviations.add(data["abbreviation"])
    return abbreviations
