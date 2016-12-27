from data import *
from collisions import *
from vector_math import *

def occlude(sphere_color, finish, ambient_color):

    return Color(
        sphere_color.r * finish.ambient * ambient_color.r,
        sphere_color.g * finish.ambient * ambient_color.g,
        sphere_color.b * finish.ambient * ambient_color.b
        )


def diffuse(dot_product, light_color, sphere_color, finish):

    glimmer = dot_product * finish.diffuse
    return Color(
        glimmer * light_color.r * sphere_color.r,
        glimmer * light_color.g * sphere_color.g,
        glimmer * light_color.b * sphere_color.b
        )


def glare(light_color, sphere, specular_intensity):

    power = 1.0 / sphere.finish.roughness
    glare = sphere.finish.specular * specular_intensity**power
    return Color(
        light_color.r * glare,
        light_color.g * glare,
        light_color.b * glare
        )


def add_colors(color1, color2, color3):

    return Color(
        color1.r + color2.r + color3.r,
        color1.g + color2.g + color3.g,
        color1.b + color2.b + color3.b
        )


def convert(color_list):

    new_list = []
    
    for color in color_list:
        new_list.append((
            int(min(color.r, 1.0)*255), 
            int(min(color.g, 1.0)*255), 
            int(min(color.b, 1.0)*255)
            ))

    return new_list


def first_collision(ray, sphere_list):

    pairs = find_intersection_points(sphere_list, ray)
    
    if pairs != []:
        mindex = 0
        for i in range(len(pairs)):
            if (
                length_vector(vector_from_to(ray.pt, pairs[mindex][1])) >
                length_vector(vector_from_to(ray.pt, pairs[i][1]))
                ):
                    mindex = i
        return pairs[mindex]
    else:
        return None
    

def is_obscured(epsilon, light_pt, light_normal, sphere_list):

    epsilon_light_ray = Ray(epsilon, light_normal)
    near_pair = first_collision(epsilon_light_ray, sphere_list)

    if near_pair != None:
        intersection_point = near_pair[1]
        if (
            length_vector(difference_point(epsilon, intersection_point)) <
            length_vector(difference_point(epsilon, light_pt))
            ):
            return True
    else:
        return False


def cast_light(
    sphere, light, epsilon, dot_product, light_normal, sphere_list
    ):

    if dot_product <= 0:
        return Color(0.0, 0.0, 0.0)

    obscured = is_obscured(epsilon, light.pt, light_normal, sphere_list)
    shine = diffuse(dot_product, light.color, sphere.color, sphere.finish)
    
    if obscured == False:
        return shine
    else:
        return Color(0.0, 0.0, 0.0)


def speculate(
    sphere, normal, light_normal, epsilon, dot_product, eye_point, lt_color
    ):

    scaled_normal = scale_vector(normal, dot_product*2)
    reflection_vector = difference_vector(light_normal, scaled_normal)
    view_vector = normalize_vector(vector_from_to(eye_point, epsilon))

    intensity = dot_vector(reflection_vector, view_vector)

    if intensity > 0:
        return glare(lt_color, sphere, intensity)
    else:
        return Color(0.0, 0.0, 0.0)


def cast_ray(ray, sphere_list, color, light, eye_point):

    near_pair = first_collision(ray, sphere_list)

    if near_pair == None:
        return Color(1.0, 1.0, 1.0)
    else:
        sphere = near_pair[0]
        point = near_pair[1]

        normal = sphere_normal_at_point(sphere, point)
        epsilon = translate_point(point, scale_vector(normal, 0.01))
        light_normal = normalize_vector(vector_from_to(epsilon, light.pt))
        dot_product = dot_vector(normal, light_normal)

        ambient_color = occlude(sphere.color, sphere.finish, color)
        light_color = cast_light(
            sphere, light, epsilon, dot_product, light_normal, sphere_list
            )
        specular_color = speculate(
            sphere, normal, light_normal, epsilon, 
            dot_product, eye_point, light.color
            )
        
        return add_colors(ambient_color, light_color, specular_color)
    
              
def get_window(min_x, max_x, min_y, max_y, width, height):

    dx = float(max_x - min_x)/width
    dy = float(max_y - min_y)/height

    pixels = []

    for j in range(int(height)):
        for i in range(int(width)):
            pixels.append(Point(min_x + dx*i, max_y - dy*j, 0))

    return pixels


def cast_all_rays(
    min_x, max_x, min_y, max_y, width, height, 
    eye_point, sphere_list, color, light
    ):

    pixels = get_window(min_x, max_x, min_y, max_y, width, height)

    color_list = [
        cast_ray(
            Ray(eye_point, vector_from_to(eye_point, pixel)), 
            sphere_list, color, light, eye_point
            )
        for pixel in pixels
        ]

    return convert(color_list)


if __name__ == '__main__':
    pass
