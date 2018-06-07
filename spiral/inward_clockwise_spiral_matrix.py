from collections import deque


class InwardClockwiseSpiralMatrix(object):
    def __init__(self, matrix):
        self.__matrix = matrix

    def __iter__(self):
        # Create a duplicate of the original matrix using a deque. This allows
        # us to destructively modify the duplicate without affecting the input
        deques = deque([deque(vector) for vector in self.__matrix])

        #
        #  ▷-------┐
        #  ┌-----┐ ┆
        #  ┆ X---┘ ┆
        #  └-------┘
        #
        while any(deques):
            # Traverse right on the top of the remaining deque
            for item in deques.popleft():
                yield item

            # Traverse down on the right side of the remaining deque
            for vector in deques:
                yield vector.pop()

            if any(deques):
                # Traverse left on the bottom side of the remaining deque
                for item in reversed(deques.pop()):
                    yield item

                # Traverse up on the left side of the remaining deque
                for vector in reversed(deques):
                    yield vector.popleft()
