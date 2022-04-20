import pytest

from bible_mem.constructs import Translation, parse_translation_string


def test_translation():
    # Invalid translation.
    with pytest.raises(ValueError):
        Translation("Not A Version", 2000)
    with pytest.raises(ValueError):
        Translation("English Standard Version", 1698)

    # Valid translation.
    translation = Translation("New International Version", 1984)
    assert repr(translation) == "<Translation(NIV 1984)>"


@pytest.mark.parametrize(
    "text, expected, expected_error",
    [
        ("King James Version (1611)", Translation("King James Version", 1611), None),
        ("ESV (2001)", Translation("English Standard Version", 2001), None),
        ("NKJV (2001)", None, ValueError),
        ("Valid Version Name (23)", None, ValueError),
    ],
)
def test_parse_translation_string(
    text: str, expected: Translation, expected_error: Exception
):
    if expected_error:
        with pytest.raises(expected_error):
            parse_translation_string(text)
        return
    assert _translations_equal(parse_translation_string(text), expected)


def _translations_equal(tx1: Translation, tx2: Translation) -> bool:
    return tx1.name == tx2.name and tx1.abbreviation == tx2.abbreviation
