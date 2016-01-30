from collections import deque

class CmdLineUser(object):
    """
    """

    def get_move(self):
        s = raw_input('Move: ')
        return s

class FakeUser(object):
    """
    """
    moves = deque([])

    def set_moves(self, moves):
        self.moves = deque(moves)

    def get_move(self):
        if self.moves:
            return self.moves.popleft()
        raise StopIteration
