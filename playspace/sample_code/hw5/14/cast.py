from collisions import *
import vector_math
import data
import math
import sys

# if distance from nearest sphere intersection point to light is < light to sphere
def distance(point1,point2):
    return math.sqrt((point1.x-point2.x)**2 + (point1.y-point2.y)**2)



def nearest_sphere(sphere_list,ray):
    #sphere_list = list of spheres and corresponding intersection points
    smallest = 0
    for i in range(1, len(sphere_list)):
        d = distance(ray.pt, sphere_list[i][1])
        if d < distance(ray.pt, sphere_list[smallest][1]):
            smallest = i
    return smallest


def color_times_finish(sphere_finish, sphere_color):
    r = sphere_color.r * sphere_finish.ambient
    g = sphere_color.g * sphere_finish.ambient
    b = sphere_color.b * sphere_finish.ambient
    return data.Color(r, g, b)


def color_times_color(color1, color2):
    r = color1.r * color2.r
    g = color1.g * color2.g
    b = color1.b * color2.b
    return data.Color(r, g, b)


def color_times_value(color, value):
    r = value * color.r
    g = value * color.g
    b = value * color.b
    return data.Color(r, g, b)


def color_plus_color(color1, color2):
    r = color1.r + color2.r
    g = color1.g + color2.g
    b = color1.b + color2.b
    return data.Color(r, g, b)


#no intersection = white,
#nearest sphere = red,
#other spheres = blue

def cast_ray(ray,sphere_list,color,light,point):
        n = find_intersection_points(sphere_list,ray) # n returns a list with spheres and corresponding intersection points
        if n == []:
            return data.Color(1.0,1.0,1.0)

        l = nearest_sphere(n, ray) #returns index of smallest sphere
        sphere_finish = n[l][0].finish
        sphere_color = n[l][0].color

        #finish.ambient times color
        finish_times_color = color_times_finish(sphere_finish, sphere_color) #sphere color x finish ambiance

        #finish_times_color x color
        color_times_ambiance = color_times_color(finish_times_color, color)

        sphere_normal = sphere_normal_at_point(n[l][0], n[l][1])
        shorter_vector = vector_math.scale_vector(sphere_normal, 0.01)
        p3 = vector_math.translate_point(n[l][1],shorter_vector) #returns point
        point_diff = vector_math.difference_point(light.point, p3) #returns vector
        Ldir = normalize_vector(point_diff)
        visible = vector_math.dot_vector(sphere_normal,Ldir)
        ray1 = data.Ray(p3, Ldir)
        list_2 = find_intersection_points(sphere_list, ray1) #[(s,i),(s,i)]


        if visible > 0 and list_2 == []:

            #dot product times light color
            dot_times_light_color = color_times_value(light.color,visible)

            #new light color times sphere color
            light_color_times_sphere_color= color_times_color(dot_times_light_color,sphere_color)

            #diffuse times sphere color
            sphere_diffuse = n[l][0].finish.diffuse
            diffuse_times_sphere_color = color_times_value(light_color_times_sphere_color, sphere_diffuse)

            #ambiance plus diffuse
            ambiance_plus_diffuse = color_plus_color(color_times_ambiance, diffuse_times_sphere_color)

            #part 5
            scalar = 2 * visible
            vector_1 = vector_math.scale_vector(sphere_normal, scalar)
            reflection_vector = vector_math.difference_vector(vector_1, Ldir)
            point_diff_2 = vector_math.difference_point(point, p3)
            Vdir = vector_math.normalize_vector(point_diff_2)
            specular_intensity = vector_math.dot_vector(Vdir, reflection_vector)

            if specular_intensity > 0:

                #light color times sphere's specular
                sphere_specular =  n[l][0].finish.specular
                color_times_specular = color_times_value(light.color,sphere_specular)

                #specular times intensity
                roughness_divided = 1/n[l][0].finish.roughness
                raised_specular = specular_intensity ** roughness_divided
                specular_times_intensity = color_times_value(color_times_specular, raised_specular)

                #specular times intensity PLUS ambiance times diffuse
                spec_and_diffuse = color_plus_color(specular_times_intensity,ambiance_plus_diffuse)

                return spec_and_diffuse

            else:
                return ambiance_plus_diffuse

        else:
            return color_times_ambiance



def cast_all_rays(min_x,max_x,min_y,max_y,width,height,eye_point,sphere_list,color,light,file_object):
    print >> file_object, 'P3'
    print >> file_object, str(width) + ' ' + str(height)
    print >> file_object, '255'

    #finds how many pixels in width and height
    dx = (max_x - min_x)/float(width)
    dy = (max_y - min_y)/float(height)
    for y in (range(height)):
        #for each y in height of image
        for x in(range(width)):
            image_point = data.Point(min_x + x * dx, max_y - y * dy, 0)
            vector = vector_math.vector_from_to(eye_point, image_point)
            ray1 = data.Ray(eye_point, vector)
            col = cast_ray(ray1, sphere_list, color, light, eye_point)
            col_r = int(col.r * 255)
            col_g = int(col.g * 255)
            col_b = int(col.b * 255)

            if col_r > 255:
                col_r = 255

            if col_g > 255:
                col_g = 255

            if col_b > 255:
                col_b = 255



            print >> file_object, col_r, col_g, col_b




