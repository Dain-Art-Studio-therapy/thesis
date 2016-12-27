from vector_math import *
from collisions import *
from data import *

#aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa

#finds the distance between 2 pts
def dist(pt1, pt2):
   return length_vector(difference_point(pt1, pt2))

def LdotN(N, Ldir):
   return dot_vector(N, Ldir)

#calculates the diffuse contribution to the point's color
def diffuse_check(sphere, light, N, Ldir):
   a = LdotN(N, Ldir)
   red = a *  light.color.r * sphere.color.r * sphere.finish.diffuse
   green = a *  light.color.g * sphere.color.g * sphere.finish.diffuse
   blue = a *  light.color.b * sphere.color.b * sphere.finish.diffuse
   return Color(red, green, blue)

#checks if any sphere in on the path from pe to the light's position
#False - nothing is in the way
#True - a sphere is in the way
def light_check(sphere_list, pe, Ldir, light):
   ray = Ray(pe, Ldir)
   newlist = find_intersection_points(sphere_list, ray)
   is_true = False
   if newlist != []:
      for n in newlist:
         if dist(n[1], pe) < dist(pe, light.pt):
            is_true = True
         else:
            is_true = False
   return is_true

#checks if the light is visible from point pe and returns the diffuse value
def diffuse(sphere_list, sphere, intersect, light, pe, N, Ldir):
   is_vis = dot_vector(N, Ldir)
   if is_vis > 0:
      if light_check(sphere_list, pe, Ldir, light) == False:
         return diffuse_check(sphere, light, N, Ldir)
      else:
         return Color(0.0, 0.0, 0.0)
   else:
      return Color(0.0, 0.0, 0.0)

def specular_intensity(sphere, light, eye_pt, pe, N, Ldir):
   LN = dot_vector(N, Ldir)
   reflection = difference_vector(Ldir, scale_vector(N, 2.0 * LN))
   Vdir = normalize_vector(vector_from_to(eye_pt, pe))
   spec_inten = dot_vector(reflection, Vdir)
   if spec_inten > 0:
      new_spec = spec_inten ** (1 / sphere.finish.roughness)
      red = LN * light.color.r * sphere.finish.specular * new_spec
      green = LN * light.color.g * sphere.finish.specular * new_spec
      blue = LN * light.color.b * sphere.finish.specular * new_spec
      return Color(red, green, blue)
   else:
      return Color(0.0, 0.0, 0.0)     

def cast_ray(ray, sphere_list, color, light, eye_pt):
   newlist = find_intersection_points(sphere_list, ray)
   if newlist == []:
      return Color(1.0, 1.0, 1.0)
   else:
      mindex = 0
      for i in  range(1, len(newlist)):
         if (length_vector(difference_point(newlist[mindex][1], ray.pt)) >
            length_vector(difference_point(newlist[i][1], ray.pt))):
            mindex = i
      N = sphere_normal_at_point(newlist[mindex][0], newlist[mindex][1])
      scaled_normal = scale_vector(N, 0.01)
      pe = translate_point(newlist[mindex][1], scaled_normal)
      Ldir = normalize_vector(vector_from_to(pe, light.pt))
      color1 = newlist[mindex][0].color
      s = specular_intensity(newlist[mindex][0], light, eye_pt, pe, N, Ldir)
      diffuse_value = diffuse(sphere_list, newlist[mindex][0], 
                              newlist[mindex][1], light, pe, N, Ldir)
      newcolor = Color(color1.r * color.r * 
                       newlist[mindex][0].finish.ambient + diffuse_value.r 
                       + s.r, color1.g * color.g * newlist[mindex]
                       [0].finish.ambient + diffuse_value.g + s.g,color1.b * 
                       color.b * newlist[mindex][0].finish.ambient + 
                       diffuse_value.b + s.b)
      return newcolor

def cast_all_rays(min_x, max_x, min_y, max_y, width, height, eye_point, 
                  sphere_list, color, light):
   print 'P3'
   print width, " ", height
   print 255
   x_change = (max_x - min_x) / float(width)
   y_change = (max_y - min_y) / float(height)
   for y in range(height):
      for x in range(width):
         x_pt = min_x + x * x_change
         y_pt = max_y - y * y_change
         dir = vector_from_to(eye_point, Point(x_pt, y_pt, 0))
         colors = cast_ray(Ray(eye_point, dir), sphere_list, color, light,
                           eye_point)
         red = int(colors.r * 255)
         green = int(colors.g * 255)
         blue = int(colors.b * 255)
         print red, green, blue
