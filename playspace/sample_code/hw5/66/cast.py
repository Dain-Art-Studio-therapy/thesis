import collisions
import vector_math
import data
import math

########## helper functions #########

def distance(pt1, pt2):
   return math.sqrt((pt2.x-pt1.x)**2 + (pt2.y-pt1.y)**2 + (pt2.z-pt1.z)**2)

def format_change(color): 
   return data.Color(min(255, int(color.r*255)), min(255, int(color.g*255)), min(255, int(color.b*255)))

def mindex(l):
   index = 0
   for i in range(1, len(l)):
      if l[i] < l[index]:
         index = i   
   return index

def calcs(ray, sphere_list, l, light):
   sphere_hit_list = [sphere for (sphere, point) in l]
   point_list = [point for (sphere, point) in l]

   dlist = []
   for (sphere, pt) in l:
      dlist.append(distance(ray.pt, pt))

   index = mindex(dlist)

   first_sphere = sphere_hit_list[index]
   first_point = point_list[index]
   n = collisions.sphere_normal_at_point(first_sphere, first_point)
   small_norm = vector_math.scale_vector(n, 0.01)
   p_e = vector_math.translate_point(first_point, small_norm)
   
   l_dir = vector_math.vector_from_to(p_e, light.pt)
   l_dir_norm = vector_math.normalize_vector(l_dir)
   dot = vector_math.dot_vector(n, l_dir_norm)   

   return [first_sphere, n, p_e, l_dir, l_dir_norm, dot]

def add_amb(first_sphere, amb_color):
   r = first_sphere.color.r * first_sphere.finish.ambient * amb_color.r
   g = first_sphere.color.g * first_sphere.finish.ambient * amb_color.g
   b = first_sphere.color.b * first_sphere.finish.ambient * amb_color.b
   return [r, g, b]

def add_diff(dot, light, first_sphere, p_e, l_dir, sphere_list):
   if dot < 0:
      option = 0
   else:
      distance_to_light = distance(p_e, light.pt)
      l2 = collisions.find_intersection_points(sphere_list, data.Ray(p_e, l_dir))
      if l2 == []:
         option = 1
      else:
         point_list_2 = [point for (sphere, point) in l2]
         d = []
         for e in point_list_2:
            d.append(distance(e, p_e))

         dmindex = mindex(d)
         if d[dmindex] > distance_to_light:
            option = 1
         else:
            option = 0

   if option == 0:
      return [0, 0, 0, 0]          # last element: if light is obstructed, no spec
   elif option == 1:
      r = dot * light.color.r * first_sphere.color.r * first_sphere.finish.diffuse
      g = dot * light.color.g * first_sphere.color.g * first_sphere.finish.diffuse
      b = dot * light.color.b * first_sphere.color.b * first_sphere.finish.diffuse
      return [r, g, b, 1]

def add_spec(l_dir_norm, dot, n, eye_point, p_e, first_sphere, light):
   v1 = vector_math.scale_vector(n, 2*dot)
   ref_vec = vector_math.difference_vector(l_dir_norm, v1)
   v_dir = vector_math.normalize_vector(vector_math.vector_from_to(eye_point, p_e))
   spec = vector_math.dot_vector(ref_vec, v_dir)

   if spec > 0:
      r = light.color.r * first_sphere.finish.specular * (spec**(1.0/first_sphere.finish.roughness))
      g = light.color.g * first_sphere.finish.specular * (spec**(1.0/first_sphere.finish.roughness)) 
      b = light.color.b * first_sphere.finish.specular * (spec**(1.0/first_sphere.finish.roughness)) 
      return [r, g, b]
   else:
      return [0, 0, 0]

########### cast_ray ####################

def cast_ray(ray, sphere_list, amb_color, light, eye_point):
   l = collisions.find_intersection_points(sphere_list, ray)
   
   if l == []:
      return data.Color(1.0, 1.0, 1.0)

   else:
      calcs1 = calcs(ray, sphere_list, l, light)

      first_sphere = calcs1[0]
      n = calcs1[1]
      p_e = calcs1[2]
      l_dir = calcs1[3]
      l_dir_norm = calcs1[4]
      dot = calcs1[5]
  
      amb = add_amb(first_sphere, amb_color)

      diff = add_diff(dot, light, first_sphere, p_e, l_dir, sphere_list)      

      if diff[3] == 1:
         spec = add_spec(l_dir_norm, dot, n, eye_point, p_e, first_sphere, light)
         
      else:
         spec = [0, 0, 0]

      return data.Color(amb[0] + diff[0] + spec[0], amb[1] + diff[1] + spec[1], amb[2] + diff[2] + spec[2])      

##########  cast_all_rays #############

def cast_all_rays(min_x, max_x, min_y, max_y, width, height, eye_point, sphere_list, amb_color, light):


   x_int = (max_x - min_x) / float(width)
   y_int = (max_y - min_y) / float(height)
 
   point_list = []
   for e in range(height):
      for f in range(width):
         point_list.append(data.Point(min_x + f*x_int, max_y - e*y_int, 0))

   ray_list = []  
   for e in point_list:
      v = vector_math.vector_from_to(eye_point, e)
      ray_list.append(data.Ray(eye_point, v))

   with open('image.ppm', 'w') as f:

      print >> f, 'P3'
      print >> f, width, height
      print >> f, 255

      for e in ray_list:
         p = format_change(cast_ray(e, sphere_list, amb_color, light, eye_point))      
         print >> f, p.r, p.g, p.b
