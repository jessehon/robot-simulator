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

    def place(self, position, direction):
        self.position = position
        self.direction = direction

    def move_by(self, step):
        new_position = self._position + (self.direction.vector * step)
        self.position = new_position

    def turn_by(self, step):
        new_drection = self.direction.turn_by(step)
        self.direction = new_drection

    def report(self):
        print ("Output: %d,%d,%s" %
                (self.position.x, self.position.y, self.direction.value))
