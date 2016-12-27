import collisions
import vector_math
import data
import math
import sys    

def cast_ray(ray, sphere_list, ambient_color, light, eye_point):
    casts = collisions.find_intersection_points(sphere_list, ray)
    intersections = []
    #find intersection nearest to origin and return its sphere's color
    if casts != []:
        for (sphere, intersection) in casts:
            intersections.append(intersection)
        nearest = nearest_point(intersections, ray.pt)
        for i in range(len(casts)):
            if casts[i][1] == nearest:
                used_sphere = casts[i][0]
                finished = add_finish(used_sphere.color, sphere, ambient_color)
                
                intense = add_specular_intensity(intersection, sphere, light, eye_point, finished)
                
                if find_light_direction(nearest, sphere, light) > 0 and (
                check_light_intersection(intersection, sphere, light, sphere_list)):
                    diffused = add_diffuse(intersection, used_sphere, light)
                    return add_colors(diffused, intense)
            
                return intense
    else:
        return data.Color(1.0, 1.0, 1.0)
        
def add_specular_intensity(intersection, sphere, light, eye_point, color):
    pe = compute_off_point(intersection, sphere)
    
    light_direction = vector_math.normalize_vector(
    vector_math.vector_from_to(pe, light.pt))
    
    normal = collisions.sphere_normal_at_point(sphere, intersection)
    
    dot = vector_math.dot_vector(light_direction, normal) 
    
    reflection_vector = vector_math.difference_point(light_direction, 
    vector_math.scale_vector(normal, (2 * dot)))
    
    eye_vector = vector_math.normalize_vector(vector_math.vector_from_to(eye_point, pe))
    
    specular_intensity = vector_math.dot_vector(reflection_vector, 
    eye_vector)
    
    if specular_intensity > 0:
        newr = light.color.r * sphere.finish.specular * specular_intensity**(1/sphere.finish.roughness)
        newg = light.color.g * sphere.finish.specular * specular_intensity**(1/sphere.finish.roughness)
        newb = light.color.b * sphere.finish.specular * specular_intensity**(1/sphere.finish.roughness)
        new_color = data.Color(newr, newg, newb)
        return add_colors(new_color, color)
    else:
        return color
        
        
def add_colors(color1, color2):
    newr = color1.r + color2.r
    newg = color1.g + color2.g
    newb = color1.b + color2.b
    return data.Color(newr, newg, newb)

def compute_off_point(point, sphere):
    normal = collisions.sphere_normal_at_point(sphere, point)
    scaled_normal = vector_math.scale_vector(normal, 0.01)
    return vector_math.translate_point(point, scaled_normal)

def find_light_direction(point, sphere, light):
    normal = collisions.sphere_normal_at_point(sphere, point)
    light_direction = vector_math.normalize_vector(
    vector_math.vector_from_to(compute_off_point(point, sphere), light.pt))
    visible = vector_math.dot_vector(normal, light_direction)
    return visible

def check_light_intersection(point, sphere, light, sphere_list):
    normal = compute_off_point(point, sphere)
    light_direction = vector_math.normalize_vector(
    vector_math.vector_from_to(compute_off_point(point, sphere), light.pt))
    vector = vector_math.vector_from_to(normal, light_direction)
    ray = data.Ray(normal, vector)
    
    intersections = []
    for (sphere, intersection) in collisions.find_intersection_points(
    sphere_list, ray):
        intersections.append(intersection)
    for intersection in intersections:
        
        if euclidean_dist(normal, light.pt) > euclidean_dist(normal, intersection):
            return True
        else:
            return False

def add_diffuse(point, sphere, light):
    dot = find_light_direction(point, sphere, light)
    dot_and_diffuse = dot * sphere.finish.diffuse
    newr = dot * light.color.r * sphere.color.r * sphere.finish.diffuse
    newg = dot * light.color.g * sphere.color.g * sphere.finish.diffuse
    newb = dot * light.color.b * sphere.color.b * sphere.finish.diffuse
    
    return data.Color(newr, newg, newb)

def add_finish(color, sphere, ambient_light):
    newr = color.r * sphere.finish.ambient * ambient_light.r
    newg = color.g * sphere.finish.ambient * ambient_light.g
    newb = color.b * sphere.finish.ambient * ambient_light.b
    return data.Color(newr, newg, newb)
    
def nearest_point(points, point):
    nearest = 0
    for i in range(1, len(points)):
        if euclidean_dist(points[i], point) < euclidean_dist(
        points[nearest], point):
            nearest = i
    return points[nearest]

def euclidean_dist(point1, point2):
    return math.sqrt((point1.x - point2.x)**2 + (point1.y - point2.y)**2 + 
    (point1.z - point2.z)**2)
    
    
def cast_all_rays(min_x, max_x, min_y, max_y, width, 
height, eye_point, sphere_list, ambient_color, light):
    delta_x = (max_x - min_x)/float(width)
    delta_y = (max_y - min_y)/float(height)
    
    pointlist = []
    for y in range(int(height)):
        for x in range(int(width)):
            pointlist.append(data.Point((min_x + x*delta_x), 
            (max_y - y*delta_y), 0))
    
    vectorlist = []
    for point in pointlist:
        vectorlist.append(vector_math.difference_point(point, eye_point))
    
    raylist = []
    for vector in vectorlist:
        raylist.append(data.Ray(eye_point, vector))
    
    pixels = []
    for ray in raylist:
       pixels.append(cast_ray(ray, sphere_list, ambient_color, light, eye_point))
    
    print "P3"
    print width, height
    print 255
    for pixel in pixels:
        color = data.convert_color(pixel)
        print color[0], color[1], color[2]