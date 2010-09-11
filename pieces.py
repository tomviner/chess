import random

from colour import Colour

ALL_SQUARES = [(x, y) for x in range(8) for y in range(8)]


class TakesAreMovesError(Exception):
    pass
class IllegalMoveError(Exception):
    pass

class Piece(object):
    can_jump = False
    def __init__(self, colour=Colour.WHITE, initial=None):
        self.colour = colour if isinstance(colour, Colour) else Colour(colour)
        self.initial = initial or notation.initial_from_piece(self.__class__, self.colour)
        self.col_pc = self.colour.initial + self.initial.upper()
        self.codepoint = getattr(notation.UNICODE_PIECE, self.col_pc)

    @property
    def as_char(self):
        return unichr(self.codepoint)

    @property
    def as_html(self):
        return '&%d;' %self.codepoint

    @staticmethod
    def from_initial(initial):
        piece_class = notation.piece_from_initial(initial)
        piece = piece_class(colour=Colour(initial), initial=initial)
        return piece

    def __unicode__(self):
        return self.as_char

    def __repr__(self):
        return '<%s %s>' %(self.__class__.__name__, self.colour)

    def is_possible_move(self, xy):
        return xy in ALL_SQUARES

    def general_moves(self, X, Y):
        for m in self.basic_moves(X, Y):
            assert isinstance(m, tuple), m
            assert len(m) == 2, m
            if self.is_possible_move(m):
                yield m

    def solely_capturing_moves(self, X, Y):
        """solely implemented by Pawn subclass
        all other pieces have take==move"""
        raise TakesAreMovesError
        
    def general_capturing_moves(self, X, Y):
        try:
            return self.solely_capturing_moves(self, X, Y)
        except TakesAreMovesError:
            return general_moves(self, X, Y)

    def basic_moves(self, X, Y):
        raise NotImplementedError

    def gen_special_moves(self, X, Y, has_moved):
        raise NotImplementedError



class King(Piece):
    def basic_moves(self, X, Y):
        a3by3 = [(x, y) for x in range(-1, 2) for y in range(-1, 2)]
        for x, y in a3by3:
            yield X+x, Y+y
    def gen_special_moves(self, X, Y, orig):
        if orig:
            # castle
            pass

class Queen(Piece):
    def basic_moves(self, X, Y):
        for move in Rook().basic_moves(X, Y):
            yield move
        for move in Bishop().basic_moves(X, Y):
            yield move

class Rook(Piece):
    def basic_moves(self, X, Y):
        for x, y in ALL_SQUARES:
            if X==x or Y==y:
                yield x, y

class Bishop(Piece):
    def basic_moves(self, X, Y):
        for x, y in ALL_SQUARES:
            if x-y == X-Y or x+y==X+Y:
                yield x, y


class Knight(Piece):
    can_jump = True
    def basic_moves(self, X, Y):
        for x, y in ALL_SQUARES:
            if set(map(abs, (X-x, Y-y))) == set([1, 2]):
                yield x, y


class Pawn(Piece):
    def __init__(self, *args, **kwargs):
        super(Pawn, self).__init__(*args, **kwargs)
        is_white = bool(self.colour.is_white)
        self.direction = 1 if is_white else -1
        self.pawn_start = 1 if is_white else 6

    def basic_moves(self, X, Y):
        if Y == self.pawn_start-self.direction:
            raise IllegalMoveError
        yield X, Y+self.direction
        if Y==self.pawn_start:
            yield X, Y+2*self.direction

    def solely_capturing_moves(self, X, Y):
        for dx in (1,-1):
            yield X+dx, Y+self.direction

#import here to avoid recursion
import notation
