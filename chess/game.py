import string

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
        width = self._board.width
        self.column_letters = string.letters[:width].lower()
        height = self._board.height
        self.row_digits = string.digits[1:height+1]

    def board_display(self):
        return self._board.display()

    def get_move(self):
        """
        Capture a move from the user,
        and return parsed to coords
        """
        s = raw_input('Move: ')
        cleaned_input = s.strip().lower()

        try:
            from_, to = cleaned_input.split()
        except ValueError:
            raise InputError

        return self.parse_square(from_), self.parse_square(to)

    def parse_square(self, coord_string):
        try:
            column_letter, row_number = coord_string.strip()
        except ValueError:
            raise InputError("Couldn't find a label from {!r}".format(coord_string))
        try:
            x = self.column_letters.index(column_letter)
        except ValueError:
            raise InputError("Couldn't find a column from {!r} in {!r}".format(column_letter, self.column_letters))
        try:
            y = self.row_digits.index(row_number)
        except ValueError:
            raise InputError("Couldn't find a row from {!r} in {!r}".format(row_number, self.row_digits))
        return x, y
