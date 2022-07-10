from dataclasses import dataclass
import functools
import re
from typing import Optional, Tuple

import blessed
from blessed.keyboard import Keystroke

# Create print function for user input.
echo = functools.partial(print, end="", flush=True)


def input_filter(keystroke: Keystroke):
    if not keystroke:
        # Empty.
        return False
    if keystroke.is_sequence:
        # Namely, deny multi-byte sequences (such as '\x1b[A').
        return False
    if ord(keystroke) < ord(" "):
        # ...or control characters (such as ^L).
        return False
    return True


def wait_for_key_enter(term: blessed.Terminal):
    ks = None
    while True:
        ks = term.inkey(timeout=3)
        if ks.code == term.KEY_ENTER:
            break


def wait_for_editor_input(term: blessed.Terminal) -> Tuple[str, bool]:
    padding = 4  # spaces
    print(term.move_down(1) + term.move_right(padding), end="")
    text = ""
    line = 0
    escape = False
    ks = None
    while True:
        echo(term.reverse(" ") + term.move_left(1))
        ks = term.inkey(timeout=3)
        if ks.code == term.KEY_ENTER:
            break
        elif ks.code == term.KEY_ESCAPE:
            escape = True
            break
        elif ks.code == term.KEY_BACKSPACE:
            if not text:
                continue
            text = text[:-1]
            echo(term.move_left(1) + " " * 2 + term.move_left(2))
            with term.location(0, 2):
                print(
                    " " * 2
                    + " " * 9
                    + term.move_left(9)
                    + f"{len(text)} / {term.width - 2 * padding}"
                )
                print(" " * 2 + str(term.width))
            if (div := len(text) // (term.width - 2 * padding)) < line:
                line = div
                with term.location(0, 4):
                    print(term.snow_on_red + " " * 2 + "BWD" + term.normal)
                echo(term.move_up(1) + term.move_x(term.width - padding - 1))
        elif input_filter(ks):
            text += ks
            echo(len(text) % 10)
            with term.location(0, 2):
                print(
                    " " * 2
                    + " " * 9
                    + term.move_left(9)
                    + f"{len(text)} / {term.width - 2 * padding}"
                )
                print(" " * 2 + str(term.width))
            if (div := len(text) // (term.width - 2 * padding)) > line:
                line = div
                with term.location(0, 4):
                    print(term.snow_on_green + " " * 2 + "FWD" + term.normal)
                echo(term.move_down(1) + term.move_x(padding))
    return text, escape


@dataclass
class Verse:
    book: str
    chapter: Optional[int]
    verse_num: int
    text: str

    def __repr__(self):
        return f"{self.book} {self.chapter}:{self.verse_num}"


def parse_reference(ref: str) -> Verse:
    expr = re.compile(r"([0-9])? *([\w ]+) +([0-9]+):?([0-9]+)")
    match = expr.fullmatch(ref)
    if not match:
        raise ValueError(f"Invalid reference: {ref!r}")
    book_num, book_name, chapter, verse_num = match.groups()
    book = f"{book_num} {book_name}" if book_num else book_name
    return Verse(book, chapter, verse_num, "")
