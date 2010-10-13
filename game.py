from itertools import cycle

from pieces import *
from board import *
from player import *


class Game(object):
    def __init__(self, inputer=raw_input):
        self.inputer = inputer
        self.board = Board(START)
        p1 = Player(Colour(False), 'Richie you Fucker!')
        p2 = Player(Colour(True), 'Jamie')
        for player in cycle((p1, p2)):
            self.do_move(player)
            
    def do_move(self, player):
        msg = ''
        while True:
            try:
                from_, to = player.get_move(msg, self.inputer)
            except KeyboardInterrupt:
                raise
            sq = self.board.look_in(from_)
            import pdb
            #pdb.set_trace()
            try:
                if not sq.occupied:
                    raise IllegalMoveError('There is no piece there, mofo!')
                if player.colour != sq.piece.colour:
                    raise IllegalMoveError("Cheat! %r is the other player's piece!" %(sq.piece))#, player.colour, sq.piece.colour))
                move = Move(sq, to, self.board)
                move.test_legal()
                possible_moves = list(self.board.get_moves_from_square(sq))
                if move not in possible_moves:
                    raise IllegalMoveError("I'm afraid a %s can't move like that! ... (MOFO)" %sq.piece)
            except IllegalMoveError, e:
                msg = getattr(e, 'message') or "That move don't fly with me buster, please try again"
            else:
                break
        print move

if __name__ == '__main__':
    g = Game()
            



