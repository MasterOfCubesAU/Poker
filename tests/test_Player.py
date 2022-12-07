from src.entities.Player import Player
from src.entities.CardSet import CardSet
from src.entities.Card import Card
import pytest


def test_bet():
    cardSet = CardSet()

    cards_to_add = [Card("THREE", "HEARTS"), Card("TWO", "SPADES"), Card("THREE", "HEARTS")]
    cardSet.add(cards_to_add)
    user = Player("Player0", cardSet, 50)

    assert user.bet == 0
    assert user.balance == 50

    user.addbet(12)

    assert user.bet == 12
    assert user.balance == 38

    cards_to_add = [Card("THREE", "HEARTS"), Card("TWO", "SPADES"), Card("THREE", "HEARTS")]
    cardSet.add(cards_to_add)
    user = Player("Player0", cardSet, 50)

    with pytest.raises(ValueError):
        user.addbet(3)

    with pytest.raises(ValueError):
        user.addbet(55)
