from unittest import TestCase
from spiral.research.location import Location
from spiral.research.visit_tracker import VisitTracker


class TestVisitTracker(TestCase):
    def test_visit(self):
        tracker = VisitTracker([[1, 2], [3, 4]])
        location = Location(1, 1)
        self.assertTrue(tracker.visitable(location))
        tracker.visit(location)
        self.assertFalse(tracker.visitable(location))

    def test_visitable_out_of_bounds(self):
        tracker = VisitTracker([[1, 2], [3, 4]])
        self.assertFalse(tracker.visitable(Location(-1, 1)))
        self.assertFalse(tracker.visitable(Location(1, -1)))
        self.assertFalse(tracker.visitable(Location(2, 1)))
        self.assertFalse(tracker.visitable(Location(1, 2)))
