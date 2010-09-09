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
    'P'
    """
    return colour.do_case(initial_from_piece_dict[piece])

UNICODE_CODEPOINT_RANGE = range(0x2654, 0x2660)
UNICODE_CHAR_LIST = map(unichr, UNICODE_CODEPOINT_RANGE)

class UNICODE_PIECE:
    WK, WQ, WR, WB, WN, WP, \
    BK, BQ, BR, BB, BN, BP, \
        = UNICODE_CODEPOINT_RANGE

