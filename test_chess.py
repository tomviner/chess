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

def test_place_more_pieces():
    b = Board(2, 2)
    b.place(0, 1, 'a')
    b.place(1, 1, 'b')
    b.place(0, 0, 'c')
    b.place(1, 0, 'd')
    exed_board = dedent(
    """
    ab
    cd
    """).strip()
    assert b.display() == exed_board
