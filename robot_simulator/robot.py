class Robot(object):
    def __init__(self, board):
        self._board = board
        self._position = None
        self._direction = None

    @property
    def board(self):
        return self._board

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, position):
        if not self._board.rect.contains(position):
            raise Exception('Invalid move')

        self._position = position

    @property
    def direction(self):
        return self._direction

    @direction.setter
    def direction(self, direction):
        self._direction = direction
