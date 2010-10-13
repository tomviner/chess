from itertools import cycle

from pieces import *
from board import *
from player import *


class Game(object):
    def __init__(self, inputer=raw_input):
        self.inputer = inputer
        import __builtin__
        self.DEBUG = (self.inputer != __builtin__.raw_input)
        self.board = Board(START)
        p1 = Player(Colour(False), 'Richie')
        p2 = Player(Colour(True), 'Jamie')
        for player in cycle((p1, p2)):
            try:
                res = self.do_move(player)
            except GameEndError, e:
                if self.DEBUG:
                    if isinstance(e, ResignError):
                        return
                    raise
                print e
                return
            
    def do_move(self, player):
        msg = ''
        while True:
            try:
                from_, to = player.get_move(msg, self.inputer, self.DEBUG)
            except KeyboardInterrupt:
                raise
            sq = self.board.look_in(from_)
            try:
                if not sq.occupied:
                    raise EmptySquareError('There is no piece there, mofo!')
                if player.colour != sq.piece.colour:
                    raise WrongColourError("Cheat! %r is the other player's piece!" %(sq.piece))
                move = Move(sq, to, self.board)
                move.test_legal()
                possible_moves = list(self.board.get_moves_from_square(sq))
                if move not in possible_moves:
                    raise IllegalForPieceError("I'm afraid a %s can't move like that! ... (MOFO)" %sq.piece)
            except GameEndError, e:
                raise
            except ChessError, e:
                if self.DEBUG:
                    raise
                msg = getattr(e, 'message') or "That move don't fly with me buster, please try again"
            else:
                break
        print move

if __name__ == '__main__':
    g = Game()
            



