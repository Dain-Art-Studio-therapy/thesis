from collisions import *
import data
import utility
import vector_math
from math import fabs

def getClosestSphere(ray, intersection_list):
    near_sphere = intersection_list[0][0]
    near_point = intersection_list[0][1]
    for spheres in intersection_list:
        sphere = spheres[0]
        intersection = spheres[1]
        min_distance = length_vector(vector_from_to(ray.pt, intersection))
        length = length_vector(vector_from_to(ray.pt, near_point))
        if (min_distance < length):
            near_sphere = sphere
            near_point = intersection

    return (near_sphere, near_point)

def getDiffuse(ray, intersection_list, sphere_list, light):
    nearest = getClosestSphere(ray, intersection_list)
    near_sphere = nearest[0]
    near_point = nearest[1]

    n_vector = sphere_normal_at_point(near_sphere, near_point)
    scaled_vector = scale_vector(n_vector, 0.01)
    p_e = translate_point(near_point, scaled_vector)
    light_vector = vector_from_to(p_e, light.pt)
    L_dir = normalize_vector(light_vector)
    ldotProduct = dot_vector(n_vector, L_dir)
    light_ray = data.Ray(p_e, L_dir)
    light_intersections = find_intersection_points(sphere_list, light_ray)
    light_distance = length_vector(light_vector)
    if_diffuse = True

    if ldotProduct > 0:
        if light_intersections != []:
            for spheres_and_points in light_intersections:
                point = spheres_and_points[1]
                difference_lengths =length_vector(difference_point(point, p_e))
                if difference_lengths < light_distance:
                    if_diffuse = False

    else:
        if_diffuse = False

    if if_diffuse:
        lClr_r = light.color.r
        lClr_g = light.color.g
        lClr_b = light.color.b
        sp_r = near_sphere.color.r
        sp_g = near_sphere.color.g
        sp_b = near_sphere.color.b

        diff_r = ldotProduct * lClr_r * sp_r * near_sphere.finish.diffuse
        diff_g = ldotProduct * lClr_g * sp_g * near_sphere.finish.diffuse
        diff_b = ldotProduct * lClr_b * sp_b * near_sphere.finish.diffuse
    else:
        diff_r = 0
        diff_g = 0
        diff_b = 0


    return (diff_r, diff_g, diff_b)

def getSpecular(ray, intersection_list, light, point):
    nearest = getClosestSphere(ray, intersection_list)
    near_sphere = nearest[0]
    near_point = nearest[1]

    n_vector = sphere_normal_at_point(near_sphere, near_point)
    scaled_vector = scale_vector(n_vector, 0.01)
    p_e = translate_point(near_point, scaled_vector)
    light_vector = vector_from_to(p_e, light.pt)
    L_dir = normalize_vector(light_vector)
    light_dot_product = dot_vector(n_vector, L_dir)

 #Compute Specular Values
    n_scale = scale_vector(n_vector, (2*light_dot_product))
    reflection = difference_vector(L_dir, n_scale)
    pe_eyevec = normalize_vector(difference_point(p_e, point))
    specularIntensity = dot_vector(pe_eyevec, reflection)

    if specularIntensity > 0:
        sphere_spec = near_sphere.finish.specular
        sphere_rough = near_sphere.finish.roughness
        specCont_r = (light.color.r * sphere_spec)* \
                     (specularIntensity** (1/float(sphere_rough)))
        specCont_g = (light.color.g * sphere_spec)* \
                     (specularIntensity** (1/float(sphere_rough)))
        specCont_b = (light.color.b * sphere_spec)* \
                     (specularIntensity** (1/float(sphere_rough)))

    else:
        specCont_r = 0
        specCont_g = 0
        specCont_b = 0

    return (specCont_r, specCont_g, specCont_b)

def getColor(ray, intersection_list):
    nearest = getClosestSphere(ray, intersection_list)
    near_sphere = nearest[0]

    sphere_color = near_sphere.color

    return (sphere_color.r, sphere_color.g, sphere_color.b)


def cast_ray(ray, sphere_list, color, light, point):
    intersections = find_intersection_points(sphere_list, ray)

    if intersections != []:

#run getColor to get the color of the sphere at a point
        sphere_color = getColor(ray, intersections)
        sphere_r = sphere_color[0]
        sphere_g = sphere_color[1]
        sphere_b = sphere_color[2]

#run getDiffuse to get Diffuse Contribution values
        diffuseValues = getDiffuse(ray, intersections, sphere_list, light)
        diffuse_r = diffuseValues[0]
        diffuse_g = diffuseValues[1]
        diffuse_b = diffuseValues[2]

#run getSpecular to get the Specular Contribution Values
        specularValues = getSpecular(ray, intersections, light, point)
        specular_r = specularValues[0]
        specular_g = specularValues[1]
        specular_b = specularValues[2]

        nearest = getClosestSphere(ray, intersections)
        near_sphere = nearest[0]
        near_point = nearest[1]

        final_color_r = color.r * sphere_r * near_sphere.finish.ambient + \
                        diffuse_r + specular_r
        final_color_g = color.g * sphere_g * near_sphere.finish.ambient + \
                        diffuse_g + specular_g
        final_color_b = color.b * sphere_b * near_sphere.finish.ambient + \
                        diffuse_b + specular_b

        final_color = data.Color(final_color_r, final_color_g, final_color_b)

        return final_color

    else:
         return data.Color(1.0, 1.0, 1.0)

def cast_all_rays(min_x, max_x, min_y, max_y, width, height, eye_point,
                  sphere_list, color, light, output):
    x_width = fabs(max_x) + fabs(min_x)
    dx = x_width / width
    xValues = [min_x + (val * dx) for val in range(width)]

    y_height = fabs(min_y) + fabs(max_y)
    dy = y_height / height
    yValues = [max_y - (val * dy) for val in range(height)]

    print >> output, 'P3'
    print >> output, str(width)+ ' ' +str(height)
    print >> output, '255'

    for y in yValues:
        for x in xValues:
            DirVec = vector_from_to(eye_point, data.Point(x,y,0))
            colors = cast_ray(data.Ray(eye_point, DirVec), sphere_list, color,
                              light, eye_point)
            redValueFinal   = str(int(colors.r*255))
            greenValueFinal = str(int(colors.g*255))
            blueValueFinal  = str(int(colors.b*255))
            if colors:

                print >> output, (redValueFinal+ ' ' +greenValueFinal+ ' '
                                  +blueValueFinal)
            else:
                print >> output, "255 255 255 "










