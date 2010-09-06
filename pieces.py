import string
import random

from django.utils.termcolors import colorize

ALL_SQUARES = [(x, y) for x in range(8) for y in range(8)]

class Colour(object):
    WHITE, BLACK = range(2)
    def __init__(self, initial_or_is_black):
        is_black = initial_or_is_black
        if isinstance(initial_or_is_black, basestring):
            is_black = initial_or_is_black.isupper()
        else:
            assert isinstance(initial_or_is_black, (bool, int)), '%r' %initial_or_is_black
            assert initial_or_is_black in (0, 1), '%r' %initial_or_is_black
        self.is_black = bool(is_black)

    def __nonzero__(self):
        return self.is_black

    def __unicode__(self):
        return 'BLACK' if self else 'WHITE'

    def do_case(self, s):
        return (string.upper if self else string.lower)(s)

class Piece(object):
    def __init__(self, colour=Colour.WHITE):
        self.colour = Colour(colour)
        self.initial = notation.initial_from_piece(self.__class__, self.colour)

    @staticmethod
    def from_initial(initial):
        piece_class = notation.piece_from_initial(initial)
        piece = piece_class()
        piece.initial = initial
        piece.colour = Colour(initial)
        return piece

    def __unicode__(self):
        return self.initial

    def __repr__(self):
        return '<%s %s>' %(self.__class__.__name__, self.colour)

    def is_possible_move(self, xy):
        return xy in ALL_SQUARES

    def gen_moves(self, X, Y):
        for m in self.basic_moves(X, Y):
            assert isinstance(m, tuple), m
            assert len(m) == 2, m
            if self.is_possible_move(m):
                yield m

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
    def basic_moves(self, X, Y):
        for x, y in ALL_SQUARES:
            if set(map(abs, (X-x, Y-y))) == set([1, 2]):
                yield x, y


class Pawn(Piece):
    def basic_moves(self, X, Y):
        is_black = bool(self.colour)
        direction = 1 if is_black else -1
        pawn_start = 1 if is_black else 6
        yield X, Y+direction
        if Y==pawn_start:
            yield X, Y+2*direction


#import here to avoid recursion
import notation
