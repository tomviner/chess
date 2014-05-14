from textwrap import dedent

import pytest
from mock import patch

from .exception import InputError
from .game import Game

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

def test_game_initialisation():
    """
    Check the board created from a string looks
    the same when re-displayed
    """
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

    for game_layout in (DRAUGHTS, CHESS):
        game = Game(initial=game_layout)
        assert game.display_board() == game_layout

@patch('chess.game.raw_input', create=True)
def test_taking_input(mock_raw_input):
    mock_raw_input.return_value = 'b2 e4'
    assert Game(initial=CHESS).get_move() == ((1, 1), (4, 3))

@pytest.mark.parametrize("input_move", (
    "notcorrect",
    "not correct",
    "so not correct",
    # only first 8 letters, a-h, not i-z
    "i1 a1",
    "d1 z2",
    # only first 8 digits (1 indexed), not 0 or 9+
    "a0 b2",
    "c7 a9",
    "d8 a10",
))
@patch('chess.game.raw_input', create=True)
def test_bad_input(mock_raw_input, input_move):
    """
    Check some invalid edge cases are indeed rejected
    """
    mock_raw_input.return_value = input_move
    with pytest.raises(InputError):
        Game(initial=CHESS).get_move()

@pytest.mark.parametrize("input_move", (
    "b2 b4",
    "a1 b1",
    "a1 a2",
))
@patch('chess.game.raw_input', create=True)
def test_size_dependant(mock_raw_input, input_move):
    full_size_board = CHESS
    dummy_tiny_board = '.'
    mock_raw_input.return_value = input_move
    with pytest.raises(InputError):
        Game(initial=dummy_tiny_board).get_move()
    Game(initial=full_size_board).get_move()
