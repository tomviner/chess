from chess.run import cmdline_game, random_game
from .rules import ASCII_START_BOARD

def test_cmdline_game_run(fake_user, capsys):
    cmdline_game()
    out, err = capsys.readouterr()
    assert ASCII_START_BOARD in out
    assert not err

def test_random_game_run(capsys):
    random_game(max_moves=50, sleep=0)
    out, err = capsys.readouterr()
    assert ASCII_START_BOARD in out
#     assert not/ err
