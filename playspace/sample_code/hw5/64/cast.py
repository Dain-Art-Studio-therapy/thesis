import collisions
import data
import vector_math


def cast_ray(ray,sphere_list,ambi,light,eye_point):
   
   answer = collisions.find_intersection_points(sphere_list,ray)
   distance = []
   if answer == []:
      print 255 , "\n" , 255 , "\n" , 255
 
   else:
      for i in answer:
         distance.append(vector_math.length_vector(vector_math.vector_from_to(i[1],ray.pt)))
      intersect = answer[distance.index(min(distance))]
      sphere = intersect[0]
      N = vector_math.normalize_vector(vector_math.vector_from_to(sphere.center, intersect[1]))
      P = vector_math.translate_point(intersect[1], vector_math.scale_vector(N,0.01))
      L = vector_math.normalize_vector(vector_math.vector_from_to(P, light.pt))
      Dot2 = vector_math.dot_vector(N,L)
      Ray2 = data.Ray(P,L)
      light_intersect = collisions.find_intersection_points(sphere_list,Ray2)
      light_intersect_point = []
      for i in light_intersect: 
         light_intersect_point.append(i[1])
      light_intersect_distance = [] 
      for i in light_intersect_point:
         light_intersect_distance.append(vector_math.length_vector(vector_math.vector_from_to(i,P)))
      if light_intersect_distance == []:
         blocked = False
      else:         
         blocked = min(light_intersect_distance) < vector_math.length_vector(vector_math.vector_from_to(P,light.pt))
      A = vector_math.dot_vector(N,vector_math.normalize_vector(L)) 
      print_r = sphere.color.r * sphere.finish.ambient * ambi.r
      print_g = sphere.color.g * sphere.finish.ambient * ambi.g
      print_b = sphere.color.b * sphere.finish.ambient * ambi.b
   
      if (Dot2 <= 0) or blocked:
         amb_r = 0
         amb_g = 0
         amb_b = 0
      else: 
         amb_r = (A * light.color.r * sphere.color.r * sphere.finish.diffuse)
         amb_g = (A * light.color.g * sphere.color.g * sphere.finish.diffuse)
         amb_b = (A * light.color.b * sphere.color.b * sphere.finish.diffuse)   
      reflection = vector_math.difference_vector(L, vector_math.scale_vector(N,2*Dot2))
      V = vector_math.normalize_vector(vector_math.vector_from_to(eye_point,P))
      spec_int = vector_math.dot_vector(reflection,V)
      if spec_int > 0:
         spec_con_r = light.color.r * sphere.finish.specular * (spec_int ** (1 / sphere.finish.roughness))
         spec_con_g = light.color.g * sphere.finish.specular * (spec_int ** (1 / sphere.finish.roughness))
         spec_con_b = light.color.b * sphere.finish.specular * (spec_int ** (1 / sphere.finish.roughness))
      else:
         spec_con_r = 0
         spec_con_g = 0
         spec_con_b = 0
      total_r = 255 * (amb_r + print_r + spec_con_r)
      total_g = 255 * (amb_g + print_g + spec_con_g)
      total_b = 255 * (amb_b + print_b + spec_con_b)
      if total_r > 255:
         final_r = 255
      else:
         final_r = total_r
      if total_g > 255:
         final_g = 255
      else:
         final_g = total_g
      if total_b > 255:
         final_b = 255
      else:
         final_b = total_b
  
      print final_r, "\n", final_g, "\n", final_b


def cast_all_rays(min_x, max_x, min_y, max_y, width, height, eye_point, sphere_list,ambi,light):
   print "P3"
   print width, height
   print 255

   for y in range(height):
      point_y = max_y - ((max_y - min_y) / float(height)) * y
      for x in range(width):
         point_x = min_x + ((max_x - min_x) / float(width)) * x          
         cast_ray(data.Ray(eye_point, vector_math.vector_from_to (eye_point, data.Point(point_x,point_y,0))), sphere_list,ambi,light,eye_point)
 
