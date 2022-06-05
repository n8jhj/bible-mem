from __future__ import annotations
import blessed
from typing import TYPE_CHECKING, List

from .__version__ import VERSION

if TYPE_CHECKING:
    from .input import Verse


def draw_text_screen(term: blessed.Terminal, content: List[str], status: str):
    # Check input.
    assert len(content) > 0, "There's no content"
    # Flush screen.
    print(term.clear + term.white_on_black + term.home)

    # Print content.
    line1_length = term.length(term.center(content[0]).rstrip())
    line1_start = line1_length - len(content[0])
    with term.location(0, term.height // 2 - 4):
        print(term.normal + term.center(content[0]))
        for line in content[1:]:
            print(term.ljust(" " * line1_start + line))

    # Print status bar.
    with term.location(0, term.height - 2):
        print(
            term.snow_on_cyan + term.ljust(" " * 2 + status) + term.cub(5) + term.normal
        )


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
        status="ENTER to submit        ESCAPE to go back",
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
        status="ENTER to submit        ESCAPE to go back",
    )


def draw_add_verse_screen_3(term: blessed.Terminal, verse: Verse):
    draw_text_screen(
        term,
        content=[f"{verse} added."],
        status="ENTER to continue",
    )
