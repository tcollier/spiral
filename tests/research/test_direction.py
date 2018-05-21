from unittest import TestCase
from spiral.research.direction import Direction


class TestDirection(TestCase):
    def test_right(self):
        self.assertEqual((3, 4), Direction.RIGHT(3, 3))

    def test_left(self):
        self.assertEqual((3, 2), Direction.LEFT(3, 3))

    def test_down(self):
        self.assertEqual((4, 3), Direction.DOWN(3, 3))

    def test_up(self):
        self.assertEqual((2, 3), Direction.UP(3, 3))
