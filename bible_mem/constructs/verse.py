from .reference import Reference
from .translation import Translation


class Verse:
    def __init__(self, reference: Reference, translation: Translation, text: str):
        self.reference = reference
        self.translation = translation
        self.text = text

    def __repr__(self):
        return (
            f"Verse<"
            f"{self.reference.readout} "
            f"({self.translation.abbreviation}; {self.translation.year_published})"
            f">"
        )
