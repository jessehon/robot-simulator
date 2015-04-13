import math

class Point(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

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

class Vector(Point):
    @property
    def magnitude(self):
        return math.sqrt(self._x**2 + self._y**2)

    def scale_by(self, scale):
        self._x = self._x*scale
        self._y = self._y*scale
