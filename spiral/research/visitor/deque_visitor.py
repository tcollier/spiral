"""
Visit each element of a matrix in a spiral path using a deque of deques. The
initial deque is a duplicate of the matrix, but is destructively consumed as it
it traversed.
"""
from collections import deque


class DequeVisitor(object):
    def __init__(self, visit_fn):
        self.__visit_fn = visit_fn

    def start(self, matrix, clockwise):
        # Create a duplicate of the original matrix using a deque. This allows
        # us to destructively modify the duplicate without affecting the input
        deques = deque([deque(vector) for vector in matrix])

        traverse_fn = (self.__cw if clockwise else self.__ccw)
        traverse_fn(deques)

    def __cw(self, deques):
        """
        :param deques: A deque of deques that is a duplicate of the matrix
        """
        while any(deques):
            # Traverse right on the top of the remaining deque
            [self.__visit_fn(i) for i in deques.popleft()]

            # Traverse down on the right side of the remaining deque
            [self.__visit_fn(v.pop()) for v in deques]

            if any(deques):
                # Traverse left on the bottom of the remaining deque
                [self.__visit_fn(i) for i in reversed(deques.pop())]

                # Traverse up on the left side of the remaining deque
                [self.__visit_fn(v.popleft()) for v in reversed(deques)]

    def __ccw(self, deques):
        """
        :param deques: A deque of deques that is a duplicate of the matrix
        """
        while any(deques):
            # Traverse down on the left side of the remaining deque
            [self.__visit_fn(v.popleft()) for v in deques]

            # Traverse right on the bottom of the remaining deque
            [self.__visit_fn(i) for i in deques.pop()]

            if any(deques):
                # Traverse up on the right side of the remaining deque
                [self.__visit_fn(v.pop()) for v in reversed(deques)]

                # Traverse left on the top of the remaining deque
                [self.__visit_fn(i) for i in reversed(deques.popleft())]
