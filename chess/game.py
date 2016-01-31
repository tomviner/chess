import itertools

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
    default_user_class = CmdLineUser

    def __init__(
            self,
            initial=ASCII_START_BOARD,
            user1=None,
            user2=None,
            max_moves=None,
            ):
        board = Board.from_string(initial)
        self.notation = Notation(board.width, board.height)
        self._board = board
        self.users = itertools.cycle([
            self.get_user(user1),
            self.get_user(user2),
            # RandomUser(board.width, board.height),
            # RandomUser(board.width, board.height),
        ])
        self.user = next(self.users)
        self.num_moves = 0
        self.max_moves = max_moves

    def get_user(self, user):
        board_data = {
            'width': self._board.width,
            'height': self._board.height,
            'board': self._board,
        }
        if not user:
            user = self.default_user_class()
        user.set_board_data(**board_data)
        return user

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

    def do_turn(self):
        """
        """
        try:
            (x1, y1), (x2, y2) = self.get_move()
        except InputError as e:
            return False, e.message
        try:
            self._board.move(x1, y1, x2, y2)
        except BadMove as e:
            msg, coords = e.args
            move_square = self.notation.compose_square(coords)
            return False, msg.format(move_square)
        return True, None

    def run(self):
        """
        Attempt to get valid moves, and apply them to the
        board. Keep asking upon invalid moves.
        """
        while True:
            yield self.display_board()
            if self.max_moves and self.num_moves >= self.max_moves:
                raise StopIteration
            while True:
                valid, msg = self.do_turn()
                if valid:
                    self.user = next(self.users)
                    self.num_moves += 1
                    break
                else:
                    yield msg
