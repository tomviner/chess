import unittest

from colour import *


class ColourTest(unittest.TestCase):
    def testInit(self):
        for input, is_black in {
            'Q':0, 0:0, False:Colour.WHITE,
            'k':1, 1:1, True:Colour.BLACK
            }.items():
            c = Colour(input)
            self.assertEquals(c.is_black, bool(is_black))
            self.assertEquals(bool(c), bool(is_black))
            self.assertEquals(unicode(c), ['WHITE','BLACK'][bool(is_black)])
