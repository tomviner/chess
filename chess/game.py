from .board import Board
from .exception import BadMove, InputError
from .notation import Notation
from .rules import ASCII_START_BOARD
from .user import CmdLineUser


class Game(object):
    """
    A game that can
        initialise a board
        take input from a player
    """
    user_class = CmdLineUser

    def __init__(self, initial=ASCII_START_BOARD):
        board = Board.from_string(initial)
        self.notation = Notation(board.width, board.height)
        self._board = board
        self.user = self.user_class()

    def display_board(self):
        return self._board.display()

    def get_move(self):
        """
        Capture a move from the user,
        and return parsed to coords:
        b2 e4 --> ((1, 1), (4, 3))
        """
        cleaned_input = self.user.get_move().strip().lower()
        print cleaned_input
        return self.notation.parse_move(cleaned_input)

    def run(self):
        """
        Attempt to get valid moves, and apply them to the
        board. Keep asking upon invalid moves.
        """
        while True:
            yield self.display_board()
            try:
                (x1, y1), (x2, y2) = self.get_move()
            except InputError as e:
                yield e.message
                continue
            try:
                self._board.move(x1, y1, x2, y2)
            except BadMove as e:
                yield e.message
                continue
