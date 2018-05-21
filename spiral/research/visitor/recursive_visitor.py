"""
Visit each element of a matrix in a spiral path using a recursive approach.
This algorithm keeps track of which elements have already been visited to ensure
that no element is visited twice.
"""
from spiral.research.compass import Compass
from spiral.research.direction import Direction
from spiral.research.location import Location
from spiral.research.visit_tracker import VisitTracker


class RecursiveVisitor(object):
    def __init__(self, visit_fn):
        self._visit_fn = visit_fn

    def start(self, matrix, clockwise):
        initial_direction = Direction.RIGHT if clockwise else Direction.DOWN

        self.__visit(
            matrix=matrix, compass=Compass(initial_direction),
            clockwise=clockwise, location=Location(0, 0),
            visit_tracker=VisitTracker(matrix))

    def __visit(self, matrix, compass, clockwise, location, visit_tracker):
        self._visit_fn(matrix[location.i][location.j])
        visit_tracker.visit(location)

        forward_location = compass.direction(location)
        if visit_tracker.visitable(forward_location):
            self.__visit(
                matrix=matrix, compass=compass, clockwise=clockwise,
                location=forward_location, visit_tracker=visit_tracker)
        else:
            compass = compass.turn(clockwise)
            forward_location = compass.direction(location)
            if visit_tracker.visitable(forward_location):
                self.__visit(
                    matrix=matrix, compass=compass, clockwise=clockwise,
                    location=forward_location, visit_tracker=visit_tracker)
