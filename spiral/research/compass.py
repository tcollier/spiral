"""
Utility class for managing the direction and rotation of a matrix traversal.
"""
from spiral.research.direction import Direction


class Compass(object):
    # The order of a clockwise rotation. After the last element, circle back to
    # the first.
    ORDER = [Direction.RIGHT, Direction.DOWN, Direction.LEFT, Direction.UP]

    def __init__(self, direction):
        self.direction = direction

    def turn(self, clockwise):
        """
        :param clockwise: True if the compass should turn in a clockwise
        direction, e.g. from "up" to "right", other wise the compass will turn
        in a counter-clockwise direction
        :return: A new compass pointing in the rotated direction
        """
        index = self.ORDER.index(self.direction)
        next_index = index + 1 if clockwise else index - 1
        return Compass(self.ORDER[next_index % 4])
