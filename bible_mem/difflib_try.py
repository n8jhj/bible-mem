import difflib
import functools

import blessed


echo = functools.partial(print, end="", flush=True)
term = blessed.Terminal()


def difflib_try():
    # B: Truth
    seq_b = "For the Spirit God gave us does not make us timid, but gives us power, love and self-discipline."
    # A: Posit
    seq_a = "The Spirit God gave us gives us power and self discipline."
    # seq_a = "God gave us power, love, and self discipline."

    echo(term.red2 + seq_b + term.normal + "\n")
    echo(term.cyan2 + seq_a + term.normal + "\n")
    echo("\n")

    pieces_a, pieces_b = generate_unify_pairs(seq_a, seq_b)

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


def generate_unify_pairs(seq_a: str, seq_b: str):
    """Generates pairs of actions to be taken to unify sequence differences.

    Args:
        seq_a: Sequence to be changed.
        seq_b: Sequence to remain the same.
    """
    matcher = difflib.SequenceMatcher()
    matcher.set_seqs(seq_a, seq_b)
    opcodes = matcher.get_opcodes()

    pieces_a = []
    pieces_b = []
    for action, a0, a1, b0, b1 in opcodes:
        slice_a = seq_a[a0:a1]
        slice_b = seq_b[b0:b1]
        if action == "equal":
            pieces_a.append(("equal", slice_a))
            pieces_b.append(("equal", slice_b))
        elif action == "replace":
            pieces_a.append(("wrong", slice_a))
            pieces_b.append(("right", slice_b))
            sa_len = len(slice_a)
            sb_len = len(slice_b)
            if sb_len > sa_len:
                pieces_a.append(("none", " " * (sb_len - sa_len)))
            elif sb_len != sa_len:
                pieces_b.append(("none", " " * (sa_len - sb_len)))
        elif action == "delete":
            pass
    return pieces_a, pieces_b
