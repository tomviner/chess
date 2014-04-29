from .board import Board
from .exception import InputError


class Game(object):
    """
    A game that can
        initialise a board
        take input from a player
    """
    def __init__(self, initial):
        self._board = Board.from_string(initial)

    def board_display(self):
        return self._board.display()

    def get_move(self):
        """
        Capture a move from the user,
        and return parsed to coords
        """

    def parse_input(self):
        """
        Convert the input string to a pair of move strings
        >>> Game(' ').parse_input()
        """

    def parse_move(self):
        pass