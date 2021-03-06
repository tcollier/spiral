"""
Visit each element of a matrix in a spiral path by keeping track of an
increasing "margin". Each time we traverse one rotation in the spiral, the
margin on all sides increases by one.
"""
from math import ceil
from spiral.research.direction import Direction


class MarginVisitor(object):
    def __init__(self, visit_fn):
        self.__visit_fn = visit_fn

    def start(self, matrix, clockwise):
        traverse_fn = (self.__cw if clockwise else self.__ccw)
        traverse_fn(matrix)

    def __cw(self, matrix):
        i, j = 0, -1
        smaller_dim = min(len(matrix), len(matrix[0]))
        max_margin = int(ceil(smaller_dim / 2))

        for margin in range(max_margin):
            visitable_width = len(matrix[0]) - 2 * margin
            visitable_height = len(matrix) - 2 * margin

            i, j = self.__visit_line(
                matrix, i, j, Direction.RIGHT, visitable_width)

            i, j = self.__visit_line(
                matrix, i, j, Direction.DOWN, visitable_height - 1)

            if margin < max_margin - 1 or not len(matrix) % 2:
                i, j = self.__visit_line(
                    matrix, i, j, Direction.LEFT, visitable_width - 1)

                if margin < max_margin - 1 or not len(matrix[0]) % 2:
                    i, j = self.__visit_line(
                        matrix, i, j, Direction.UP, visitable_height - 2)

    def __ccw(self, matrix):
        i, j = -1, 0
        smaller_dim = min(len(matrix), len(matrix[0]))
        max_margin = int(ceil(smaller_dim / 2))

        for margin in range(max_margin):
            visitable_width = len(matrix[0]) - 2 * margin
            visitable_height = len(matrix) - 2 * margin

            i, j = self.__visit_line(
                matrix, i, j, Direction.DOWN, visitable_height)

            i, j = self.__visit_line(
                matrix, i, j, Direction.RIGHT, visitable_width - 1)

            if margin < max_margin - 1 or not len(matrix[0]) % 2:
                i, j = self.__visit_line(
                    matrix, i, j, Direction.UP, visitable_height - 1)

                if margin < max_margin - 1 or not len(matrix) % 2:
                    i, j = self.__visit_line(
                        matrix, i, j, Direction.LEFT, visitable_width - 2)

    def __visit_line(self, matrix, i, j, direction, num_visits):
        """
        Visit `num_visits` elements of the matrix in a straight line
        :param matrix: The matrix that is being traversed
        :param location: Initial location to start the traversal
        :param direction: Direction of the traversal
        :param num_visits: Number of elements to be traversed
        :return: Location of the last element that is traversed
        """
        for _ in range(num_visits):
            i, j = direction(i, j)
            self.__visit_fn(matrix[i][j])

        return [i, j]
