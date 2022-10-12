from toyrobot.commands import PlaceCommand, ReportCommand, MoveCommand, LeftCommand, RightCommand
from toyrobot.directions import Directions

import unittest
from unittest.mock import Mock, PropertyMock


class TestCommands(unittest.TestCase):

    def setUp(self):
        self.display_mock = Mock()
        self.robot = Mock()
        self.robot.move = Mock()

    def test_move_commands(self):
        move_command = MoveCommand()

        move_command.move_on(self.robot)

        self.robot.moves.assert_called_once()

    def test_report_commands(self):
        type(self.robot).x_position = PropertyMock(return_value=1)
        type(self.robot).y_position = PropertyMock(return_value=2)
        type(self.robot).directions = PropertyMock(return_value='NORTH')

        report_command = ReportCommand(self.display_mock)
        report_command.move_on(self.robot)

        self.display_mock.assert_called_once_with('1,2,NORTH')

    def test_place_command_places_the_robot_if_within_the_board(self):
        place_command = PlaceCommand('1,2,NORTH')
        self.robot.place = Mock()

        place_command.move_on(self.robot)

        self.robot.placement.assert_called_once_with(coordinates_at_xy(1,2), Directions.NORTH)

    def test_place_command_does_nothing_if_outside_of_board(self):
        place_command = PlaceCommand('1,6,NORTH')
        self.robot.place = Mock()

        place_command.move_on(self.robot)

        self.robot.place.assert_not_called()

    def test_left_command_turns_robot_left(self):
        self.robot.left_side = Mock()
        left_command = LeftCommand()

        left_command.move_on(self.robot)

        self.robot.left_side.assert_called_once()

    def test_right_command_turns_robot_right(self):
        self.robot.right_side = Mock()
        right_command = RightCommand()

        right_command.move_on(self.robot)

        self.robot.right_side.assert_called_once()


class CoordinatesMatcher:
    def __init__(self, x_position, y_position) -> None:
        self.x_position = x_position
        self.y_position = y_position

    def __eq__(self, new_item):
        matches = new_item.x_position == self.x_position and new_item.y_position == self.y_position
        if not matches:
            raise AssertionError(f"Expected a coordiate with x,y={self.x_position},{self.y_position}, got x,y={new_item.x_position},{new_item.y_position}")
        return matches


def coordinates_at_xy(x, y):
    return CoordinatesMatcher(x, y)
