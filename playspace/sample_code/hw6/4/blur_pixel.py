# Name: Audrey Chan
# Instructor: Aaron Keen
# Section: 09

def epsilon_equal(n, m, epsilon = 0.00001):
    return (n - epsilon) < m and (n + epsilon > m)

class Pixel():
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b
    def __eq__(self, other):
        return epsilon_equal(self.r, other.r) and epsilon_equal(self.g, other.g) and epsilon_equal(self.b, other.b)
