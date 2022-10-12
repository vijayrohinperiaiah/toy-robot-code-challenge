from toyrobot.directions import Directions
from toyrobot.coordinates import Coordinates


class ToyRobot:

    def moves(self):
        self.coordinates = self.directions.coordinates_movement(self.coordinates)

    @property
    def x_position(self) -> int:
        return self.coordinates.x_position

    @property
    def y_position(self) -> int:
        return self.coordinates.y_position

    def left_side(self) -> None:
        self.directions = self.directions.left()

    def right_side(self) -> None:
        self.directions = self.directions.right()

    def placement(self, coordinates: Coordinates, directions: Directions) -> None:
        self.coordinates = coordinates
        self.directions = directions