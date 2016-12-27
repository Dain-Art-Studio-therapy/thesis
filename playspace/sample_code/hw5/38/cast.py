import data
import vector_math
import collisions
import sys
from sys import *

def cast_ray(ray, sphere_list, color, light):
   v = collisions.find_intersection_points(sphere_list, ray)
   
   if v <= []:
      return data.Color(1.0, 1.0, 1.0)
   else:
      first = vector_math.length_vector(vector_math.vector_from_to(ray.pt, v[0][1]))
       
      sh = v[0][0]
      for i in v:
         vect = (vector_math.vector_from_to(ray.pt, i[1]))
         other = vector_math.length_vector(vect)
         if (first > other):
            first = other
      sh = i[0]
      firstp = i[1]
      n = collisions.sphere_normal_at_point(sh, firstp) 
      scale = vector_math.scale_vector(n, 0.01)
      #short = length * 0.01
      pe = vector_math.translate_point(firstp, scale)
      lightpe = vector_math.vector_from_to(light.pt, pe)
      if (collisions.find_intersection_points(sphere_list, lightpe) == []):
         somevalue = 0
      else:
         somevalue = 1

      ldir = vector_math.normalize_vector(lightpe)
      dot = vector_math.dot_product(n, ldir)
      ray = data.Ray(pe, ldir)
      if (dot >= 0):
         dot = 0
        
      diffuse = dot * somevalue * sh.finish.diffuse  
      return data.Color((sh.color.r * sh.finish.ambient * color.r), (sh.color.g * sh.finish.ambient * color.g), (sh.color.b * sh.finish.ambient * color.b))
		 
def cast_all_rays(min_x, max_x, min_y, max_y, width, height, eye_point,sphere_list, color, light):
    hpixels = (max_y - min_y)/float(height)
    wpixels = (max_x - min_x)/float(width)
    for y in range(height):
       for x in range(width):
           xpos = min_x + wpixels * x
	   ypos = max_y - hpixels * y
	   ray = data.Ray(eye_point,vector_math.vector_from_to(eye_point,data.Point(xpos,ypos,0)))
    result = (cast_ray(ray, sphere_list, color, light)) 
    f = open('image.ppm', 'rb')
    prt = f.write((int(255 * result.r), int(255 * result.g), int(255 * result.b)))
    
    return f
    
    #print (int(255 * result.r), int(255 * result.g), int(255 * result.b))
    
def openfile():
   with open('image.ppm', 'rb') as f:
      data












	   
