"""
Traverse a matrix in a clockwise spiral, applying a visit function to each
element when it is visited.
"""
from collections import deque


class Traverser(object):
    def __init__(self, matrix):
        self._matrix = matrix

    def start(self, visit_fn=print):
        if not len(self._matrix) or not len(self._matrix[0]):
            return

        # Create a duplicate of the original matrix using a deque. This allows
        # us to destructively modify the duplicate without affecting the input
        dup = deque([deque(vector) for vector in self._matrix])
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
