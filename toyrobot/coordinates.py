class Coordinates:
    maximum_steps = 4
    minimum_steps = 0

    def __init__(self, x_pos: int, y_pos: int):
        self.x_position = self.__check_steps_valdity(x_pos)
        self.y_position = self.__check_steps_valdity(y_pos)

    @classmethod
    def __check_steps_valdity(cls, x_pos_or_y_pos: int) -> int:
        if x_pos_or_y_pos > cls.maximum_steps or x_pos_or_y_pos < cls.minimum_steps:
            raise InvalidCoordinates(x_pos_or_y_pos)
        return x_pos_or_y_pos

    def stepup_x_position(self) -> 'Coordinates':
        if self.x_position == self.maximum_steps:
            return self
        return Coordinates(self.x_position + 1, self.y_position)

    def stepdown_x_position(self) -> 'Coordinates':
        if self.x_position == self.minimum_steps:
            return self
        return Coordinates(self.x_position - 1, self.y_position)

    def stepup_y_position(self) -> 'Coordinates':
        if self.y_position == self.maximum_steps:
            return self
        return Coordinates(self.x_position, self.y_position + 1)

    def stepdown_y_position(self) -> 'Coordinates':
        if self.y_position == self.minimum_steps:
            return self
        return Coordinates(self.x_position, self.y_position - 1)


class InvalidCoordinates(Exception):
    def __init__(self, x_pos_or_y_pos: int) -> None:
        super().__init__('"' + str(x_pos_or_y_pos) + '" is out of range')