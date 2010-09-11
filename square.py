class Square(object):
    def __init__(self, x, y, piece=None):
        self.x = x
        self.y = y
        self.piece = piece

    @property
    def xy(self):
        return (x, y)

    def __unicode__(self):
        return unicode(self.piece)

    def __repr__(self):
        return unicode(self.piece)

    def get_moves(self):
        for move in self.piece.general_moves(self.x, self.y):
            if move in ALL_SQUARES:
                yield move

    def practical_moves(self, X, Y, board):
        #if 
        for x, y in self.get_moves(X, Y):
            if board.path_blocked(self.xy, (X,Y)):
                pass
