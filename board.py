from pieces import *
import notation

START = """\
RNBQKBNR
PPPPPPPP




pppppppp
rnbqkbnr\
"""
EMPTY_SQUARE = ' '

class Square(object):
    def __init__(self, x, y, piece=None):
        self.x = x
        self.y = y
        self.xy = (x, y)
        self.piece = piece

    def __unicode__(self):
        return unicode(self.piece)

    def __repr__(self):
        return unicode(self.piece)

    def get_moves(self):
        for move in self.piece.gen_moves(self.x, self.y):
            if move in ALL_SQUARES:
                yield move


class Board(object):
    def __init__(self, layout=None):
        self.board = [list([EMPTY_SQUARE]*8) for _ in range(8)]
        if isinstance(layout, basestring):
            self.place_from_string(layout)
        elif isinstance(layout, dict):
            self.place_from_dict(layout)

    def place_from_string(self, s):
        for y, rank in enumerate(s.splitlines()):
            for x, initial in enumerate(rank):
                if initial != EMPTY_SQUARE:
                    piece = Piece.from_initial(initial)
                    self.board[y][x] = Square(x, y, piece)

    def place_from_dict(self, dic):
        for (x,y), piece in dic.iteritems():
            if not isinstance(piece, Piece):
                piece = Piece.from_initial(piece)
            self.place((x, y), piece)

    def place(self, xy, piece):
        if xy in ALL_SQUARES:
            x, y = xy
            self.board[y][x] = Square(x, y, piece)

    def place_moves(self, piece, XY):
        d = dict([(xy, piece) for xy in piece.gen_moves(*XY)])
        self.place_from_dict(d)
        self.place(XY, '.')

    @property
    def pieces(self):
        return [p for row in self.board for p in row if p!=EMPTY_SQUARE]

    @staticmethod
    def random_square():
        return random.choice(ALL_SQUARES)

    def __unicode__(self):
        edge = ['|']
        end = [list('+--------+')]

        def wrap(i, rank, edge=edge):
            if i not in (0,9):
                rank = edge+rank+edge
            return rank

        ranks = [''.join(map(unicode, wrap(i, rank))) for i, rank in enumerate(end+self.board+end)]
        return '\n'.join(ranks)

    def __repr__(self):
        return '<Board with %d pieces>' %(len(self.pieces))


class TextBoard(object):
    def __init__(self, board=None, n=1):
        if board:
            self.rows = unicode(board).splitlines()
        self.n = n

    @classmethod
    def from_rows(cls, rows, n):
        tb = cls(n=n)
        tb.rows = rows
        return tb

    @classmethod
    def make_empty(cls, n):
        tb = cls()
        tb.rows = list([''])*n
        return tb

    def __add__(self, other):
        SEP = '   ' if self.rows[0] and other.rows[0] else ''
        return self.from_rows(
            [SEP.join(row_pair) for row_pair in zip(self.rows, other.rows)],
            self.n + other.n)

    @staticmethod
    def split_len(seq, length=104):
        return [seq[i:i+length] for i in range(0, len(seq), length)]

    def __str__(self):
        lines = zip(*map(self.split_len, self.rows))
        return self.colourise('\n'.join(row for line in lines for row in line))

    def colourise(self, s):
        cols = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']
        inits = 'RBNQKP.rbnqkp'
        for initial in inits:
            i = inits.index(initial.upper())
            col = cols[i]
            ground = 'fg'
            d = {ground: col}
            coloured_initial = colorize(initial, **d)
            s = s.replace(initial, coloured_initial)
        return s


    @classmethod
    def demo(cls, pieces):
        board_walk = cls.make_empty(10)
        for initial in pieces:
            p = Piece.from_initial(initial)
            b = Board()
            b.place_moves(p, Board.random_square())
            board_walk += cls(b)
        print board_walk


if __name__ == '__main__':
    b = Board(START)
    TextBoard.demo('KqRbNpP')
