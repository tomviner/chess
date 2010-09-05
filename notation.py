from pieces import *

#class Notation(object):
piece_from_initial_dict = {
    'K':King,
    'Q':Queen,
    'R':Rook,
    'B':Bishop,
    'N':Knight,
    'P':Pawn,
}

def piece_from_initial(initial):
    return piece_from_initial_dict[initial.upper()]

initial_from_piece_dict = dict((v, k) for k, v in piece_from_initial_dict.items())

def initial_from_piece(piece):
    return initial_from_piece_dict[piece]

