from deck import Deck
from players import Human, Croupier


class WrongActionException(Exception):
    pass


class GameOverPlayerException(Exception):
    pass


class GameOverCroupierException(Exception):
    pass


class Game:
    def __init__(self) -> None:
        self.game_deck = Deck()
        self.player = Human()
        self.croupier = Croupier()


    @staticmethod
    def _print_menu() -> None:
        print('''Available action:
            1) hit
            2) pass 
                ''')


    def _player_drawing_card(self) -> None:
        self.player.draw_card(self.game_deck.hit_card())
        if self.player.card_value_counter > 21:
            raise GameOverPlayerException('You are over 21 points. Croupier win!')


    def _player_pass(self) -> None:
        while self.croupier.card_value_counter <= self.player.card_value_counter:
            self.croupier.draw_card(self.game_deck.hit_card())
            if self.croupier.card_value_counter > 21:
                raise GameOverCroupierException('Croupier are over 21 points. You win!')
        raise GameOverPlayerException(f'Croupier have {self.croupier.card_value_counter} points when you have {self.player.card_value_counter}. Croupier win!')


    def player_action(self, action:str) -> None:
        if action == 'hit':
            self._player_drawing_card()
        elif action == 'pass':
            self._player_pass()
        else:
            raise WrongActionException('Wrong action. Try again')


    def show_hand(self) -> str:
        return print(self.player)


    def black_jack(self) -> None:
        if self.player.card_value_counter == 22:
            raise GameOverCroupierException('Black Jack!!! You win!')


    def start_game(self) -> None:
        self.game_deck.shuffle_deck()
        self.player.draw_card(self.game_deck.hit_card())
        self.player.draw_card(self.game_deck.hit_card())
        self.croupier.draw_card(self.game_deck.hit_card())
        self.croupier.draw_card(self.game_deck.hit_card())
        self.black_jack()

        while True:
            self.show_hand()
            action = input(self._print_menu())
            try:
                self.player_action(action.lower())
            except WrongActionException as e:
                print(str(e))
                continue
            except (GameOverPlayerException, GameOverCroupierException) as e:
                print(self.player)
                print(self.croupier)
                print(str(e))
                break
