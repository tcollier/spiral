from unittest import TestCase
from spiral.spiral_matrix import SpiralMatrix


class TestOutwardClockwise(TestCase):
    def test_traverse_empty(self):
        matrix = []
        actual = [i for i in SpiralMatrix(matrix, inward=False)]
        self.assertEqual([], actual)

    def test_traverse_empty_vector(self):
        matrix = [[]]
        actual = [i for i in SpiralMatrix(matrix, inward=False)]
        self.assertEqual([], actual)

    def test_traverse_single_element(self):
        matrix = [[1]]
        actual = [i for i in SpiralMatrix(matrix, inward=False)]
        self.assertEqual([1], actual)

    def test_traverse_row_vector(self):
        matrix = [[1, 2, 3]]
        actual = [i for i in SpiralMatrix(matrix, inward=False)]
        self.assertEqual([3, 2, 1], actual)

    def test_traverse_column_vector(self):
        matrix = [
            [1],
            [2],
            [3]]
        actual = [i for i in SpiralMatrix(matrix, inward=False)]
        self.assertEqual([3, 2, 1], actual)

    def test_traverse_even_square(self):
        matrix = [
            [1, 2],
            [3, 4]]
        actual = [i for i in SpiralMatrix(matrix, inward=False)]
        self.assertEqual([2, 4, 3, 1], actual)

    def test_traverse_odd_square(self):
        matrix = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]
        actual = [i for i in SpiralMatrix(matrix, inward=False)]
        self.assertEqual([5, 2, 3, 6, 9, 8, 7, 4, 1], actual)

    def test_traverse_wide_odd_height_rectangle(self):
        matrix = [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12]]
        actual = [i for i in SpiralMatrix(matrix, inward=False)]
        self.assertEqual(
            [7, 6, 2, 3, 4, 8, 12, 11, 10, 9, 5, 1], actual)

    def test_traverse_wide_even_height_rectangle(self):
        matrix = [
            [1, 2, 3, 4],
            [5, 6, 7, 8]]
        actual = [
            i for i in SpiralMatrix(matrix, inward=False)]
        self.assertEqual(
            [2, 3, 4, 8, 7, 6, 5, 1], actual)

    def test_traverse_tall_odd_width_rectangle(self):
        matrix = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
            [10, 11, 12]]
        actual = [i for i in SpiralMatrix(matrix, inward=False)]
        self.assertEqual(
            [8, 5, 2, 3, 6, 9, 12, 11, 10, 7, 4, 1], actual)

    def test_traverse_tall_even_width_rectangle(self):
        matrix = [
            [1, 2],
            [3, 4],
            [5, 6],
            [7, 8]]
        actual = [
            i for i in SpiralMatrix(matrix, inward=False)]
        self.assertEqual(
            [2, 4, 6, 8, 7, 5, 3, 1], actual)

    def test_traverse_large_matrix(self):
        matrix = [[i * 1000 + j for j in range(0, 1000)]
                  for i in range(0, 1000)]
        actual = [i for i in SpiralMatrix(matrix, inward=False)]
        self.assertEqual([499500, 500500, 500499, 499499], actual[0:4])
        self.assertEqual([3000, 2000, 1000, 0],
                         actual[-4:])
