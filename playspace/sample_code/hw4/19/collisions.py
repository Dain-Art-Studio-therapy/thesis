import math
from vector_math import *

"""returns the closest point on the sphere that intersects with the ray"""
def sphere_intersection_point(ray, sphere):
  A = dot_vector(ray.dir, ray.dir)
  raysphere = difference_point(ray.pt, sphere.center)
  B = (2*dot_vector(raysphere, ray.dir))
  C = dot_vector(raysphere, raysphere) - sphere.radius**2
  if B**2-(4*A*C) >=0:
    quadEq1 =(-B+math.sqrt(B**2-4*A*C))/(2*A)
    quadEq2 =(-B-math.sqrt(B**2-4*A*C))/(2*A)
    if quadEq1 == quadEq2:
      if quadEq1 >=0:
        t = quadEq1
        return Point(ray.pt.x + t* ray.dir.x,ray.pt.y + t* ray.dir.y,ray.pt.z + t* ray.dir.z)
    elif quadEq1>=0 and quadEq2>=0:
      t= min(quadEq1, quadEq2)
      return Point(ray.pt.x + t* ray.dir.x,ray.pt.y + t* ray.dir.y,ray.pt.z + t* ray.dir.z)
    elif quadEq1<0 and quadEq2<0:
      return None
    elif quadEq1>=0 and quadEq2<0:
      t= quadEq1
      return Point(ray.pt.x + t* ray.dir.x,ray.pt.y + t* ray.dir.y,ray.pt.z + t* ray.dir.z)
    elif quadEq1<0 and quadEq2>=0:
      t= quadEq2
      return Point(ray.pt.x + t* ray.dir.x,ray.pt.y + t* ray.dir.y,ray.pt.z + t* ray.dir.z)
  else:
    return None

""" returns a list of tuples containing (the_sphere, the_intersection_point)"""
def find_intersection_points(sphere_list, ray):
  l =[]
  if sphere_list == []:
    return None
  for e in sphere_list:
    if sphere_intersection_point(ray,e) != None:
      l.append((e,sphere_intersection_point(ray,e)))
  return l

"""returns a single tuple containing (the_closest_sphere_to_the_ray, the_intersection_point"""
def find_closest_sphere(sphere_list, ray):
  intpoints= find_intersection_points(sphere_list, ray)
  if intpoints == []:
    return None
  closest_sphere = 0 
  currentdis = length_to_from(intpoints[0][1], ray.pt)
  for p in range(len(intpoints)):
    if currentdis > length_to_from(intpoints[p][1], ray.pt):
      currentdis = length_to_from(intpoints[p][1], ray.pt)
      closest_sphere = p
  #print intpoints[closest_sphere][0].radius
  return intpoints[closest_sphere]

#test1= find_closest_sphere([Sphere(Point(1,0,0),3,Color(2,2,2)),Sphere(Point(-5,0,0),2,Color(1,1,1))], Ray(Point(-10,0,0), Vector(1,0,0)))  

""" returns a direction vector from sphere's center to point on sphere"""
def sphere_normal_at_point(sphere, point):
  rawvec= vector_from_to(sphere.center, point)
  return normalize_vector(rawvec) 

""" returns a point just off the sphere from a point actually on the sphere"""
def fake_point_translate(sphere, point):
  true_normal= sphere_normal_at_point(sphere, point)
  tiny_normal= scale_vector(true_normal, 0.01)
  fake_point=translate_point(point, tiny_normal)
  return fake_point


def light_normal(fake_point, light):
  lightray = vector_from_to(fake_point, light.pt)
  lightnormal = normalize_vector(lightray)
  return lightnormal

"""returns a diffuse value based of the dot product from the fake_normal_vector and the normal vector from the point to the light"""
def light_diffuse(sphere, true_point, light):
  fake_point = fake_point_translate(sphere, true_point)
  Ldir= light_normal(fake_point, light)
  fake_normal= sphere_normal_at_point(sphere, fake_point)
  diffuse = dot_vector(Ldir, fake_normal)
  return diffuse


def specular_value(eyepoint, true_point, sphere, light, lightdiffuse):
   true_normal= sphere_normal_at_point(sphere, true_point)
   fake_point= fake_point_translate(sphere,true_point)
   Ldir= light_normal(fake_point, light)
   reflectvec= difference_vector(Ldir, scale_vector(true_normal, lightdiffuse*2))
   spectvec= normalize_vector(vector_from_to(eyepoint, fake_point))
   intensity = dot_vector(spectvec, reflectvec)
   return intensity

def specular_shade(specular, sphere, light):
   intensity = specular**(1/sphere.finish.roughness)
   r = intensity*light.color.r*sphere.finish.specular
   g = intensity*light.color.g*sphere.finish.specular
   b = intensity*light.color.b*sphere.finish.specular
   return Color(r,g,b)

#dif1 = light_diffuse(Sphere(Point(5,0,0), 1, Color(1,1,1), 1), Point(6,0,0), Light(Point(0,0,0), Color(1,1,1)))
#print dif1 

def sphere_ambient_finish(sphere, ambientlight):
 r = (sphere.color.r*ambientlight.r)*sphere.finish.ambience
 g = (sphere.color.g*ambientlight.g)*sphere.finish.ambience
 b = (sphere.color.b*ambientlight.b)*sphere.finish.ambience
 return Color(r,g,b)

def sphere_lightpoint(sphere, light, theta):
  #print lightdiffuse
  r=sphere.color.r*light.color.r*sphere.finish.diffuse*theta
  g=sphere.color.g*light.color.g*sphere.finish.diffuse*theta
  b=sphere.color.b*light.color.b*sphere.finish.diffuse*theta
  return Color(r,g,b)

def add_shades(sphereshade, lightshade, specularshade):
  r=sphereshade.r+lightshade.r+specularshade.r
  g=sphereshade.g+lightshade.g+specularshade.g
  b=sphereshade.b+lightshade.b+specularshade.b
  return Color(r,g,b)


def convert_color(color):
  r = int(color.r*255)
  g = int(color.g*255)
  b = int(color.b*255)
  if r>255:
     r=255
  if g>255:
     g=255
  if b>255:
     b=255
  return Color(r,g,b)
