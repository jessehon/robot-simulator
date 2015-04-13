from robot import Robot
from board import Board
from command_parser import CommandParser

class Simulation(object):
    def __init__(self):
        reset()

    def reset(self):
        self.board = Board(5, 5)
        self.robot = Robot(board)

    def run_file(self, input_file):
        command_parser = CommandParser()
        commands = command_parser.parse_file(input_file)
        run(commands)

    def run(self, commands):
        for command in commands:
            command.invoke(target=self.robot)
