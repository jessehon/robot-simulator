import re

class ParseError(Exception):
    pass

class CommandParser(object):
    command_classes = [PlaceCommand, MoveCommand, LeftCommand, RightCommand, ReportCommand]

    def parse_file(self, input_file):
        lines = input_file.read().splitlines()
        commands = []
        for line in lines:
            command = parse_line(line)
            commands.push(command)
        return commands

    def parse_line(self, line):
        m = re.match(r"(\w+) ?(.*)?")
        identifier = m.group(0)
        arguments = m.group(1).split(',')

        for command_class in command_classes:
            if identifier == command_class.identifier:
                try:
                    command = command_class(arguments)
                    return command
                except:
                    raise ParseError("Problem with parsing " % command_class.__name__)

        return None
