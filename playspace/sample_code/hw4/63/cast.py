

from collisions import *
from data import *
import math


def distance(point1, point2):
    x_val = (point1.x - point2.x)**2
    y_val = (point1.y - point2.y)**2 
    z_val = (point1.z - point2.z)**2
    return math.sqrt(x_val + y_val + z_val)


def nearest_sphere_index(point, list):
    if list == []:
        return None

    nearest = 0
    
    for i in range(0, len(list)):
        if distance(point, list[i][1]) < distance(point, list[nearest][1]):
            nearest = i

    return nearest




def isLight(pe, l_point, l_dir, sphere_list):
    islight = True
    l_ray = Ray(pe, l_dir)

    newlist = find_intersection_points(sphere_list, l_ray)

    if newlist != []:
        newindex = nearest_sphere_index(pe, newlist)

        if newindex is not None:
            newpoint = newlist[newindex][1]
            distance_new = distance(newpoint, pe)
            distance_old = distance(l_point, pe)

            if distance_new < distance_old:
               islight = False

    return islight



def calc_spec(s_in, light, s_fin):
     color = Color(0.0, 0.0, 0.0)
     l_col = light.color
     if s_in > 0:
        power = 1.0 / s_fin.roughness
        factor = (s_in)** power
        spec = s_fin.specular
        color.r = l_col.r * spec * factor
        color.g = l_col.g * spec * factor
        color.b = l_col.b * spec * factor
        return color
     else:
        return color


def get_specular(l_dir, dot_p, norm, pe, e_pt):
    reflect = difference_vector(l_dir, scale_vector(norm, dot_p * 2))
    e_2_p = vector_from_to(e_pt, pe)
    v_dir = normalize_vector(e_2_p)
    spec_int = dot_vector(reflect, v_dir)

    return spec_int
    



def color_comp(i_sphere, i_pt, sphere_list, light, e_pt):
    s_color = i_sphere.color    
    s_fin = i_sphere.finish
    fin_d = s_fin.diffuse

    s_normal = sphere_normal_at_point(i_sphere, i_pt)
    scaled_n = scale_vector(s_normal, 0.01)
    pe = translate_point(i_pt, scaled_n)

    l_dir = normalize_vector(vector_from_to(pe, light.pt))
    dot_p = dot_vector(s_normal, l_dir)

    spec = get_specular(l_dir, dot_p, s_normal, pe, e_pt)
    comp = calc_spec(spec, light, s_fin)


    if dot_p <= 0.0:
       return add_colors(comp, Color(0.0, 0.0, 0.0))
  
    islight = isLight(pe, light.pt, l_dir, sphere_list)
    

    if islight:
        l_color = light.color
        red = l_color.r * dot_p * fin_d * s_color.r
        green = l_color.g * dot_p * fin_d * s_color.g
        blue = l_color.b * dot_p * fin_d * s_color.b
        result = Color(red, green, blue)
        return add_colors(result, comp)                 
    else:
        return add_colors(Color(0.0, 0.0, 0.0), comp)





def add_colors(color1, color2):
    red = color1.r + color2.r
    green = color1.g + color2.g
    blue = color1.b + color2.b
    result = Color(red, green, blue)
    return result




 
def apply_light(sphere_list, ray, amb_light, light, e_pt):
    list = find_intersection_points(sphere_list, ray)
    s_index = nearest_sphere_index(ray.pt, list)

    if s_index is None:
        return Color(1.0, 1.0, 1.0)


    i_sphere = list[s_index][0]
    i_pt = list[s_index][1]
    s_color = i_sphere.color
    s_finish = i_sphere.finish    

    comp = color_comp(i_sphere, i_pt, sphere_list, light, e_pt)

    
    new_red = s_color.r * s_finish.ambient * amb_light.r
    new_green = s_color.g * s_finish.ambient * amb_light.g
    new_blue = s_color.b * s_finish.ambient * amb_light.b
    newcolor = Color(new_red, new_green, new_blue)
    result_color = add_colors(newcolor, comp)
    return result_color



def cast_ray(ray, sphere_list, amb_light, light, e_pt):
    if sphere_list == []:
        return Color(1.0, 1.0, 1.0)

    return apply_light(sphere_list, ray, amb_light, light, e_pt)





def cast_all_rays(min_x, max_x, min_y, max_y, width, height,
 eye_point, sphere_list, amb_light, light):

    width = float(width)
    height = float(height)

    y_delta = float(max_y - min_y) / (height)
    x_delta = float(max_x - min_x) / (width)
    
    pos_x = min_x
    pos_y = max_y

        
    while (pos_y > min_y):
        while (pos_x < max_x):
            pt = Point(pos_x, pos_y, 0)
            dir = difference_point(pt, eye_point)
            ray = Ray(eye_point, dir)
                          
            color = cast_ray(ray, sphere_list, amb_light, light, eye_point)
            red = min(color.r*255, 255)
            green = min(color.g*255, 255)
            blue = min(color.b*255, 255)
            print int(red), int(green), int(blue)
            pos_x += x_delta
        pos_y -= y_delta
        pos_x = min_x













