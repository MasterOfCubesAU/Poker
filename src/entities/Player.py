from .CardSet import CardSet
import config


class Player:
    def __init__(self, name: str, hand: CardSet, balance: int) -> None:
        self.name = name
        self.hand = [].append(hand)
        self.bet = 0
        self.balance = balance

    def addbet(self, bet: int):
        if (self.bet + bet) < config.minbet:
            raise ValueError(f" Valule cannot be greater than {config.minbet}")
        if bet > self.balance:
            raise ValueError(" Valule cannot be less than the Player balance")
        else:
            self.bet += bet
            self.balance -= bet
