from .CardSet import CardSet
from ..utils.ConfigHandler import ConfigHandler


class Player:
    def __init__(self, name: str, hand: CardSet, balance: int) -> None:
        ConfigHandler.load("config.yaml")
        self.name = name
        self.hand = CardSet()
        self.bet = 0
        self.balance = balance

    def addbet(self, bet: int):
        bigblind = ConfigHandler.get("bigblind")
        if (self.bet + bet) < bigblind:
            raise ValueError(f" Valule cannot be greater than {bigblind}")
        if bet > self.balance:
            raise ValueError(" Valule cannot be less than the Player balance")
        else:
            self.bet += bet
            self.balance -= bet
