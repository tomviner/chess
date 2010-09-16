EMPTY_SQUARE = ' '

class Move(object):
    def __init__(self, start_square, end_xy, board):
        self.square = start_square
        self.piece = start_square.piece
        self.x1, self.y1 = start_square.xy
        self.x2, self.y2 = end_xy
        self.xy1 = start_square.xy
        self.xy2 = end_xy
        self.delta = self.x2-self.x1, self.y2-self.y1
        self.dx, self.dy = self.delta
        self.board = board
        self.board_occupied_squares = self.board.occupied
        self.special_move = False

    def __repr__(self):
        return '<%r to %r>' %(self.square, self.xy2)

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
        return self.dx/mx, self.dy/mx

    @property
    def path_clear(self):
        unit = self.unit_move
        move = list(self.xy1)
        end_pos = list(self.xy2)
        occupied_squares = self.board_occupied_squares
        while move != end_pos:
            move[0] += unit[0]
            move[1] += unit[1]
            if move == end_pos:
                return True
            if tuple(move) in occupied_squares:
                return False
        return True

    @property
    def valid_end(self):
        end = self.board.look_in(self.xy2)
        if not end.occupied:
            return True
        if end.piece.colour == self.piece.colour:
            # can't capture own piece
            return False
        elif end.piece.name == 'King':
            # can't capture opponents King
            return False
        return True

    @property
    def is_legal(self):
        if not (self.piece.can_jump or self.special_move):
            assert self.is_right_angle or self.is_diagonal, \
            'expecting a straight line move, got %d, %d' %self.delta

        if not (self.piece.can_jump or self.path_clear):
            return False

        if not self.valid_end:
            return False
        return True
