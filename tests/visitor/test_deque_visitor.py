from unittest import TestCase
from spiral.visitor.deque_visitor import DequeVisitor
from spiral.traverser import Traverser
from ..test_traverser import TestTraverser


class TestDequeVisitor(TestTraverser.Shared, TestCase):
    def visitor(self):
        return DequeVisitor(self.accumulator.append)


def test_deque_visitor_large_matrix(benchmark):
    matrix = [[i * 20 + j for j in range(0, 20)]
              for i in range(0, 20)]
    accumulator = []
    benchmark(Traverser(matrix).start, DequeVisitor(accumulator.append))
