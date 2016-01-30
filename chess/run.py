from .game import Game

def main():
    game_runner = Game()
    game = game_runner.run()
    for msg in game:
        print msg
        print
