from pieces import Piece

class Square(object):
    def __init__(self, x, y, piece, board):
        self.x = x
        self.y = y
        self.xy = x,y
        self.piece = piece
        self.board = board

    @property
    def occupied(self):
        return isinstance(self.piece, Piece)

    def __unicode__(self):
        return unicode(self.piece or ' ')

    def __str__(self):
        return unicode(self).encode('utf-8')

    def __repr__(self):
        return '<Square (%d,%d) %s %s>' %(self.x, self.y, self.piece.colour, self.piece.name)

    def __eq__(self, other):
        return unicode(self) == unicode(other)

    def get_moves(self):
        for move in self.piece.general_moves(self.x, self.y):
            if move in ALL_SQUARES:
                yield Move(self.xy, move)

    def practical_moves(self, X, Y):
        for move in self.get_moves(X, Y):
            if move.path_clear(self.board):
                yield move
