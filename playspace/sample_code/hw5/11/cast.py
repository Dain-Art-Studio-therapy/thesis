from data import *
from collisions import *
from utility import *
from vector_math import *
from math import *

def cast_ray(ray, sphere_list, ambient_light, light, eye_point):
    l = find_intersection_points(sphere_list,ray)
    if (l != []):
        closest = distform(ray.pt,l[0][1])
        closest_pt = l[0][1]
        closest_sphere = l[0][0]
        for s in l:
           dform = distform(ray.pt,s[1])
           if dform < closest:
               closest = dform
               closest_pt = s[1]
               closest_sphere = s[0]
        amb = ambient_coloring(closest_sphere, ambient_light)
        dif = diff_cmpnt(closest_pt,light,closest_sphere, sphere_list)
        spe = spec_cmpnt(closest_pt,light,closest_sphere, sphere_list,eye_point)
        return limit_colors(amb+dif+spe)
    else:
        return Color(1.0,1.0,1.0)

def cast_all_rays(min_x,max_x,min_y,max_y,width,height,eye_point,sphere_list,
color,light):
    output = open('image.ppm', 'w')
    output.write("P3\n")
    output.write(str(width)+" "+ str(height)+"\n")
    output.write("255\n")
    
    h1 = (max_y - min_y)/float(height)
    w1 = (max_x - min_x)/float(width)
    x1 = min_x
    y1 = max_y
    
    while( y1 > min_y):
        while( x1 >= min_x and x1 < max_x):
            if (cast_ray(Ray(eye_point, vector_from_to(eye_point,
 Point(x1,y1,0))),sphere_list, color, light, eye_point) != Color(1.0,1.0,1.0)):
                l =  convert_color(cast_ray(Ray(eye_point, 
vector_from_to(eye_point,Point(x1,y1,0))), sphere_list, color, light,eye_point))
                output.write(str(int(l[0]))+" "+str(int(l[1]))+" "\
+str(int(l[2])) +" \n")
            else:
                output.write("255 255 255\n")
            x1 += w1
        x1 = min_x
        y1 -= h1

def distform(pt1,pt2):
    return sqrt((pt2.x - pt1.x)**2 + (pt2.y - pt1.y)**2 + (pt2.z - pt1.z)**2)

def limit_colors(c):
    if c.r > 255.0:
       c.r = 255.0
    if c.g > 255.0:
       c.g = 255.0
    if c.b > 255.0:
       c.b = 255.0
    return c

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

def diff_cmpnt(intersection_point, light, sphere, sphere_list):
    N  = sphere_normal_at_point(sphere, intersection_point)
    Pe = translate_point(intersection_point, scale_vector(N, 0.01))
    ldir = normalize_vector(vector_from_to(Pe, light.pt))
    visible = dot_vector(N, ldir)
    if visible < 0:
        return Color(0,0,0)
    l = find_intersection_points(sphere_list,Ray(Pe,ldir))

    if len(l) != 0:
        for i in l:
            if distform(light.pt, Pe) > distform(Pe, i[1]):
                return Color(0,0,0)
     
    r = dot_vector(N, ldir)*light.color.r*sphere.color.r*sphere.finish.diffuse
    g = dot_vector(N, ldir)*light.color.g*sphere.color.g*sphere.finish.diffuse
    b = dot_vector(N, ldir)*light.color.b*sphere.color.b*sphere.finish.diffuse
    return Color(r,g,b)
    

def spec_cmpnt(intersection_point, light, sphere, sphere_list,eye):
    N = sphere_normal_at_point(sphere, intersection_point)
    Pe = translate_point(intersection_point, scale_vector(N, 0.01))
    ldir = normalize_vector(vector_from_to(Pe, light.pt))
    ldotn = dot_vector(N, ldir)
    reflection_vector = difference_vector(ldir,scale_vector(N,(2 * ldotn)))
    vdir  = normalize_vector(vector_from_to(eye, Pe))
    spec_intensity = dot_vector(reflection_vector, vdir)
    if spec_intensity > 0:
        sval =sphere.finish.specular*spec_intensity**(1/sphere.finish.roughness)
        return Color(light.color.r*sval,light.color.g*sval,light.color.b*sval)
    else:
         return Color(0,0,0)
