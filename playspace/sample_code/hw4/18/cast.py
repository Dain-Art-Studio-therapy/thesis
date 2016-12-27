from collisions import *
from data import *
from vector_math import *

maxColor = 255


def cast_ray(ray, sphere_list, ambient, light, eyepos):
   ntrSctns = find_intersection_points(sphere_list, ray)

   if ntrSctns != []:
      # closestIndex checks for the closest sphere that the ray hits
      closestIndex = find_closest_intersection_index(ray, ntrSctns)

      # Values mostly used to compute light diffusion
      N = sphere_normal_at_point(ntrSctns[closestIndex][0], 
         ntrSctns[closestIndex][1])
      pointE = compute_point_epsilon(ntrSctns[closestIndex][1], N)
      lDir = normalize_vector(vector_from_to(pointE, light.pt))
      dotLDirandN = dot_vector(lDir, N)
      s = ntrSctns[closestIndex][0]
      
      # Values used to compute specular light. There is not a separate func
      # used to calculate specIntens because I figured that I did not need to
      # calculate it multiple times.
      reflectV = difference_vector(lDir, scale_vector(N, 2 * dotLDirandN))
      viewDir = normalize_vector(vector_from_to(eyepos, pointE))
      specIntens = dot_vector(reflectV, viewDir)
      specLightContr = compute_spec_light(light.color, s.finish.specular, 
         specIntens, s.finish.roughness) # specLightContr is Color(0,0,0) if
         # specIntens <= 0. This if statement is in the compute_spec_light func

      if dotLDirandN <= 0:    
         return handle_lighting(s.color, s.finish, ambient, Color(0,0,0),
               specLightContr)
               
      else:
         lightNtrSctns = find_intersection_points(sphere_list, Ray(pointE, 
            lDir))
      
         if lightNtrSctns != []:
            # closestNtr here relates to the intersection of the ray from 
            # pointE to the light source with the closest sphere
            closestNtr = find_closest_intersection_index(Ray(pointE, lDir), 
               lightNtrSctns)
            if (pseudo_dist(lightNtrSctns[closestNtr][1], pointE) < 
               pseudo_dist(pointE, light.pt)):
               return handle_lighting(s.color, s.finish, ambient, Color(0,0,0), 
                  specLightContr)
      
         else:
            return handle_lighting(s.color, s.finish, ambient,
               calculate_diffused_light(dotLDirandN, light.color, s.color, 
               s.finish.diffuse), specLightContr)

   else: 
      return Color(1.0,1.0,1.0)  # return white


def cast_all_rays(min_x, max_x, min_y, max_y, width, height, eye_point, 
   sphere_list, ambient, light):
   print "P3"
   print width , height
   print maxColor
   xIncrement = (max_x - min_x) / float(width)
   yIncrement = (max_y - min_y) / float(height)

   for j in range(height):
      for i in range(width):
         displayColor = cast_ray(Ray(eye_point, vector_from_to(eye_point, 
            Point(min_x + xIncrement * i, max_y - yIncrement * j, 0))), 
            sphere_list, ambient, light, eye_point) 
         print min(int(maxColor * displayColor.r), 255) , min(255,int(maxColor 
            * displayColor.g)), 
         print min(255, int(maxColor * displayColor.b)) ,
      print "" # this is printed at the end of each line so that the next row 
               # goes on the next line


def handle_lighting(sColor, sFinish, ambient, diffuseLight, specLight):
   return Color(sColor.r * sFinish.ambient * ambient.r + diffuseLight.r + 
      specLight.r, sColor.g * sFinish.ambient * ambient.g + diffuseLight.g +
      specLight.g, sColor.b * sFinish.ambient * ambient.b + diffuseLight.b + 
      specLight.b)


def find_closest_intersection_index(ray, ntrSctns):
   closestIndex = 0
   for i in range(1, len(ntrSctns)):
      if (pseudo_dist(ray.pt, ntrSctns[i][1]) <
         pseudo_dist(ray.pt, ntrSctns[closestIndex][1])):
         closestIndex = i
   return closestIndex


def compute_point_epsilon(point, normalV):
   return translate_point(point, scale_vector(normalV, .01))

# Computes the color of the diffused light
def calculate_diffused_light(dotLandN, lColor, sColor, sFinishDiffuse):
   return Color(dotLandN * lColor.r * sColor.r * sFinishDiffuse, dotLandN *
      lColor.g * sColor.g * sFinishDiffuse, dotLandN * lColor.b * sColor.b *
      sFinishDiffuse)

# Pseudo dist is used so that I can cut down on math.sqrt calls
def pseudo_dist(pt1, pt2):
   return (pt2.x - pt1.x) ** 2 + (pt2.y - pt1.y) ** 2 + (pt2.z - pt1.z) ** 2


# Computes the color of the specular light. If the specular Intensity is not 
# positive then there is no specLight color and the func returns a black color
def compute_spec_light(lColor, sFinishSpec, specIntens, sFinishRough):
   if specIntens > 0:
      return Color(lColor.r * sFinishSpec * specIntens ** (1 / sFinishRough),
         lColor.g * sFinishSpec * specIntens ** (1 / sFinishRough), lColor.b * 
         sFinishSpec * specIntens ** (1 / sFinishRough))
   else: 
      return Color(0,0,0)
