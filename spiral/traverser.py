"""
Traverse a matrix in a clockwise or counter clockwise spiral, applying a visit
function to each element when it is visited.
"""
from collections import deque


class Traverser(object):
    def __init__(self, matrix):
        self._matrix = matrix

    def start(self, visit_fn=print, clockwise=True):
        """
        :param visitor: Visitor class that visits each element in the matrix in
        a spiral path
        :param clockwise: If True, then visit each element in a clockwise
        spiral, otherwise visit in a counter-clockwise spiral
        """
        if not len(self._matrix) or not len(self._matrix[0]):
            return

        # Create a duplicate of the original matrix using a deque. This allows
        # us to destructively modify the duplicate without affecting the input
        dup = deque([deque(vector) for vector in self._matrix])

        if clockwise:
            self._visit_clockwise(visit_fn, dup)
        else:
            self._visit_counter_clockwise(visit_fn, dup)

    @staticmethod
    def _visit_clockwise(visit_fn, dup):
        while len(dup) and len(dup[0]):
            for item in dup.popleft():
                visit_fn(item)

            for vector in dup:
                if len(vector):
                    visit_fn(vector.pop())

            if len(dup):
                for item in reversed(dup.pop()):
                    visit_fn(item)

            for vector in reversed(dup):
                if len(vector):
                    visit_fn(vector.popleft())

    @staticmethod
    def _visit_counter_clockwise(visit_fn, dup):
        while len(dup) and len(dup[0]):
            for vector in dup:
                if len(vector):
                    visit_fn(vector.popleft())

            for item in dup.pop():
                visit_fn(item)

            for vector in reversed(dup):
                if len(vector):
                    visit_fn(vector.pop())

            if len(dup):
                for item in reversed(dup.popleft()):
                    visit_fn(item)
