import math

def epsilon_equal(n, m, epsilon=0.00001):
   return (n - epsilon) < m and (n + epsilon > m)

def convert_float(float):
   if float > 1.0:
      float = 1.0
   return int(float*255)

def distance_from_a_point(x,y,z,origin):
   return math.sqrt((x-origin.x)**2 + (y-origin.y)**2 + (z-origin.z)**2)

def nearest_to_point(list,point):
   if list == []:
      return None
   index_of_nearest = 0
   for i in range(1,len(list)):
      if distance_from_a_point(list[i].x,list[i].y,list[i].z,point) < distance_from_a_point(list[index_of_nearest].x,list[index_of_nearest].y,list[index_of_nearest].z,point):
         index_of_nearest = i
   return index_of_nearest
