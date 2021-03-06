from unittest import TestCase
from spiral.research.visitor.iterative_visitor import IterativeVisitor
from spiral.research.traverser import Traverser
from tests.research.test_traverser import TestTraverser


class TestIterativeVisited(TestTraverser.Shared, TestCase):
    def visitor(self):
        return IterativeVisitor(self.accumulator.append)


def test_iterative_visitor_large_matrix(benchmark):
    matrix = [[i * 20 + j for j in range(0, 20)]
              for i in range(0, 20)]
    accumulator = []
    benchmark(Traverser(matrix).start, IterativeVisitor(accumulator.append))
