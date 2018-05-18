from unittest import TestCase
from spiral.compass import Compass
from spiral.direction import Direction


class TestCompass(TestCase):
    def test_turn_from_right(self):
        compass = Compass(Direction.RIGHT)
        self.assertEqual(Direction.DOWN, compass.turn(True).direction)

    def test_turn_from_down(self):
        compass = Compass(Direction.DOWN)
        self.assertEqual(Direction.LEFT, compass.turn(True).direction)

    def test_turn_from_left(self):
        compass = Compass(Direction.LEFT)
        self.assertEqual(Direction.UP, compass.turn(True).direction)

    def test_turn_from_up(self):
        compass = Compass(Direction.UP)
        self.assertEqual(Direction.RIGHT, compass.turn(True).direction)
