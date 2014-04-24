from exception import BadMove


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
        self._board = []
        for y in xrange(height):
            row = [self.empty_square_char] * width
            self._board.append(row)

    @classmethod
    def from_string(cls, initial):
        rows = initial.splitlines()
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

    def display(self):
        ranks = [''.join(rank) for rank in self._board]
        return '\n'.join(ranks)
    __repr__ = display

    def place(self, x, y, piece):
        """
        Place a piece at:
            x - the column, starting from 0, LTR
            y - the rank, starting from 0, bottom up
        """
        self._set(x, self.height-y-1, piece)

    def look(self, x, y):
        """
        Get the piece (character) at:
            x - the column, starting from 0, LTR
            y - the rank, starting from 0, bottom up
        Returns None if empty
        """
        piece = self._get(x, self.height-y-1)
        if piece == self.empty_square_char:
            return None
        return piece

    def move(self, x1, y1, x2, y2):
        """
        Move the piece at x1, xy to x2, y2
        """
        piece = self.look(x1, y1)
        if piece is None:
            raise BadMove
        self.place(x1, y1, self.empty_square_char)
        self.place(x2, y2, piece)



