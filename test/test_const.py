from bible_mem import const


def test_books():
    # The books JSON file should have no duplicate abbreviations.
    assert len(_set_of_book_abbreviations()) == const.BIBLE_BOOK_COUNT_TOTAL


def _set_of_book_abbreviations() -> set[str]:
    abbreviations = set()
    for testament, books in const.BIBLE_BOOKS.items():
        for name, data in books.items():
            abbreviations.add(data["abbreviation"])
    return abbreviations


def test_translations():
    # The translations JSON file should have no duplicate abbreviations.
    abbreviations = _list_of_configured_translation_abbreviations()
    assert len(abbreviations) == len(set(abbreviations))


def _list_of_configured_translation_abbreviations() -> list[str]:
    return list(const.BIBLE_TRANSLATION_ABBREVIATION_MAP.values())
