from .Card import Card

from src.exceptions.CardSetException import CardSetException

import random
from typing import List


class CardSet:
    def __init__(self) -> None:
        self.cards: List[Card] = []

    def showDeck(self) -> List[str]:
        return [str(card) for card in self.cards]

    def shuffle(self, seed: int | None = None) -> None:
        if seed is not None:
            random.seed(seed)
        random.shuffle(self.cards)

    def draw(self, amount: int = 1) -> List[Card]:
        if amount > len(self.cards):
            raise CardSetException(
                f"Not enough cards in the set to draw {amount} cards"
            )
        return [self.cards.pop() for _ in range(amount)]

    def play(self, cards: List[Card]) -> None:
        if len(cards) > len(self.cards):
            raise CardSetException(
                f"Not enough cards in the set to play {len(cards)} cards"
            )
        for card in cards:
            if card not in self.cards:
                raise CardSetException(
                    f"Could not play {str(card)}. This card does not belong in the set."
                )
            else:
                self.cards.remove(card)

    def add(self, cards: List[Card]) -> None:
        self.cards.extend(cards)

    def __len__(self) -> int:
        return len(self.cards)

    def __contains__(self, card: Card) -> bool:
        return card in self.cards
