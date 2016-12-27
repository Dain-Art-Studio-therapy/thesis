#Mostly here just for Color...

class Color:
   def __init__(self, r, g, b):
      self.r = r
      self.g = g
      self.b = b

   def __eq__(self, other):
      return (self.r == other.r and self.g == other.g and self.b == other.b)








