from collections import deque


class SpiralMatrix(object):
    COMPASS = [
        (0, 1),   # Right
        (1, 0),   # Down
        (0, -1),  # Left
        (-1, 0)]  # Up

    def __init__(self, matrix, clockwise=True, inward=True):
        self.__matrix = matrix
        self.__clockwise = clockwise
        self.__inward = inward

    def __reversed__(self):
        return SpiralMatrix(
            self.__matrix, clockwise=not self.__clockwise,
            inward=not self.__inward)

    def __iter__(self):
        if not self.__matrix or not self.__matrix[0]:
            return

        if self.__inward:
            compass_index = 0 if self.__clockwise else 1
            i, j = (0, 0)
            visited = [[False for _ in vector] for vector in self.__matrix]
            height = len(self.__matrix)
            width = len(self.__matrix[0])

            num_elements = height * width

            # We know a priori that we want to visit each element in the matrix
            # exactly once, so we can iterate `num_elements` times
            for _ in range(num_elements):
                yield self.__matrix[i][j]
                visited[i][j] = True

                direction = self.COMPASS[compass_index]
                i2, j2 = i + direction[0], j + direction[1]
                if 0 <= i2 < height and 0 <= j2 < width and not visited[i2][j2]:
                    i, j = i2, j2
                else:
                    # Turn 90 degrees in the proper direction
                    compass_index = compass_index + (1 if self.__clockwise else -1)
                    compass_index %= 4
                    direction = self.COMPASS[compass_index]
                    i, j = i + direction[0], j + direction[1]
        else:
