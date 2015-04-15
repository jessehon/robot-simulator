from nose.tools import raises
from robot_simulator.robot import *
from robot_simulator.board import Board
from robot_simulator.commands import *
from robot_simulator.positioning import Point, Vector
from robot_simulator.direction import Direction

class TestCommands():
    def setup(self):
        self.board = Board(5, 5)
        self.robot = Robot(self.board)

    def test_place(self):
        command = PlaceCommand(["0","1","NORTH"])
        command.invoke(target=self.robot)
        assert self.robot.position == Point(0,1)
        assert self.robot.direction == Direction("NORTH")

    def test_move(self):
        place_command = PlaceCommand(["4","0","NORTH"])
        place_command.invoke(target=self.robot)
        move_command = MoveCommand()
        move_command.invoke(target=self.robot)
        assert self.robot.position == Point(4,1)
        assert self.robot.direction == Direction("NORTH")

    def test_left(self):
        place_command = PlaceCommand(["2","4","NORTH"])
        place_command.invoke(target=self.robot)
        left_command = LeftCommand()
        left_command.invoke(target=self.robot)
        assert self.robot.position == Point(2,4)
        assert self.robot.direction == Direction("WEST")

    def test_right(self):
        place_command = PlaceCommand(["2","4","NORTH"])
        place_command.invoke(target=self.robot)
        right_command = RightCommand()
        right_command.invoke(target=self.robot)
        assert self.robot.position == Point(2,4)
        assert self.robot.direction == Direction("EAST")

    def test_report(self):
        place_command = PlaceCommand(["2","4","NORTH"])
        place_command.invoke(target=self.robot)
        report_command = ReportCommand()
        report_command.invoke(target=self.robot)
