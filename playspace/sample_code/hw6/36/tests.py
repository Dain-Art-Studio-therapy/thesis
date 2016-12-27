import unittest
import puzzle

class TestCases(unittest.TestCase):
  def test_decode(self):
    l = [[20, 40, 40], [35, 40, 20], [1, 2, 4]]
    o = [[200, 200, 200], [255, 255, 255], [10, 10, 10]]
    self.assertEqual(puzzle.decode(l), o)


  def test_is_float(self):
    x = '2'
    y = 2
    self.assertAlmostEqual(puzzle.is_float(x), y)


  def test_groups_of_3(self):
    x = [432, 2342 ,1,    123,      9, 9,  7, 7,     7]
    y = [[432, 2342, 1], [123, 9, 9], [7, 7, 7]]
    self.assertEqual(puzzle.groups_of_3(x), y)


if __name__ == '__main__':
   unittest.main()
