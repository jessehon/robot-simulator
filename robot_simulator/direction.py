from position import Vector

class Direction(object):
    VALUES = ['NORTH', 'EAST', 'SOUTH', 'WEST']
    NORTH, EAST, SOUTH, WEST = VALUES
    VECTORS = {
        NORTH: Vector(0, 1),
        EAST: Vector(1, 0),
        SOUTH: Vector(0, -1),
        WEST: Vector(-1, 0),
    }

    def __init__(self, value):
        if value not in self.VALUES:
            raise Exception('bad direction')
        self._value = value

    @property
    def vector(self):
        return self.VECTORS[self._value]

    @property
    def value(self):
        return self._value

    def turn(self, step=1):
        index = self.VALUES.index(self._value)
        new_index = (index + step) % len(self.VALUES)
        new_value = self.VALUES[new_index]
        return self.__class__(new_value)
