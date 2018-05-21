"""
Visit each element of a matrix in a spiral path using an iterative approach.
This algorithm keeps track of which elements have already been visited to ensure
that no element is visited twice.
"""
from spiral.research.direction import Direction
from spiral.research.visit_tracker import VisitTracker


class IterativeVisitor(object):
    COMPASS = [Direction.RIGHT, Direction.DOWN, Direction.LEFT, Direction.UP]

    def __init__(self, visit_fn):
        self.__visit_fn = visit_fn

    def start(self, matrix, clockwise):
        direction_index = 0 if clockwise else 1
        i = 0
        j = 0
        visit_tracker = VisitTracker(matrix)

        num_elements = len(matrix) * len(matrix[0])

        # We know a priori that we want to visit each element in the matrix
        # exactly once, so we can iterate `num_elements` times
        for _ in range(num_elements):
            self.__visit_fn(matrix[i][j])
            visit_tracker.visit(i, j)

            next_i, next_j = self.COMPASS[direction_index](i, j)
            if visit_tracker.visitable(next_i, next_j):
                i, j = next_i, next_j
            else:
                direction_index = direction_index + (1 if clockwise else -1)
                direction_index %= 4
                i, j = self.COMPASS[direction_index](i, j)
