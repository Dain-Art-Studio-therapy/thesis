import unittest
from fade_scale import *
from fade import *


class TestData(unittest.TestCase):
    def test_dist_from_center_1(self):
        pixel_pt = Point(5, 12)
        row = 0
        col = 0
        self.assertAlmostEqual(dist_from_center(row, col, pixel_pt),
                               13)

    def test_dist_from_center_2(self):
        pixel_pt = Point(495, 512)
        row = 500
        col = 500
        self.assertAlmostEqual(dist_from_center(row, col, pixel_pt),
                               13)


if __name__ == '__main__':
    unittest.main()

