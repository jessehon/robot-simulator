from abc import ABCMeta, abstractmethod
from position import Point
from direction import Direction

class BaseCommand():
    __metaclass__ = ABCMeta
    identifier = ""
    _params = []

    def __init__(self, params=None):
        self.params = params

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
    identifier = "PLACE"

    @BaseCommand.params.setter
    def params(self, values):
        BaseCommand.params.fset(self, values)
        self._position = Point(values[0], values[1])
        self._direction = Direction(values[2])

    def invoke(self, target):
        target.place(self._position, self._direction)

class MoveCommand(BaseCommand):
    identifier = "MOVE"

    def invoke(self, target):
        target.move_by(1)

class LeftCommand(BaseCommand):
    identifier = "LEFT"

    def invoke(self, target):
        target.turn_by(-1)

class RightCommand(BaseCommand):
    identifier = "RIGHT"

    def invoke(self, target):
        target.turn_by(1)

class ReportCommand(BaseCommand):
    identifier = "REPORT"

    def invoke(self, target):
        target.report()
