import unittest2 as unittest

from colour import *
from pieces import *

class ColourTest(unittest.TestCase):
    def testInit(self):
        for input, is_black in {
            'Q':0, 0:0, False:Colour.WHITE, Colour.WHITE:Colour.WHITE,
            'k':1, 1:1, True:Colour.BLACK, Colour.BLACK:Colour.BLACK,
            }.items():
            c = Colour(input)
            self.assertEquals(c.is_black, bool(is_black))
            self.assertEquals(bool(c), bool(is_black))
            self.assertEquals(unicode(c), ['WHITE','BLACK'][bool(is_black)])
    def testPieceColour(self):
        self.assertEqual(bool(Rook(0).colour), Colour.WHITE)

class PieceTest(unittest.TestCase):
    def testCanJump(self):
        self.assertEqual(King().can_jump, False)
        self.assertEqual(Knight().can_jump, True)
    def testSolelyCapturing(self):
        self.assertRaises(TakesAreMovesError, Queen().solely_capturing_moves, 4, 3)
        with self.assertRaises(IllegalMoveError):
            list(Pawn().general_moves(0, 0))
        self.assertRaises(IllegalMoveError, lambda x,y:list(Pawn(Colour.WHITE).general_moves(x,y)), 0,0)
        self.assertEqual(set(Pawn(0).solely_capturing_moves(4, 3)), set([(3,4), (5,4)]))
