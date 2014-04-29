from .board import Board
from .exception import InputError


class Game(object):
    """
    A game that can
        initialise a board
        take input from a player
    """
    def __init__(self, initial):
        self.board = Board.from_string(initial)

    def board_display(self):
        return self.board.display()
