from unittest import TestCase
from spiral.visitor.margin_visitor import MarginVisitor
from ..test_traverser import TestTraverser


class TestMarginVisitor(TestTraverser.Shared, TestCase):
    def visitor(self):
        return MarginVisitor(self.accumulator.append)
