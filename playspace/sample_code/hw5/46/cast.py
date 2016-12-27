from data import *
from vector_math import *
from collisions import *


def cast_ray(ray, sphere_list, clr, lght, pt):
    intersect_list = find_intersection_points(sphere_list, ray)
    if intersect_list:
        nearest = 0
        for s in range(1, len(intersect_list)):
            if dist_from_ray_pt(ray, intersect_list[s][1]) < \
               dist_from_ray_pt(ray, intersect_list[nearest][1]):
                nearest = s
        
        int_pt = sphere_intersection_point(ray, intersect_list[nearest][0])
        p_epsilon = point_off_sphere(intersect_list[nearest][0], int_pt)
        sp_norm = sphere_normal_at_point(intersect_list[nearest][0], int_pt)
        norm_to_light = normalize_vector(vector_from_to(p_epsilon, lght.pt))
        
        dot_prod = dot_vector(sp_norm, norm_to_light)
        if dot_prod <= 0:
            dot_prod = 0
        
        diff = intersect_list[nearest][0].finish.diffuse
        spclr = calc_spclr(intersect_list[nearest][0], sp_norm, norm_to_light,
                           dot_prod, pt, p_epsilon)
        
        ray_to_light = Ray(p_epsilon, vector_from_to(p_epsilon, lght.pt))
        
        if is_light_obscured(p_epsilon, ray_to_light, sphere_list):
            diff = 0
            spclr = 0
        
        r = final_r(intersect_list[nearest][0], 
                    clr, dot_prod, lght, diff, spclr)
        g = final_g(intersect_list[nearest][0], 
                    clr, dot_prod, lght, diff, spclr)
        b = final_b(intersect_list[nearest][0], 
                    clr, dot_prod, lght, diff, spclr)
        
        return Color(r, g, b)
        
    else:
        return Color(1.0, 1.0, 1.0)


def cast_all_rays(min_x, max_x, min_y, max_y, width, height, eye_point, 
                  sphere_list, clr, lght, file_object):
                  #clr argument is ambient light color
    
    print >> file_object, 'P3'
    print >> file_object, width, height
    print >> file_object, 255, '\n'
    
    dy = (max_x - min_x) / float(width)
    dx = (max_y - min_y) / float(height)
    y = max_y
    x = min_x
    
    while y > min_y:
        while x < max_x:
            color = cast_ray(Ray(eye_point, 
                                 vector_from_to(eye_point, Point(x, y, 0))),
                             sphere_list, clr, lght, eye_point)
            
            print >> file_object, int(color.r * 255),\
                                  int(color.g * 255),\
                                  int(color.b * 255)
            
            x += dx
        y -= dy
        x = min_x

#-------------------------------helper functions-------------------------------

def dist_from_ray_pt(ray, point):
    return length_vector(difference_point(ray.pt, point))


def point_off_sphere(sphere, point):
    return translate_point(point, scale_normal(sphere, point))


def scale_normal(sphere, point):
    return scale_vector(sphere_normal_at_point(sphere, point), 0.01)


def calc_spclr(sphere, sp_norm, norm_to_light, dot_prod, pt, p_epsilon):
    reflect_vec = difference_vector(norm_to_light, 
                                    scale_vector(sp_norm, (2 * dot_prod)))
    view_dir = normalize_vector(vector_from_to(pt, p_epsilon))
    spec_intensity = dot_vector(reflect_vec, view_dir)
    if spec_intensity <= 0:
        spec_intensity = 0
    spclr = sphere.finish.specular *\
            (spec_intensity ** (1.0/sphere.finish.roughness))
    return spclr


def is_light_obscured(point, ray_to_light, spheres):
    for s in range(len(spheres)):
        if sphere_intersection_point(ray_to_light, spheres[s]):
            if length_vector(vector_from_to(point,
               sphere_intersection_point(ray_to_light, spheres[s])))\
               <= length_vector(ray_to_light.dir):
                return True
            else:
                return False


def final_r(sphere, sp_color, dot_prod, light, diff, spclr):
    final_r = sphere.color.r *\
              sphere.finish.ambient * sp_color.r +\
              (dot_prod * light.color.r * sphere.color.r * diff) +\
              (light.color.r * spclr)
    if final_r > 1.0:
        final_r = 1.0
    return final_r


def final_g(sphere, sp_color, dot_prod, light, diff, spclr):
    final_g = sphere.color.g *\
              sphere.finish.ambient * sp_color.g +\
              (dot_prod * light.color.g * sphere.color.g * diff) +\
              (light.color.g * spclr)
    if final_g > 1.0:
        final_g = 1.0
    return final_g


def final_b(sphere, sp_color, dot_prod, light, diff, spclr):
    final_b = sphere.color.b *\
              sphere.finish.ambient * sp_color.b +\
              (dot_prod * light.color.b * sphere.color.b * diff) +\
              (light.color.b * spclr)
    if final_b > 1.0:
        final_b = 1.0
    return final_b

