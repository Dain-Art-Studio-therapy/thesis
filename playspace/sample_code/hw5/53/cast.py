import math
import data
import collisions
import vector_math
import sys

def cast_ray(ray, sphere_list, colorambient, light, eye_point):

   interlist = find_points(sphere_list, ray)
   nearinfo = get_nearest_point(interlist, ray)
   N = norm_vector_at_sphere(nearinfo)
   Peps = get_p_epsilon(nearinfo, N)
   Ldir = vector_math.normalize_vector(vector_math.vector_from_to(Peps, light.point))
   LdotN = vector_math.dot_vector(N, Ldir)
   rayLdir = data.Ray(Peps, Ldir)
   diffuse = check_diffuse(sphere_list, nearinfo, rayLdir, Peps, light, LdotN)
   specintense = specular_intensity(N, Ldir, eye_point, Peps, LdotN)
   finalspec = final_specular(specintense, nearinfo)
   spherespec = sphere_specular(nearinfo, specintense)
   ambient = nearinfo[0].finish.ambient
   color = nearinfo[0].color
   ambientcolor = ambient_color(color, colorambient, ambient)
   diffusecolor = diffuse_color(color, LdotN, diffuse, light)
   specularcolor = specular_color(light, spherespec, finalspec)
   finalcolor = final_color(ambientcolor, diffusecolor, specularcolor)

   return finalcolor
   
  

def cast_all_rays(min_x, max_x, min_y, max_y, width, height, eye_point, sphere_list, ambientlight, light):
   finalfile = open('sphere_test.ppm', 'w')
   deltax = (max_x - min_x) / float(width)
   deltay = (max_y - min_y) / float(height)
   xcord = min_x
   ycord = max_y
   print >> finalfile, 'P3'
   print >> finalfile, width, height
   print >> finalfile, 255 

   for y in range(int(height)):


      for x in range(int(width)):

         currentcord = data.Point(xcord, ycord, 0)
         eyevec = vector_math.vector_from_to(eye_point, currentcord)
         rayeye = data.Ray(eye_point, eyevec)
         checkpoint = cast_ray(rayeye, sphere_list, ambientlight, light, eye_point)
         
         
         print >> finalfile, min(int(checkpoint.r * 255), 255), min(int(checkpoint.g * 255), 255),  min(int(checkpoint.b * 255), 255)
         xcord = xcord + deltax

      ycord = ycord - deltay

      xcord = min_x
                 

def find_points(sphere_list, ray):

   interlist = collisions.find_intersection_points(sphere_list, ray)
   
   if interlist == []:
      return data.Color(1.0, 1.0, 1.0)
   return interlist

def get_nearest_point(interlist, ray):
   smallest = 0
   nearest = vector_math.length_vector(vector_math.difference_point(ray.pt, interlist[0][1]))
   
   for (x, y) in enumerate(interlist):
      
      if nearest >= vector_math.length_vector(vector_math.difference_point(ray.pt, y[1])):
         
         smallest = x
         nearest = vector_math.length_vector(vector_math.difference_point(ray.pt, y[1]))
  
   nearinfo = interlist[smallest]
   return nearinfo

def norm_vector_at_sphere(nearinfo):
   N = collisions.sphere_normal_at_point(nearinfo[0], nearinfo[1])
   return N

def get_p_epsilon(nearinfo, N):
   Peps = vector_math.translate_point(nearinfo[1], vector_math.scale_vector(N, .01))
   return Peps


def check_diffuse(sphere_list, nearinfo, rayLdir, Peps, light, LdotN):
   diffuse = nearinfo[0].finish.diffuse
  
   for i in sphere_list:
      checkPeps = collisions.sphere_intersection_point(rayLdir, i)
      Peps2sphere = vector_math.vector_from_to(i.center, Peps)
      Peps2light = vector_math.vector_from_to(light.point, Peps)
      P2smag = vector_math.length_vector(Peps2sphere)
      P2lmag = vector_math.length_vector(Peps2light)
      
      
      if (checkPeps != None and (P2smag < P2lmag)) or LdotN <= 0:
      
          diffuse = 0

   return diffuse

def specular_intensity(N, Ldir, eye_point, Peps, LdotN):
   
   Ldot = LdotN * 2
   Normedit = vector_math.scale_vector(N, Ldot)
   reflecvec = vector_math.difference_vector(Ldir, Normedit)
   Vdir = vector_math.normalize_vector(vector_math.vector_from_to(eye_point, Peps))
   specintense = vector_math.dot_vector(reflecvec, Vdir)
   return specintense

def final_specular(specintense, nearinfo):
   finalspec = (specintense) ** (1 / nearinfo[0].finish.roughness)
   return finalspec

def sphere_specular(nearinfo, specintense):
   spherespec = nearinfo[0].finish.specular
   if specintense <= 0:
      spherespec = 0
   return spherespec

def ambient_color(color, colorambient, ambient):

   ambientcolor = data.Color(color.r * colorambient.r * ambient, color.g * colorambient.g * ambient, color.b * colorambient.b * ambient)
   return ambientcolor

def diffuse_color(color, LdotN, diffuse, light):

   diffusecolor = data.Color(color.r * light.color.r * LdotN * diffuse, color.g * light.color.g * LdotN * diffuse, color.b * light.color.b * LdotN * diffuse)
   return diffusecolor

def specular_color(light, spherespec, finalspec):

   specularcolor = data.Color(light.color.r * spherespec * finalspec, light.color.g * spherespec * finalspec, light.color.b * spherespec * finalspec)
   return specularcolor

def final_color(ambientcolor, diffusecolor, specularcolor):
   finalcolor = data.Color(ambientcolor.r + diffusecolor.r + specularcolor.r, ambientcolor.g + diffusecolor.g + specularcolor.g, ambientcolor.b + diffusecolor.b + specularcolor.b)
   return finalcolor
                     
