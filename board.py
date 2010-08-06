from pieces import *

START = """\
RNBQKBNR
PPPPPPPP
        
        
        
        
pppppppp
rnbqkbnr\
"""

class Board(object):
    def __init__(self):
        self.board = [list([' ']*8) for _ in range(8)]
        for y, rank in enumerate(START.splitlines()):
            for x, square in enumerate(rank):
                if square==' ':
                    continue
                self.board[y][x] = Notation.piece_from_initial[square.upper()](square.isupper())

    def __str__(self):
        ranks = [''.join(map(str, rank)) for rank in self.board]
        return '\n'.join(ranks)
        
if __name__ == '__main__':
    b = Board()
    print b
