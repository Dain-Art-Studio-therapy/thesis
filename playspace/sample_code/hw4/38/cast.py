#cast
import data
import collisions
import math
import vector_math
from vector_math import scale_vector, dot_vector, length_vector
from vector_math import normalize_vector, difference_point
from vector_math import difference_vector, translate_point
from vector_math import vector_from_to


def distance_between_points(point1, point2):
  d = ((point1.x-point2.x)**2+(point1.y-point2.y)**2+
         (point1.z-point2.z)**2)**0.5
  return d

def closest_point_index(point_list, eye_point):
  mindex = 0
  for p in range(len((point_list))):
    if (distance_between_points(point_list[p], eye_point)<=
     distance_between_points(point_list[mindex], eye_point)):
      mindex = p
  return mindex





def final_color_nolight(sphere, ambient):
  f = data.Color(0, 0, 0)
  f.r = sphere.color.r * ambient.r * sphere.finish.ambient
  f.g = sphere.color.g * ambient.g * sphere.finish.ambient
  f.b = sphere.color.b * ambient.b * sphere.finish.ambient
  return f

def final_color(sphere, ambient, light, ipoint, sphere_list,
                dot, eye_point):
  s = sphere_obscure(ipoint, sphere, light.point, sphere_list)
  if s == True:
    t = data.Color(0.0, 0.0, 0.0)
    q = light_color_contrib(light, sphere, dot, ipoint, eye_point)
    o = spec_color_contrib(light, sphere, ipoint, eye_point)
    y = final_color_nolight(sphere, ambient)
    t.r = q.r + o.r + y.r
    t.g = q.g + o.g + y.g
    t.b = q.b + o.b + y.b
    return t
  elif s == False:
    return final_color_nolight(sphere, ambient)
  
def light_color_contrib(light, sphere, dot, ipoint, eye_point):
  f = data.Color(0.0, 0.0, 0.0)
  f.r += float(dot * light.color.r * sphere.color.r * sphere.finish.diffuse)
  f.g += float(dot * light.color.g * sphere.color.g * sphere.finish.diffuse)
  f.b += float(dot * light.color.b * sphere.color.b * sphere.finish.diffuse)
  return f

def spec_color_contrib(light, sphere, ipoint, eye_point):
  o = data.Color(0.0, 0.0, 0.0)
  o.r += spec_int_color(light.color.r, sphere.finish.specular,
         sphere.finish.roughness, specular_intensity(ipoint, sphere,
         light.point, eye_point))
  o.g += spec_int_color(light.color.g, sphere.finish.specular,
         sphere.finish.roughness, specular_intensity(ipoint, sphere,
         light.point, eye_point))
  o.b += spec_int_color(light.color.b, sphere.finish.specular,
         sphere.finish.roughness, specular_intensity(ipoint, sphere,
         light.point, eye_point))
  return o



def sphere_normal(point, sphere):
  return collisions.sphere_normal_at_point(sphere, point)

def vector_to_pz(point, sphere):
  return scale_vector(sphere_normal(point, sphere), 0.01)

def find_pz(point, sphere):
  v = vector_to_pz(point, sphere)
  return translate_point(point, v)

def vector_pz_to_light(point, sphere, light_point):
  pz = find_pz(point, sphere)
  return normalize_vector(vector_from_to(pz, light_point))


def dot_product_pz(point, sphere, light_point):
  v1 = sphere_normal(point, sphere)
  v2 = vector_pz_to_light(point, sphere, light_point)
  dot = dot_vector(v1, v2)
  return dot

def sphere_obscure(point, sphere, light_point, sphere_list):
  pz = find_pz(point, sphere)
  if dot_product_pz(point, sphere, light_point)<=0.0:
    return False
  else:
    r = data.Ray(pz, vector_pz_to_light(point, sphere, light_point))
    f = collisions.find_intersection_points(sphere_list, r)
    if f == []:
      return True
    else:
      return False



def reflection_vector(ipoint, sphere, light_point):
  v1 = vector_pz_to_light(ipoint, sphere, light_point)
  dt = dot_product_pz(ipoint, sphere, light_point)
  n = sphere_normal(ipoint, sphere)
  rv = normalize_vector(difference_vector(v1, scale_vector(n, (2*dt))))
  return rv

def specular_intensity(point, sphere, light_point, eye_point):
  rv = reflection_vector(point, sphere, light_point)
  vd = vector_pz_to_light(eye_point, sphere, point)
  dt = dot_vector(rv, vd)
  return dt

def spec_int_color(light_component, sphere_specular,
                    sphere_roughness, spec_inten):
  if spec_inten > 0.0:
    return light_component*sphere_specular*spec_inten**(1/float(sphere_roughness))
  else: return 0.0





def cast_ray(ray, sphere_list, ambient_color, light, eye_point):
  f = collisions.find_intersection_points(sphere_list, ray)
  if f == []:
    return data.Color(1.0, 1.0, 1.0)
  else: 
    n=[]
    for s in f:
      n.append(s[1])
    i = closest_point_index(n, ray.pt)
    return final_color(f[i][0], ambient_color, light, n[i], sphere_list,
                      dot_product_pz(n[i], f[i][0], light.point), eye_point)
    

def casted_rays_list(min_x, max_x, min_y, max_y,
            width, height, eye_point):
  dx = (max_x - min_x)/ float(width)
  dy = (max_y - min_y)/ float(height)

  viewed_points = []
  for h in range(height):
    for w in range(width):
      x = float(min_x + dx*w)
      y = float(max_y - dy*h)
      viewed_points.append(data.Point(x, y, 0.0))

  return [data.Ray(eye_point, 
           vector_math.difference_point(v, eye_point))
           for v in viewed_points]

def cast_all_rays(min_x, max_x, min_y, max_y, width,
            height, eye_point, sphere_list, ambient_color, light):

  print 'P3'
  print width, height
  print 255

  ray_list = casted_rays_list(min_x, max_x, min_y, max_y,
            width, height, eye_point)

  for r in ray_list:
    c = cast_ray(r, sphere_list, ambient_color, light, eye_point)
    k = int(255*c.r)
    g = int(255*c.g)
    b = int(255*c.b)
    if k>255:
      k = 255
    elif g > 255:
      g = 255
    elif b > 255:
      b=255
    print k, g, b
