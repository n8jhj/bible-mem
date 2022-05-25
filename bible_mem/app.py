import blessed

from .db import reset_db
from .input import wait_for_editor_input, wait_for_key_enter
from .view import draw_add_verse_screen_1, draw_reset_db_screen, draw_splash_screen


term = blessed.Terminal()


def main_loop():
    draw_splash_screen(term)

    with term.hidden_cursor(), term.cbreak():
        ks = None
        while True:
            ks = term.inkey(timeout=3)
            if ks.code == term.KEY_ESCAPE:
                break
            elif ks == "0":
                reset_db()
                draw_reset_db_screen(term)
                wait_for_key_enter(term)
                draw_splash_screen(term)
            elif ks == "1":
                draw_add_verse_screen_1(term)
                input_ = wait_for_editor_input(term)
                draw_splash_screen(term)
                print(f"..> {input_}")
