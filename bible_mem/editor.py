import functools

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


def wait_for_editor_input(term: blessed.Terminal):
    ks = None
    while True:
        echo(term.reverse(" ") + term.move_left(1))
        ks = term.inkey(timeout=3)
        if ks.code == term.KEY_ENTER:
            break
        elif ks.code == term.KEY_BACKSPACE:
            echo(term.move_left(1) + "  " + term.move_left(2))
        elif input_filter(ks):
            echo(ks)
