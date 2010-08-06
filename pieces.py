
ALL_SQUARES = [(x, y) for x in range(1,9) for y in range(1,9)]

class Piece(object):
    pass
    
class King(Piece):
    def gen_moves(X, Y):
        a3by3 = [(x, y) for x in range(-1, 2) for y in range(-1, 2)]
        for x, y in a3by3:
            yield X+x, Y+y
    def gen_special_moves(X, Y, orig):
        if orig:
            # castle
            pass
        
    
class Queen(Piece):
    def gen_moves(X, Y):
        for move in Rook.gen_moves():
            yield move
        for move in Bishop.gen_moves():
            yield move
    
                
class Rook(Piece): 
    def gen_moves(X, Y):
        for x, y in ALL_SQUARES:
            if X==x or Y==y:
                yield x, y

class Bishop(Piece):
    def gen_moves(X, Y):
        diff = X-Y
        for x, y in ALL_SQUARES:
            if y-x == diff:
                yield x, y
        

class Knight(Piece):
    def gen_moves(X, Y):
        for x, y in ALL_SQUARES:
            if set(map(abs, (X-x, Y-y))) == set([1, 2]):
                yield x, y
                

class Pawn(Piece):
    def gen_moves(X, Y):
        yield X, Y+1
        if Y==2:
            yield X, Y+2
