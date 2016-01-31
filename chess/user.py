from collections import deque
from random import choice

from .notation import Notation


class BaseUser(object):
    """
    """
    def set_board_data(self, width, height, board):
        self.width = width
        self.height = height
        self.board = board


class CmdLineUser(BaseUser):
    """
    """
    def get_move(self):
        s = raw_input('Move: ')
        return s

class RandomUser(BaseUser):
    """
    """
    def set_board_data(self, width, height, board):
        super(RandomUser, self).set_board_data(
            width, height, board)
        self.notation = Notation(width, height)

    def get_used_square(self):
        coords = choice(self.board.squares_used())
        return self.notation.compose_square(coords)

    def get_random_square(self):
        return '{}{}'.format(
            choice(self.notation.column_letters),
            choice(self.notation.row_digits),
        )

    def get_move(self):
        return '{} {}'.format(
            self.get_used_square(),
            self.get_random_square(),
        )

class FakeUser(BaseUser):
    """
    """
    # same object for all instances
    moves = deque([])

    def set_moves(self, moves):
        self.moves.extend(moves)

    def get_move(self):
        if self.moves:
            return self.moves.popleft()
        raise StopIteration
