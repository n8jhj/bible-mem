from bible_mem.view import splash_screen, term


if __name__ == "__main__":
    with term.fullscreen(), term.cbreak():
        splash_screen()
        term.inkey()
