from src.entities.StandardDeck import StandardDeck
from src.entities.Card import Card
from src.enums.CardValue import CardValue
from src.enums.CardSuit import CardSuit

def test_valid():
    cardSet = StandardDeck()
    assert len(cardSet) == 52
    
    # Ensure set now is a full deck
    for suite_idx, suite in enumerate(CardSuit):
        for value_idx, value in enumerate(CardValue):
            actual_card = cardSet.cards[(suite_idx * len(CardValue)) + value_idx]
            expected_card = Card(value.name, suite.name)
            assert actual_card == expected_card