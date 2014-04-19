
class Board(object):
    def __init__(self, height, width):
        self._board = []
        for y in xrange(height):
            row = []
            for x in xrange(width):
                row.append('.')
            self._board.append(row)

    def display(self):
        ranks = [''.join(rank) for rank in self._board]
        return '\n'.join(ranks)