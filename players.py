from deck import Card


class Player:
    def __init__(self) -> None:
        self.card_value_counter = 0
        self.own_cards = []
    

    def draw_card(self, card:Card) -> None:
        self.own_cards.append(card)
        self.card_value_counter += card.value


    def __repr__(self) -> str:
        return f": {str(self.own_cards).strip('[]')}\nValue: {self.card_value_counter}"


class Human(Player):
    def __init__(self) -> None:
        super().__init__()


    def __repr__(self) -> str:
        return "Your hand " + super().__repr__()


class Croupier(Player):
    def __init__(self) -> None:
        super().__init__()


    def __repr__(self) -> str:
        return "Croupier hand " + super().__repr__()
