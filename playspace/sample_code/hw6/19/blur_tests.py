import unittest
import blur

class Tests(unittest.TestCase):
   def test_two_dimension_list_1(self):
       list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
       width = 5
       height = 2
       expected = [['a', 'b', 'c', 'd', 'e'], ['f', 'g', 'h', 'i', 'j']]
       self.assertEqual(blur.two_dimension_list(list, width, height), expected)

   def test_two_dimension_list_2(self):
       list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
       width = 3
       height = 3
       expected = [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']]
       self.assertEqual(blur.two_dimension_list(list, width, height), expected)

if __name__ == '__main__':
   unittest.main()