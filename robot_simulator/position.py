class Point(object):
    def __init__(self, x=0, y=0):
        self._x = x
        self._y = y

    def __eq__(self, other):
        return (self.x == other.x) and (self.y == other.y)

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = int(value)

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        self._y = int(value)

    def add(self, other):
        self._x = self._x + other.x
        self._y = self._y + other.y
