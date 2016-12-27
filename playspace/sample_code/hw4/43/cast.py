__author__ = 'Jarrett'

import collisions
import vector_math
import data
import utility

def cast_ray(ray, sphere_list, ambient, light, eye):
    intersect_list = collisions.find_intersection_points(sphere_list, ray)
    if (intersect_list != []):
        min_dist_index = 0

        for i in range(len(intersect_list)):
            if (utility.distance(ray.pt, intersect_list[i][1])
                < utility.distance(ray.pt, intersect_list[min_dist_index][1])):
                min_dist_index = i

        close_sphere = intersect_list[min_dist_index][0]
        intersect_pt = intersect_list[min_dist_index][1]

        # normal from the sphere's center to the intersection point
        sphere_normal = collisions.sphere_normal_at_point(close_sphere, intersect_pt)
        ambient_color = utility.color_scale(utility.color_mult(close_sphere.color, ambient), close_sphere.finish.ambient)

        # a "fake" point that is 0.01 off of the sphere in the direction of the sphere's normal
        pe = vector_math.translate_point(intersect_pt, vector_math.scale_vector(sphere_normal, 0.01))
        # pe_circle_vector = vector_math.normalize_vector(vector_math.vector_from_to(close_sphere.center, pe))

        # normalized vector from pe to the light source (point)
        pe_to_light = vector_math.normalize_vector(vector_math.vector_from_to(pe, light.pt))

        x = vector_math.dot_vector(sphere_normal, pe_to_light)


        if (x <= 0):
            diffuse_color = data.Color(0, 0, 0)

        else:
            # check to see if the light hits another sphere in front of the original intersection point
            if (collisions.find_intersection_points(sphere_list, data.Ray(pe, pe_to_light)) == []):
                # diffuse_color = x * pe_to_light * sphere_color * sphere_finish
                diffuse_color = utility.color_scale(utility.color_mult(close_sphere.color, utility.color_scale(light.color, x)),
                                              close_sphere.finish.diffuse)

            else:
                diffuse_color = data.Color(0, 0, 0)


        a = vector_math.scale_vector(sphere_normal, (2 * x))
        reflect_vector = vector_math.difference_vector(pe_to_light, a)
        eye_to_pe = vector_math.normalize_vector(vector_math.vector_from_to(eye, pe))

        spec_intensity = vector_math.dot_vector(eye_to_pe, reflect_vector)

        if (spec_intensity > 0):
            spec_color = utility.color_scale(utility.color_scale(light.color, close_sphere.finish.specular), spec_intensity**(1 / close_sphere.finish.roughness))

        else:
            spec_color = data.Color(0, 0, 0)


        final_color = utility.color_add(utility.color_add(ambient_color, diffuse_color), spec_color)
        return final_color

    else:
        return data.Color(1, 1, 1)


def cast_all_rays(min_x, max_x, min_y, max_y, width, height, eye_point, sphere_list, ambient, light):
    print "P3"
    print width, height
    print 255

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
            print externalColor.r, externalColor.g, externalColor.b
            x = x + delta_x
        y = y - delta_y
