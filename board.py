from pieces import *
from text_board import *
from square import *
from rules import *
import notation

EMPTY_SQUARE = ' '

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
                    self.place((x,7-y), Square(x, y, piece, self))

    def place_from_dict(self, dic):
        for (x,y), piece in dic.iteritems():
            if not isinstance(piece, Piece):
                piece = Piece.from_initial(piece)
            self.place((x, y), piece)

    def place(self, xy, piece):
        if xy in ALL_SQUARES:
            x, y = xy
            self.board[7-y][x] = Square(x, y, piece, self)

    def get_moves_from_square(self, square):
        piece_to_xys = square.piece.general_moves(*square.xy)
        piece_moves = [Move(self, piece, square.xy, to_xy) for to_xy in piece_to_xys]
        piece_moves = filter(lambda move:move.is_legal, piece_moves)
        for m in piece_moves:
            yield m

    def place_moves(self, piece, XY):
        d = dict((xy, piece) for xy in piece.general_moves(*XY))
        self.place_from_dict(d)
        self.place(XY, '.')

    def place_all_moves(self):
        for square in self.squares:
            if square == EMPTY_SQUARE:
                continue
            moves = self.get_moves_from_square(square)
            for move in moves:
                pass

    @property
    def squares(self):
        return [s for row in self.board for s in row]

    @property
    def pieces(self):
        return [s.piece for s in self.squares if s!=EMPTY_SQUARE]

    @property
    def occupied_positions(self):
        return [s.xy for s in self.squares if s!=EMPTY_SQUARE]

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



if __name__ == '__main__':
    b = Board(START)
    #b.
    tb = TextBoard(b)
    print unicode(tb)
    #t = TextBoard.demo('KqRbNpP')
