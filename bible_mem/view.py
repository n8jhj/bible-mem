import blessed

from .__version__ import VERSION


term = blessed.Terminal()


def splash_screen():
    print(
        term.move_y(term.height // 2)
        + term.center("Welcome to Bible_mem!")
        + term.center(f"v.{VERSION}").rstrip()
    )
