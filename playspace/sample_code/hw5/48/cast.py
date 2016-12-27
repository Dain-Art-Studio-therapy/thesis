from collisions import *
from data import *
from vector_math import *
import sys

def cast_ray(ray,sphere_list,ambientColor,light,eyePoint):
        closest = find_closest_point(ray,sphere_list)
	if closest != None:
            ##ADD TOGETHER THE MODIFICATIONS MADE TO THE SPHERE
                amb =  scale_color(closest[0].color,closest[0].finish.ambient)
                amb1 = reflect_light(amb,ambientColor)
                diffColor = calculate_light_behavior(closest[1],closest[0],sphere_list,light)
                part4 = add_color(amb1,diffColor)
                spec = calculate_specular(closest[1],closest[0],light,eyePoint)                
                return add_color(part4,spec)
        else:
                return Color(1.0,1.0,1.0)
def find_closest_point(ray,sphere_list):

	##get all the intersection points for the ray
        L = find_intersection_points(sphere_list,ray)
        if L != []:
                closest = L[0]
                ##search the list for the closest point
                for i in range(1,len(L)):
                        point = L[i][1]
                        vec = difference_point(ray.pt,point)
                        dist = length_vector(vec)
                        controlvec = difference_point(ray.pt,closest[1])
                        controldist = length_vector(controlvec)
                        if dist<controldist:
                                closest = L[i]
                        else:
                                pass
                return closest

def calculate_specular(point,sphere,light,eyePoint):
        translate = scale_vector(sphere_normal_at_point(sphere,point),0.01)
        pointe = translate_point(point,translate)
        ldir = vector_from_to(pointe,light.point)
        nldir = normalize_vector(ldir)
        normal = sphere_normal_at_point(sphere,point)
        dot = dot_vector(normal,nldir)
        vdir = vector_from_to(eyePoint,pointe)
        nvdir = normalize_vector(vdir)
        reflecVec  = Vector(0,0,0)
        reflecVec.x = nldir.x - (2 * dot) * normal.x
        reflecVec.y = nldir.y - (2 * dot) * normal.y
        reflecVec.z = nldir.z - (2 * dot) * normal.z
        intensity = dot_vector(nvdir, reflecVec)
        if intensity > 0:
                newr = light.color.r * sphere.finish.specular * intensity**(1.0/sphere.finish.roughness)
                newg = light.color.g * sphere.finish.specular * intensity**(1.0/sphere.finish.roughness)
                newb = light.color.b * sphere.finish.specular * intensity**(1.0/sphere.finish.roughness)
                spec = Color(newr,newg,newb)
        else:
                spec = Color(0.0,0.0,0.0)
        return spec

def calculate_light_behavior(point,sphere,sphereList,light):
        translate = scale_vector(sphere_normal_at_point(sphere,point),0.01)
        pointe = translate_point(point,translate)
        ldir = vector_from_to(pointe,light.point)
        nldir = normalize_vector(ldir)
        normal = sphere_normal_at_point(sphere,point)
        dot = dot_vector(normal,nldir)
        ray = Ray(light.point,ldir)
        oppRay = Ray(pointe,vector_from_to(pointe,light.point))
        closest_sphere = find_intersection_points(sphereList,oppRay)
        if closest_sphere == []:
                if dot > 0:
                        new_r = sphere.color.r * light.color.r * sphere.finish.diffuse * dot
                        new_g = sphere.color.g * light.color.g * sphere.finish.diffuse * dot
                        new_b = sphere.color.b * light.color.b * sphere.finish.diffuse * dot
                        newColor = Color(new_r,new_g,new_b)
                        return newColor
                else:
                        return Color(0.0,0.0,0.0)
        else:
                return Color(0.0,0.0,0.0)

def cast_all_rays(min_x,max_x,min_y,max_y,width,height,eye_point,sphere_list,ambientColor,light):
        delta_x = float(max_x-min_x)/width
        delta_y = float(max_y-min_y)/height
        pointList = []
        intersections = []
  ##CREATE A POINT LIST
        for y in range(int(height),0, -1):
                for x in range(int(width)):
                        point = Point(x*delta_x + min_x, y*delta_y+min_y,0)
                        pointList.append(point)
  ##USE POINT LIST TO CHECK IF INTERSECTING WITH A SPHERE
        image =  open('image.ppm','wb')
        print_header(int(height),int(width),image)
        for i in range(len(pointList)):
                ####print >> sys.stderr, i/float(len(pointList))
                thisRay = ray_from_to(eye_point,pointList[i])
                pixelColor =  cast_ray(thisRay,sphere_list,ambientColor,light,eye_point)
                if pixelColor != None:
                        ##black
                       # color = Color(1.0,1.0,1.0)
                       # color = convertColorBit(color)
                       # print color[0],color[1],color[2]
                       # print 0,0,0
                        intColor = convertColorBit(pixelColor)
                        intColor = capColor(intColor)
                        print >> image, int(intColor.r),int(intColor.g),int(intColor.b)
###CAP THE COLOR AT 255 BEFORE PRINTING
                else:
                        ##white
                       # color = Color(0.0,0.0,0.0)
                       # color = convertColorBit(color)
                       # print color[0],color[1],color[2]
                        print >> image, 255,255,255
        image.close()

def print_header(width,height,file):
        print >> file,"P3"
        print >> file,height,width
        print >> file,255

def ray_from_to(point1,point2):
        newVec = difference_point(point2,point1)
        ##using point1 for the ray,,,
        newRay = Ray(point1,newVec)
        return newRay

def convertColorBit(inputColor):
        maxNum = 255
        return scale_color(inputColor,maxNum)

def scale_color(inputColor, maxNum):
        new_r = (inputColor.r*maxNum)
        new_g = (inputColor.g*maxNum)
        new_b = (inputColor.b*maxNum)
        newColor = Color(new_r, new_g,new_b)
        return newColor

def reflect_light(inputColor,lightColor):
        new_r = (inputColor.r*lightColor.r)
        new_g = (inputColor.g*lightColor.g)
        new_b = (inputColor.b*lightColor.b)
        newColor = Color(new_r, new_g, new_b)
        return newColor

def add_color(col1,col2):
        newr = col1.r + col2.r
        newg = col1.g + col2.g
        newb = col1.b + col2.b
        newColor = Color(newr, newg, newb)
        return newColor

def capColor(color):
        if color.r > 255:
                color.r = 255
        if color.g > 255:
                color.g = 255
        if color.b > 255:
                color.b = 255
        return color
