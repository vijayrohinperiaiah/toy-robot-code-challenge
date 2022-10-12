import re
from typing import Callable
from toyrobot.commands import LeftCommand, RightCommand, MoveCommand, ReportCommand, PlaceCommand

class CommandsController:

    def __init__(self, display: Callable[[str], None]) -> None:
        self.display = display
        self.commands = {
            re.compile('^MOVE$'): lambda: MoveCommand(),
            re.compile('^REPORT$'): lambda: ReportCommand(display),
            re.compile('^PLACE \d,\d,(NORTH|SOUTH|EAST|WEST)$'): lambda args: PlaceCommand(args),
            re.compile('^LEFT$'): lambda: LeftCommand(),
            re.compile('^RIGHT$'): lambda: RightCommand(),
        }

    def to_cmd(self, cmd_str: str):
        cmd_tuple = filter(self.__on_cmd_match(cmd_str), self.commands.items())
        cmd_pool = next(map(self.__to_dict_value(), cmd_tuple), None)
        if cmd_pool is None:
            raise InvalidCommands(cmd_str)
        return self.__create_cmd_with_any_args(cmd_str, cmd_pool)

    @staticmethod
    def __to_dict_value():
        return lambda kv: kv[1]

    @staticmethod
    def __on_cmd_match(cmd_str):
        return lambda kv: kv[0].match(cmd_str)

    @staticmethod
    def __create_cmd_with_any_args(cmd_str, cmd_pool):
        cmd_sections = cmd_str.split(' ')
        if len(cmd_sections) == 2:
            return cmd_pool(cmd_sections[1])
        return cmd_pool()


class InvalidCommands(Exception):
    def __init__(self, msg) -> None:
        super().__init__('Specified entry - "' + msg + '" is an invalid command.')