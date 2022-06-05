from __future__ import annotations
from pathlib import Path
import sqlite3
from typing import TYPE_CHECKING

import platformdirs

from bible_mem.__version__ import VERSION

if TYPE_CHECKING:
    from .input import Verse


APP_NAME = "bible_mem"
DB_NAME = "userdata.sqlite"
DB_PATH = Path(platformdirs.user_data_dir(APP_NAME, False, VERSION)) / DB_NAME


def reset_db():
    delete_db()
    create_db()


def delete_db():
    DB_PATH.unlink(missing_ok=True)


def create_db():
    # Forge directory path.
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    # Open database connection.
    con = sqlite3.connect(DB_PATH)
    # Connection context automatically calls con.commit() if nested code
    # executes successfully.
    with con:
        con.execute(
            """
            CREATE TABLE verses (
                id INTEGER PRIMARY KEY,
                book TEXT NOT NULL,
                chapter INTEGER,
                verse_num INTEGER NOT NULL,
                text TEXT NOT NULL
            )
            """
        )
    # Must close when finished.
    con.close()


def add_verse(verse: Verse):
    con = sqlite3.connect(DB_PATH)
    with con:
        con.execute(
            """
            INSERT INTO verses (book, chapter, verse_num, text)
            VALUES (?, ?, ?, ?)
            """,
            (verse.book, verse.chapter, verse.verse_num, verse.text),
        )
    con.close()
