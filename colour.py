import string

class Colour(object):
    WHITE, BLACK = False, True
    def __init__(self, initial_or_is_black):
        is_black = initial_or_is_black
        if isinstance(initial_or_is_black, basestring):
            is_black = initial_or_is_black.islower()
        else:
            assert isinstance(initial_or_is_black, (bool, int)), '%r' %initial_or_is_black
            assert initial_or_is_black in (0, 1), '%r' %initial_or_is_black
        self.is_black = bool(is_black)
        self.is_white = not self.is_black

    def __nonzero__(self):
        return self.is_black

    def __unicode__(self):
        return 'BLACK' if self.is_black else 'WHITE'

    def __repr__(self):
        return '<Colour %s>' %unicode(self)

    def do_case(self, s):
        return (string.upper if self.is_white else string.lower)(s)

    @property
    def initial(self):
        return unicode(self)[0]
