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
        for (x,y), initial in dic.iteritems():
            piece = Piece.from_initial(initial)
            self.board[y][x] = Square(x, y, piece)

    def __str__(self):
        ranks = [''.join(map(str, rank)) for rank in self.board]
        return '\n'.join(ranks)

    def __repr__(self):
        return '<Board with %d pieces>' %(len(self.pieces))

    @property
    def pieces(self):
        return [p for row in self.board for p in row if p!=EMPTY_SQUARE]


if __name__ == '__main__':
    b = Board(START)
    print b
