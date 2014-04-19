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

def test_place_piece():
    b = Board(3, 3)
    b.place(1, 2, 'X')
    exed_board = dedent(
    """
    .X.
    ...
    ...
    """).strip()
    assert b.display() == exed_board
