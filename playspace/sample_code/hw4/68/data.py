import utility


class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __eq__(self, other):
        return utility.epsilon_equal(self.x, other.x) and utility.epsilon_equal(self.y,
                                                                                other.y) and utility.epsilon_equal(
            self.z, other.z)


class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __eq__(self, other):
        return utility.epsilon_equal(self.x, other.x) and utility.epsilon_equal(self.y,
                                                                                other.y) and utility.epsilon_equal(
            self.z, other.z)


class Ray:
    def __init__(self, pt, dirs):
        self.pt = pt
        self.dirs = dirs

    def __eq__(self, other):
        return (self.pt == other.pt) and (self.dirs == other.dirs)


class Sphere:
    def __init__(self, center, radius, color, finish):
        self.center = center
        self.radius = radius
        self.color = color
        self.finish = finish

    def __eq__(self, other):
        return (self.center == other.center) and (self.radius == other.radius) and (self.color == other.color) and (
            self.finish == other.finish)


class Color:
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

    def __eq__(self, other):
        return (self.r == other.r) and (self.g == other.g) and (self.b == other.b)


class Finish:
    # data.Finish(.4, .2)
    def __init__(self, ambient, diffuse):
        self.ambient = ambient
        self.diffuse = diffuse

    def __eq__(self, other):
        return utility.epsilon_equal(self.ambient, other.ambient) and utility.epsilon_equal(self.diffuse, other.diffuse)


class Light:
    # data.Light(Point(x,y,z), Color(1,1,1))
    def __init__(self, pt, color):
        self.pt = pt
        self.color = color

    def __eq__(self, other):
        return (self.pt == other.pt) and (self.color == other.color)