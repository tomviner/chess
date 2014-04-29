from textwrap import dedent

from mock import patch

from .game import Game


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

@patch('chess.game.raw_input', create=True)
def test_taking_input(mock_raw_input):
    mock_raw_input.return_value = 'e2 e4'
    assert Game(initial=' ').get_move() == ((4, 1), (4, 3))
