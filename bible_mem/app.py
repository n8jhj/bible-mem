import difflib

import blessed

from .db import add_verse, reset_db, select_random_verse
from .input import parse_reference, wait_for_editor_input, wait_for_key_enter
from .view import (
    draw_add_verse_screen_1,
    draw_add_verse_screen_1_error,
    draw_add_verse_screen_2,
    draw_add_verse_screen_3,
    draw_quiz_verse_screen_1,
    draw_quiz_verse_screen_2,
    draw_reset_db_screen,
    draw_splash_screen,
)


term = blessed.Terminal()


def main_loop():
    with term.fullscreen(), term.hidden_cursor(), term.cbreak():
        draw_splash_screen(term)
        ks = None
        while True:
            ks = term.inkey(timeout=3)
            if ks.code == term.KEY_ESCAPE:
                break
            elif ks == "0":
                do_reset_db()
            elif ks == "1":
                do_add_verse()
            elif ks == "2":
                do_quiz_verse()


def do_reset_db():
    reset_db()
    draw_reset_db_screen(term)
    wait_for_key_enter(term)
    draw_splash_screen(term)


def do_add_verse():
    while True:
        draw_add_verse_screen_1(term)
        input_, escape = wait_for_editor_input(term)
        if escape:
            draw_splash_screen(term)
            return
        verse = None
        try:
            verse = parse_reference(input_)
        except ValueError:
            draw_add_verse_screen_1_error(term, input_)
            wait_for_key_enter(term)
            continue
        break
    draw_add_verse_screen_2(term)
    text, escape = wait_for_editor_input(term)
    if escape:
        draw_splash_screen(term)
        return
    verse.text = text
    add_verse(verse)
    draw_add_verse_screen_3(term, verse)
    wait_for_key_enter(term)
    draw_splash_screen(term)


def do_quiz_verse():
    verse = select_random_verse()
    draw_quiz_verse_screen_1(term, verse)
    if not verse:
        wait_for_key_enter(term)
        draw_splash_screen(term)
        return
    input_, escape = wait_for_editor_input(term)
    if escape:
        draw_splash_screen(term)
        return
    d = difflib.Differ()
    result = list(d.compare([verse.text + "\n"], [input_ + "\n"]))
    draw_quiz_verse_screen_2(term, result)
    wait_for_key_enter(term)
    draw_splash_screen(term)
