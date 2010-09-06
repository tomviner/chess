from pieces import *

piece_from_initial_dict = {
    'K':King,
    'Q':Queen,
    'R':Rook,
    'B':Bishop,
    'N':Knight,
    'P':Pawn,
}

def piece_from_initial(initial):
    """
    >>> piece_from_initial('k')
    <class 'chess.pieces.King'>
    """
    return piece_from_initial_dict[initial.upper()]

initial_from_piece_dict = dict((v, k) for k, v in piece_from_initial_dict.items())

def initial_from_piece(piece, colour):
    """
    >>> initial_from_piece(Queen, Colour('Q'))
    'Q'
    >>> initial_from_piece(Pawn, Colour(False))
    'p'
    """
    return colour.do_case(initial_from_piece_dict[piece])

