"""
Visit each element of a matrix in a spiral path by keeping track of an
increasing "margin". Each time we traverse one rotation in the spiral, the
margin on all sides increases by one.
"""
from math import ceil
from spiral.research.direction import Direction
from spiral.research.location import Location


class MarginVisitor(object):
    def __init__(self, visit_fn):
        self._visit_fn = visit_fn

    def start(self, matrix, clockwise):
        if clockwise:
            self.__visit_clockwise(matrix)
        else:
            self.__visit_counter_clockwise(matrix)

    def __visit_clockwise(self, matrix):
        location = Location(0, -1)
        smaller_dim = min(len(matrix), len(matrix[0]))
        max_margin = ceil(smaller_dim / 2)

        for margin in range(max_margin):
            visitable_width = len(matrix[0]) - 2 * margin
            visitable_height = len(matrix) - 2 * margin

            location = self.__visit_line(
                matrix, location, Direction.RIGHT, visitable_width)

            location = self.__visit_line(
                matrix, location, Direction.DOWN, visitable_height - 1)

            if margin < max_margin - 1 or not len(matrix) % 2:
                location = self.__visit_line(
                    matrix, location, Direction.LEFT, visitable_width - 1)

                if margin < max_margin - 1 or not len(matrix[0]) % 2:
                    location = self.__visit_line(
                        matrix, location, Direction.UP, visitable_height - 2)

    def __visit_counter_clockwise(self, matrix):
        location = Location(-1, 0)
        smaller_dim = min(len(matrix), len(matrix[0]))
        max_margin = ceil(smaller_dim / 2)

        for margin in range(max_margin):
            visitable_width = len(matrix[0]) - 2 * margin
            visitable_height = len(matrix) - 2 * margin

            location = self.__visit_line(
                matrix, location, Direction.DOWN, visitable_height)

            location = self.__visit_line(
                matrix, location, Direction.RIGHT, visitable_width - 1)

            if margin < max_margin - 1 or not len(matrix[0]) % 2:
                location = self.__visit_line(
                    matrix, location, Direction.UP, visitable_height - 1)

                if margin < max_margin - 1 or not len(matrix) % 2:
                    location = self.__visit_line(
                        matrix, location, Direction.LEFT, visitable_width - 2)

    def __visit_line(self, matrix, location, direction, num_visits):
        """
        Visit `num_visits` elements of the matrix in a straight line
        :param matrix: The matrix that is being traversed
        :param location: Initial location to start the traversal
        :param direction: Direction of the traversal
        :param num_visits: Number of elements to be traversed
        :return: Location of the last element that is traversed
        """
        for _ in range(num_visits):
            location = direction(location)
            self._visit_fn(matrix[location.i][location.j])

        return location
