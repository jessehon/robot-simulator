import re
from commands import *

class CommandParseError(Exception):
    pass

class CommandNotFoundError(Exception):
    pass

class CommandParser(object):
    command_classes = [PlaceCommand, MoveCommand, LeftCommand, RightCommand, ReportCommand]

    def parse(self, line):
        m = re.match(r"(\w+)( (.*))?", line)
        identifier = m.group(1)
        params_text = m.group(3)
        if params_text:
            params = params_text.split(',')
        else:
            params = []

        for command_class in self.command_classes:
            if identifier == command_class.identifier:
                try:
                    command = command_class(params)
                    return command
                except:
                    raise CommandParseError("Problem with parsing %s" % identifier)

        raise CommandNotFoundError("Problem finding matching command for %s" % identifier)
