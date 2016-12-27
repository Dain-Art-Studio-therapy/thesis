# Name: Audrey Chan
# Instructor: Aaron Keen
# Section: 09

import collisions
import data
import vector_math

def distance(ray, point):
    return vector_math.length_vector(vector_math.difference_point(ray.pt, point))

def cast_ray(ray, sphere_list, amb, light, eye_pt):

    cl = collisions.find_intersection_points(sphere_list, ray)
    if cl == []:
        return data.Color(1.0, 1.0, 1.0)

    distances = []
    for c in cl:
        distances.append((distance(ray,c[1]), c[0], c[1]))
    distances.sort()
    nearest_dist = distances[0][0]
    nearest_sph = distances[0][1]
    nearest_pt = distances[0][2]
    
    return_value_r = nearest_sph.color.r * amb.r * nearest_sph.finish.ambient
    return_value_g = nearest_sph.color.g * amb.g * nearest_sph.finish.ambient
    return_value_b = nearest_sph.color.b * amb.b * nearest_sph.finish.ambient

    #computing new point Pe, will point just off the sphere
    for c in cl:
        #sphere's normal at intersection point N
        N = collisions.sphere_normal_at_point(nearest_sph, nearest_pt)
        pe = vector_math.translate_point(c[1], vector_math.scale_vector(N, 0.01))
    
    #if light is on opposite side
        L_dir = vector_math.normalize_vector(vector_math.vector_from_to(pe, light.pt))
        L_dot_N = vector_math.dot_vector(N, L_dir)
        
        if L_dot_N <= 0:
            difflight_cont = False
        else:
            difflight_cont = True

        #check if another sphere is in path of pe to light's position
        cl2 = collisions.find_intersection_points(sphere_list, data.Ray(pe, L_dir))
        difflight_cont2 = True
        for c2 in cl2:
            if distance(data.Ray(pe, L_dir), c2[1]) < distance(data.Ray(pe, L_dir), light.pt):
                difflight_cont2 = False

        if difflight_cont and difflight_cont2:
            #if light contributes to point's color
            contr_r = vector_math.dot_vector(N, L_dir) * light.color.r * nearest_sph.color.r * nearest_sph.finish.diffuse
            contr_g = vector_math.dot_vector(N, L_dir) * light.color.g * nearest_sph.color.g * nearest_sph.finish.diffuse
            contr_b = vector_math.dot_vector(N, L_dir) * light.color.b * nearest_sph.color.b * nearest_sph.finish.diffuse
            return_value_r += contr_r
            return_value_g += contr_g
            return_value_b += contr_b

        # calculate specular contribution
        refl_vect = vector_math.difference_vector(L_dir, vector_math.scale_vector(N, 2 * L_dot_N))
        V_dir = vector_math.normalize_vector(vector_math.vector_from_to(eye_pt, pe))
        spec_int = vector_math.dot_vector(refl_vect, V_dir)

        if spec_int <= 0:
            spec_cont = False
        else:
            spec_cont = True

        if spec_cont:
            #if specular intensity contributes to point's color
            contr_spec_r = light.color.r * nearest_sph.finish.specular * (spec_int ** (1 / nearest_sph.finish.roughness))
            contr_spec_g = light.color.g * nearest_sph.finish.specular * (spec_int ** (1 / nearest_sph.finish.roughness))
            contr_spec_b = light.color.b * nearest_sph.finish.specular * (spec_int ** (1 / nearest_sph.finish.roughness))
            return_value_r += contr_spec_r
            return_value_g += contr_spec_g
            return_value_b += contr_spec_b

        return data.Color(return_value_r, return_value_g, return_value_b)




def cast_all_rays(min_x, max_x, min_y, max_y, width, height, eye_point, sphere_list, amb, light):
    
    print 'P3'
    print width, height
    print 255

    pixels = []
    y = max_y
    x = min_x
    while y > min_y:
        x = min_x
        while x < max_x:
            pixels.append(data.Point(x, y, 0))
            x += (max_x - min_x) / float(width)
        y -= (max_y - min_y) / float(height)

    rays = []
    for i in range(len(pixels)):
        rays.append(data.Ray(eye_point, vector_math.vector_from_to(eye_point, pixels[i])))

    for ray in rays:
        color = cast_ray(ray, sphere_list, amb, light, eye_point)
        R = int(color.r * 255)
        G = int(color.g * 255)
        B = int(color.b * 255)
        print R, G, B,
