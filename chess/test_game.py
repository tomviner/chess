from textwrap import dedent

import pytest
from mock import patch

from .game import Game
from .exception import InputError


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
    mock_raw_input.return_value = 'b2 e4'
    assert Game(initial='.').get_move() == ((1, 1), (4, 3))


@pytest.mark.parametrize("input", (
    "notcorrect",
    "not correct",
    "so not correct",
    # only first 8 letters, a-h, not i-z
    "i1 a1",
    "d1 z2",
    # only first 8 digits (1 indexed), not 0
    "a0 b2",
    # only first 8 digits (1 indexed), not 9 onwards
    "c7 a9",
    "d8 a10",
))
@patch('chess.game.raw_input', create=True)
def test_bad_input(mock_raw_input, input_move):
    with pytest.raises(InputError):
        mock_raw_input.return_value = input_move
        Game(initial=' ').get_move()
