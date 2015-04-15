import re
from commands import *

class InvalidCommandFormatError(Exception):
    pass

class CommandNotFoundError(Exception):
    pass

class CommandParser(object):
    command_classes = [PlaceCommand, MoveCommand, LeftCommand, RightCommand, ReportCommand]

    def parse(self, line):
        m = re.match(r"(\w+)( (.*))?", line)
        identifier = m.group(1)
        params = (m.group(3) or "").split(',')

        for command_class in self.command_classes:
            if identifier == command_class.identifier:
                command = command_class(params)
                return command

        raise CommandNotFoundError("Problem finding matching command for %s" % identifier)
