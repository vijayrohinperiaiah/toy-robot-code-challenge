from unittest import TestCase
from toyrobot.coordinates import Coordinates, InvalidCoordinates


class TestCoordinates(TestCase):
    def test_when_stepup_x_position_returns_the_incremented_x_value(self):
        coordinates = Coordinates(0, 0).stepup_x_position()

        self.assertEqual(coordinates.x_position, 1)

    def test_when_stepup_x_position_does_not_overflow(self):
        coordinates = Coordinates(4, 0).stepup_x_position()

        self.assertEqual(coordinates.x_position, 4)

    def test_when_stepdown_x_position_returns_the_decremented_x_value(self):
        coordinates = Coordinates(2, 0).stepdown_x_position()

        self.assertEqual(coordinates.x_position, 1)

    def test_when_stepdown_x_position_does_not_underflow(self):
        coordinates = Coordinates(0, 0).stepdown_x_position()

        self.assertEqual(coordinates.x_position, 0)

    def test_when_stepup_y_position_returns_the_incremented_y_value(self):
        coordinates = Coordinates(0, 0).stepup_y_position()

        self.assertEqual(coordinates.y_position, 1)

    def test_when_stepup_y_position_does_not_overflow(self):
        coordinates = Coordinates(0, 4).stepup_y_position()

        self.assertEqual(coordinates.y_position, 4)

    def test_when_stepdown_y_position_returns_the_decremented_y_value(self):
        coordinates = Coordinates(0, 2).stepdown_y_position()

        self.assertEqual(coordinates.y_position, 1)

    def test_when_stepdown_y_position_does_not_underflow(self):
        coordinates = Coordinates(0, 0).stepdown_y_position()

        self.assertEqual(coordinates.y_position, 0)

    def test_when_constructed_with_an_x_above_the_range_it_raises_an_exception(self):
        with self.assertRaisesRegex(InvalidCoordinates, '"99" is out of range'):
            Coordinates(99, 0)

    def test_when_constructed_with_a_y_above_the_range_it_raises_an_exception(self):
        with self.assertRaisesRegex(InvalidCoordinates, '"150" is out of range'):
            Coordinates(0, 150)
            
    def test_when_constructed_with_an_x_below_the_range_it_raises_an_exception(self):
        with self.assertRaisesRegex(InvalidCoordinates, '"-1" is out of range'):
            Coordinates(-1, 0)

    def test_when_constructed_with_a_y_below_the_range_it_raises_an_exception(self):
        with self.assertRaisesRegex(InvalidCoordinates, '"-2" is out of range'):
            Coordinates(0, -2)
