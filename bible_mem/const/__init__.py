import json
from pathlib import Path


BIBLE_BOOK_COUNT_OLD_TESTAMENT = 39
BIBLE_BOOK_COUNT_NEW_TESTAMENT = 27
BIBLE_BOOK_COUNT_TOTAL = 66

with open(Path(__file__).parent / "books.json", "r") as jf:
    BIBLE_BOOKS = json.load(jf)["BIBLE_BOOKS"]

BIBLE_BOOKS_FLAT = (
    BIBLE_BOOKS["OLD_TESTAMENT_BOOKS"] | BIBLE_BOOKS["NEW_TESTAMENT_BOOKS"]
)

with open(Path(__file__).parent / "translations.json", "r") as jf:
    BIBLE_TRANSLATIONS = json.load(jf)["BIBLE_TRANSLATIONS"]

BIBLE_TRANSLATION_ABBREVIATION_MAP = {}
for name, data in BIBLE_TRANSLATIONS.items():
    BIBLE_TRANSLATION_ABBREVIATION_MAP[data["abbreviation"]] = name
