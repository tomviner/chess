#http://www.voidspace.org.uk/python/articles/unittest2.shtml
import unittest2 as unittest
import sys

from colour import *
from pieces import *
from board import *
from rules import *
from player import *
from game import *

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
        self.assertEqual(Rook(Colour.WHITE).colour.is_black, False)
        self.assertEqual(Rook(Colour.BLACK).colour.is_black, True)

class PieceTest(unittest.TestCase):
    def testCanJump(self):
        self.assertEqual(King().can_jump, False)
        self.assertEqual(Knight().can_jump, True)

    def testSolelyCapturing(self):
        self.assertRaises(TakesAreMovesError, Queen().solely_capturing_moves, 4, 3)
        self.assertItemsEqual(Pawn(0).solely_capturing_moves(4, 3), [(3,4), (5,4)])

    def testIllegalPosition(self):
        with self.assertRaises(IllegalPositionError):
            # pawn can't be behind starting position
            list(Pawn().general_moves(0, 0))

    def testBasicRookMoves(self):
        gen_ms = Rook().general_moves(0, 0)
        cap_ms = Rook().general_capturing_moves(0, 0)
        correct_moves = [(0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7),
                         (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0)]
        self.assertItemsEqual(gen_ms, correct_moves)
        self.assertItemsEqual(cap_ms, correct_moves)

    def testBasicKingMoves(self):
        ms = King().general_moves(0, 0)
        correct_moves = [(0,1), (1,1), (1,0)]
        self.assertItemsEqual(ms, correct_moves)

    def testBasicPawnMoves(self):
        ms = Pawn(Colour.WHITE).general_moves(0, 1)
        self.assertItemsEqual(ms, [(0, 2), (0, 3)])

        ms = Pawn(Colour.BLACK).general_moves(0, 1)
        self.assertItemsEqual(ms, [(0, 0)])

    def testCapturingPawnMoves(self):
        ms = Pawn(Colour.WHITE).general_capturing_moves(5, 1)
        self.assertItemsEqual(ms, [(4, 2), (6, 2)])

class BoardTest(unittest.TestCase):
    def testPlace(self):
        b = Board()
        with self.assertRaises(IllegalPositionError):
            # board uses 0 to 7 squared
            b.place((8, 8), Queen())
        b.place((2,3), Rook())

class InputCycler(object):
    def __init__(self, inputs):
        self.inputs = list(inputs)

    def __call__(self, prompt):
        if self.inputs:
            return self.inputs.pop()
        raise ResignError("InputCycler has run out of inputs")
        #sys.exit()

class GameTest(unittest.TestCase):
    def testgame(self):
        with self.assertRaises(InputError):
            g = Game(InputCycler(['wrong']))
        with self.assertRaises(InputError):
            g = Game(InputCycler(['wro ng']))
        with self.assertRaises(InputError):
            g = Game(InputCycler(['a2 QQ']))
        g = Game(InputCycler(['a2 a4']))

        with self.assertRaises(WrongColourError):
            g = Game(InputCycler(['c7 c6']))
        g = Game(InputCycler(['a2 a3', 'c7 c6']))

        with self.assertRaises(EmptySquareError):
            g = Game(InputCycler(['a4 a5']))

        with self.assertRaises(IllegalForPieceError):
            g = Game(InputCycler(['a2 c4']))
        # knight move
        g = Game(InputCycler(['b1 c3']))


