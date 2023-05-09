import difflib
import functools

import blessed


echo = functools.partial(print, end="", flush=True)
term = blessed.Terminal()


def difflib_try():
    # A: Truth
    seq_a = "For the Spirit God gave us does not make us timid, but gives us power, love and self-discipline."
    # B: Posit
    seq_b = "God gave us power, love, and self discipline."

    echo(term.red2 + seq_a + term.normal + "\n")
    echo(term.cyan2 + seq_b + term.normal + "\n")
    echo("\n")

    pieces_a, pieces_b = generate_diff_pairs(seq_a, seq_b)

    for flavor, text in pieces_a:
        if flavor == "right":
            echo(term.snow_on_green)
        elif flavor == "wrong":
            echo(term.snow_on_darkred)
        elif flavor == "equal":
            echo(term.snow_on_snow3)
        echo(text + term.normal)
    echo("\n")

    for flavor, text in pieces_b:
        if flavor == "right":
            echo(term.snow_on_green)
        elif flavor == "wrong":
            echo(term.snow_on_darkred)
        elif flavor == "equal":
            echo(term.snow_on_snow3)
        echo(text + term.normal)
    echo("\n")


def generate_diff_pairs(seq_a: str, seq_b: str):
    matcher = difflib.SequenceMatcher()
    matcher.set_seq1(seq_a)
    matcher.set_seq2(seq_b)
    opcodes = matcher.get_opcodes()

    pieces_a = []
    pieces_b = []
    for action, a0, a1, b0, b1 in opcodes:
        slice_a = seq_a[a0:a1]
        slice_b = seq_b[b0:b1]
        if action == "equal":
            pieces_a.append(("equal", slice_a))
            pieces_b.append(("equal", slice_b))
        if action == "replace":
            pieces_a.append(("right", slice_a))
            pieces_b.append(("wrong", slice_b))
            len_diff = len(slice_b) - len(slice_a)
            if len_diff > 0:
                pieces_a.append(("nada", " " * len_diff))
            else:
                pieces_b.append(("nada", " " * -len_diff))
        elif action == "delete":
            pass
    return pieces_a, pieces_b
