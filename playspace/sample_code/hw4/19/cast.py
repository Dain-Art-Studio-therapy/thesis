from collisions import *
from data import *
'''all helper functions contained in collisions.py'''
def cast_ray(eyeray, sphere_list, ambient_light, lightsource, eye_point):
  if find_closest_sphere(sphere_list, eyeray) != None:
    closest_sphere =  find_closest_sphere(sphere_list, eyeray)
    intersect_point = closest_sphere[1]
    
    lightray = Ray(lightsource.pt, vector_from_to(lightsource.pt, intersect_point))
    
    closest_sphere_to_light = find_closest_sphere(sphere_list, lightray)
    light_intersect_point = closest_sphere_to_light[1]
    
    #print diffuse
    sphereshade= sphere_ambient_finish(closest_sphere[0], ambient_light)
    if intersect_point == light_intersect_point:
      lightdiffuse = light_diffuse(closest_sphere_to_light[0], intersect_point, lightsource)
      if lightdiffuse > 0:
        lightshade= sphere_lightpoint(closest_sphere_to_light[0], lightsource, lightdiffuse)
        intensity= specular_value(eye_point, intersect_point, closest_sphere[0], lightsource, lightdiffuse)
        if intensity >0:
          specularshade = specular_shade(intensity, closest_sphere[0], lightsource)
          finalshade =add_shades(sphereshade, lightshade, specularshade)
        else:
          finalshade = add_shades(sphereshade, lightshade, Color(0,0,0))
      #print finalshade.r
      else:
        #print 'hit'
        finalshade = add_shades(sphereshade, Color(0,0,0), Color(0,0,0))
      #print finalshade.r
    else:
      finalshade =add_shades(sphereshade, Color(0,0,0), Color(0,0,0))
      
    return finalshade 

  else:
    return Color(1,1,1)
#test1= cast_ray(Ray(Point(0,0,0), Vector(5,0,0)), Ray(Point(0,0,0), Vector(10,0,0)), [Sphere(Point(11,0,0),2,Color(220,130,44), 0.5), Sphere(Point(5,0,0),1,Color(134,234,23), 0.2)], Color(1.0,1.0,1.0), Light(Point(0,0,0), Color(1.2,1.3,1.1)))

def cast_all_rays(min_x, max_x, min_y, max_y,
                  width, height, eye_point, sphere_list, ambient_light, lightsource):
  print "P3"
  print width, height
  print 255
  current_x= min_x
  current_y= max_y
  step_x = (max_x-min_x)/float(width)
  step_y = (max_y-min_y)/float(height)
  while current_y>min_y:
    current_x = min_x
    while current_x<max_x:
      #print current_x,current_y
      currentVector= vector_from_to(eye_point, Point(current_x, current_y,0))
      currentray = Ray(eye_point, currentVector)
      currentcolor = cast_ray(currentray, sphere_list, ambient_light, lightsource, eye_point)
      #print currentcolor.r
      color= convert_color(currentcolor)
      print color.r, color.g, color.b
      current_x += step_x
    current_y= current_y -step_y 
  
#test1= cast_all_rays(-10,10,-10,10,100,80,Point(0,0,10),[Sphere(Point(1,1,0),2,Color(220,130,44), 0.4), Sphere(Point(5,5,0),2,Color(134,234,23), 0.5)],
                     #Color(1,1,1), Light(Point(0,10,14), Color(1.5,1.5,1.5)))

