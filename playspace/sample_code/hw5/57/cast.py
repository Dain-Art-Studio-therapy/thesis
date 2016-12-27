from collisions import *
from data import *
from vector_math import *

def cast_ray(ray,sphere_list,color,light,point):
   list = find_intersection_points(sphere_list,ray)
   if list != []:
      mindex = 0
      for i in range(1,len(list)):
         if (length_vector(vector_from_to(ray.pt,list[mindex][1])) >
            length_vector(vector_from_to(ray.pt,list[i][1]))):
            mindex = i
      d = diffuse_contribution(ray,sphere_list,color,light)
      s = specular_contribution(ray,sphere_list,color,light)
      return Color((list[mindex][0].color.r * list[mindex][0].finish.ambient *\
                    color.r) + d.r + s.r,
                   (list[mindex][0].color.g * list[mindex][0].finish.ambient *\
                    color.g) + d.g + s.g,
                   (list[mindex][0].color.b * list[mindex][0].finish.ambient *\
                    color.b) + d.b + s.b)
   else:
      return Color(1.0,1.0,1.0)

   
def cast_all_rays(min_x,max_x,min_y,max_y,width,height,eye_point,sphere_list,
                  color,light):
   change_x = (max_x - min_x) / float(width)
   change_y = (max_y - min_y) / float(height)
   output = open("image.ppm", 'w')
   output.write("P3 ")
   output.write(str(width)+ " " + str(height))
   output.write(" 255 ")
   for j in range(0,height):
      for i in range(0,width):
         x = min_x + change_x * i
         y = max_y - change_y * j
         z = 0        
         point = Point(x,y,z)
         v = vector_from_to(eye_point,point)
         r = Ray(eye_point,v)
         c = cast_ray(r,sphere_list,Color(1.0,1.0,1.0),Light(Point(-100.0,100.0,-100.0),Color(1.0,1.0,1.0)),Point(0.0,0.0,-14.0))
         color = scale_color(c,255)
         if color.r > 255:
            color.r = 255
         if color.g > 255:
            color.g = 255
         if color.b > 255:
            color.b = 255
         output.write(str(int(color.r))+" "+str(int(color.g))+" "+str(int(color.b))+" ")


def diffuse_contribution(ray,sphere_list,color,light):
   list = find_intersection_points(sphere_list,ray)
   if list != []:
      mindex = 0
      for i in range(1,len(list)):
         if (length_vector(vector_from_to(ray.pt,list[mindex][1])) > 
            length_vector(vector_from_to(ray.pt,list[i][1]))):
            mindex = i
   N = sphere_normal_at_point(list[mindex][0],list[mindex][1])
   pe = translate_point(list[mindex][1],scale_vector(N,0.01))
   ldir = normalize_vector(vector_from_to(pe,light.pt))
   dp = dot_vector(N,ldir)
   newray = Ray(pe,ldir)
   newlist = find_intersection_points(sphere_list,newray)
   if newlist != []:
      if (length_vector(vector_from_to(pe,light.pt)) >
          length_vector(vector_from_to(pe,newlist[0][1]))):
         return Color(0.0,0.0,0.0)
   else:
      if dp <= 0:
         return Color(0.0,0.0,0.0)
      else:
         return Color(dp * light.color.r * list[mindex][0].color.r * \
                      list[mindex][0].finish.diffuse,
                      dp * light.color.g * list[mindex][0].color.g *\
                      list[mindex][0].finish.diffuse,
                      dp * light.color.b * list[mindex][0].color.b *\
                      list[mindex][0].finish.diffuse)



def specular_contribution(ray,sphere_list,color,light):
  list = find_intersection_points(sphere_list,ray)
  if list != []:
      mindex = 0
      for i in range(1,len(list)):
         if (length_vector(vector_from_to(ray.pt,list[mindex][1])) > 
             length_vector(vector_from_to(ray.pt,list[i][1]))):         
            mindex = i
  N = sphere_normal_at_point(list[mindex][0],list[mindex][1])
  pe = translate_point(list[mindex][1],scale_vector(N,0.01))
  ldir = normalize_vector(vector_from_to(pe,light.pt))
  LdotN = dot_vector(N,ldir)
  newLdotN = 2 * LdotN
  rv = difference_vector(ldir,Vector((newLdotN * N.x),(newLdotN * N.y),
                         (newLdotN * N.z)))
  ep = Point(0.0,0.0,-14.0)
  vdir = normalize_vector(vector_from_to(ep,pe))
  si = dot_vector(rv,vdir)
  if si > 0:
    return Color(light.color.r * list[mindex][0].finish.specular * \
                 (si**(1/list[mindex][0].finish.roughness)),
                 light.color.g * list[mindex][0].finish.specular * \
                 (si**(1/list[mindex][0].finish.roughness)),
                 light.color.b * list[mindex][0].finish.specular * \
                 (si**(1/list[mindex][0].finish.roughness)))     
  else:
     return Color(0.0,0.0,0.0)
