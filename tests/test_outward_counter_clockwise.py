from unittest import TestCase
from spiral.spiral_matrix import SpiralMatrix


class TestOutwardCounterClockwise(TestCase):
    def test_traverse_empty(self):
        matrix = []
        actual = [i for i in SpiralMatrix(matrix, clockwise=False, inward=False)]
        self.assertEqual([], actual)

    def test_traverse_empty_vector(self):
        matrix = [[]]
        actual = [i for i in SpiralMatrix(matrix, clockwise=False, inward=False)]
        self.assertEqual([], actual)

    def test_traverse_single_element(self):
        matrix = [[1]]
        actual = [i for i in SpiralMatrix(matrix, clockwise=False, inward=False)]
        self.assertEqual([1], actual)

    def test_traverse_row_vector(self):
        matrix = [[1, 2, 3]]
        actual = [i for i in SpiralMatrix(matrix, clockwise=False, inward=False)]
        self.assertEqual([3, 2, 1], actual)

    def test_traverse_column_vector(self):
        matrix = [
            [1],
            [2],
            [3]]
        actual = [i for i in SpiralMatrix(matrix, clockwise=False, inward=False)]
        self.assertEqual([3, 2, 1], actual)

    def test_traverse_even_square(self):
        matrix = [
            [1, 2],
            [3, 4]]
        actual = [i for i in SpiralMatrix(matrix, clockwise=False, inward=False)]
        self.assertEqual([3, 4, 2, 1], actual)

    def test_traverse_odd_square(self):
        matrix = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]
        actual = [i for i in SpiralMatrix(matrix, clockwise=False, inward=False)]
        self.assertEqual([5, 4, 7, 8, 9, 6, 3, 2, 1], actual)

    def test_traverse_wide_odd_height_rectangle(self):
        matrix = [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12]]
        actual = [
            i for i in SpiralMatrix(matrix, clockwise=False, inward=False)]
        self.assertEqual(
            [7, 6, 5, 9, 10, 11, 12, 8, 4, 3, 2, 1], actual)

    def test_traverse_wide_even_height_rectangle(self):
        matrix = [
            [1, 2, 3, 4],
            [5, 6, 7, 8]]
        actual = [
            i for i in SpiralMatrix(matrix, clockwise=False, inward=False)]
        self.assertEqual(
            [5, 6, 7, 8, 4, 3, 2, 1], actual)

    def test_traverse_tall_even_width_rectangle(self):
        matrix = [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [13, 14, 15, 16],
            [17, 18, 19, 20]]
        actual = [
            i for i in SpiralMatrix(matrix, clockwise=False, inward=False)]
        self.assertEqual(
            [10, 14, 15, 11, 7, 6, 5, 9, 13, 17, 18, 19, 20, 16, 12, 8, 4, 3, 2, 1],
            actual)

    def test_traverse_tall_odd_width_rectangle(self):
        matrix = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
            [10, 11, 12]]
        actual = [
            i for i in SpiralMatrix(matrix, clockwise=False, inward=False)]
        self.assertEqual(
            [8, 5, 4, 7, 10, 11, 12,9, 6, 3, 2, 1], actual)

    def test_traverse_large_matrix(self):
        matrix = [[i * 1000 + j for j in range(0, 1000)]
                  for i in range(0, 1000)]
        actual = [i for i in SpiralMatrix(matrix, clockwise=False, inward=False)]
        self.assertEqual([500499, 500500, 499500, 499499], actual[0:4])
        self.assertEqual([3, 2, 1, 0],
                         actual[-4:])
