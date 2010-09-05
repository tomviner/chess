
ALL_SQUARES = [(x, y) for x in range(1,9) for y in range(1,9)]

class Colour(object):
    def __init__(self, initial_or_is_black):
        if isinstance(initial_or_is_black, basestring):
            self.is_black = initial_or_is_black.isupper()
        else:
            assert isinstance(initial_or_is_black, bool), '%r' %initial_or_is_black
        self.is_black = bool(initial_or_is_black)

    def __nonzero__(self):
        return self.is_black

class Piece(object):
    def __init__(self, colour):
        self.colour = Colour(colour)
        self.initial = notation.initial_from_piece(self.__class__)

    @classmethod
    def from_initial(cls, initial):
        piece_class = notation.piece_from_initial(initial)
        piece = piece_class(initial)
        piece.initial = initial
        return piece


    def __str__(self):
        return self.initial

    def __repr__(self):
        return '<%s>' %self.__class__.__name__

    def gen_moves(self, X, Y):
        raise NotImplementedError

    def gen_special_moves(self, X, Y, has_moved):
        raise NotImplementedError



class King(Piece):
    def gen_moves(self, X, Y):
        a3by3 = [(x, y) for x in range(-1, 2) for y in range(-1, 2)]
        for x, y in a3by3:
            yield X+x, Y+y
    def gen_special_moves(self, X, Y, orig):
        if orig:
            # castle
            pass


class Queen(Piece):
    def gen_moves(self, X, Y):
        for move in Rook.gen_moves():
            yield move
        for move in Bishop.gen_moves():
            yield move

class Rook(Piece):
    def gen_moves(self, X, Y):
        for x, y in ALL_SQUARES:
            if X==x or Y==y:
                yield x, y

class Bishop(Piece):
    def gen_moves(self, X, Y):
        diff = X-Y
        for x, y in ALL_SQUARES:
            if y-x == diff:
                yield x, y


class Knight(Piece):
    def gen_moves(self, X, Y):
        for x, y in ALL_SQUARES:
            if set(map(abs, (X-x, Y-y))) == set([1, 2]):
                yield x, y


class Pawn(Piece):
    def gen_moves(self, X, Y):
        yield X, Y+1
        if Y==2:
            yield X, Y+2


import notation
