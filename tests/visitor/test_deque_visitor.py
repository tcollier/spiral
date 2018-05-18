from unittest import TestCase
from spiral.visitor.deque_visitor import DequeVisitor
from ..test_traverser import TestTraverser


class TestDequeVisitor(TestTraverser.Shared, TestCase):
    def visitor(self):
        return DequeVisitor(self.accumulator.append)
