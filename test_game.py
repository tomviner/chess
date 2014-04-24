from textwrap import dedent

from board import Board
from game import Game


def test_game_initialisation():
    DRAUGHTS = dedent(
    """
    .O.O.O.O
    O.O.O.O.
    .O.O.O.O
    O.O.O.O.
    ........
    ........
    .X.X.X.X
    X.X.X.X.
    .X.X.X.X
    X.X.X.X.
    """).strip()

    CHESS = dedent(
    """
    rnbkqbnr
    pppppppp
    ........
    ........
    ........
    ........
    PPPPPPPP
    RNBQKBNR
    """).strip()

    for game_layout in (DRAUGHTS, CHESS):
        game = Game(initial=game_layout)
        assert game.board_display() == game_layout