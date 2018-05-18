"""
Visit each element of a matrix in a spiral path using a deque of deques. The
initial deque is a duplicate of the matrix, but is destructively consumed as it
it traversed.
"""
from collections import deque


class DequeVisitor(object):
    def __init__(self, visit_fn):
        self._visit_fn = visit_fn

    def start(self, matrix, clockwise):
        # Create a duplicate of the original matrix using a deque. This allows
        # us to destructively modify the duplicate without affecting the input
        deques = deque([deque(vector) for vector in matrix])

        if clockwise:
            self.__visit_clockwise(deques)
        else:
            self.__visit_counter_clockwise(deques)

    def __visit_clockwise(self, deques):
        """
        :param deques: A deque of deques that is a duplicate of the matrix
        """
        while len(deques) and len(deques[0]):
            for item in deques.popleft():
                self._visit_fn(item)

            for vector in deques:
                if len(vector):
                    self._visit_fn(vector.pop())

            if len(deques):
                for item in reversed(deques.pop()):
                    self._visit_fn(item)

            for vector in reversed(deques):
                if len(vector):
                    self._visit_fn(vector.popleft())

    def __visit_counter_clockwise(self, deques):
        """
        :param deques: A deque of deques that is a duplicate of the matrix
        """
        while len(deques) and len(deques[0]):
            for vector in deques:
                if len(vector):
                    self._visit_fn(vector.popleft())

            for item in deques.pop():
                self._visit_fn(item)

            for vector in reversed(deques):
                if len(vector):
                    self._visit_fn(vector.pop())

            if len(deques):
                for item in reversed(deques.popleft()):
                    self._visit_fn(item)

