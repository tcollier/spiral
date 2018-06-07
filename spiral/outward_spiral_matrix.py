class OutwardSpiralMatrix(object):
    COMPASS = [
        (0, 1),   # Right
        (1, 0),   # Down
        (0, -1),  # Left
        (-1, 0)]  # Up

    RIGHT = 0
    DOWN = 1
    LEFT = 2
    UP = 3

    def __init__(self, matrix):
        self._matrix = matrix

    @property
    def height(self):
        return len(self._matrix)

    @property
    def width(self):
        return len(self._matrix[0])

    @property
    def num_elements(self):
        return self.width * self.height

    @property
    def is_tall(self):
        return self.height > self.width

    @property
    def is_wide(self):
        return self.width > self.height

    @property
    def has_even_height(self):
        return self.height % 2 == 0

    @property
    def has_even_width(self):
        return self.width % 2 == 0
