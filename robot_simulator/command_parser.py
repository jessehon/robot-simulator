import re

class ParseError(Exception):
    pass

class CommandParser(object):
    command_classes = [PlaceCommand, MoveCommand, LeftCommand, RightCommand, ReportCommand]

    def parse_file(self, input_file):
        lines = input_file.read().splitlines()
        commands = []
        for line in lines:
            command = self.parse_line(line)
            commands.append(command)
        return commands

    def parse_line(self, line):
        m = re.match(r"(\w+)( (.*))?", line)
        identifier = m.group(1)
        arguments = m.group(3).split(',')

        for command_class in self.command_classes:
            if identifier == command_class.identifier:
                try:
                    command = command_class(arguments)
                    return command
                except:
                    raise ParseError("Problem with parsing %s" % command_class.__name__)

        return None
