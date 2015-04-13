from abc import ABCMeta, abstractmethod
from point import Point
from direction import Direction

class BaseCommand():
    __metaclass__ = ABCMeta
    _identifier = ""
    _params = []

    def __init__(self, params=None):
        self.params = params

    @property
    def identifier(self):
        return self._identifier

    @property
    def params(self):
        return self._params

    @params.setter
    def params(self, values):
        self._params = values

    @abstractmethod
    def invoke(self, target):
        pass

class PlaceCommand(BaseCommand):
    _identifier = "PLACE"

    @BaseCommand.params.setter
    def params(self, values):
        super(BaseCommand, self).params(values)
        self.position = Point(values[0], values[1])
        self.direction = Direction(values[2])

    def invoke(self, target):
        target.position = self.position
        target.direction = self.direction
