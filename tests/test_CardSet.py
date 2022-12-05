from src.entities.StandardDeck import StandardDeck
from src.entities.CardSet import CardSet
from src.entities.Card import Card


from src.exceptions.CardSetException import CardSetException

import pytest

def test_add():
    # Empty set
    cardSet = CardSet()
    assert len(cardSet) == 0
    
    # Populated set
    cards_to_add = [Card("THREE", "HEARTS"), Card("TWO", "SPADES"), Card("THREE", "HEARTS")]
    cardSet.add(cards_to_add)
    assert len(cardSet) == 3
    assert cardSet.cards[0] == Card("THREE", "HEARTS")
    assert cardSet.cards[1] == Card("TWO", "SPADES")
    assert cardSet.cards[2] ==  Card("THREE", "HEARTS")

def test_shuffle():
    cardSet = StandardDeck()
    cardSet.shuffle(1)

    assert cardSet.cards[0] == Card("JACK", "DIAMONDS")
    assert cardSet.cards[1] == Card("TEN", "CLUBS")
    assert cardSet.cards[2] == Card("QUEEN", "HEARTS")

def test_draw_valid():
    cardSet = StandardDeck()

    assert cardSet.draw(3) == [Card("KING", "DIAMONDS"), Card("QUEEN", "DIAMONDS"), Card("JACK", "DIAMONDS")]
    assert cardSet.draw() == [Card("TEN", "DIAMONDS")]
    assert len(cardSet) == 48

def test_draw_invalid():
    cardSet = StandardDeck()

    assert len(cardSet.draw(51)) == 51
    with pytest.raises(CardSetException):
        cardSet.draw(2)

def test_play_valid():
    cardSet = StandardDeck()
    cardSet.draw(50)
    
    cards_to_play = [Card("ACE", "CLUBS"), Card("TWO", "CLUBS")]
    cardSet.play(cards_to_play)

    assert len(cardSet) == 0

def test_play_invalid():
    cardSet = StandardDeck()   
    cardSet.play([Card("QUEEN", "DIAMONDS")])

    assert len(cardSet) == 51
    with pytest.raises(CardSetException):
        cardSet.play([Card("QUEEN", "DIAMONDS")])
        cardSet.play(StandardDeck())
