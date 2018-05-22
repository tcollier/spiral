"""
Visit each element of a matrix in a spiral path using an iterative approach.
This algorithm keeps track of which elements have already been visited to ensure
that no element is visited twice.
"""


class IterativeVisitor(object):
    COMPASS = [
        (0, 1),   # Right
        (1, 0),   # Down
        (0, -1),  # Left
        (-1, 0)]  # Up

    def __init__(self, visit_fn):
        self.__visit_fn = visit_fn

    def start(self, matrix, clockwise):
        direction_index = 0 if clockwise else 1
        i, j = (0, 0)
        visited = [[False for _ in vector] for vector in matrix]
        height = len(matrix)
        width = len(matrix[0])

        num_elements = height * width

        # We know a priori that we want to visit each element in the matrix
        # exactly once, so we can iterate `num_elements` times
        for _ in range(num_elements):
            self.__visit_fn(matrix[i][j])
            visited[i][j] = True

            direction = self.COMPASS[direction_index]
            i2, j2 = i + direction[0], j + direction[1]
            if 0 <= i2 < height and 0 <= j2 < width and not visited[i2][j2]:
                i, j = i2, j2
            else:
                # Turn 90 degrees in the proper direction
                direction_index = direction_index + (1 if clockwise else -1)
                direction_index %= 4
                direction = self.COMPASS[direction_index]

                i, j = i + direction[0], j + direction[1]
