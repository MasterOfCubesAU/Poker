from src.entities.Card import Card

import pytest


def test_invalid():
    with pytest.raises(ValueError):
        Card("A", "B")
        Card("ACE", "B")
        Card("A", "SPADES")


def test_valid():
    Card("ACE", "SPADES")
