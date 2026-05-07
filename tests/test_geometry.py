import unittest

from pa_package.point import Point
from pa_package.line import Line


class TestPoint(unittest.TestCase):

    def test_distance_between_two_points(self):

        p1 = Point(0, 0)
        p2 = Point(3, 4)

        result = p1.distance_to(p2)

        self.assertEqual(result, 5.0)

    def test_distance_between_same_points(self):

        p1 = Point(2, 2)
        p2 = Point(2, 2)

        result = p1.distance_to(p2)

        self.assertEqual(result, 0.0)

class TestLine(unittest.TestCase):

    def test_line_length(self):

        p1 = Point(0, 0)
        p2 = Point(3, 4)

        line = Line(p1, p2)

        result = line.length()

        self.assertEqual(result, 5.0)
    
    def test_perpendicular_distance(self):

        line = Line(Point(0, 0), Point(4, 0))
        point = Point(0, 3)

        result = line.perpendicular_distance(point)

        self.assertEqual(result, 3.0)

if __name__ == "__main__":
    unittest.main()

  