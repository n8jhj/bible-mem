from __future__ import annotations
from typing import TYPE_CHECKING, List, Optional

import blessed

from .__version__ import VERSION

if TYPE_CHECKING:
    from .input import Verse


def draw_text_screen(term: blessed.Terminal, content: List[str], status: str):
    # Check input.
    assert len(content) > 0, "There's no content"
    # Flush screen.
    print(term.clear + term.white_on_black + term.home)

    # Print status bar.
    with term.location(0, term.height - 2):
        print(
            term.snow_on_cyan
            + term.ljust(" " * 2 + status)
            + term.move_left(5)
            + term.normal
        )

    # Print content.
    line1_length = term.length(term.center(content[0]).rstrip())
    line1_start = line1_length - len(content[0])
    print(term.move_xy(0, term.height // 2 - 4) + term.normal + term.center(content[0]))
    for line in content[1:]:
        print(term.ljust(" " * line1_start + line))


def draw_splash_screen(term: blessed.Terminal):
    draw_text_screen(
        term,
        content=[
            "Welcome to Bible_mem!",
            f"     v {VERSION}",
            "",
            "  0: Reset database",
            "  1: Add verse",
            "  2: Quiz verses",
        ],
        status="ESCAPE to quit",
    )


def draw_reset_db_screen(term: blessed.Terminal):
    draw_text_screen(
        term,
        content=["Database reset"],
        status="ENTER to continue",
    )


def draw_add_verse_screen_1(term: blessed.Terminal):
    draw_text_screen(
        term,
        content=[
            "Type verse reference:",
            "  (E.g. 2 Timothy 1:7)",
        ],
        status="ENTER to submit" + " " * 8 + "ESCAPE to go back",
    )


def draw_add_verse_screen_1_error(term: blessed.Terminal, bad_ref: str):
    draw_text_screen(
        term,
        content=[f"Invalid reference: {bad_ref!r}"],
        status="ENTER to continue",
    )


def draw_add_verse_screen_2(term: blessed.Terminal):
    draw_text_screen(
        term,
        content=["Type verse text:"],
        status="ENTER to submit" + " " * 8 + "ESCAPE to go back",
    )


def draw_add_verse_screen_3(term: blessed.Terminal, verse: Verse):
    draw_text_screen(
        term,
        content=[f"{verse} added."],
        status="ENTER to continue",
    )


def draw_quiz_verse_screen_1(term: blessed.Terminal, verse: Optional[Verse]):
    if not verse:
        draw_text_screen(
            term,
            content=["There are no verses in the database."],
            status="Enter to continue",
        )
        return
    draw_text_screen(
        term,
        content=["Type verse text for:", f"  {verse}"],
        status="ENTER to submit" + " " * 8 + "ESCAPE to go back",
    )


def draw_quiz_verse_screen_2(term: blessed.Terminal, diff_lines: list[str]):
    draw_text_screen(
        term,
        content=diff_lines,
        status="Enter to continue",
    )
