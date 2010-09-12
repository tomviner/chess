class Square(object):
    def __init__(self, x, y, piece, board):
        self.x = x
        self.y = y
        self.xy = x,y
        self.piece = piece
        self.board = board

    def __unicode__(self):
        return unicode(self.piece)

    def __repr__(self):
        return unicode(self.piece)

    def get_moves(self):
        for move in self.piece.general_moves(self.x, self.y):
            if move in ALL_SQUARES:
                yield Move(self.xy, move)

    def practical_moves(self, X, Y):
        for move in self.get_moves(X, Y):
            if move.path_clear(self.board):
                yield move
