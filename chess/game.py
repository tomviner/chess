from .board import Board


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
        s = raw_input('Move: ')
        from_, to = s.strip().lower().split()
        def parse_move(coord_string):
            import string
            print coord_string
            column_letter, row_number = coord_string
            x = string.letters.index(column_letter)
            y = string.digits[1:].index(row_number)
            return x, y
        return parse_move(from_), parse_move(to)
