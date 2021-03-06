from .exception import BadMove


class Board(object):
    """
    A board that can:
        place pieces
        display itself
        move pieces
    """
    empty_square_char = '.'

    def __init__(self, height, width):
        self.height = height
        self.width = width
        # self._board is a list of lists
        # starting with the bottom rank
        self._board = []
        for _ in xrange(height):
            row = [self.empty_square_char] * width
            self._board.append(row)

    @classmethod
    def from_string(cls, initial):
        rows = initial.splitlines()
        # initial starts from top of board, but our internal rep starts from
        # the lowest rank first
        rows.reverse()
        height = len(rows)
        width = len(rows[0])
        board = cls(height, width)
        for y, row in enumerate(rows):
            for x, square in enumerate(row):
                board._set(x, y, square)
        return board

    def _get(self, x, y):
        return self._board[y][x]

    def _set(self, x, y, piece):
        self._board[y][x] = piece

    def squares_used(self):
        return [
            (x, y)
            for y, rank in enumerate(self._board)
            for x, piece in enumerate(rank)
            if piece != self.empty_square_char
        ]

    def display(self):
        ranks = [''.join(rank) for rank in self._board]
        # as above, convert from internal rep (lowest rank first) to highest
        # rank shown at top of display
        return '\n'.join(reversed(ranks))
    __repr__ = display

    def place(self, x, y, piece):
        """
        Place a piece at:
            x - the column, starting from 0, LTR
            y - the rank, starting from 0, bottom up
        """
        self._set(x, y, piece)

    def look(self, x, y):
        """
        Get the piece (character) at:
            x - the column, starting from 0, LTR
            y - the rank, starting from 0, bottom up
        Returns None if empty
        """
        piece = self._get(x, y)
        if piece == self.empty_square_char:
            return None
        return piece

    def move(self, x1, y1, x2, y2):
        """
        Move the piece at x1, xy to x2, y2
        """
        piece = self.look(x1, y1)
        if piece is None:
            raise BadMove(
                "No piece at {}",
                (x1, y1)
            )
        self.place(x1, y1, self.empty_square_char)
        self.place(x2, y2, piece)
