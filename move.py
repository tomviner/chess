
class Move(object):
    def __init__(self, startXY, endXY):
        self.x1, self.y1 = startXY
        self.x2, self.y2 = endXY
        self.xy1 = startXY
        self.xy2 = endXY
        self.delta = self.x2-self.x1, self.y2-self.y1
        self.dx, self.dy = self.delta

    @property
    def is_right_angle(self):
        return not self.dx or not self.dy

    @property
    def is_diagonal(self):
        return (self.x1-self.y1 == self.x2-self.y2 or
        self.x1+self.y1 == self.x2+self.y2)

    @property
    def unit_move(self):
        mx = max(abs(self.dx), abs(self.dy))
        return dx/mx, dy/mx

    def path_clear(self, board):
        assert self.is_right_angle() or self.is_diagonal(), \
        'expecting a straight line move, got %d, %d' %self.delta
        unit = self.unit_move
        move = self.xy1
        occupied_squares = board.occupied_positions
        while move != self.xy2:
            move[0] += unit[0]
            move[1] += unit[1]
            if move == self.xy2:
                return True
            if move in occupied_squares:
                return False
        return True

