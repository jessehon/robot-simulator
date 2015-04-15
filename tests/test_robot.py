from nose.tools import raises
from robot_simulator.robot import *
from robot_simulator.board import Board
from robot_simulator.position import Point
from robot_simulator.direction import Direction

class TestRobot():
    def setup(self):
        self.board = Board(5, 5)
        self.robot = Robot(self.board)

    def test_place(self):
        self.robot.place(Point(0, 1), Direction("NORTH"))
        assert self.robot.position == Point(0,1)
        assert self.robot.direction == Direction("NORTH")

    @raises(MoveOutOfBoundsError)
    def test_place_out_of_lower_bounds(self):
        self.robot.place(Point(4, 5), Direction("NORTH"))

    @raises(MoveOutOfBoundsError)
    def test_place_out_of_upper_bounds(self):
        self.robot.place(Point(-1, 3), Direction("EAST"))

    def test_move(self):
        self.robot.place(Point(0, 1), Direction("NORTH"))
        self.robot.move_by(1)
        assert self.robot.position == Point(0,2)
        assert self.robot.direction == Direction("NORTH")

    @raises(MissingPlaceError)
    def test_move_without_place(self):
        self.robot.move_by(1)

    @raises(MoveOutOfBoundsError)
    def test_move_out_of_lower_bounds(self):
        self.robot.place(Point(0, 4), Direction("WEST"))
        self.robot.move_by(1)

    @raises(MoveOutOfBoundsError)
    def test_move_out_of_upper_bounds(self):
        self.robot.place(Point(4, 0), Direction("SOUTH"))
        self.robot.move_by(1)

    def test_left(self):
        self.robot.place(Point(2, 4), Direction("NORTH"))
        self.robot.turn_by(-1)
        assert self.robot.position == Point(2,4)
        assert self.robot.direction == Direction("WEST")

        self.robot.turn_by(-1)
        assert self.robot.position == Point(2,4)
        assert self.robot.direction == Direction("SOUTH")

        self.robot.turn_by(-1)
        assert self.robot.position == Point(2,4)
        assert self.robot.direction == Direction("EAST")

        self.robot.turn_by(-1)
        assert self.robot.position == Point(2,4)
        assert self.robot.direction == Direction("NORTH")

    @raises(MissingPlaceError)
    def test_left_without_place(self):
        self.robot.turn_by(-1)

    def test_right(self):
        self.robot.place(Point(2, 4), Direction("NORTH"))
        self.robot.turn_by(1)
        assert self.robot.position == Point(2,4)
        assert self.robot.direction.value == "EAST"

        self.robot.turn_by(1)
        assert self.robot.position == Point(2,4)
        assert self.robot.direction.value == "SOUTH"

        self.robot.turn_by(1)
        assert self.robot.position == Point(2,4)
        assert self.robot.direction.value == "WEST"

        self.robot.turn_by(1)
        assert self.robot.position == Point(2,4)
        assert self.robot.direction.value == "NORTH"

    @raises(MissingPlaceError)
    def test_right_without_place(self):
        self.robot.turn_by(1)

    def test_report(self):
        self.robot.place(Point(2, 4), Direction("NORTH"))
        assert self.robot.report() == "2,4,NORTH"

    @raises(MissingPlaceError)
    def test_report_without_place(self):
        self.robot.report()
