from toyrobot.commands import MoveCommand, ReportCommand, PlaceCommand, LeftCommand, RightCommand
from toyrobot.commands_controller import CommandsController, InvalidCommands

import unittest
from unittest.mock import Mock, PropertyMock


class CommandControllerTests(unittest.TestCase):

    def setUp(self):
        self.commands_controller = CommandsController(Mock())

    def test_move_command(self):
        cmd = self.commands_controller.to_cmd('MOVE')

        self.assertIsTypeOfClass(cmd, MoveCommand)

    def test_report_command(self):
        cmd = self.commands_controller.to_cmd('REPORT')

        self.assertIsTypeOfClass(cmd, ReportCommand)

    def test_place_place_command(self):
        cmd = self.commands_controller.to_cmd('PLACE 1,2,NORTH')

        self.assertIsTypeOfClass(cmd, PlaceCommand)

    def test_left_command(self):
        cmd = self.commands_controller.to_cmd('LEFT')

        self.assertIsTypeOfClass(cmd, LeftCommand)

    def test_right_command(self):
        cmd = self.commands_controller.to_cmd('RIGHT')

        self.assertIsTypeOfClass(cmd, RightCommand)

    def test_raise_an_exception_for_unknown_commands(self):
        self.assertRaises(InvalidCommands, self.commands_controller.to_cmd, 'Jump')

    def assertIsTypeOfClass(self, cmd, gClass):
        self.assertEqual(cmd.__class__, gClass)