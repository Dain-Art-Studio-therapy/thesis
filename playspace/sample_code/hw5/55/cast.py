from collisions import *
from data import *
'''all helper functions contained in collisions.py'''
White_Default= Color(1,1,1)

def cast_ray(eyeray, sphere_list, ambient_light, lightsource, eye_point):
  closest_sphere =  find_closest_sphere(sphere_list, eyeray)
  if closest_sphere != None:
    point = closest_sphere[1]
    sphere= closest_sphere[0]
    true_normal= sphere_normal_at_point(sphere, point)
    fake_point= translate_point(point, scale_vector(true_normal, 0.01))
    lightray = Ray(lightsource.pt, normalize_vector(vector_from_to(fake_point, lightsource.pt)))
    #light_visible = compare_sphere_to_light(sphere_list, lightray, lightsource)
    #print diffuse
    sphereshade= sphere_ambient_finish(sphere, ambient_light)
    
    diffuse_and_intensity= sphere_diffuse_and_intensity(sphere, point, lightsource, sphere_list, eye_point)
    return add_shades(sphereshade, diffuse_and_intensity)
  else:
    return White_Default
#test1= cast_ray(Ray(Point(0,0,0), Vector(5,0,0)), Ray(Point(0,0,0), Vector(10,0,0)), [Sphere(Point(11,0,0),2,Color(220,130,44), 0.5), Sphere(Point(5,0,0),1,Color(134,234,23), 0.2)], Color(1.0,1.0,1.0), Light(Point(0,0,0), Color(1.2,1.3,1.1)))

def sphere_diffuse_and_intensity(sphere, point, lightsource, sphere_list, eye_point):
  fake_point = fake_point_translate(sphere, point)
  temp = light_diffuse(sphere, point, fake_point, lightsource)
  lightdiffuse= temp[0]
  Ldir= temp[1]
  if hidden_sphere(sphere_list, point, lightsource, Ldir)== False:
    if lightdiffuse <= 0:
      return Color(0,0,0)
    if find_closest_sphere(sphere_list, Ray(fake_point, Ldir)) != None:
      return Color(0,0,0)
    lightshade= sphere_lightpoint(sphere, lightsource, lightdiffuse)
    intensity= specular_value(eye_point, point, sphere, lightsource, lightdiffuse)
    if intensity > 0:
      specularshade = specular_shade(intensity, sphere, lightsource)
      finalshade=add_shades(lightshade, specularshade)
    else:
      finalshade= lightshade
    return finalshade
  return Color(0,0,0)

def write_to_file(width, height, pixel):
   with open('image.ppm', 'w') as file:
      file.write('P3\n'+str(width)+' '+str(height)+'\n255\n')
      file.write(''.join(pixel))

'''def percent_complete(var, height, temp):
  percent= var*100/height
  if percent>4 and percent<6 and check==0:
    print 'The program is: '+str(percent)+'% done'
  if percent>9 and percent<11 and check==1:
    print 'The program is: '+str(percent)+'% done'
  if percent>24 and percent<26 and check==2:
    print 'The program is: '+str(percent)+'% done'
  if percent>49 and percent<51 and check==3:
    print 'The program is: '+str(percent)+'% done'
  if percent>74 and percent<76 and check==4:
    print 'The program is: '+str(percent)+'% done'
  if percent>89 and percent<91 and check==5:
    print 'The program is: '+str(percent)+'% done'''
    
def cast_all_rays(min_x, max_x, min_y, max_y,
                  width, height, eye_point, sphere_list, ambient_light, lightsource):
   pixels= []
   current_x= min_x
   current_y= max_y
   #rawpercent=0
   step_x = (max_x-min_x)/float(width)
   step_y = (max_y-min_y)/float(height)
   while current_y>min_y:
      current_x = min_x
      #rawpercent+=1
      #percent_complete(rawpercent, height, check)
      while current_x<max_x:
      #print current_x,current_y
         currentVector= vector_from_to(eye_point, Point(current_x, current_y,0))
         currentray = Ray(eye_point, currentVector)
         currentcolor = cast_ray(currentray, sphere_list, ambient_light, lightsource, eye_point)
      #print currentcolor.r
         color= convert_color(currentcolor)
         pixels.append(str(color.r)+' '+str(color.g)+' '+str(color.b)+'\n')
         current_x += step_x
      current_y= current_y -step_y 
   write_to_file(int(width), int(height), pixels)

  
#test1= cast_all_rays(-10,10,-10,10,100,80,Point(0,0,10),[Sphere(Point(1,1,0),2,Color(220,130,44), 0.4), Sphere(Point(5,5,0),2,Color(134,234,23), 0.5)],
                     #Color(1,1,1), Light(Point(0,10,14), Color(1.5,1.5,1.5)))

