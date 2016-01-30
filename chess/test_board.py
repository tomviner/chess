from textwrap import dedent

import pytest

from .board import Board
from .exception import BadMove


def test_empty_board():
    b = Board(3, 3)
    empty_board = dedent(
        """
        ...
        ...
        ...
        """
    ).strip()
    assert b.display() == empty_board

def test_place_piece():
    b = Board(3, 3)
    b.place(1, 2, 'X')
    expected_board = dedent(
        """
        .X.
        ...
        ...
        """
    ).strip()
    assert b.display() == expected_board

def test_place_more_pieces():
    b = Board(2, 2)
    grid = {
        (0, 1): 'a', (1, 1): 'b',
        (0, 0): 'c', (1, 0): 'd'}
    for (x, y), piece in grid.items():
        b.place(x, y, piece)
        assert b.look(x, y) == piece
    expected_board = dedent(
        """
        ab
        cd
        """
    ).strip()
    assert b.display() == expected_board

def test_move_piece():
    b = Board(2, 2)
    b.place(1, 1, 'X')
    b.move(1, 1, 0, 0)
    expected_board = dedent(
        """
        ..
        X.
        """
    ).strip()
    assert b.display() == expected_board

def test_move_empty_square():
    b = Board(2, 2)
    with pytest.raises(BadMove):
        b.move(0, 0, 1, 1)
