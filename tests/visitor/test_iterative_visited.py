from unittest import TestCase
from spiral.visitor.iterative_visitor import IterativeVisitor
from ..test_traverser import TestTraverser


class TestIterativeVisited(TestTraverser.Shared, TestCase):
    def visitor(self):
        return IterativeVisitor(self.accumulator.append)
