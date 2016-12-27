import data
import math

def epsilon_equal(n, m, epsilon=0.00001):
   return (n - epsilon) < m and (n + epsilon > m)

def distance_3d(pt1, pt2):
   return math.sqrt( (pt2.x-pt1.x)**2 + (pt2.y-pt1.y)**2 + (pt2.z - pt1.z)**2 )
