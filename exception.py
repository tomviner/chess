class ChessError(Exception):
    def __init__(self, message=''):
        self.message = message
        
    def __str__(self):
        return '%s %s' %(self.__class__.__name__, self.message)

class IllegalPositionError(ChessError):
    pass

class WrongColourError(ChessError):
    pass

class EmptySquareError(ChessError):
    pass

class IllegalForPieceError(ChessError):
    pass


class InputError(ChessError):
    pass
    
class TakesAreMovesError(ChessError):
    pass

class IllegalMoveError(ChessError):
    pass

class CheckError(ChessError):
    pass


# Game End Errors

class GameEndError(ChessError):
    pass

class ResignError(GameEndError):
    pass

class DrawError(GameEndError):
    pass

class CheckMateError(GameEndError):
    pass


