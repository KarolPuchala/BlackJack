from game import WrongActionException, GameOverPlayerException, GameOverCroupierException, Game


game = Game()
game.start_game()
print('Game stared')

while True:
    game.show_hand()
    action = input(game._print_menu())
    try:
        game.player_action(action.lower())
    except WrongActionException as e:
        print(str(e))
        continue
    except (GameOverPlayerException, GameOverCroupierException) as e:
        print(str(e))
        break
    finally:
        print(game.player)
        print(game.croupier)
        print(len(game.game_deck))
print('Game over')
