from enum import Enum

class Suits(Enum):
    #TODO: the values could be strings
    HEART = 1
    DIAMOND = 2
    CLUB = 3
    SPADE = 4

class Ranks(Enum):
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13
    ACE = 14 

class HandRanks(Enum):
    HIGH_CARD = 1
    PAIR = 2
    TWO_PAIR = 3
    TRIPS = 4
    STRAIGHT = 5
    FLUSH = 6
    FULL_HOUSE = 7
    QUADS = 8
    STRAIGHT_FLUSH = 9


class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def get_rank(self, val=True):
        if val:
            return self.rank.value
        return self.rank

    def get_suit(self, val=True):
        if val:
            return self.suit.value
        return self.suit
        
    def __repr__(self):
        rank = self.rank.value
        suit = self.suit
        suitstr = ""
        rankstr = ""
        if rank < 10:
            rankstr = str(rank)
        else:
            if rank == 10:
                rankstr = "T"
            elif rank == 11:
                rankstr = "J"
            elif rank == 12:
                rankstr = "Q"
            elif rank == 13:
                rankstr = "K"
            elif rank == 14:
                rankstr = "A"
        
        if suit == Suits.HEART:
            suitstr = "H"
        elif suit == Suits.DIAMOND:
            suitstr = "D"
        elif suit == Suits.CLUB:
            suitstr = "C"
        elif suit == Suits.SPADE:
            suitstr = "S"

        return rankstr+suitstr
    
