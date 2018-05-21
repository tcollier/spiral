from unittest import TestCase
from spiral.research.visitor.recursive_visitor import RecursiveVisitor
from spiral.research.traverser import Traverser
from tests.research.test_traverser import TestTraverser


class TestRecursiveVisitor(TestTraverser.Shared, TestCase):
    def visitor(self):
        return RecursiveVisitor(self.accumulator.append)

    # This test is known to fail with a RecursionError
    def test_traverse_large_matrix(self):
        pass


def test_recursive_visitor_large_matrix(benchmark):
    matrix = [[i * 20 + j for j in range(0, 20)]
              for i in range(0, 20)]
    accumulator = []
    benchmark(Traverser(matrix).start, RecursiveVisitor(accumulator.append))
