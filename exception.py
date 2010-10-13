class TakesAreMovesError(Exception):
    pass
class IllegalPositionError(Exception):
    pass

class InputError(Exception):
    def __init__(self, message):
        self.message = message

class IllegalMoveError(Exception):
    def __init__(self, message):
        self.message = message

