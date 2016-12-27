from data import *
from collisions import *
from utility import *
from vector_math import *
from math import *

def cast_ray(ray, sphere_list, ambient_light, light, eye_point):
    if (find_intersection_points(sphere_list, ray) != []):
        l = find_intersection_points(sphere_list, ray)
        closest = distform(ray.pt,l[0][1])
        closest_pt = l[0][1]
        closest_sphere = l[0][0]
        for s in l:
           if (distform(ray.pt,s[1]) < closest):
               closest = distform(ray.pt,s[1])
               closest_pt = s[1]
               closest_sphere = s[0]
        amb= ambient_coloring(closest_sphere, ambient_light)
        dif= diffuse_component(closest_pt,light,closest_sphere, sphere_list)
        spe= specular_component(closest_pt,light,closest_sphere, sphere_list,eye_point)
        return Color(amb.r + dif.r +spe.r , amb.g + dif.g + spe.g , amb.b + dif.b + spe.b)
    else:
        return Color(1.0,1.0,1.0)

def cast_all_rays(min_x, max_x, min_y, max_y, width, height, eye_point, sphere_list, color, light):
    print "P3"
    print width ,  height
    print "255"
    
    h1 = (max_y - min_y)/float(height)
    w1 = (max_x - min_x)/float(width)
    x1 = min_x
    y1 = max_y
    
    while( y1 > min_y):
        while( x1 >= min_x and x1 < max_x):
            if (cast_ray(Ray(eye_point, vector_from_to(eye_point, Point(x1,y1,0))),
 sphere_list, color, light, eye_point) != Color(1.0,1.0,1.0)):
                l =  convert_color(cast_ray(Ray(eye_point, vector_from_to(eye_point,
 Point(x1,y1,0))), sphere_list, color, light,eye_point))
                print int(l[0]),int(l[1]),int(l[2])
            else:
                print "255 255 255"
            x1 += w1
        x1 = min_x
        y1 -= h1

def distform(pt1,pt2):
    return sqrt((pt2.x - pt1.x)**2 + (pt2.y - pt1.y)**2 + (pt2.z - pt1.z)**2)

def convert_color(c):
    r1 = c.r * 255
    g1 = c.g * 255
    b1 = c.b * 255
    return r1,g1,b1

def ambient_coloring(closest_sphere, ambient_light):
    r = closest_sphere.color.r * closest_sphere.finish.ambient
    g = closest_sphere.color.g * closest_sphere.finish.ambient
    b = closest_sphere.color.b * closest_sphere.finish.ambient
    return Color(r,g,b) * ambient_light

def diffuse_component(intersection_point, light, sphere, sphere_list):
    N  = sphere_normal_at_point(sphere, intersection_point)
    Pe = translate_point(intersection_point, scale_vector(N, 0.01))
    ldir = normalize_vector(vector_from_to(Pe, light.pt))
    visible = dot_vector(N, ldir)
    if visible < 0:
        return Color(0,0,0)
    l = find_intersection_points(sphere_list,Ray(Pe,ldir))

    if len(l) != 0:
        for i in l:
            if distform(light.pt, Pe) > distform(light.pt, i[1]):
                return Color(0,0,0)
     
    r = dot_vector(N, ldir) * light.color.r * sphere.color.r * sphere.finish.diffuse
    g = dot_vector(N, ldir) * light.color.g * sphere.color.g * sphere.finish.diffuse
    b = dot_vector(N, ldir) * light.color.b * sphere.color.b * sphere.finish.diffuse
    return Color(r,g,b)
    

def specular_component(intersection_point, light, sphere, sphere_list,eye):
    N = sphere_normal_at_point(sphere, intersection_point)
    Pe = translate_point(intersection_point, scale_vector(N, 0.01))
    ldir = normalize_vector(vector_from_to(Pe, light.pt))
    ldotn = dot_vector(N, ldir)
    reflection_vector = difference_vector(ldir,scale_vector(N,(2 * ldotn)) )
    vdir  = normalize_vector(vector_from_to(eye, Pe))
    spec_intensity = dot_vector(reflection_vector, vdir)
    if spec_intensity > 0:
         return Color(light.color.r*sphere.finish.specular*spec_intensity**(1/sphere.finish.roughness),
 light.color.g*sphere.finish.specular*spec_intensity**(1/sphere.finish.roughness),
 light.color.b*sphere.finish.specular*spec_intensity**(1/sphere.finish.roughness))
    else:
         return Color(0,0,0)
