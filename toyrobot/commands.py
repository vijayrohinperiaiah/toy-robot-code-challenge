from typing import Callable

from toyrobot.coordinates import Coordinates, InvalidCoordinates
from toyrobot.directions import Directions
from toyrobot.toyrobot import ToyRobot


class MoveCommand:
    @staticmethod
    def move_on(toyrobot: ToyRobot) -> None:
        toyrobot.moves()


class ReportCommand:
    def __init__(self, display: Callable[[str], None]) -> None:
        self.display = display

    def move_on(self, toyrobot: ToyRobot) -> None:
        self.display(f"{toyrobot.x_position},{toyrobot.y_position},{toyrobot.directions}")


class PlaceCommand:
    def __init__(self, args) -> None:
        self.args = args

    def move_on(self, toyrobot: ToyRobot):
        # Strict return of one args for these commands
        x_position, y_position, directions = self.args.split(',')
        try:
            toyrobot.placement(Coordinates(int(x_position), int(y_position)), Directions.from_str(directions))
        except InvalidCoordinates:
            pass  # Skip coordinates that place the robot off the table


class LeftCommand:
    @staticmethod
    def move_on(toyrobot: ToyRobot) -> None:
        toyrobot.left_side()


class RightCommand:
    @staticmethod
    def move_on(toyrobot: ToyRobot) -> None:
        toyrobot.right_side()