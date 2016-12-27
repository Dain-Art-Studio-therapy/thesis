import sys
import data
import cast
import commandline

def main(argv):
   outfile = open_file('image.ppm', 'w')
   outfile.write('P3\n')
   sphere_list = []
   if len(argv) > 1:
      with open_file(argv[1], 'rb') as f:
         spheres = process_file(f)
         sphere_list = spheres
         arguments = commandline.arguments(argv)
         minx = arguments[1][0]
         maxx = arguments[1][1]
         miny = arguments[1][2]
         maxy = arguments[1][3]
         width = arguments[1][4]
         height = arguments[1][5]
         eye_point = arguments[0]
         ambient_light = arguments[3]
         light = arguments[2]

         print ambient_light.r
         print ambient_light.g
         print ambient_light.b

         outfile.write(str(width) + '\n')
         outfile.write(str(height) + '\n')
         outfile.write('255\n')

         if len(argv) > 2:
            usage_printer = commandline.usage(argv)
            if usage_printer != '':
               print usage_printer

         cast.cast_all_rays(minx, maxx, miny, maxy, width, height, eye_point, sphere_list, ambient_light, light, outfile)
#         cast.cast_all_rays(-10, 10, -7.5, 7.5, 1024, 768, data.Point(0.0, 0.0, -14.0), sphere_list, data.Color(1.0, 1.0, 1.0), data.Light(data.Point(-100, 100, -100), data.Color(1.5, 1.5, 1.5)), outfile)
   else:
      print 'Not Enough Command Line Arguments'
      exit(1)

def open_file(name, method):
   try:
      return open(name, method)

   except IOError as e:
      print >> sys.stderr, '{0} : {1}'.format(name, e.strerror)
      exit(1)

def process_file(f):
   spheres = []
   for line in f:
      list_strings = line.split()
      if len(list_strings) == 11:
         list_floats = str_to_float_list(list_strings)
         spheres.append(sphere_creator(list_floats))
      else:
         print 'Malformed sphere ... skipping'
         exit(1)
   return spheres

def str_to_float_list(list):
   newList = []
   for n in list:
      try:
         newList.append(float(n))
      except IOError as e:
         print 'IO', e
         exit(1)
   return newList

def sphere_creator(list):
   try:
      sphere_point = data.Point(list[0], list[1], list[2])
      sphere_radius = list[3]
      sphere_color = data.Color(list[4], list[5], list[6])
      sphere_finish = data.Finish(list[7], list[8], list[9], list[10])
      return data.Sphere(sphere_point, sphere_radius, sphere_color, sphere_finish)
   except IOError as e:
      print 'IO', e
      exit(1)

if __name__ == '__main__':
   main(sys.argv)
