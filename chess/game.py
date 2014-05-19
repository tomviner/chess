from .board import Board
from .notation import Notation
from .exception import InputError


class Game(object):
    """
    A game that can
        initialise a board
        take input from a player
    """
    def __init__(self, initial):
        board = Board.from_string(initial)
        self.notation = Notation(board.width, board.height)
        self._board = board

    def display_board(self):
        return self._board.display()

    def get_move(self):
        """
        Capture a move from the user,
        and return parsed to coords:
        b2 e4 --> ((1, 1), (4, 3))
        """
        s = raw_input('Move: ')
        cleaned_input = s.strip().lower()

        return self.notation.parse_move(cleaned_input)

    def run(self):
        """
        Attempt to get valid moves, and apply them to the
        board. Keep asking upon invalid moves.
        """
        while True:
            try:
                (x1, y1), (x2, y2) = self.get_move()
            except InputError:
                continue
            self._board.move(x1, y1, x2, y2)
