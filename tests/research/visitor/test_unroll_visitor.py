from unittest import skip, TestCase
from spiral.research.visitor.unroll_visitor import UnrollVisitor
from spiral.research.traverser import Traverser
from tests.research.test_traverser import TestTraverser


class TestUnrollVisitor(TestTraverser.Shared, TestCase):
    def visitor(self):
        return UnrollVisitor(self.accumulator.append)

    @skip("Known to fail with a RecursionError.")
    def test_traverse_large_matrix(self):
        pass


def test_unroll_visitor_large_matrix(benchmark):
    matrix = [[i * 20 + j for j in range(0, 20)]
              for i in range(0, 20)]
    accumulator = []
    benchmark(Traverser(matrix).start, UnrollVisitor(accumulator.append))
