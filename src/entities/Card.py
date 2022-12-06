from ..enums.CardSuit import CardSuit
from ..enums.CardValue import CardValue


class Card:
    def __init__(self, value: str, suit: str) -> None:
        if value not in [v.name for v in CardValue]:
            raise ValueError(f"Value must be one of {[v.name for v in CardValue]}")
        if suit not in [s.name for s in CardSuit]:
            raise ValueError(f"Suit must be one of {[s.name for s in CardSuit]}")
        self.value = getattr(CardValue, value)
        self.suite = getattr(CardSuit, suit)

    def __str__(self) -> str:
        return f"{self.value.name} {self.suite.name}"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Card):
            return NotImplemented
        return bool(self.value == other.value and self.suite == other.suite)
