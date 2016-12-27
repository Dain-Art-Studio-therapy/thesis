import unittest
import fade

class Tests(unittest.TestCase):
    def test_groups_of_three_1(self):
       l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
       expected = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
       self.assertEqual(fade.groups_of_3(l), expected)

    def test_groups_of_three_2(self):
        l = [1, 2, 3, 1, 2, 4, 4, 5, 6, 1, 2, 3, 0, 9, 8, 7, 6, 5]
        expected = [[1, 2, 3], [1, 2, 4], [4, 5, 6], [1, 2, 3], [0, 9, 8], [7, 6, 5]]
        self.assertEqual(fade.groups_of_3(l), expected)


    def test_distance_1(self):
        x1 = 0
        y1 = 0
        x2 = 3
        y2 = 0
        expected = 3
        self.assertEqual(fade.distance(x1, y1, x2, y2), expected)

    def test_distance_2(self):
        x1 = 0
        y1 = 0
        x2 = 3
        y2 = 4
        expected = 5
        self.assertEqual(fade.distance(x1, y1, x2, y2), expected)

if __name__ == '__main__':
   unittest.main()