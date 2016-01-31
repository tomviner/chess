import time

from .game import Game
from .user import RandomUser


def cmdline_game():
    game_runner = Game()
    game = game_runner.run()
    for msg in game:
        print msg
        print

def random_game(max_moves=None, sleep=0.1):
    game_runner = Game(
        user1=RandomUser(),
        user2=RandomUser(),
        max_moves=max_moves,
    )
    game = game_runner.run()
    for msg in game:
        print msg
        print
        time.sleep(sleep)
