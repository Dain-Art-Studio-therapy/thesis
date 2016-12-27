import unittest
from blur import *

class TestCollisions(unittest.TestCase):
   def test_calc_color(self):
      x=1
      y=1
      a=[0,0,0]
      b=[5,5,5]
      pixel_list=[[a,a,a],[a,a,a],[a,a,a],[a,a,b],[a,a,b],[a,a,b],[a,a,b],[a,a,b],[a,a,b]]
      self.assertAlmostEqual(calc_color(x,y,pixel_list,1,3,3)[3],.6666666666)
   def test_make_list(self):
      list=[1,2,3,4,5,6,7,8]
      x=2
      y=4
      test=make_list(list,x,y)
      print str(len(test))
      self.assertEqual(test[3][1],8)

if __name__=='__main__':
   unittest.main()
