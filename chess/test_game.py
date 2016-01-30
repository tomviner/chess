from textwrap import dedent

import pytest

from .exception import InputError
from .game import Game
from .rules import ASCII_START_BOARD


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
        """
    ).strip()

    for game_layout in (DRAUGHTS, ASCII_START_BOARD):
        game = Game(initial=game_layout)
        assert game.display_board() == game_layout


def test_taking_input(fake_user):
    game = Game(initial=ASCII_START_BOARD)
    game.user.set_moves(['b2 e4'])
    assert game.get_move() == ((1, 1), (4, 3))


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
def test_bad_input(fake_user, input_move):
    """
    Check some invalid edge cases are indeed rejected
    """
    with pytest.raises(InputError):
        game = Game(initial=ASCII_START_BOARD)
        game.user.set_moves([input_move])
        game.get_move()


@pytest.mark.parametrize("input_move", (
    "b2 b4",
    "A1 B1",  # test upper case
    "a1 a2",
))
def test_size_dependant(fake_user, input_move):
    full_size_board = ASCII_START_BOARD
    dummy_tiny_board = '.'
    with pytest.raises(InputError):
        game = Game(initial=dummy_tiny_board)
        game.user.set_moves([input_move])
        game.get_move()
    game = Game(initial=full_size_board)
    game.user.set_moves([input_move])
    game.get_move()


def test_run_game(fake_user):
    MOVED_ASCII_START_BOARD = dedent(
        """
        rnbkqbnr
        pppppppp
        ..N.....
        ........
        ........
        ........
        PPPPPPPP
        R.BQKBNR
        """
    ).strip()

    move_knight_thrice = (
        'b1 c3',  # move Knight up
        'b0 d4',  # an invalid square
        'c3 z3',  # an invalid square
        'c3 e4',  # move across two, up one
        'e5 e6',  # no piece here
        'e4 c6',  # move up two, across two: we have no
                  # piece restrictions as yet!
    )
    game = Game(initial=ASCII_START_BOARD)
    game.user.set_moves(move_knight_thrice)
    for msg in game.run():
        print msg
        print
    assert game.display_board() == MOVED_ASCII_START_BOARD
