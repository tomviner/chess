from board import Board


def test_board():
    b = Board(3, 3)
    assert b.board == [['.', '.', '.'], ['.', '.', '.'] ,['.', '.', '.']]
