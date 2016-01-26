import string

from .exception import InputError


class Notation(object):
    """
    Convert Algebraic chess notation into 0-indexed start
    stop coordinates
    http://en.wikipedia.org/wiki/Algebraic_chess_notation

    >>> Notation(width=8, height=8).parse_move("d2 d4")
    ((3, 1), (3, 3))
    """
    def __init__(self, width, height):
        self.column_letters = string.letters[:width].lower()
        self.row_digits = string.digits[1:height+1]

    def parse_move(self, move_string):
        try:
            from_, to = move_string.split()
        except ValueError:
            raise InputError(
                "Couldn't find two squares at {!r}"
                .format(move_string))

        return self.parse_square(from_), self.parse_square(to)

    def parse_square(self, coord_string):
        try:
            column_letter, row_number = coord_string.strip()
        except ValueError:
            raise InputError(
                "Couldn't find square {!r}"
                .format(coord_string))

        x = self.parse_column(column_letter)
        y = self.parse_row(row_number)
        return x, y

    def parse_column(self, column_letter):
        try:
            return self.column_letters.index(column_letter)
        except ValueError:
            raise InputError(
                "Couldn't find column {!r} in {!r}"
                .format(column_letter, self.column_letters))

    def parse_row(self, row_number):
        try:
            return self.row_digits.index(row_number)
        except ValueError:
            raise InputError(
                "Couldn't find row {!r} in {!r}"
                .format(row_number, self.row_digits))
