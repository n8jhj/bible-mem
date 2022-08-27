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
    ],
)
def test_generate_unify_pairs(seq_a, seq_b, expected_pairs_a, expected_pairs_b):
    pairs_a, pairs_b = generate_unify_pairs(seq_a, seq_b)
    assert pairs_a == expected_pairs_a
    assert pairs_b == expected_pairs_b
