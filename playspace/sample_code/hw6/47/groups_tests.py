import unittest
import groups


class TestGroups(unittest.TestCase):

   def assertListAlmostEqual(self, l1, l2):
      self.assertEqual(len(l1), len(l2))
      for el1, el2 in zip(l1, l2):
         self.assertAlmostEqual(el1, el2)


   def test_1(self):
      list = [3, 4, 6, 8, 2, 9]
      answer = [[3, 4, 6], [8, 2, 9]]
      self.assertEqual(groups.groups_of_3(list), answer)

   def test_2(self):
      list = [5, 7, 8, 3, 4, 5, 3, 7]
      answer = [[5, 7, 8], [3, 4, 5], [3, 7]]
      self.assertEqual(groups.groups_of_3(list), answer)

   def test_3(self):
      list = ["255"]
      answer = [["255"]]
      self.assertEqual(groups.groups_of_3(list),answer)

if __name__ == '__main__':
   unittest.main()
