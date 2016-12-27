__author__ = 'Jarrett'

import collisions
import vector_math
import data
import utility

def intersect(sphere_list, ray):
    intersect_list = collisions.find_intersection_points(sphere_list, ray)
    if (intersect_list != []):
        min_dist_index = 0

        for i in range(len(intersect_list)):
            if (utility.distance(ray.pt, intersect_list[i][1])
                < utility.distance(ray.pt, intersect_list[min_dist_index][1])):
                min_dist_index = i

        return intersect_list[min_dist_index]

    else:
        return None

def calc_ambient_color(sphere, ambient):
    ambient_color = utility.color_scale(utility.color_mult(sphere.color, ambient), sphere.finish.ambient)
    return ambient_color

def calc_diffuse(sphere, sphere_list, pe, pe_to_light, light,  dot_light_sphere):
    if (dot_light_sphere <= 0):
        diffuse_color = data.Color(0, 0, 0)

    else:
        # check to see if the light hits another sphere in front of the original intersection point
        if (collisions.find_intersection_points(sphere_list, data.Ray(pe, pe_to_light)) == []):
            # diffuse_color = x * pe_to_light * sphere_color * sphere_finish
            diffuse_color = utility.color_scale(utility.color_mult(sphere.color,
                                                                   utility.color_scale(light.color, dot_light_sphere)),
                                                sphere.finish.diffuse)

        else:
            diffuse_color = data.Color(0, 0, 0)

    return diffuse_color

def calc_specular(sphere, sphere_normal, eye, light, pe, pe_to_light, dot_light_sphere):

    a = vector_math.scale_vector(sphere_normal, (2 * dot_light_sphere))
    reflect_vector = vector_math.difference_vector(pe_to_light, a)
    eye_to_pe = vector_math.normalize_vector(vector_math.vector_from_to(eye, pe))

    spec_intensity = vector_math.dot_vector(eye_to_pe, reflect_vector)

    if (spec_intensity > 0):
        spec_color = utility.color_scale(utility.color_scale(light.color, sphere.finish.specular),
                                         spec_intensity**(1 / sphere.finish.roughness))

    else:
        spec_color = data.Color(0, 0, 0)

    return spec_color

def cast_ray(ray, sphere_list, ambient, light, eye):
    # gets the tuples of the sphere intersections
    # returns white if no sphere is hit
    if intersect(sphere_list, ray) == None:
        return data.Color(1, 1, 1)

    else:
        intersect_tuple = intersect(sphere_list, ray)

        close_sphere = intersect_tuple[0]
        intersect_pt = intersect_tuple[1]

        # normal from the sphere's center to the intersection point
        sphere_normal = collisions.sphere_normal_at_point(close_sphere, intersect_pt)

        # a "fake" point that is 0.01 off of the sphere in the direction of the sphere's normal
        pe = vector_math.translate_point(intersect_pt, vector_math.scale_vector(sphere_normal, 0.01))
        # pe_circle_vector = vector_math.normalize_vector(vector_math.vector_from_to(close_sphere.center, pe))

        # normalized vector from pe to the light source (point)
        pe_to_light = vector_math.normalize_vector(vector_math.vector_from_to(pe, light.pt))

        # dot product of the sphere normal and the vector from the fake point to the light
        x = vector_math.dot_vector(sphere_normal, pe_to_light)

        # calculates the ambient contribution
        ambient_color = calc_ambient_color(close_sphere, ambient)
        # calculates the diffuse contribution
        diffuse_color = calc_diffuse(close_sphere, sphere_list, pe, pe_to_light, light, x)
        # calculates the specular contribution
        spec_color = calc_specular(close_sphere, sphere_normal, eye, light, pe, pe_to_light, x)

        # final_color = ambient_color
        # final_color = utility.color_add(ambient_color, diffuse_color)
        final_color = utility.color_add(utility.color_add(ambient_color, diffuse_color), spec_color)
        return final_color


def cast_all_rays(min_x, max_x, min_y, max_y, width, height, eye_point, sphere_list, ambient, light):
    # pixel_list = ["P3\n" + str(width) + " " + str(height) + "\n" + "255\n"]
    pixel_list = str.format("P3\n{0} {1}\n255\n", width, height)

    # establishes how much the x and y values have to move
    # to accommodate all the pixels inside the rectangle
    delta_x = (max_x - min_x) / float(width)
    delta_y = (max_y - min_y) / float(height)

    # makes each pixel inside the rectangle
    y = max_y

    while (min_y < y):
        x = min_x
        while (x < max_x):
            newColor = cast_ray(data.Ray(eye_point, vector_math.vector_from_to(eye_point, data.Point(x, y, 0))),
                                 sphere_list, ambient, light, eye_point)
            externalColor = utility.convert_color(newColor)
            # pixel_list.join(str(externalColor.r) + " " + str(externalColor.g) + " " + str(externalColor.b) + "\n")
            # print externalColor.r, externalColor.g, externalColor.b
            new_pt = str.format("{0} {1} {2}\n", externalColor.r, externalColor.g, externalColor.b)
            pixel_list += new_pt
            # print pixel_list
            x = x + delta_x
        y = y - delta_y

    return pixel_list
