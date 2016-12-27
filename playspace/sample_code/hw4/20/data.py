from utility import *

class Point():
  """Represents a point in 3-D space. x, y, z"""

  def __init__(self, x=0, y=0, z=0):
    self.x = x
    self.y = y
    self.z = z


  def __eq__(self, other):
    return epsilon_equal(self.x, other.x) and epsilon_equal(self.y, other.y) and epsilon_equal(self.z, other.z)


class Vector:
  def __init__(self, x, y, z):
    self.x = x
    self.y = y
    self.z = z


  def __eq__(self, other):
    return epsilon_equal(self.x, other.x) and epsilon_equal(self.y, other.y) and epsilon_equal(self.z, other.z)


class Ray:
  def __init__(self, pt, dir):
    self.pt = pt
    self.dir = dir

  def __eq__(self, other):
    return (self.pt == other.pt) and (self.dir == other.dir)


class Sphere:
  def __init__(self, center, radius, color, finish):
    self.center = center
    self.radius = radius
    self.color = color
    self.finish = finish

  def __eq__(self, other):
    return (self.center == other.center) and epsilon_equal(self.radius, other.radius) \
           and (self.color == other.color) and (self.finish == other.finish)


class Color:
  def __init__(self, r, g, b):
    self.r = r
    self.g = g
    self.b = b

  def multiply(self, other):
    mr = self.r * other.r
    mg = self.g * other.g
    mb = self.b * other.b

    return Color(mr, mg, mb)

  def __eq__(self, other):
    #return (self.r == other.r) and (self.g == other.g) and (self.b == other.b)
    return epsilon_equal(self.r, other.r) and epsilon_equal(self.g, other.g) \
           and epsilon_equal(self.b, other.b)

  def __repr__(self):
      return 'Color: r = ' + str(self.r) + ' g = ' + str(self.g) + ' b = ' + str(self.b)


class Finish:
    def __init__(self, ambient, diffuse, specular, roughness):
        self.ambient = ambient
        self.diffuse = diffuse
        self.specular = specular
        self.roughness = roughness

    def __eq__(self, other):
        return (self.ambient == other.ambient) \
               and (self.diffuse == other.diffuse) \
               and (self.specular == other.specular) \
               and (self.roughness == other.roughness)


class Light:
    def __init__(self, point, color):
        self.point = point
        self.color = color

    def __eq__(self, other):
        return (self.point == other.point) and (self.color == other.color)