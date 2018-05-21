"""
Visit each element of a matrix in a spiral path using an iterative approach.
This algorithm keeps track of which elements have already been visited to ensure
that no element is visited twice.
"""
from spiral.research.compass import Compass
from spiral.research.direction import Direction
from spiral.research.location import Location
from spiral.research.visit_tracker import VisitTracker


class IterativeVisitor(object):
    def __init__(self, visit_fn):
        self.__visit_fn = visit_fn

    def start(self, matrix, clockwise):
        initial_direction = Direction.RIGHT if clockwise else Direction.DOWN
        compass = Compass(initial_direction)

        location = Location(0, 0)
        visit_tracker = VisitTracker(matrix)

        num_elements = len(matrix) * len(matrix[0])

        # We know a priori that we want to visit each element in the matrix
        # exactly once, so we can iterate `num_elements` times
        for _ in range(num_elements):
            self.__visit_fn(matrix[location.i][location.j])
            visit_tracker.visit(location)

            forward_location = compass.direction(location)
            if visit_tracker.visitable(forward_location):
                location = forward_location
            else:
                compass = compass.turn(clockwise)
                location = compass.direction(location)
