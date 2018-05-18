from unittest import TestCase
from spiral.visitor.recursive_visitor import RecursiveVisitor
from ..test_traverser import TestTraverser


class TestRecursiveVisitor(TestTraverser.Shared, TestCase):
    def visitor(self):
        return RecursiveVisitor(self.accumulator.append)

    # This test is known to fail with a RecursionError
    def test_traverse_large_matrix(self):
        pass
