import data 
import collisions
import math
import vector_math 
import utility

def cast_ray(ray, sphere_list, color, light, eye_point):
    intersection_list = collisions.find_intersection_points(sphere_list, ray)
    if intersection_list != []: 
        mindex = closest_sphere(intersection_list, ray.pt)
        return finish_all(intersection_list, mindex, eye_point, light, color, sphere_list, ray)  
    return data.Color(1.0, 1.0, 1.0)  
    
def cast_all_rays(min_x, max_x, min_y, max_y, width, height, eye_point, sphere_list, ambient_color, light):  
    x_length = max_x - min_x
    y_length = max_y - min_y 
    delta_x = x_length/width
    delta_y = y_length/height 
    for y in xrange(height): 
        for x in xrange(width):
            color = cast_ray(data.Ray(eye_point, vector_math.vector_from_to(eye_point, data.Point(min_x + x * delta_x, max_y - y*delta_y, 0))), sphere_list, ambient_color, light, eye_point)
            print int(min(255 * color.r, 255)), int(min(255 * color.g, 255)),int(min(255 * color.b, 255))
def closest_sphere(list_of_tuples, eye_point):
    list_of_points = [b for (a,b) in list_of_tuples]
    mindex = 0
    for point in list_of_points:
        if distance(eye_point, point)<distance(eye_point, list_of_points[mindex]):
            mindex = list_of_points.index(point)
    return mindex

def distance(point1, point2):
    distance_vector = vector_math.difference_point(point1, point2)
    return vector_math.length_vector(distance_vector)

def finish_ambient(color, sphere):
    return data.Color(sphere.color.r * color.r * sphere.finish.ambient, sphere.color.g * color.g * sphere.finish.ambient, sphere.color.b * color.b * sphere.finish.ambient)
    
def find_n(point, sphere):
    return collisions.sphere_normal_at_point(sphere, point)
    #vector_math.normalize_vector(vector_math.vector_from_to(point, eye_point)) 
def find_new_point(point, eye_point, sphere): 
    return vector_math.translate_point(point, vector_math.scale_vector(find_n(point, sphere), 0.01)) 

def find_light_dir(sphere, point, point2):
    normal = collisions.sphere_normal_at_point(sphere, point)
    new_point = find_new_point(point, normal, sphere)
    return vector_math.normalize_vector(vector_math.vector_from_to(new_point, point2)) 

def find_point_normal(sphere, point, light, eye_point):
    new_point = find_new_point(point, eye_point, sphere)
    return vector_math.dot_vector(find_n(new_point, sphere), find_light_dir(sphere, new_point, light.pt)) 

def finish_diffuse(tuple_list, index, eye_point, light, sphere_list, ray):
    col = data.Color(0, 0, 0)
    new_tuple_list = collisions.find_intersection_points(sphere_list, data.Ray(light.pt, vector_math.vector_from_to(light.pt, tuple_list[index][1]))) 
    new_index = closest_sphere(new_tuple_list, light.pt)  
    point_normal = find_point_normal(tuple_list[index][0], tuple_list[index][1], light, eye_point) 
    if tuple_list[index][0] != new_tuple_list[new_index][0]:
        return col 
    if point_normal > 0: 
        col.r = point_normal * light.color.r * tuple_list[index][0].color.r * tuple_list[index][0].finish.diffuse
        col.g = point_normal * light.color.g * tuple_list[index][0].color.g * tuple_list[index][0].finish.diffuse
        col.b = point_normal * light.color.b * tuple_list[index][0].color.b * tuple_list[index][0].finish.diffuse 
    return col 

def finish_specular(point, eye_point, sphere, light): 
    new_point = find_new_point(point, eye_point, sphere) # Two parts of the intersection tuple and the eye_point 
    ldir = find_light_dir(sphere, new_point, light.pt)    
    n = find_n(point, sphere) 
    light_n = find_point_normal(sphere, point, light, eye_point)     
    reflect_vec = vector_math.difference_vector(ldir, vector_math.scale_vector(n, (2 * light_n)))  
    vdir = find_light_dir(sphere, eye_point, new_point) 
    spec = vector_math.dot_vector(reflect_vec, vdir) 
    col = data.Color(0, 0, 0) 
    if spec > 0:  
        col.r = light.color.r * sphere.finish.specular * spec ** (1/sphere.finish.roughness)    
        col.g = light.color.g * sphere.finish.specular * spec ** (1/sphere.finish.roughness)
        col.b = light.color.b * sphere.finish.specular * spec ** (1/sphere.finish.roughness) 
    return col

def finish_all(tuple_list, index, eye_point, light, color, sphere_list, ray):
    col = finish_ambient(color, tuple_list[index][0]) 
    diff = finish_diffuse(tuple_list, index, eye_point, light, sphere_list, ray)
    spec = finish_specular(tuple_list[index][1], eye_point, tuple_list[index][0], light) 
    return data.Color(col.r + spec.r + diff.r, col.g + spec.g + diff.g, col.b + spec.b + diff.b) 
    


