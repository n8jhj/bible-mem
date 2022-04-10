from .reference import Reference


class Verse:
    def __init__(self, reference: Reference, text: str):
        self.reference = reference
        self.text = text

    def __repr__(self):
        return f"Verse<{self.reference.readout}>"
