import math
from data import *
from collisions import *
from vector_math import *


def cast_ray(ray, sphere_list, ambient_light, light, eye_point):
    intersection_points = find_intersection_points(sphere_list, ray)

    if intersection_points != []:
        # return the color of the sphere with the nearest intersection
        nearest_intersect = nearest_intersection(intersection_points, ray)

        return light_model(nearest_intersect, sphere_list, ambient_light,
                           light, eye_point)

        # return nearest_sphere.color

    # if no intersection, return white: 1.0, 1.0, 1.0
    return Color(1.0, 1.0, 1.0)


def light_model(nearest_intersect, sphere_list, ambient_light,
                light, eye_point):

    # returns color

    sphere = nearest_intersect[0]

    ambient_r = sphere.color.r * sphere.finish.ambient * ambient_light.r
    ambient_g = sphere.color.g * sphere.finish.ambient * ambient_light.g
    ambient_b = sphere.color.b * sphere.finish.ambient * ambient_light.b

    diffuse = diffuse_light(nearest_intersect, sphere_list, light)

    specular = specular_component(nearest_intersect, light, eye_point)

    r = ambient_r + diffuse.r + specular.r
    g = ambient_g + diffuse.g + specular.g
    b = ambient_b + diffuse.b + specular.b

    return Color(r, g, b)


def diffuse_light(nearest_intersect, sphere_list, light):
    # function returns the diffuse contribution of the point light

    # compute a new point 0.01 off of the sphere,
    # as well as the normal vector from the sphere's center to the intersect point

    sphere = nearest_intersect[0]
    intersect_point = nearest_intersect[1]

    vector = difference_point(intersect_point, sphere.center)
    normal_vector = normalize_vector(vector)
    vector = scale_vector(normal_vector, 0.01)

    point = translate_point(intersect_point, vector)

    # compute a normalized vector from the point to the light
    light_vector = difference_point(light.point, point)
    light_vector_normal = normalize_vector(light_vector)

    dot_normal_light = dot_vector(normal_vector, light_vector_normal)

    if dot_normal_light <= 0:
        return Color(0.0, 0.0, 0.0)

    # check for obstructing spheres
    ray = Ray(point, light_vector_normal)

    if not light_obstructions(point, sphere_list, ray, light_vector):
        r = light.color.r * sphere.color.r * sphere.finish.diffuse \
            * dot_normal_light
        g = light.color.g * sphere.color.g * sphere.finish.diffuse \
            * dot_normal_light
        b = light.color.b * sphere.color.b * sphere.finish.diffuse \
            * dot_normal_light

        return Color(r, g, b)

    else:
        return Color(0.0, 0.0, 0.0)


def specular_component(nearest_intersect, light, eye_point):
    # returns the specular component of the point light

    sphere = nearest_intersect[0]
    intersect_point = nearest_intersect[1]

    vector = difference_point(intersect_point, sphere.center)
    normal_vector = normalize_vector(vector)
    vector = scale_vector(normal_vector, 0.01)

    point = translate_point(intersect_point, vector)

    # compute a normalized vector from the point to the light
    light_vector = difference_point(light.point, point)
    light_vector_normal = normalize_vector(light_vector)

    dot_normal_light = dot_vector(normal_vector, light_vector_normal)

    # compute light_vector_normal - (2*dot_normal_light)*normal_vector

    n = scale_vector(normal_vector, 2 * dot_normal_light)
    reflection_vector = difference_vector(light_vector_normal, n)

    view_vector = difference_point(point, eye_point)
    view_direction = normalize_vector(view_vector)

    specular_intensity = dot_vector(reflection_vector, view_direction)

    if specular_intensity > 0:
        r = light.color.r * sphere.finish.specular \
            * math.pow(specular_intensity, (1 / sphere.finish.roughness))
        g = light.color.g * sphere.finish.specular \
            * math.pow(specular_intensity, (1 / sphere.finish.roughness))
        b = light.color.b * sphere.finish.specular \
            * math.pow(specular_intensity, (1 / sphere.finish.roughness))

        return Color(r, g, b)
    else:
        return Color(0.0, 0.0, 0.0)


def light_obstructions(point, sphere_list, ray, light_vector):
    # returns true or false, if there are any spheres blocking the light
    # true if there is a sphere obstructing the light

    obstructions = find_intersection_points(sphere_list, ray)
    distance_to_light = length_vector(light_vector)

    if obstructions == []:
        return False

    for i in obstructions:
        point_to_intersect = difference_point(i[1], point)
        distance_to_intersect = length_vector(point_to_intersect)

        if distance_to_intersect < distance_to_light:
            return True

    return False


def close_point(nearest_intersect):
    # computes and returns a new point 0.01 off of the sphere
    sphere = nearest_intersect[0]
    intersect_point = nearest_intersect[1]

    vector = difference_point(intersect_point, sphere.center)
    vector = normalize_vector(vector)
    vector = scale_vector(vector, 0.01)

    point = translate_point(intersect_point, vector)

    return point


def nearest_intersection(intersection_points, ray):
    # returns tuple with nearest (sphere, intersection point)
    #  to the origin of the ray

    nearest = intersection_points[0]

    for intersect in intersection_points:

        dist_intersect = length_vector(difference_point(intersect[1], ray.pt))
        dist_nearest = length_vector(difference_point(nearest[1], ray.pt))

        if dist_intersect < dist_nearest:
            nearest = intersect

    return nearest


def cast_all_rays(min_x, max_x, min_y, max_y, width, height,
                  eye_point, sphere_list, ambient_light, light):

    print "P3"
    print width, height
    print 255

    for h in range(height):
        dy = (max_y - min_y) / float(height)
        y = max_y - (h * dy)

        for w in range(width):
            dx = (max_x - min_x) / float(width)
            x = min_x + (w * dx)

            ray = Ray(eye_point, difference_point(Point(x, y, 0), eye_point))

            color = cast_ray(ray, sphere_list, ambient_light, light, eye_point)

            rgb = convert_to_RGB(color)
            print rgb.r, rgb.g, rgb.b


def convert_to_RGB(color):
    r = int(255 * color.r)
    g = int(255 * color.g)
    b = int(255 * color.b)

    if color.r > 1.0:
        r = 255
    if color.g > 1.0:
        g = 255
    if color.b > 1.0:
        b = 255

    return Color(r, g, b)


if __name__ == '__main__':
    pass