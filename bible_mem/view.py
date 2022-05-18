import blessed

from .__version__ import VERSION
from .db import reset_db


term = blessed.Terminal()


def main_loop():
    draw_splash_screen()

    with term.cbreak():
        ks = None
        while True:
            ks = term.inkey(timeout=3)
            if ks.code == term.KEY_ESCAPE:
                break
            elif ks == "0":
                reset_db()
                draw_reset_db_screen()
                wait_for_key_enter()
                draw_splash_screen()
            elif ks == "1":
                draw_add_verse_screen_1()
                wait_for_input()
                draw_splash_screen()


def draw_splash_screen():
    welcome_text = "Welcome to Bible_mem!"
    version_text = f"v {VERSION}"
    options_text = [
        "  0: Reset database",
        "  1: Add verse",
        "  2: Quiz verses",
    ]
    status_text = "Press ESCAPE to quit"

    # Flush screen.
    print(term.clear + term.white_on_black + term.home)

    # Print content.
    line1_length = term.length(term.center(welcome_text).rstrip())
    line1_start = line1_length - len(welcome_text)
    line2_start = line1_length - len(version_text) - 2
    with term.location(0, term.height // 2 - 4):
        print(
            term.normal
            + term.center(welcome_text)
            + term.ljust(" " * line2_start + version_text)
            + term.ljust("")
        )
        for line in options_text:
            print(
                term.ljust(" " * line1_start + line)
            )

    # Print status bar.
    with term.location(0, term.height - 2):
        print(
            term.snow_on_cyan
            + term.ljust(f"  {status_text}")
            + term.cub(5)
            + term.normal
        )


def draw_reset_db_screen():
    info_text = "Database reset"
    status_text = "Press ENTER to continue"

    # Flush screen.
    print(term.clear + term.white_on_black + term.home)

    # Print content.
    with term.location(0, term.height // 2 - 4):
        print(
            term.normal
            + term.center(info_text)
        )

    # Print status bar.
    with term.location(0, term.height - 2):
        print(
            term.snow_on_cyan
            + term.ljust(f"  {status_text}")
            + term.cub(5)
            + term.normal
        )


def wait_for_key_enter():
    ks = None
    while True:
        ks = term.inkey(timeout=3)
        if ks.code == term.KEY_ENTER:
            break


def draw_add_verse_screen_1():
    info_text = [
        "Type verse reference:",
        "  (E.g. 2 Timothy 1:7)",
    ]
    info_text_margin = 12
    status_text = "Press ENTER to submit"
    status_text_margin = 2

    # Flush screen.
    print(term.clear + term.white_on_black + term.home)

    # Print content.
    with term.location(0, term.height // 2 - 4):
        term.normal
        for line in info_text:
            print(
                term.ljust(" " * info_text_margin + line)
            )
        print()

    # Print status bar.
    with term.location(0, term.height - 2):
        print(
            term.snow_on_cyan
            + term.ljust(" " * status_text_margin + f"{status_text}")
            + term.cub(5)
            + term.normal
        )


def wait_for_input():
    ks = None
    while True:
        ks = term.inkey(timeout=3)
        if ks.code == term.KEY_ENTER:
            break
        elif not ks.is_sequence:
            print(ks, end="", flush=True)
