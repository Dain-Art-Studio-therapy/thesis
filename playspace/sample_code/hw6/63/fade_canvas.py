# Used for canvas and point objects

class Canvas:
   def __init__(self, f_pt, width, height):
      self.f_pt = f_pt
      self.width = int(width) - 1
      self.height = int(height) - 1 # Need to shift
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

class Point:
   def __init__(self, x, y):
      self.x = x
      self.y = y
