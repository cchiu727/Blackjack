"""This file contains the Card and Deck classes"""

from collections import namedtuple
from random import shuffle

"""Card object - namedtuple with attributes rank and suit"""
Card = namedtuple('Card', ['rank', 'suit'])

def _str_card(card):
    """Converts and returns a card as a formatted string"""
    return f'{card._rank} of {card._suit}'

# Assigns _str_card method as the __str__ method for Card
Card.__str__ = _str_card


class Deck:
    """Initializes a standard 52-card deck and contains methods for gameplay"""    

    # All possible ranks and suits. Assigns a value to each rank
    ranks = ['Ace'] + [str(x) for x in range(2, 11)] + 'Jack Queen King'.split()
    suits = '♣ ♦ ♥ ♠'.split()
    values = list(range(1, 11)) + [10, 10, 10]
    value_dict = dict(zip(ranks, values))

    def __init__(self):
        """Create standard 52-card deck of Cards"""
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        """Returns the number of cards in the deck"""
        return len(self._cards)

    def __str__(self):
        """Returns the deck as a formatting string"""
        return ", ".join(map(str, self._cards))

    def get_cards(self):
        """Returns the deck as a list"""
        return self._cards

    def shuffle(self, num=1):
        """Shuffles the deck n times (default 1 time)"""
        for _ in range(num):
            shuffle(self._cards)

    def deal(self, num=1):
        """Pops from deck and returns n cards (default 1 card)"""
        return [self._cards.pop() for _ in range(num)]

    def merge(self, deck):
        """Merge the current deck with a given deck"""
        self._cards = self._cards + deck._cards
