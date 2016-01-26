class User(object):
    """
    """
    def get_move(self):
        return

class CmdLineUser(User):
    """
    """
    def get_move(self):
        super(CmdLineUser, self).get_move()
        s = raw_input('Move: ')
        return s.strip().lower()
