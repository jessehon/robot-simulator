from nose.tools import raises
from robot_simulator.command_parser import *

class TestCommandParser():
    def setup(self):
        self.commandParser = CommandParser()

    def test_place(self):
        command = self.commandParser.parse_line("PLACE 0,1,NORTH")
        assert command.identifier == "PLACE"
        assert command.params == ["0", "1", "NORTH"]

    def test_move(self):
        command = self.commandParser.parse_line("MOVE")
        assert command.identifier == "MOVE"

    def test_left(self):
        command = self.commandParser.parse_line("LEFT")
        assert command.identifier == "LEFT"

    def test_right(self):
        command = self.commandParser.parse_line("RIGHT")
        assert command.identifier == "RIGHT"

    def test_report(self):
        command = self.commandParser.parse_line("REPORT")
        assert command.identifier == "REPORT"

    @raises(CommandNotFoundError)
    def test_invalid_command(self):
        command = self.commandParser.parse_line("TEST")
