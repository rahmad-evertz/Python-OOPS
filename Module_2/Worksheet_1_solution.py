#Problem 6
from enum import Enum

class suit(Enum):
    SPADES = 1
    HEARTS = 2
    DIAMONDS = 3
    CLUBS = 4

class PlayingCard:
    def __init__(self, rank = 0, suit = suit.SPADES):
        self.rank = rank
        self.suit = suit
        

#Problem 7
class Player:
    def __init__(self, name="Riyan", hand = []):
        self.name = name
        self.hand = hand
        

#Problem 8

class Deck:
    def __init__(self):
        self.cards = []
        for i in range(13):
            self.cards.append(PlayingCard(i+2, suit.SPADES))
            self.cards.append(PlayingCard(i+2, suit.DIAMONDS))
            self.cards.append(PlayingCard(i+2, suit.HEARTS))
            self.cards.append(PlayingCard(i+2, suit.CLUBS))
