import data
import math
import vector_math
import cast

#Returns the nearest point of intersection or 0 if there are none
def sphere_intersection_point(ray, sphere):
   A = vector_math.dot_vector(ray.dir, ray.dir)
   B = vector_math.dot_vector(vector_math.scale_vector(vector_math.difference_point(ray.pt, sphere.center),2), ray.dir)
   C = (vector_math.dot_vector(vector_math.difference_point(ray.pt, sphere.center), vector_math.difference_point(ray.pt, sphere.center)) - sphere.radius**2)
   if (B**2) - (4*A*C) < 0:
      return 0
   elif (B**2) - (4*A*C) == 0:
      t = ((B*(-1)) + math.sqrt((B**2) - (4*A*C)))/(2*A)
      return data.Point(ray.pt.x + t*ray.dir.x, ray.pt.y + t*ray.dir.y, ray.pt.z + t*ray.dir.z)
   else:
      t = ((B*(-1)) + math.sqrt((B**2) - (4*A*C)))/(2*A)
      t2 = ((B*(-1)) - math.sqrt((B**2) - (4*A*C)))/(2*A)
      if t < t2 and t > 0 or t > 0 and t2 < 0: 
         return data.Point(ray.pt.x + t*ray.dir.x, ray.pt.y + t*ray.dir.y, ray.pt.z + t*ray.dir.z)
      elif t < 0 and t2 < 0:
         return 0
      elif t2 < t and t2 > 0 or t < 0 and t2 > 0:   
         return data.Point(ray.pt.x + t2*ray.dir.x, ray.pt.y + t2*ray.dir.y, ray.pt.z + t2*ray.dir.z)
     
 

      
    

#Checks if the ray intersects each sphere in sphere_list and returns a list of successful spheres and intersection points
def find_intersection_points(ray, sphere_list):
   new_sphere_list_of_success = []
   for i in sphere_list:
      if sphere_intersection_point(ray, i) != 0:
         new_sphere_list_of_success.append([sphere_intersection_point(ray, i), i])
   return new_sphere_list_of_success




