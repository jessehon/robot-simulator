from robot import Robot, MoveOutOfBoundsError, MissingPlaceError
from board import Board
from command_parser import CommandParser

class Simulation(object):
    def __init__(self):
        self.command_parser = CommandParser()
        self.reset()

    def reset(self):
        self.board = Board(5, 5)
        self.robot = Robot(self.board)

    def run(self, line):
        command = self.command_parser.parse(line)

        try:
            command.invoke(target=self.robot)
        except MoveOutOfBoundsError as e:
            print 'Skip %s:' % command.identifier, e
        except MissingPlaceError as e:
            print 'Skip %s:' % command.identifier, e
