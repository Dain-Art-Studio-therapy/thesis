import sys
from cast import *

def cast_all_rays_from_file(filename, eye_point, view, light, ambient):
   sphere_list = get_spheres_from_file(filename)
   print "Generating", len(sphere_list), "spheres!"
   # [-eye x y z] [-view min_x max_x min_y max_y width height] [-light x y z r g b] [-ambient r g b]
   print "EYE", eye_point.x, eye_point.y, eye_point.z
   print "VIEW", view.min_x, view.max_x, view.min_y, view.max_y, view.width, view.height
   print "LIGHT", light.pt.x, light.pt.y, light.pt.z, light.color.r, light.color.g, light.color.b
   print "AMBIENT", ambient.r, ambient.g, ambient.b
   cast_all_rays(view, eye_point, sphere_list, ambient, light)

def get_spheres_from_file(filename):
   with open_file(filename, 'rb') as f:
      sphere_list = []
      for index, line in enumerate(f, 1):
         values = line.split()
         try:
            if len(values) == 12:
               print "malformed sphere on line " + index + "...skipping"
            else:
               n = [float(i) for i in values]
               # x y z radius r g b ambient diffuse specular roughness
               sphere = Sphere(Point(n[0], n[1], n[2]), n[3], Color(n[4], n[5], n[6]), Finish(n[7], n[8], n[9], n[10]))
               sphere_list.append(sphere)
         except:
            print "malformed sphere on line " + str(index) + "...skipping"
      return sphere_list

def open_file(name, mode):
   try:
      return open(name, mode)
   except IOError as e:
      print >> sys.stderr, '{0} : {1}'.format(name, e.strerror)
      exit(1)
