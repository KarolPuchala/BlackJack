
from random import shuffle
from itertools import product
from card import card_colour, card_figure, Card

class Deck:
    def __init__(self) -> None:
        full_cards_combination = list(product([item for item in card_colour],[item for item in card_figure]))
        self._cards = [Card(colour, figure) for colour, figure in full_cards_combination]
    
    def hit_card(self) -> Card:
        poped_card = self._cards.pop(0)
        return poped_card

    def shuffle_deck(self) -> None:
        shuffle(self._cards)

    def __len__(self) -> int:
        return len(self._cards)
