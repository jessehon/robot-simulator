from robot import Robot, MoveOutOfBoundsError, MissingPlaceError
from board import Board
from command_parser import CommandParser

class Simulation(object):
    def __init__(self):
        self.reset()

    def reset(self):
        self.board = Board(5, 5)
        self.robot = Robot(self.board)

    def run_file(self, input_file):
        command_parser = CommandParser()
        commands = command_parser.parse_file(input_file)
        self.run(commands)

    def run(self, commands):
        for command in commands:
            command.invoke(target=self.robot)

            try:
                command.invoke(target=self.robot)
            except MoveOutOfBoundsError as e:
                print 'Skip %s:' % command.identifier, e
            except MissingPlaceError as e:
                print 'Skip %s:' % command.identifier, e
