import functions
import unittest

class TestData(unittest.TestCase):
   # Point
   def test_get_color(self):
      self.assertEqual(functions.get_color(71, 230, 71, 255, 0, 0, 0, 255), 14)
   
if __name__ == "__main__":
        unittest.main()


