import sys
from commandline import * 
from cast import *
from data import *

def main(argv):
   try:
      with open(argv[1], 'rb') as f:
         colors = process_file(f, sys.argv)
      print_to_file(colors)
   except:
      print 'Given file could not be found'

def process_file(f, argv):
   color_list = []
   sphere_list = file_to_list(f)
   eye_point = set_eye(argv)
   min_x, max_x, min_y, max_y, width, height = set_view(argv)
   light = set_light(argv)
   color = set_ambient(argv)
   color_list = cast_all_rays(min_x, max_x, min_y, max_y, width, height, 
                          eye_point, sphere_list, color, light)
   return color_list
   
   

def file_to_list(f):
   sphere_list = []
   counter = 1
   s = 'Malformed sphere on line %r...skipping' % counter
   for line in f:
      nums = line.split(' ')
      if len(nums) != 11:
         sphere_list.append(s)
      else: 
         try:
            sphere = Sphere(Point(float(nums[0]), float(nums[1]), 
                     float(nums[2])), float(nums[3]), Color(float(nums[4]),
                     float(nums[5]), float(nums[6])), Finish(float(nums[7]),
                     float(nums[8]), float(nums[9]), float(nums[10])))
            sphere_list.append(sphere)
         except:
            sphere_list.append(s)
   return sphere_list
   
def print_to_file(color_list):
   output_file = open('image.ppm', 'w')
   print >> output_file, 'P3'
   print >> output_file, '1024 768'
   print >> output_file, '255'
   for color in color_list:
      print >> output_file, color.r, color.g, color.b

main(sys.argv)
