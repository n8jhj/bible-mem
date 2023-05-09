import pytest

from bible_mem.difflib_try import generate_unify_pairs


@pytest.mark.parametrize(
    ["seq_a", "seq_b", "expected_pairs_a", "expected_pairs_b"],
    [
        (
            "yo",
            "Yo",
            [("wrong", "y"), ("equal", "o")],
            [("right", "Y"), ("equal", "o")],
        ),
        (
            "This be a sente!",
            "This is a sentence.",
            [
                ("equal", "This "),
                ("wrong", "be"),
                ("equal", " a sente"),
                ("wrong", "!"),
                ("none", "   "),
            ],
            [
                ("equal", "This "),
                ("right", "is"),
                ("equal", " a sente"),
                ("right", "nce."),
            ],
        ),
        (
            "The Spirit God gave us gives us power and self discipline.",
            "For the Spirit God gave us does not make us timid, but gives us power, love and self-discipline.",
            [
                ("wrong", "T"),
                ("equal", "he Spirit God gave us "),
            ],
            [
                ("right", "For t"),
                ("equal", "he Spirit God gave us "),
                (),
            ],
        ),
    ],
)
def test_generate_unify_pairs(seq_a, seq_b, expected_pairs_a, expected_pairs_b):
    pairs_a, pairs_b = generate_unify_pairs(seq_a, seq_b)
    assert pairs_a == expected_pairs_a
    assert pairs_b == expected_pairs_b
