from pieces import *

START = """\
RNBQKBNR
PPPPPPPP




pppppppp
rnbqkbnr\
"""

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
    def __init__(self):
        self.board = [list([' ']*8) for _ in range(8)]
        for y, rank in enumerate(START.splitlines()):
            for x, initial in enumerate(rank):
                if initial != ' ':
                    piece = Notation.piece_from_initial[initial.upper()](initial.isupper())
                    self.board[y][x] = Square(x, y, piece)

    def __str__(self):
        ranks = [''.join(map(str, rank)) for rank in self.board]
        return '\n'.join(ranks)

if __name__ == '__main__':
    b = Board()
    print b
