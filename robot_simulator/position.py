import math

class Point(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return (self.x == other.x) and (self.y == other.y)

    def __add__(self, other):
        x = self._x + other.x
        y = self._y + other.y
        return self.__class__(x, y)

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



class Vector(Point):
    def __mul__(self, scale):
        x = self._x*scale
        y = self._y*scale
        return self.__class__(x, y)

    @property
    def magnitude(self):
        return math.sqrt(self._x**2 + self._y**2)

class Rect(object):
    def __init__(self, point1, point2):
        self._top = max(point1.y, point2.y)
        self._right = max(point1.x, point2.x)
        self._bottom = min(point1.y, point2.y)
        self._left = min(point1.x, point2.x)

    @property
    def top(self):
        return self._top

    @property
    def right(self):
        return self._right

    @property
    def bottom(self):
        return self._bottom

    @property
    def left(self):
        return self._left

    def contains(self, point):
        contains_x = (self._left <= point.x) and (point.x <= self._right)
        contains_y = (self._bottom <= point.y) and (point.y <= self._top)
        return contains_x and contains_y
