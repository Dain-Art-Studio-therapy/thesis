import unittest
from blur_clr_avg import *


class TestData(unittest.TestCase):
    def test_blur_clr_avg(self):
        pixel_grid = [[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],
                      [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],
                      [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]]
        self.assertEqual(blur_clr_avg(pixel_grid, 0), 0)





if __name__ == '__main__':
    unittest.main()


