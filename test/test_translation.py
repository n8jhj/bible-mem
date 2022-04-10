import pytest

from bible_mem.constructs import Translation


def test_translation():
    # Invalid translation.
    with pytest.raises(ValueError):
        Translation("Not A Version", 2000)
    with pytest.raises(ValueError):
        Translation("English Standard Version", 1698)

    # Valid translation.
    translation = Translation("New International Version", 1984)
    assert repr(translation) == "Translation<NIV (1984)>"
