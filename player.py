from exception import *
from pieces import *

class Player(object):
    def __init__(self, colour, name=None):
        self.colour = colour
        self.name = name or str(colour)

    def get_move(self, msg = '', inputer=raw_input):
        while True:
            input = inputer('\n'.join((msg, 'please move %s (%s)' %(self.name, self.colour))).strip()+': ')
            try:
                return self.parse_move(input)
            except (InputError, IllegalMoveError), e:
                msg = e.message

    def parse_square(self, input):
        try:
            l, d = input.lower()
            x = 'abcdefgh'.index(l)
            y = '12345678'.index(d)
        except ValueError:
            raise InputError('%r is not a square on the board!' %input)
        return (x, y)

    def parse_move(self, input):
        """A2 A4"""
        try:
            from_, to = input.split()
        except ValueError:
            raise InputError('Error: Please enter somelike "A1 A3"')

        from_ = self.parse_square(from_)
        to = self.parse_square(to)
        return (from_, to)

