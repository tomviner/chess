ALL_SQUARES = [(x, y) for x in range(1,9) for y in range(1,9)]

class Colour():
    WHITE = 0
    BLACK = 1


class Piece(object):
    def __init__(self, colour):
        assert colour in (0,1)
        self.colour = colour
        self.initial = Notation.initial_from_piece[self.__class__]
        self.initial = (str.upper if self.colour else str.lower)(self.initial)
        
    def __str__(self):
        return self.initial

class King(Piece):
    def gen_moves(self, X, Y):
        a3by3 = [(x, y) for x in range(-1, 2) for y in range(-1, 2)]
        for x, y in a3by3:
            yield X+x, Y+y
    def gen_special_moves(self, X, Y, orig):
        if orig:
            # castle
            pass
        
    
class Queen(Piece):
    def gen_moves(self, X, Y):
        for move in Rook.gen_moves():
            yield move
        for move in Bishop.gen_moves():
            yield move
    
                
class Rook(Piece): 
    def gen_moves(self, X, Y):
        for x, y in ALL_SQUARES:
            if X==x or Y==y:
                yield x, y

class Bishop(Piece):
    def gen_moves(self, X, Y):
        diff = X-Y
        for x, y in ALL_SQUARES:
            if y-x == diff:
                yield x, y
        

class Knight(Piece):
    def gen_moves(self, X, Y):
        for x, y in ALL_SQUARES:
            if set(map(abs, (X-x, Y-y))) == set([1, 2]):
                yield x, y
                

class Pawn(Piece):
    def gen_moves(self, X, Y):
        yield X, Y+1
        if Y==2:
            yield X, Y+2


class Notation():
    piece_from_initial = {      
        'K':King,
        'Q':Queen,
        'R':Rook,
        'B':Bishop,
        'N':Knight,
        'P':Pawn,
    }
    initial_from_piece = dict((v, k) for k, v in piece_from_initial.items())


