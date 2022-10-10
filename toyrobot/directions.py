from toyrobot.coordinates import Coordinates


class Directions:
    def __str__(self):
        return self.__corrected_class_name()

    def __corrected_class_name(self):
        return self.__class__.__name__.upper()[1:]

    maximum_steps = 4
    minimum_steps = 0

    @classmethod
    def from_str(cls, directions_str: str) -> 'Directions':
        return getattr(cls, directions_str, None)


class _North(Directions):
    @staticmethod
    def left() -> 'Directions':
        return Directions.WEST

    @classmethod
    def coordinates_movement(cls, coordinates: Coordinates) -> Coordinates:
        return coordinates.stepup_y_position()


class _South(Directions):
    @staticmethod
    def left() -> 'Directions':
        return Directions.EAST

    @classmethod
    def coordinates_movement(cls, coordinates: Coordinates) -> Coordinates:
        return coordinates.stepdown_y_position()


class _East(Directions):
    @staticmethod
    def left() -> 'Directions':
        return Directions.NORTH

    @classmethod
    def coordinates_movement(cls, coordinates: Coordinates) -> Coordinates:
        return coordinates.stepup_x_position()


class _West(Directions):
    @staticmethod
    def left() -> 'Directions':
        return Directions.SOUTH

    @classmethod
    def coordinates_movement(cls, coordinates: Coordinates) -> Coordinates:
        return coordinates.stepdown_x_position()

Directions.NORTH = _North()
Directions.SOUTH = _South()
Directions.EAST = _East()
Directions.WEST = _West()
