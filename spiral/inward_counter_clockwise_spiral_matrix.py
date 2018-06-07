from collections import deque


class InwardCounterClockwiseSpiralMatrix(object):
    def __init__(self, matrix):
        self.__matrix = matrix

    def __iter__(self):
        # Create a duplicate of the original matrix using a deque. This allows
        # us to destructively modify the duplicate without affecting the input
        deques = deque([deque(vector) for vector in self.__matrix])

        #
        #  ▽ ┌---┐
        #  ┆ ┆ X ┆
        #  ┆ ┆ ┆ ┆
        #  ┆ └-┘ ┆
        #  └-----┘
        #
        while any(deques):
            # Traverse down on the left side of the remaining deque
            for vector in deques:
                yield vector.popleft()

            # Traverse right on the bottom of the remaining deque
            for item in deques.pop():
                yield item

            if any(deques):
                # Traverse up on the right side of the remaining deque
                for vector in reversed(deques):
                    yield vector.pop()

                # Traverse left on the top side of the remaining deque
                for item in reversed(deques.popleft()):
                    yield item
