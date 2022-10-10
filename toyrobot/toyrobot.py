from toyrobot.directions import Directions
from toyrobot.coordinates import Coordinates


class ToyRobot:

    def moves(self):
        self.coordinates = self.directions.coordinates_direction(self.coordinates)

    @property
    def x_position(self) -> int:
        return self.coordinates.x

    @property
    def y_position(self) -> int:
        return self.coordinates.y

    def left_side(self) -> None:
        self.directions.left()

    def right_side(self) -> None:
        self.directions.right()

    def placement(self, coordinate: Coordinates, direction: Directions) -> None:
        self.coordinates = coordinates
        self.directions = directions