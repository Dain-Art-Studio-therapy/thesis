from collisions import *
from data import *
from vector_math import *

def closest_sphere_index(ray, sphere_list): # helper function
    if sphere_list == []:
        return None
    else:
        closest = 0
        for i in range(len(sphere_list)):
            closest_vector = length_vector(
                vector_from_to(ray.pt, sphere_list[i][1]))
            compared_vector = length_vector(
                vector_from_to(ray.pt, sphere_list[closest][1]))
            if closest_vector < compared_vector: # check for closest sphere
                closest = i
        return closest # index of the closest sphere tuple

def ambient_color_change(sphere, ambient_color): # helper function
    ambient_red = sphere.color.r * ambient_color.r * sphere.finish.ambient
    ambient_green = sphere.color.g * ambient_color.g * sphere.finish.ambient
    ambient_blue = sphere.color.b * ambient_color.b * sphere.finish.ambient
    return Color(ambient_red, ambient_green, ambient_blue)
    # the color of sphere modified by the ambient value

def diffuse_color_change(visible, sphere, light): # helper function
    if visible <= 0: # light is obscured
        return Color(0.0, 0.0, 0.0)
    else:
        diffuse_red = (visible * light.color.r * sphere.color.r * 
                    sphere.finish.diffuse)
        diffuse_green = (visible * light.color.g * sphere.color.g * 
                    sphere.finish.diffuse)
        diffuse_blue = (visible * light.color.b * sphere.color.b * 
                    sphere.finish.diffuse)
    return Color(diffuse_red, diffuse_green, diffuse_blue)
    # the color of sphere modified by the diffuse value

def specular_color_change(light, sphere, specular_intensity): # helper function
    if specular_intensity <= 0: # light is not reflected
        return Color(0.0, 0.0, 0.0)
    else:
        specular_red = (light.color.r * sphere.finish.specular * 
                    (specular_intensity ** (1 / sphere.finish.roughness)))
        specular_green = (light.color.g * sphere.finish.specular * 
                    (specular_intensity ** (1 / sphere.finish.roughness)))
        specular_blue = (light.color.b * sphere.finish.specular * 
                    (specular_intensity ** (1 / sphere.finish.roughness)))
        return Color(specular_red, specular_green, specular_blue)
        # the color of sphere modified by specular and roughness value

def cast_ray(ray, sphere_list, ambient_color, light, eye_point):
    contact_sphere = find_intersection_points(sphere_list, ray)
    if contact_sphere == []:
        return Color(1.0, 1.0, 1.0) # return white color
    else:
        mindex = closest_sphere_index(ray, contact_sphere)
        closest_sphere = contact_sphere[mindex]

        # check for visibility of light
        N = sphere_normal_at_point(closest_sphere[0], closest_sphere[1])
        vector_epsilon = scale_vector(N, 0.01)
        point_epsilon = translate_point(closest_sphere[1], vector_epsilon)
        light_direction = normalize_vector(
                            vector_from_to(point_epsilon, light.pt))
        visible = dot_vector(N, light_direction)

        # check for the specular intensity
        reflection_vector = difference_vector(light_direction, 
                            scale_vector(N, (2 * visible)))
        view = vector_from_to(eye_point, point_epsilon)
        view_direction = normalize_vector(view)
        specular_intensity = dot_vector(reflection_vector, view_direction)

        # check for the path of the light_ray to spheres
        light_ray = Ray(point_epsilon, light_direction)
        light_contact_sphere = find_intersection_points(sphere_list, light_ray)
        light_check = closest_sphere_index(light_ray, light_contact_sphere)

        # modified color value
        finish_ambient = ambient_color_change(closest_sphere[0], ambient_color)
        finish_diffuse = diffuse_color_change(visible, closest_sphere[0], 
                                                light)
        finish_specular = specular_color_change(light, closest_sphere[0], 
                                                specular_intensity)

        if light_contact_sphere != []:
            if (length_vector(vector_from_to(point_epsilon, light.pt)) > 
                length_vector(vector_from_to(point_epsilon, 
                    light_contact_sphere[light_check][1]))): 
                    # light blocked by another sphere
                finish_red = finish_ambient.r + finish_specular.r
                finish_green = finish_ambient.g + finish_specular.g
                finish_blue = finish_ambient.b + finish_specular.b
        else:
            finish_red = (finish_ambient.r + finish_diffuse.r + 
                            finish_specular.r)
            finish_green = (finish_ambient.g + finish_diffuse.g + 
                            finish_specular.g)
            finish_blue = (finish_ambient.b + finish_diffuse.b + 
                            finish_specular.b)

        return Color(finish_red, finish_green, finish_blue)
        # color of the closest sphere modified by ambience

def cast_all_rays(
    min_x, max_x, min_y, max_y, width, height, eye_point, sphere_list, 
    ambient_color, light):
    print 'P3'
    print width, height
    print 255

    dx = (max_x - min_x)/float(width) # change in x, pixel
    dy = (max_y - min_y)/float(height) # change in y, pixel
    
    for y in range(height):
        for x in range(width):
            point = Point(min_x + x * dx, max_y - y * dy, 0)
            ray = Ray(eye_point, difference_point(point, eye_point))
            color_result = cast_ray(ray, sphere_list, ambient_color, light, 
                                    eye_point)
            ppm_red = min(int(color_result.r * 255), 255)
            ppm_green = min(int(color_result.g * 255), 255)
            ppm_blue = min(int(color_result.b * 255), 255)
            print ppm_red, ppm_green, ppm_blue # color in file color format
            