
class Board(object):
    def __init__(self, height, width):
        self.board = []
        for y in xrange(height):
            row = []
            for x in xrange(width):
                row.append('.')
            self.board.append(row)