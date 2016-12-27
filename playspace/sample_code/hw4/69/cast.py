from collisions import *
from vector_math import *
from data import *

def closest_sphere(sphere_tuple, eye):
   x = point_distance(eye, sphere_tuple[0][1])
   i = sphere_tuple[0]
   for eachtuple in sphere_tuple:
      shortest_dist = point_distance(eye, eachtuple[1])
      if shortest_dist < x:
         x = shortest_dist
         i = eachtuple
   return i[0]

def color_scale(color_comp):
   if color_comp > 1.0:
      return 255
   else:
      return int(color_comp * 255)

def cast_ray(ray, sphere_list, amcolor, light, eyept):
   pts = find_intersection_points(sphere_list, ray)
   if pts == []:
      return Color(1.0, 1.0, 1.0)
   else:
      s = closest_sphere(pts, ray.pt)

      inpt = sphere_intersection_point(ray, s) #point
      Nor = sphere_normal_at_point(s, inpt) #vector
      scaled_normal = scale_vector(Nor, 0.01) #vector
      pe = translate_point(inpt, scaled_normal) #pt
      Ldir = vector_from_to(pe, light.pt) #vector  
      Ldir_normalized = normalize_vector(Ldir) #vector
      d_prod = dot_vector(Nor, Ldir_normalized) #number

      reflec_vec = (difference_vector(Ldir_normalized, 
      (scale_vector(Nor, d_prod * 2)))) #vector
      Vdir = normalize_vector(vector_from_to(eyept, pe)) #vector
      spec_inten = dot_vector(reflec_vec, Vdir) #number

      if d_prod <= 0:
         a_contribution = 0
      else:
         a_contribution = d_prod

      if spec_inten > 0:
         spec_contr = spec_inten**(1/s.finish.roughness)
      else:
         spec_contr = 0.0

      number_of_points = (len(find_intersection_points(sphere_list, Ray(light.pt,
       vector_from_to(light.pt, inpt)))))
      if number_of_points >= 2:
         ##make shadow
         obstruction = 0.0
      else:
         ##basically don't do anything
         obstruction = 1.0

      Rvalue = ((s.color.R * s.finish.ambient * amcolor.R) + 
         (a_contribution * light.color.R * s.color.R * 
            s.finish.diffuse * obstruction) + 
         (light.color.R * s.finish.specular * spec_contr))

      Gvalue = ((s.color.G * s.finish.ambient * amcolor.G) + (a_contribution * 
         light.color.G * s.color.G * s.finish.diffuse * obstruction) + 
      (light.color.G * s.finish.specular * spec_contr))

      Bvalue = ((s.color.B * s.finish.ambient * amcolor.B) + (a_contribution * 
         light.color.B * s.color.B * s.finish.diffuse * obstruction) + 
      (light.color.B * s.finish.specular * spec_contr))

      return Color(Rvalue, Gvalue, Bvalue)

def cast_all_rays(min_x, max_x, min_y, max_y, width, height, eye_point, 
   sphere_list, amcolor, light):

   deltax = (max_x - min_x)/float(width)
   deltay = (max_y - min_y)/float(height)
   pixel = Point(min_x, max_y, 0)

   ylist = range(height)
   xlist = range(width)

   for yitem in ylist:
      for xitem in xlist:
         pixel = Point(min_x + (xitem * deltax), max_y - (yitem * deltay), 0)
         los = cast_ray(Ray(eye_point, vector_from_to(eye_point, pixel)), 
            sphere_list, amcolor, light, eye_point)
         if los == Color(1.0, 1.0, 1.0):
            print 255, 255, 255
         else:
            print color_scale(los.R), color_scale(los.G), color_scale(los.B)
