from unittest import TestCase
from unittest.mock import Mock

from toyrobot.directions import Directions
from toyrobot.coordinates import Coordinates


class TestDirections(TestCase):

    def setUp(self):
        super().setUp()
        self.coordinates = Coordinates(0, 0)

    def test_left_for_north_facing_returns_west(self):
        self.assertEqual(Directions.NORTH.left(), Directions.WEST)

    def test_left_for_south_facing_returns_east(self):
        self.assertEqual(Directions.SOUTH.left(), Directions.EAST)

    def test_left_for_east_facing_returns_north(self):
        self.assertEqual(Directions.EAST.left(), Directions.NORTH)

    def test_left_for_west_facing_returns_south(self):
        self.assertEqual(Directions.WEST.left(), Directions.SOUTH)

    def test_coordinates_movement_for_north_returns_a_coordinate_with_y_incremented(self):
        incremented_y_coordinates = Mock()
        self.coordinates.stepup_y_position = Mock(return_value=incremented_y_coordinates)

        new_coordinates = Directions.NORTH.coordinates_movement(self.coordinates)

        self.assertEqual(new_coordinates, incremented_y_coordinates)

    def test_coordinates_movement_for_south_returns_a_coordinate_with_y_decremented(self):
        decremented_y_coordinates = Mock()
        self.coordinates.stepdown_y_position = Mock(return_value=decremented_y_coordinates)

        new_coordinates = Directions.SOUTH.coordinates_movement(self.coordinates)

        self.assertEqual(new_coordinates, decremented_y_coordinates)

    def test_coordinates_movement_for_east_returns_a_coordinate_with_x_incremented(self):
        incremented_x_coordinates = Mock()
        self.coordinates.stepup_x_position = Mock(return_value=incremented_x_coordinates)

        new_coordinates = Directions.EAST.coordinates_movement(self.coordinates)

        self.assertEqual(new_coordinates, incremented_x_coordinates)

    def test_coordinates_movement_for_west_returns_a_coordinate_with_x_decremented(self):
        decremented_x_coordinates = Mock()
        self.coordinates.stepdown_x_position = Mock(return_value=decremented_x_coordinates)

        new_coordinates = Directions.WEST.coordinates_movement(self.coordinates)

        self.assertEqual(new_coordinates, decremented_x_coordinates)

    def test_from_str_for_north_returns_a_north_direction(self):
        self.assertEqual(Directions.from_str('NORTH'), Directions.NORTH)

    def test_from_str_for_south_returns_a_south_direction(self):
        self.assertEqual(Directions.from_str('SOUTH'), Directions.SOUTH)

    def test_from_str_for_east_returns_a_east_direction(self):
        self.assertEqual(Directions.from_str('EAST'), Directions.EAST)

    def test_from_str_for_west_returns_a_west_direction(self):
        self.assertEqual(Directions.from_str('WEST'), Directions.WEST)

    def test___str__for_north(self):
        self.assertEqual(str(Directions.NORTH), 'NORTH')

    def test___str__for_south(self):
        self.assertEqual(str(Directions.SOUTH), 'SOUTH')

    def test___str__for_east(self):
        self.assertEqual(str(Directions.EAST), 'EAST')

    def test___str_for_west(self):
        self.assertEqual(str(Directions.WEST), 'WEST')

