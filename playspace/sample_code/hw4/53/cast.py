import collisions
import vector_math
import data
import math
# part4 works but there is a problem with part5
def cast_ray(ray,sphere_list,color,light,point):
    listing = collisions.find_intersection_point(sphere_list,ray)
    if listing == []:
        return data.Color(1.0,1.0,1.0)
    else:
        mind = 0
        for i in range(1,len(listing)):
            a = vector_math.length_vector(vector_math.difference_vector(ray.pt,listing[i][1]))
            b = vector_math.length_vector(vector_math.difference_vector(ray.pt,listing[mind][1]))
            if a < b:
                mind = i
        diffuse_value = visibility(listing[mind][0], listing[mind][1], light, sphere_list)
        specular_value = specular(ray,listing[mind][0],listing[mind][1],light,sphere_list)
        spheres = listing[mind][0]
        red = spheres.color.r *color.r *spheres.finish.ambient+diffuse_value[0]+ specular_value[0]
        green = spheres.color.g*color.g*spheres.finish.ambient+diffuse_value[1]+ specular_value[1]
        blue = spheres.color.b *color.b*spheres.finish.ambient+diffuse_value[2]+ specular_value[2] 
        Sphere_color = data.Color(red, green, blue)                    
        return Sphere_color
    
def specular(ray,sphere, intersect_pt, light,sphere_list):
    n = collisions.sphere_normal_at_point(sphere,intersect_pt)
    px = vector_math.translate_point(intersect_pt, vector_math.scale_vector(n, 0.01))
    Ldir = vector_math.normalize_vector(vector_math.vector_from_to(px, light.pt))
    dot_product = vector_math.dot_vector(n, Ldir)
    reflection_vector = vector_math.difference_vector(Ldir,vector_math.scale_vector(n,(2 * dot_product)))
    Vdir = vector_math.normalize_vector(vector_math.vector_from_to(ray.pt, light.pt))
    specular_vector_intensity = vector_math.dot_vector(reflection_vector, Vdir)
    listing = collisions.find_intersection_point(sphere_list,ray)
    if specular_vector_intensity > 0:
        diffuse_value = visibility(sphere, intersect_pt, light, sphere_list)
        mind = 0
        for i in range(1,len(listing)):
            a = vector_math.length_vector(vector_math.difference_vector(ray.pt,listing[i][1]))
            b = vector_math.length_vector(vector_math.difference_vector(ray.pt,listing[mind][1]))
            if a < b:
                mind = i
        spheres = listing[mind][0]
        red = light.color.r * spheres.finish.specular * (specular_vector_intensity ** (1/spheres.finish.roughness))
        green = light.color.g * spheres.finish.specular * (specular_vector_intensity ** (1/spheres.finish.roughness))
        blue = light.color.b * spheres.finish.specular * (specular_vector_intensity ** (1/spheres.finish.roughness))
        return (red,green,blue)
    else:
        return (0.0,0.0,0.0)
    
def visibility(sphere, intersect_pt, light, sphere_list):
   n = collisions.sphere_normal_at_point(sphere, intersect_pt)
   px = vector_math.translate_point(intersect_pt, vector_math.scale_vector(n, 0.01))
   Ldir = vector_math.normalize_vector(vector_math.vector_from_to(px, light.pt))
   dot_product = vector_math.dot_vector(n, Ldir)

   if dot_product > 0:
      if obscured(sphere, intersect_pt, light, sphere_list) == False:
         diffuse_value = light_contribution(sphere, intersect_pt, light)
         return diffuse_value
      else:
         diffuse_value = (0.0,0.0,0.0)
         return diffuse_value
   else:
      diffuse_value = (0.0,0.0,0.0)
      return diffuse_value

def obscured(sphere, intersect_pt, Light, sphere_list):
    n = collisions.sphere_normal_at_point(sphere, intersect_pt)
    px = vector_math.translate_point(intersect_pt, vector_math.scale_vector(n, 0.01))
    Ldir = vector_math.normalize_vector(vector_math.vector_from_to(px, Light.pt)) 
    ray_to_light = data.Ray(px, Ldir)
    listing = collisions.find_intersection_point(sphere_list, ray_to_light)
    if listing == []:
        return False
    elif listing != []:
        for (sphere, intersect_pt) in listing:
            if (distance(ray_to_light, intersect_pt) < distance(ray_to_light, Light.pt)):
                return True
    else:
        return False
def distance(ray, intersect_pt):
    intp = intersect_pt
    return math.sqrt((intp.x - ray.pt.x)**2 + (intp.y -  ray.pt.y)**2 + (intp.z - ray.pt.z)**2)

def light_contribution(sphere, intersect_pt, Light):
   n = collisions.sphere_normal_at_point(sphere, intersect_pt)
   px =vector_math.translate_point(intersect_pt, vector_math.scale_vector(n,0.01))
   Ldir = vector_math.normalize_vector(vector_math.vector_from_to(px, Light.pt))
   L = Light.color
   S = sphere.color
   red_diffuse = vector_math.dot_vector(n,Ldir)* L.r* S.r * sphere.finish.diffuse
   green_diffuse = vector_math.dot_vector(n,Ldir)* L.g* S.g * sphere.finish.diffuse
   blue_diffuse = vector_math.dot_vector(n,Ldir)* L.b* S.b * sphere.finish.diffuse
   return [red_diffuse, green_diffuse, blue_diffuse]            
    
def cast_all_rays(min_x, max_x, min_y, max_y, width, height, eye_point, sphere_list,color,light, point):
    deltax = (max_x-min_x)/float(width)
    deltay = (max_y - min_y)/float(height)
    for y in range(0, height):
        for x in range(0, width):
            y_value = max_y - y * deltay
            x_value = min_x + deltax * x
            ray = data.Ray(eye_point,vector_math.vector_from_to(eye_point,data.Point(x_value,y_value,0)))
            answer = cast_ray(ray ,sphere_list,color,light,point)
            print int(255 * answer.r), int(255 * answer.g), int(255 * answer.b) 
    
