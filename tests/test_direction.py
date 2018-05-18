from unittest import TestCase
from spiral.direction import Direction
from spiral.location import Location


class TestDirection(TestCase):
    def test_right(self):
        self.assertEqual(Location(3, 4), Direction.RIGHT(Location(3, 3)))

    def test_left(self):
        self.assertEqual(Location(3, 2), Direction.LEFT(Location(3, 3)))

    def test_down(self):
        self.assertEqual(Location(4, 3), Direction.DOWN(Location(3, 3)))

    def test_up(self):
        self.assertEqual(Location(2, 3), Direction.UP(Location(3, 3)))
