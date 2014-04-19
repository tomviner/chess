from textwrap import dedent

from board import Board


def test_board():
    b = Board(3, 3)
    empty_board = dedent(
    """
    ...
    ...
    ...
    """).strip()
    assert b.display() == empty_board