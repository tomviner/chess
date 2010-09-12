from django.utils.termcolors import colorize
import notation
from pieces import *
from board import *

class TextBoard(object):
    def __init__(self, board=None, n=1):
        if board:
            self.rows = unicode(board).splitlines()
        self.board = board
        self.n = n

    @classmethod
    def from_rows(cls, rows, n):
        tb = cls(n=n)
        tb.rows = rows
        return tb

    @classmethod
    def make_empty(cls, n):
        tb = cls()
        tb.rows = list([''])*n
        return tb

    def __add__(self, other):
        SEP = '   ' if self.rows[0] and other.rows[0] else ''
        return self.from_rows(
            [SEP.join(row_pair) for row_pair in zip(self.rows, other.rows)],
            self.n + other.n)

    @staticmethod
    def split_len(seq, length=104):
        return [seq[i:i+length] for i in range(0, len(seq), length)]

    def __unicode__(self):
        lines = zip(*map(self.split_len, self.rows))
        return self.colourise('\n'.join(row for line in lines for row in line))

    def __str__(self):
        return unicode(self).encode('utf-8')

    def __repr__(self):
        return '<%r>' %self.board

    def colourise(self, s):
        cols = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']
        piece_chars = 'RBNQKP.rbnqkp'
        piece_chars = notation.UNICODE_CHAR_LIST
        markers = '.Xx'
        def get_fg_kwargs(ch):
            d = {'opts':('bold',)}
            if ch in piece_chars:
                i = piece_chars.index(ch)
                is_black = i >= 6
                get_fg = {0: 'white', 1: 'red'}
                d['fg'] = get_fg[is_black]
            elif ch in markers:
                d['fg'] = 'green'
            else:
                return {}
            return d

        in_board = 0
        is_white = 1
        get_bg = {0:'', 1:'black'}
        checked = ''
        for i, ch in enumerate(s):
            orig_ch = ch
            bg_kwargs = {}
            if in_board and ch != '|':
                is_white = not is_white
                if is_white:
                    bg_kwargs['bg'] = get_bg[is_white]
            if orig_ch=='|':
                in_board = not in_board
            elif orig_ch=='\n':
                assert not in_board, s[i-10:i+10]
                is_white = not is_white
            d = bg_kwargs
            d.update(get_fg_kwargs(ch))
            if d:
                ch = colorize(ch, **d)+colorize()
            checked += ch
        return checked


    @classmethod
    def demo(cls, pieces='KqRbNpP'):
        board_walk = cls.make_empty(10)
        for initial in pieces:
            p = Piece.from_initial(initial)
            b = Board()
            b.place_moves_from_piece_at(p, Board.random_xy())
            board_walk += cls(b)
        print unicode(board_walk)
        return board_walk
    @classmethod

    def demo2(cls, pieces='KqRbNpP'):
        board_walk = cls.make_empty(10)
        for initial in pieces:
            b = Board(START)
            sq = b.random_occupied_square
            ms = b.get_moves_from_square(sq)
            for m in ms:
                b.place(m.xy2, m.piece)
            b.place(sq.xy, '.')
            board_walk += cls(b)
        print unicode(board_walk)
        return board_walk
