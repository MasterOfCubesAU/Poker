from src.entities.Card import Card
from src.entities.CardSet import CardSet


def main():
    hand = CardSet()
    hand.add([Card("ACE", "SPADES")])
    print(Card("ACE", "SPADES") in hand)
    hand.draw()
    print(Card("ACE", "SPADES") in hand)


if __name__ == "__main__":
    main()
