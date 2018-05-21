from unittest import TestCase
from spiral.research.visit_tracker import VisitTracker


class TestVisitTracker(TestCase):
    def test_visit(self):
        tracker = VisitTracker([[1, 2], [3, 4]])
        self.assertTrue(tracker.visitable(1, 1))
        tracker.visit(1, 1)
        self.assertFalse(tracker.visitable(1, 1))

    def test_visitable_out_of_bounds(self):
        tracker = VisitTracker([[1, 2], [3, 4]])
        self.assertFalse(tracker.visitable(-1, 1))
        self.assertFalse(tracker.visitable(1, -1))
        self.assertFalse(tracker.visitable(2, 1))
        self.assertFalse(tracker.visitable(1, 2))
