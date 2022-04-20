import re

from bible_mem.const import BIBLE_TRANSLATION_ABBREVIATION_MAP, BIBLE_TRANSLATIONS


class Translation:
    def __init__(self, name: str, year_published: int):
        tx_data = BIBLE_TRANSLATIONS.get(name)
        if tx_data is None:
            raise ValueError(f"Unknown translation {name!r}")
        if year_published not in tx_data["publish-years"]:
            raise ValueError(f"Invalid publish year {year_published}")
        self.name = name
        self.abbreviation = tx_data["abbreviation"]
        self.year_published = year_published

    @property
    def readout(self):
        return f"{self.abbreviation} {self.year_published}"

    def __repr__(self):
        return f"<Translation({self.readout})>"


def parse_translation_string(text: str) -> Translation:
    """Parses a string representation of a Translation."""
    abbreviation_regex = re.compile(r"([A-Z]+) \(([0-9]{4})\)")
    fullname_or_abbreviation_regex = re.compile(r"([\w ]+) \(([0-9]{4})\)")
    # Since the second regex object will also match the abbreviation style,
    # run it after the first.
    match = abbreviation_regex.fullmatch(text)
    if match is None:
        match = fullname_or_abbreviation_regex.fullmatch(text)
        if match is None:
            raise ValueError(f"Translation parsing failed for: {text!r}")
        else:
            name = match.group(1)
            year = int(match.group(2))
    else:
        trans = match.group(1)
        year = int(match.group(2))
        name = BIBLE_TRANSLATION_ABBREVIATION_MAP[trans]
    return Translation(name, year)
