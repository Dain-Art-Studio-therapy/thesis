import sys
from cast import *
from commandline import *
import data

def create_eye(argv):
   eye = obtain_eye_point(argv)
   finish_eye_point = data.Point(eye[0],eye[1],eye[2])
   return finish_eye_point

def create_light(argv):
   light = obtain_light_object(argv)
   light_point = data.Point(light[0],light[1],light[2])
   light_color = data.Color(light[3],light[4],light[5])
   finish_light = data.Light(light_point,light_color)
   return finish_light

def create_ambient(argv):
   ambient = obtain_ambient_color(argv)
   finish_ambient = data.Color(ambient[0],ambient[1],ambient[2])
   return finish_ambient

def create_all_spheres(argv):
   spheres_list = obtain_sphere(argv)
   final_list = []
   for sphere in spheres_list:
      if len(sphere) == 11:
         sphere_center = data.Point(sphere[0],sphere[1],sphere[2])
         sphere_radius = sphere[3]
         sphere_color = data.Color(sphere[4],sphere[5],sphere[6])
         sphere_finish = data.Finish(sphere[7],sphere[8],sphere[9],\
                         sphere[10])
         finish_sphere = data.Sphere(sphere_center,sphere_radius,sphere_color,\
                         sphere_finish)
         final_list.append(finish_sphere)
   return final_list

def main(argv):
   view = obtain_view(argv)
   min_x = view[0]
   max_x = view[1]
   min_y = view[2]
   max_y = view[3]
   width = view[4]
   height = view[5]
   eye_point = create_eye(argv)
   sphere_list = create_all_spheres(argv)
   ambient_color = create_ambient(argv)
   light = create_light(argv)

   cast_all_rays(min_x, max_x, min_y, max_y, width, height, eye_point, sphere_list,\
                ambient_color, light, 'image.ppm')

if __name__ == '__main__':
   main(sys.argv)
