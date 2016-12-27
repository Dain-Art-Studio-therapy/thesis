from collisions import *
import data
import utility
import vector_math
from math import fabs
def cast_ray(ray, sphere_list, color, light, point):
    intersections = find_intersection_points(sphere_list, ray)

    if intersections != []:
        #sphere = intersections[0][0]
        #intersection = intersections[0][1]


        for pair in intersections:
            sphere = pair[0]
            intersection = pair[1]
            min_distance = length_vector(vector_from_to(ray.pt, intersection))
            length =  length_vector(vector_from_to(ray.pt, pair[1]))
            if (length < min_distance):
                sphere = pair[0]
                intersection = pair[1]
                min_distance = length

        n_vector = sphere_normal_at_point(sphere, intersection)
        scaled_vector = scale_vector(n_vector, 0.01)
        p_e = translate_point(intersection, scaled_vector)
        light_vector = vector_from_to(p_e, light.pt)
        L_dir = normalize_vector(light_vector)
        light_dot_product = dot_vector(n_vector, L_dir)
        light_ray = data.Ray(p_e, L_dir)
        light_intersections = find_intersection_points(sphere_list, light_ray)
        light_distance = length_vector(light_vector)
        if_diffuse = True



#Calculate Diffuse
        if light_dot_product > 0:
            if light_intersections != []:
                for spheres_and_points in light_intersections:
                    point = spheres_and_points[1]
                    difference_lengths = length_vector(difference_point(point, p_e))
                    if difference_lengths < light_distance:
                        if_diffuse = False

        else:
            if_diffuse = False
#Compute Specular Values
        n_scale = scale_vector(n_vector, (2*light_dot_product))
        reflection = difference_vector(L_dir, n_scale)
        pe_eyevec = normalize_vector(difference_point(p_e, point))
        specularIntensity = dot_vector(pe_eyevec, reflection)

        if specularIntensity > 0:
            sphere_spec = sphere.finish.specular
            sphere_rough = sphere.finish.roughness
            specCont_r = (light.color.r * sphere_spec)* (specularIntensity** (1/float(sphere_rough)))
            specCont_g = (light.color.g * sphere_spec)* (specularIntensity** (1/float(sphere_rough)))
            specCont_b = (light.color.b * sphere_spec)* (specularIntensity** (1/float(sphere_rough)))

        else:
            specCont_r = 0
            specCont_g = 0
            specCont_b = 0


        if if_diffuse:
            lclr_r = light.color.r
            lclr_g = light.color.g
            lclr_b = light.color.b
            sp_r = sphere.color.r
            sp_g = sphere.color.g
            sp_b = sphere.color.b

            diff_r = light_dot_product * lclr_r * sp_r * sphere.finish.diffuse
            diff_g = light_dot_product * lclr_g * sp_g * sphere.finish.diffuse
            diff_b = light_dot_product * lclr_b * sp_b * sphere.finish.diffuse
        else:
            diff_r = 0
            diff_g = 0
            diff_b = 0
        #
        # min_distance = length_vector(vector_from_to(ray.pt, intersection))
        # for pair in intersections:
        #     length =  length_vector(vector_from_to(ray.pt, pair[1]))
        #     if (length < min_distance):
        #         sphere = pair[0]
        #         intersection = pair[1]
        #         min_distance = length

        sphere_color = sphere.color
        final_color_r = color.r * sphere_color.r *sphere.finish.ambient+diff_r+specCont_r
        final_color_g = color.g * sphere_color.g *sphere.finish.ambient+diff_g+specCont_g
        final_color_b = color.b * sphere_color.b *sphere.finish.ambient+diff_b+specCont_b

        final_color = data.Color(final_color_r, final_color_g, final_color_b)


        return final_color

    else:
        return data.Color(1.0, 1.0, 1.0)

def cast_all_rays(min_x, max_x, min_y, max_y, width, height, eye_point, sphere_list, color, light):
    x_width = fabs(max_x) + fabs(min_x)
    dx = x_width / width
    xValues = [min_x + (val * dx) for val in range(width)]

    y_height = fabs(min_y) + fabs(max_y)
    dy = y_height / height
    yValues = [max_y - (val * dy) for val in range(height)]

    for y in yValues:
        for x in xValues:
            DirVec = vector_from_to(eye_point, data.Point(x,y,0))
            colors = cast_ray(data.Ray(eye_point, DirVec), sphere_list, color, light, eye_point)
            if colors:
                print(str(int(colors.r*255))+ ' ' + str(int(colors.g*255))+ ' ' +str(int(colors.b*255)))
            else:
                print "255 255 255 "










