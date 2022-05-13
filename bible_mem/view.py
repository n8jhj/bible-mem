import blessed

from .__version__ import VERSION


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
                reset_db_screen()
                draw_splash_screen()


def draw_splash_screen():
    welcome_text = "Welcome to Bible_mem!"
    version_text = f"v {VERSION}"
    options_text = [
        "0: Reset database",
        "1: Add verse",
        "2: Quiz verse",
    ]
    status_text = "Press ESCAPE to quit"

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
                term.ljust(" " * (line1_start + 2) + line)
            )

    # Print status bar.
    with term.location(0, term.height - 2):
        print(
            term.snow_on_cyan
            + term.ljust(f"  {status_text}")
            + term.cub(5)
            + term.normal
        )


def reset_db_screen():
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

    # Wait for input.
    ks = None
    while True:
        ks = term.inkey(timeout=3)
        if ks.code == term.KEY_ENTER:
            break
