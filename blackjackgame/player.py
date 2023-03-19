"""This file contains the Player class and Dealer subclass to represent a user or Dealer AI"""

from .cards import Deck


class Player:
    """Represents a user/player in the game"""

    def __init__(self, name, bankroll=10000):
        self._name = name
        self._bankroll = bankroll
        self.hand = []
        self.wager_amount = 0

    def __str__(self):
        """Returns player's info as a formatted string"""
        return f"""{self._name}
        ${self._bankroll}"""

    def add_money(self, amount):
        """Adds amount to player's bankroll"""
        self._bankroll += amount

    def sub_money(self, amount):
        """Deducts amount from player's bankroll"""
        self._bankroll -= amount

    def give_bank(self, amount, bank):
        """Gives money to the bank (Dealer)"""
        bank._bankroll += amount

    def set_wager(self, amount):
        """Assigns wager amount to player"""
        self.wager_amount = amount

    def print_hand(self):
        """Prints player hand"""
        for card in self.hand:
            print(card)

    def add_to_hand(self, card):
        """Adds card to hand"""
        self.hand.extend(card)

    def hand_value(self):
        """Returns total value of cards in hand"""
        total = 0
        for card in self.hand:
            if card.rank == "Ace" and total < 11:
                total += 11
            else:
                total += Deck.value_dict[card.rank]
        return total


class Dealer(Player):
    """Dealer subclass from Player"""
