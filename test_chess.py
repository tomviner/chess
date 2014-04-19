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
    expected_board = dedent(
    """
    .X.
    ...
    ...
    """).strip()
    assert b.display() == expected_board

def test_place_more_pieces():
    b = Board(2, 2)
    grid = {
        (0, 1): 'a', (1, 1): 'b',
        (0, 0): 'c', (1, 0): 'd'}
    for (x, y), piece in grid.items():
        b.place(x, y, piece)
    expected_board = dedent(
    """
    ab
    cd
    """).strip()
    assert b.display() == expected_board

def test_move_piece():
    b = Board(2, 2)
    b.place(1, 1, 'X')
    b.move(1, 1, 0, 0)
    expected_board = dedent(
    """
    ..
    X.
    """).strip()
    assert b.display() == expected_board