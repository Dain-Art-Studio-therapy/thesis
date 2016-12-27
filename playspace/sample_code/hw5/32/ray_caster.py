from data import *
from cast import *
from commandline import *
import sys


def main(args):
   # Get command line info here
   file_name = get_file_name(args)
   in_file = open_file(file_name, 'r')
   
   # Get spheres
   sphere_list = spheres_from_input(in_file)
   in_file.close()
   
   # Process rest of flags
   def_flags = [('-eye',[0.0, 0.0, -14.0]),
            ('-view', [-10.0, 10.0, -7.5, 7.5, 1024, 768]),
            ('-light', [-100.0, 100.0, -100.0, 1.5, 1.5, 1.5]),
            ('-ambient', [1.0, 1.0, 1.0])]
   processed_flags = process_optional_args(args, def_flags)

   # El fin
   write_to_file(sphere_list, processed_flags)


def write_to_file(sphere_list, processed_flags):
   # Get handle on info
   eye_info = processed_flags[0]
   view_info = processed_flags[1]
   light_info = processed_flags[2]
   ambient_info = processed_flags[3]
   
   # Get properties ready
   eye_pt = Point(eye_info[0], eye_info[1], eye_info[2])
   min_x = view_info[0]
   max_x = view_info[1]
   min_y = view_info[2]
   max_y = view_info[3]
   width = view_info[4]
   height = view_info[5]
   amb_color = Color(ambient_info[0], ambient_info[1], ambient_info[2])
   light = Light(Point(light_info[0], light_info[1], light_info[2]),
                 Color(light_info[3], light_info[4], light_info[5]))


   # Write to file
   with open('image.ppm', 'w+') as f:

      # Write info about image
      f.write('P3\n1024 768\n255\n')
      
      # Cast all rays and pass in file
      cast_all_rays(min_x, max_x, min_y, max_y, width, height, eye_pt, sphere_list, amb_color, light, f)


def open_file(name, mode):
   try:
      # Successful opening
      return open(name, mode)
   except IOError as e:
      # Unsuccessful, print error and exit
      print >> sys.stderr, '{0} : {1}'.format(name, e.strerror)
      exit(1)

def spheres_from_input(file):
   sphere_list = []
   line_num = 1
   
   # Iterate through lines
   for line in file:
      vals = line.split()
      
      if len(vals) != 11:
         print 'malformed sphere on line {0} ... skipping'.format(line_num)
         line_num +=1
         continue
      
      try:
         # convert to floats
         for i in range(len(vals)):
            vals[i] = float(vals[i])
         # Make a sphere
         new_s = (Sphere(Point(vals[0], vals[1], vals[2]), vals[3],
                 Color(vals[4], vals[5], vals[6]),
                 Finish(vals[7], vals[8], vals[9], vals[10])))
         sphere_list.append(new_s)
      except:
         print 'malformed sphere on line {0} ... skipping'.format(line_num)
      line_num += 1

   return sphere_list


# Only run main function
if __name__ == '__main__':
   main(sys.argv)