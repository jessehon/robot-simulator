from nose.tools import raises
from robot_simulator.command_parser import *

class TestCommandParser():
    def setup(self):
        self.commandParser = CommandParser()

    def test_place(self):
        command = self.commandParser.parse("PLACE 0,1,NORTH")
        assert command.identifier == "PLACE"
        assert command.params == ["0", "1", "NORTH"]

    def test_move(self):
        command = self.commandParser.parse("MOVE")
        assert command.identifier == "MOVE"

    def test_left(self):
        command = self.commandParser.parse("LEFT")
        assert command.identifier == "LEFT"

    def test_right(self):
        command = self.commandParser.parse("RIGHT")
        assert command.identifier == "RIGHT"

    def test_report(self):
        command = self.commandParser.parse("REPORT")
        assert command.identifier == "REPORT"

    @raises(CommandNotFoundError)
    def test_invalid_command(self):
        command = self.commandParser.parse("TEST")
