from .board import Board
from .notation import Notation


class Game(object):
    """
    A game that can
        initialise a board
        take input from a player
    """
    def __init__(self, initial):
        self._board = Board.from_string(initial)
        width = self._board.width
        height = self._board.height
        self.notation = Notation(width, height)

    def display_board(self):
        return self._board.display()

    def get_move(self):
        """
        Capture a move from the user,
        and return parsed to coords:
        >>> Game().get_move('b2 e4')
        ((1, 1), (4, 3))
        """
        s = raw_input('Move: ')
        cleaned_input = s.strip().lower()

        return self.notation.parse_move(cleaned_input)
