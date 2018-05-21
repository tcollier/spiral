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
        while len(deques) and len(deques[0]):
            [self.__visit_fn(i) for i in deques.popleft()]
            [self.__visit_fn(v.pop()) for v in deques]

            if len(deques) and len(deques[0]):
                [self.__visit_fn(i) for i in reversed(deques.pop())]
                [self.__visit_fn(v.popleft()) for v in reversed(deques)]

    def __ccw(self, deques):
        """
        :param deques: A deque of deques that is a duplicate of the matrix
        """
        while len(deques) and len(deques[0]):
            [self.__visit_fn(v.popleft()) for v in deques]
            [self.__visit_fn(i) for i in deques.pop()]

            if len(deques) and len(deques[0]):
                [self.__visit_fn(v.pop()) for v in reversed(deques)]
                [self.__visit_fn(i) for i in reversed(deques.popleft())]
