"""
Visit each element of a matrix in a spiral path using a recursive approach.
This algorithm keeps track of which elements have already been visited to ensure
that no element is visited twice.
"""
from spiral.research.direction import Direction
from spiral.research.visit_tracker import VisitTracker


class RecursiveVisitor(object):
    COMPASS = [Direction.RIGHT, Direction.DOWN, Direction.LEFT, Direction.UP]

    def __init__(self, visit_fn):
        self.__visit_fn = visit_fn

    def start(self, matrix, clockwise):
        direction_index = 0 if clockwise else 1

        self.__visit(
            matrix=matrix, direction_index=direction_index,
            clockwise=clockwise, i=0, j=0,
            visit_tracker=VisitTracker(matrix))

    def __visit(self, matrix, direction_index, clockwise, i, j, visit_tracker):
        self.__visit_fn(matrix[i][j])
        visit_tracker.visit(i, j)

        next_i, next_j = self.COMPASS[direction_index](i, j)
        if visit_tracker.visitable(next_i, next_j):
            self.__visit(
                matrix=matrix, direction_index=direction_index,
                clockwise=clockwise, i=next_i, j=next_j,
                visit_tracker=visit_tracker)
        else:
            direction_index = direction_index + (1 if clockwise else -1)
            direction_index %= 4
            i, j = self.COMPASS[direction_index](i, j)
            if visit_tracker.visitable(i, j):
                self.__visit(
                    matrix=matrix, direction_index=direction_index,
                    clockwise=clockwise, i=i, j=j, visit_tracker=visit_tracker)
