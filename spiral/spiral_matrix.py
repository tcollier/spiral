from collections import deque


class SpiralMatrix(object):
    def __init__(self, matrix, clockwise=True):
        self.__matrix = matrix
        self.__clockwise = clockwise

    def __reversed__(self):
        return SpiralMatrix(self.__matrix, clockwise=not self.__clockwise)

    def __iter__(self):
        if not self.__matrix or not self.__matrix[0]:
            return

        # Create a duplicate of the original matrix using a deque. This allows
        # us to destructively modify the duplicate without affecting the input
        deques = deque([deque(vector) for vector in self.__matrix])

        while len(deques) and len(deques[0]):
            if self.__clockwise:
                # Traverse right on the top of the remaining deque
                for item in deques.popleft():
                    yield item

                # Traverse down on the right side of the remaining deque
                for vector in deques:
                    yield vector.pop()

                if len(deques) and len(deques[0]):
                    # Traverse left on the bottom side of the remaining deque
                    for item in reversed(deques.pop()):
                        yield item

                    # Traverse up on the left side of the remaining deque
                    for vector in reversed(deques):
                        yield vector.popleft()
            else:
                # Traverse down on the left side of the remaining deque
                for vector in deques:
                    yield vector.popleft()

                # Traverse right on the bottom of the remaining deque
                for item in deques.pop():
                    yield item

                if len(deques) and len(deques[0]):
                    # Traverse up on the right side of the remaining deque
                    for vector in reversed(deques):
                        yield vector.pop()

                    # Traverse left on the top side of the remaining deque
                    for item in reversed(deques.popleft()):
                        yield item
