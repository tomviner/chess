from pieces import *
from text_board import *
from rules import *
from square import *
from move import *
import notation

EMPTY_SQUARE = ' '

class Board(object):
    def __init__(self, layout=None):
        self.board = [[Square(y, x, None, self) for y in range(8)] for x in range(8)]
        if isinstance(layout, basestring):
            self.place_from_string(layout)
        elif isinstance(layout, dict):
            self.place_from_dict(layout)

    def place_from_string(self, s):
        """see rules.START for example string"""
        for y, rank in enumerate(s.splitlines()):
            for x, initial in enumerate(rank):
                if initial != EMPTY_SQUARE:
                    piece = Piece.from_initial(initial)
                    # strings are numbered from the top
                    self.place((x, 7-y), piece)

    def place_from_dict(self, dic):
        """eg dic={(3,0):King, (4,0):'Q'}"""
        for (x,y), piece in dic.iteritems():
            if not isinstance(piece, Piece):
                piece = Piece.from_initial(piece)
            self.place((x, y), piece)

    def place(self, xy, piece):
        """put a piece on the board
        y is numbered from the bottom up 0 to 7"""
        if xy not in ALL_SQUARES:
            raise IllegalPositionError
        x, y = xy
        if isinstance(piece, Piece):
            piece = Square(x, y, piece, self)
        else:
            assert isinstance(piece, basestring), piece
        # board rows are numbered from the top
        self.board[7-y][x] = piece

    def look_in(self, xy):
        """returns Square objects
        xy is numbered from the bottom up 0 to 7"""
        x, y = xy
        # board rows are numbered from the top
        return self.board[7-y][x]

    @property
    def squares(self):
        return [s for row in self.board for s in row]

    @property
    def occupied_squares(self):
        return [s for row in self.board for s in row if getattr(s,'occupied',None)]

    @property
    def pieces(self):
        return [s.piece for s in self.squares if getattr(s,'occupied',None)]

    @property
    def occupied(self):
        return [s.xy for s in self.squares if getattr(s,'occupied',None)]

    #@property
    @staticmethod
    def random_xy():
        return random.choice(ALL_SQUARES)

    @property
    def random_occupied_square(self):
        return random.choice(self.occupied_squares)

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


    def place_moves_from_piece_at(self, piece, XY):
        d = dict((xy, piece) for xy in piece.general_moves(*XY))
        self.place_from_dict(d)
        self.place(XY, '.')


    def get_moves_from_square(self, square):
        if not square.piece:
            raise StopIteration
        piece_to_xys = list(square.piece.general_moves(*square.xy))
        piece_moves = [Move(square, to_xy, self) for to_xy in piece_to_xys]
        moves = piece_moves[:]
        piece_moves = []
        for move in moves:
            legal = move.is_legal
            if legal:
                piece_moves.append(move)
        #piece_moves = [move for move in piece_moves if move.is_legal]
        for m in piece_moves:
            yield m

    def place_all_moves(self):
        b = Board()
        move_sets = [list(self.get_moves_from_square(square)) for square in self.occupied_squares]
        for moves in move_sets:
            for move in moves:
                b.place(move.xy2, move.piece)
                b.place(move.xy1, '.')
        return b


if __name__ == '__main__':
    #b1 = Board(START)
    #b = b1.place_all_moves()
    #tb = TextBoard(b)
    #print unicode(tb)
    t = TextBoard.demo()
    t = TextBoard.demo2()

