from spiral.research.traverser import Traverser


class TestTraverser(object):
    class Shared(object):
        def setUp(self):
            self.accumulator = []

        def visitor(self):
            raise NotImplementedError('Test classes must implement this')

        def test_traverse_empty(self):
            matrix = []
            Traverser(matrix).start(self.visitor())
            self.assertEqual([], self.accumulator)

        def test_traverse_empty_vector(self):
            matrix = [[]]
            Traverser(matrix).start(self.visitor())
            self.assertEqual([], self.accumulator)

        def test_traverse_single_element(self):
            matrix = [[1]]
            Traverser(matrix).start(self.visitor())
            self.assertEqual([1], self.accumulator)

        def test_traverse_single_element_ccw(self):
            matrix = [[1]]
            Traverser(matrix).start(self.visitor(), clockwise=False)
            self.assertEqual([1], self.accumulator)

        def test_traverse_row_vector(self):
            matrix = [[1, 2, 3]]
            Traverser(matrix).start(self.visitor())
            self.assertEqual([1, 2, 3], self.accumulator)

        def test_traverse_row_vector_ccw(self):
            matrix = [[1, 2, 3]]
            Traverser(matrix).start(self.visitor(), clockwise=False)
            self.assertEqual([1, 2, 3], self.accumulator)

        def test_traverse_column_vector(self):
            matrix = [
                [1],
                [2],
                [3]]
            Traverser(matrix).start(self.visitor())
            self.assertEqual([1, 2, 3], self.accumulator)

        def test_traverse_column_vector_ccw(self):
            matrix = [
                [1],
                [2],
                [3]]
            Traverser(matrix).start(self.visitor(), clockwise=False)
            self.assertEqual([1, 2, 3], self.accumulator)

        def test_traverse_even_square(self):
            matrix = [
                [1, 2],
                [3, 4]]
            Traverser(matrix).start(self.visitor())
            self.assertEqual([1, 2, 4, 3], self.accumulator)

        def test_traverse_even_square_ccw(self):
            matrix = [
                [1, 2],
                [3, 4]]
            Traverser(matrix).start(self.visitor(), clockwise=False)
            self.assertEqual([1, 3, 4, 2], self.accumulator)

        def test_traverse_odd_square(self):
            matrix = [
                [1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]]
            Traverser(matrix).start(self.visitor())
            self.assertEqual([1, 2, 3, 6, 9, 8, 7, 4, 5], self.accumulator)

        def test_traverse_odd_square_ccw(self):
            matrix = [
                [1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]]
            Traverser(matrix).start(self.visitor(), clockwise=False)
            self.assertEqual([1, 4, 7, 8, 9, 6, 3, 2, 5], self.accumulator)

        def test_traverse_wide_rectangle(self):
            matrix = [
                [1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 10, 11, 12]]
            Traverser(matrix).start(self.visitor())
            self.assertEqual(
                [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7], self.accumulator)

        def test_traverse_wide_rectangle_ccw(self):
            matrix = [
                [1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 10, 11, 12]]
            Traverser(matrix).start(self.visitor(), clockwise=False)
            self.assertEqual(
                [1, 5, 9, 10, 11, 12, 8, 4, 3, 2, 6, 7], self.accumulator)

        def test_traverse_tall_rectangle(self):
            matrix = [
                [1, 2, 3],
                [4, 5, 6],
                [7, 8, 9],
                [10, 11, 12]]
            Traverser(matrix).start(self.visitor())
            self.assertEqual(
                [1, 2, 3, 6, 9, 12, 11, 10, 7, 4, 5, 8], self.accumulator)

        def test_traverse_tall_rectangle_ccw(self):
            matrix = [
                [1, 2, 3],
                [4, 5, 6],
                [7, 8, 9],
                [10, 11, 12]]
            Traverser(matrix).start(self.visitor(), clockwise=False)
            self.assertEqual(
                [1, 4, 7, 10, 11, 12, 9, 6, 3, 2, 5, 8], self.accumulator)

        def test_traverse_large_matrix(self):
            matrix = [[i * 1000 + j for j in range(0, 1000)]
                      for i in range(0, 1000)]
            Traverser(matrix).start(self.visitor())
            self.assertEqual([0, 1, 2, 3], self.accumulator[0:4])
            self.assertEqual([499499, 499500, 500500, 500499],
                             self.accumulator[-4:])
