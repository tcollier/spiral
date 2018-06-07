from unittest import TestCase
from spiral.spiral_matrix import SpiralMatrix


class TestInwardCounterClockwise(TestCase):
    def test_traverse_empty(self):
        matrix = []
        actual = [i for i in SpiralMatrix(matrix, clockwise=False)]
        self.assertEqual([], actual)

    def test_traverse_empty_vector(self):
        matrix = [[]]
        actual = [i for i in SpiralMatrix(matrix, clockwise=False)]
        self.assertEqual([], actual)

    def test_traverse_single_element(self):
        matrix = [[1]]
        actual = [i for i in SpiralMatrix(matrix, clockwise=False)]
        self.assertEqual([1], actual)

    def test_traverse_row_vector(self):
        matrix = [[1, 2, 3]]
        actual = [i for i in SpiralMatrix(matrix, clockwise=False)]
        self.assertEqual([1, 2, 3], actual)

    def test_traverse_column_vector(self):
        matrix = [
            [1],
            [2],
            [3]]
        actual = [i for i in SpiralMatrix(matrix, clockwise=False)]
        self.assertEqual([1, 2, 3], actual)

    def test_traverse_even_square(self):
        matrix = [
            [1, 2],
            [3, 4]]
        actual = [i for i in SpiralMatrix(matrix, clockwise=False)]
        self.assertEqual([1, 3, 4, 2], actual)

    def test_traverse_odd_square(self):
        matrix = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]
        actual = [i for i in SpiralMatrix(matrix, clockwise=False)]
        self.assertEqual([1, 4, 7, 8, 9, 6, 3, 2, 5], actual)

    def test_traverse_wide_rectangle(self):
        matrix = [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12]]
        actual = [i for i in SpiralMatrix(matrix, clockwise=False)]
        self.assertEqual(
            [1, 5, 9, 10, 11, 12, 8, 4, 3, 2, 6, 7], actual)

    def test_traverse_tall_rectangle(self):
        matrix = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
            [10, 11, 12]]
        actual = [i for i in SpiralMatrix(matrix, clockwise=False)]
        self.assertEqual(
            [1, 4, 7, 10, 11, 12, 9, 6, 3, 2, 5, 8], actual)

    def test_traverse_large_matrix(self):
        matrix = [[i * 1000 + j for j in range(0, 1000)]
                  for i in range(0, 1000)]
        actual = [i for i in SpiralMatrix(matrix, clockwise=False)]
        self.assertEqual([0, 1000, 2000, 3000], actual[0:4])
        self.assertEqual([499499, 500499, 500500, 499500],
                         actual[-4:])
