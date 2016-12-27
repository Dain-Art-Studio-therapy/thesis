import collisions
import data
import vector_math
import math

def cast_ray(ray, sphere_list, ambient_color, light, eye_point):
    L = collisions.find_intersection_points(sphere_list, ray)
    possible_list = []
    side_of_light = 0
    diffuse_light = data.Color(0,0,0)
    spec_light = data.Color(0,0,0)
    if L != []:
        for i in L:
            possible = distance(ray.pt, i[1])
            possible_list.append(possible)
            n = collisions.sphere_normal_at_point(i[0], i[1])
            pe = n_to_pe(n, i[1])
            ldir = vector_math.normalize_vector(vector_math.vector_from_to(pe, light.pt))
            side_of_light = vector_math.dot_vector(n, ldir)
            int_ray = data.Ray(pe, ldir)
            scaled_n = vector_math.scale_vector(n, side_of_light *2)
            ref_vec = vector_math.difference_vector(ldir, scaled_n)
            vdir = vector_math.normalize_vector(vector_math.vector_from_to(eye_point, pe))
            spec_intensity = vector_math.dot_vector(ref_vec, vdir)
            rough_val = i[0].finish.roughness
            spec_int_contrib = spec_intensity ** (1.0/rough_val)
            color_index = index_of_smallest(possible_list)
            uc_c =  L[color_index][0].color
            amb_newr = uc_c.r * ambient_color.r * L[color_index][0].finish.ambient
            amb_newg = uc_c.g * ambient_color.g * L[color_index][0].finish.ambient
            amb_newb = uc_c.b * ambient_color.b * L[color_index][0].finish.ambient
            if side_of_light <= 0:
                side_of_light = 0
            if spec_intensity > 0:
                spec_light.r = light.color.r * i[0].finish.specular * spec_int_contrib
                spec_light.g = light.color.g * i[0].finish.specular * spec_int_contrib
                spec_light.b = light.color.b * i[0].finish.specular * spec_int_contrib
            else:
                spec_light = data.Color(0,0,0)
            if collisions.find_intersection_points(sphere_list, int_ray) == []:
                    diffuse_light.r = side_of_light * light.color.r * i[0].color.r * i[0].finish.diffuse
                    diffuse_light.g = side_of_light * light.color.g * i[0].color.g * i[0].finish.diffuse
                    diffuse_light.b = side_of_light * light.color.b * i[0].color.b * i[0].finish.diffuse
            if collisions.find_intersection_points(sphere_list, int_ray) != []:
                    return data.Color(amb_newr, amb_newg, amb_newb)
            finalr = amb_newr+diffuse_light.r+spec_light.r
            finalg = amb_newg+diffuse_light.g+spec_light.g
            finalb = amb_newb+diffuse_light.b+spec_light.b
        return data.Color(finalr, finalg, finalb)

    else:
        return data.Color(1.0,1.0,1.0)

def index_of_smallest(nums):
    mindex = 0
    if nums == []:
        return None
    else:
        for i in range(len(nums)):
            if nums[i]<nums[mindex]:
                mindex = i
        return mindex 

def n_to_pe(input, int_point):
    input = vector_math.scale_vector(input, 0.01)
    pe = vector_math.translate_point(int_point, input)
    return pe

def distance(p1, p2):
    return math.sqrt((p2.x-p1.x)**2 + (p2.y-p1.y)**2 + (p2.z-p1.z)**2)

def convert_color(color):
    r = color.r * 255
    g = color.g * 255
    b = color.b * 255
    return data.Color(r, g, b)

def cast_all_rays(min_x, max_x, min_y, max_y, width, height, eye_point, sphere_list, ambient_color, light):
    dx = (max_x-min_x)/float(width)
    dy = (max_y-min_y)/float(height)

    list_of_points = []
    for y in range(height, 0, -1):
        for x in range(width):
            list_of_points.append(data.Point(min_x + dx*x,min_y + dy*y,0)) 

    for i in range(len(list_of_points)):
        temp_vector = vector_math.vector_from_to(eye_point, list_of_points[i])
        temp_ray = data.Ray(eye_point, temp_vector)
        light_color = data.Color(1.5,1.5,1.5)
        light_pt = data.Point(-100.0,100.0,-100.0)
        bool = cast_ray(temp_ray, sphere_list, data.Color(1.0,1.0,1.0), data.Light(light_pt, light_color), eye_point)
        resulting_color = convert_color(bool)
        if resulting_color.r > 255:
            resulting_color.r = 255
        if resulting_color.g > 255:
            resulting_color.g = 255
        if resulting_color.b > 255:
            resulting_color.b = 255
        print int(resulting_color.r), int(resulting_color.g), int(resulting_color.b)
