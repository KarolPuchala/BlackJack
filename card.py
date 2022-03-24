from enum import Enum


class card_colour(Enum):
    Spade = '\u2660'
    Diamond = '\u2666'
    Club = '\u2663'
    Heart = '\u2665'


class card_figure(Enum):
    Two = '2', 2
    Three = '3', 3
    Four = '4', 4
    Five = '5', 5
    Six = '6', 6
    Seven = '7', 7
    Eight = '8', 8
    Nine = '9', 9
    Ten = '10', 10
    Jack = 'J', 10
    Queen = 'Q', 10
    King = 'K', 10
    Ace = 'A', 11


class Card:
    def __init__(self, colour:card_colour, figure:card_figure) -> None:
        self.color = colour.value
        self.figure = figure.value[0]
        self.value = figure.value[1] 

    def __repr__(self) -> str:
        return f"{self.color}{self.figure}"
        