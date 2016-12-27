import unittest
from blur_computations import *
from blur import *


class TestCases(unittest.TestCase):
   
   def test_neighbors(self):
      pixels = [[5, 4, 2], [2, 4, 5], [5, 3, 6], [2, 4, 6], [1, 2, 4],
         [4, 5, 2], [3, 4, 5], [5, 2, 5], [1, 6, 5], [3, 5, 56], [66, 34, 2],
         [5, 3, 4]]
      width = 4
      height = 3
      radius = 1
      test = find_neighbors(pixels, width, height, 0, 2, radius) 
      self.assertEqual(test[0], pixels[1])
      self.assertEqual(test[1], pixels[2])
      self.assertEqual(test[2], pixels[3])
      self.assertEqual(test[3], pixels[5]) 
      self.assertEqual(test[4], pixels[6])
      self.assertEqual(test[5], pixels[7])


   def test_neighbors_2(self):
      pixels = [[4, 5, 23], [4, 3, 5], [2, 3, 5], [8, 123, 545], [43, 65, 23],
         [54, 6, 34], [23, 5, 45], [43, 12, 5], [23, 5, 4], [32, 65, 7],
         [6, 56, 23], [34, 7, 12], [768, 23, 5], [234, 767, 12], [34, 6, 4],
         [43, 3, 5], [12, 65, 23], [12, 54, 236], [12, 65, 23], [12, 545, 23],
         [23, 54, 17], [23, 34, 6], [47, 234, 45], [234, 56, 23], [10, 40, 2]]
      width = 5
      height = 4
      radius = 2
      test = find_neighbors(pixels, width, height, 3, 3, radius)
      self.assertEqual(test[0], pixels[6])
      self.assertEqual(test[1], pixels[7])
      self.assertEqual(test[2], pixels[8])
      self.assertEqual(test[3], pixels[9])
      self.assertEqual(test[4], pixels[11]) 
      self.assertEqual(test[5], pixels[12])
      self.assertEqual(test[6], pixels[13])
      self.assertEqual(test[7], pixels[14])
      self.assertEqual(test[8], pixels[16])
      self.assertEqual(test[9], pixels[17])
      self.assertEqual(test[10], pixels[18])
      self.assertEqual(test[11], pixels[19])
      

   def test_neighbors_3(self):
      pixels = [[5, 4, 34], [23, 43, 2], [3, 43, 3],
         [23, 54, 23], [43, 2, 4], [23, 5, 1],
         [32, 54523, 124], [23, 5, 125], [23, 61, 345]]
      width = 3
      height = 3
      test = find_neighbors(pixels, width, height, 1, 2, 1)
      self.assertEqual(test[0], pixels[1])
      self.assertEqual(test[1], pixels[2])
      self.assertEqual(test[2], pixels[4])
      self.assertEqual(test[3], pixels[5])
      self.assertEqual(test[4], pixels[7])
      self.assertEqual(test[5], pixels[8])
      

   def test_neighbors_4(self):
      pixels = [[34, 23, 5], [323, 5, 12], [3, 3, 5],
         [54, 23, 5], [645, 12, 5], [23, 5, 34],
         [23, 45, 2], [23, 54, 34], [12, 545, 23]]
      width = 3
      height = 3
      test = find_neighbors(pixels, width, height, 0, 0, 1)
      self.assertEqual(test[0], pixels[0])
      self.assertEqual(test[1], pixels[1])
      self.assertEqual(test[2], pixels[3])
      self.assertEqual(test[3], pixels[4])


   def test_average(self):
      pixels = [[5, 6, 2], [3, 1, 6], [3, 5, 2]]
      test = average_pixels(pixels)
      self.assertEqual(test, [3, 4, 3])


   def test_average_2(self):
      pixels = [[3, 5, 45], [3, 2, 4], [3, 2, 4], [3, 4, 46]]
      test = average_pixels(pixels)
      self.assertEqual(test, [3, 3, 24])
      

if __name__ == '__main__':
   unittest.main()
