from src.entities.Card import Card
from src.enums.CardSuit import CardSuit
from src.enums.CardValue import CardValue

from .CardSet import CardSet


class StandardDeck(CardSet):
    def __init__(self) -> None:
        super().__init__()
        super().add([Card(value.name, suite.name) for suite in CardSuit for value in CardValue])
