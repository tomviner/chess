from exception import BadMove


EMPTY_SQUARE = '.'

class Board(object):
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self._board = []
        for y in xrange(height):
            row = [EMPTY_SQUARE] * width
            self._board.append(row)

    def _get(self, x, y):
        return self._board[self.height-y-1][x]

    def _set(self, x, y, piece):
        self._board[self.height-y-1][x] = piece

    def display(self):
        ranks = [''.join(rank) for rank in self._board]
        return '\n'.join(ranks)

    def place(self, x, y, piece):
        """
        Place a piece at:
            x - the column, starting from 0, LTR
            y - the rank, starting from 0, bottom up
        """
        self._board[self.height-y-1][x] = piece

    def move(self, x1, y1, x2, y2):
        """
        Move the piece at x1, xy to x2, y2
        """
        piece = self._get(x1, y1)
        if piece == EMPTY_SQUARE:
            raise BadMove
        self._set(x1, y1, EMPTY_SQUARE)
        self._set(x2, y2, piece)
