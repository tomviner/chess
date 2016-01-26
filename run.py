from chess.game import Game

if __name__ == '__main__':
    game_runner = Game()
    game = game_runner.run()
    for msg in game:
        print msg
        print
