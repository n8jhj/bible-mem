from bible_mem.const import BIBLE_TRANSLATIONS


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
        return f"{self.abbreviation} ({self.year_published})"

    def __repr__(self):
        return f"Translation<{self.readout}>"
