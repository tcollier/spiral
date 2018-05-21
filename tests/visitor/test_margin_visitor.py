from unittest import TestCase
from spiral.visitor.margin_visitor import MarginVisitor
from spiral.traverser import Traverser
from ..test_traverser import TestTraverser


class TestMarginVisitor(TestTraverser.Shared, TestCase):
    def visitor(self):
        return MarginVisitor(self.accumulator.append)


def test_margin_visitor_large_matrix(benchmark):
    matrix = [[i * 20 + j for j in range(0, 20)]
              for i in range(0, 20)]
    accumulator = []
    benchmark(Traverser(matrix).start, MarginVisitor(accumulator.append))
