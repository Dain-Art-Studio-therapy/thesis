# Used for grid and point objects

class PixelGrid:
   # Pixels must be groups of three
   def __init__(self, pixels, width, height):
      self.width = int(width) - 1
      self.height = int(height) - 1 # Need to shift
      self.grid = self.createGrid(pixels, width, height)
      self.cur_pt = Point(0, 0)
   
   def updateCur(self):
      # Only update if end has not been reached
      c_pt = self.cur_pt
      w = self.width
      h = self.height
      if self.cur_pt != None:
         # Determine whether y needs to change
         if c_pt.x < w:
            c_pt.x += 1
         else:
            if c_pt.y < h:
               c_pt.y += 1
               c_pt.x = 0
            else:
               c_pt = None

   def createGrid(self, vals, width, height):
      g = []
      for i in range(height):
         g.append(vals[i * width : (i + 1) * width])

      return g

   def get_surrounding_pix_of_cur(self, rad):
      c_pt = self.cur_pt
      pixels = []
      
      # Get range and check that it's valid
      y_start = max(c_pt.y - rad, 0)
      y_end = min(c_pt.y + rad + 1, self.height + 1)
      x_start = max(c_pt.x - rad, 0)
      x_end = min(c_pt.x + rad + 1, self.width + 1)


      for y in range(y_start, y_end):
         for x in range(x_start, x_end):
            pixels.append(self.grid[y][x])
      return pixels

class Point:
   def __init__(self, x, y):
      self.x = x
      self.y = y
