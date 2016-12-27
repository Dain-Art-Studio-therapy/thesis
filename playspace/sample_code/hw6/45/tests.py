import unittest
from blur import *

class Test(unittest.TestCase):
   def test1(self):
      self.assertEqual(get_start_pts(6, 2, 3), (3, 0))

   def test2(self):
      pass

if __name__ == '__main__':
   unittest.main()
