from mock import patch

from .game import Game
from .rules import ASCII_START_BOARD


def test_fake_cmdline_user(fake_user):
    """
    """
    game = Game(initial=ASCII_START_BOARD)
    game.user.set_moves(['b2 e4'])
    assert game.get_move() == ((1, 1), (4, 3))

@patch('chess.user.raw_input', create=True)
def test_cmdline_user(mock_raw_input):
    """
    """
    game = Game(initial=ASCII_START_BOARD)
    mock_raw_input.side_effect = iter(['b2 e4'])
    assert game.get_move() == ((1, 1), (4, 3))
