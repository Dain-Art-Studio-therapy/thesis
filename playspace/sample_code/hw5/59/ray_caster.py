import sys
from commandline import *
from cast import *


NUM_ARGUMENTS = 11


def main(argv):
   
   def process_file(file):
      elements = []
      line_num = 1

      with open_file(file, 'rb') as f:
         for line in f:
            current = process_line(line, line_num)
            if current is not None:
               elements.append(current)
            line_num += 1
         return elements


   def process_line(line, line_num):
      l = line.split()
      error = False

      if len(l) != NUM_ARGUMENTS:
         error = True

      else:
         try:
            return [float(i) for i in l]
         except:
            error = True

      if error == True:
         print >> sys.stderr, ('Malformed sphere on line {0} ... skipping'.
            format(line_num))

      return None


   def initialize_spheres(file):
      sphere_elements = process_file(file)
      sphere_list = []
      
      for sphere in sphere_elements:
         center = Point(sphere[0], sphere[1], sphere[2])
         radius = sphere[3]
         color = Color(sphere[4], sphere[5], sphere[6])
         finish = Finish(sphere[7], sphere[8], sphere[9], sphere[10])

         sphere = Sphere(center, radius, color, finish)
         sphere_list.append(sphere)

      return sphere_list


   def initialize_settings(argv):
      check = check_flags(argv)
      
      eye_point = Point(check[0][0], check[0][1], check[0][2])

      min_x = check[1][0]
      max_x = check[1][1]
      min_y = check[1][2]
      max_y = check[1][3]
      width = int(check[1][4])
      height = int(check[1][5])

      point = Point(check[2][0], check[2][1], check[2][2])
      color = Color(check[2][3], check[2][4], check[2][5])
      light = Light(point, color)
 
      ambient = Color(check[3][0], check[3][1], check[3][2])
         
      return [eye_point, min_x, max_x, min_y, max_y, width, height, light,
         ambient]


   with open('image.ppm', 'wb+') as image:
      if len(argv) < 2:
         return open_file(None, 'rb')

      sphere_list = initialize_spheres(argv[1])
      settings = initialize_settings(argv)

      eye_point, min_x, max_x, min_y, max_y, width, height, light, \
         ambient = settings

      cast = cast_all_rays(min_x, max_x, min_y, max_y, width, height,
         eye_point, sphere_list, ambient, light, eye_point, image)

      print >> image, cast
   

if __name__ == '__main__':
   main(sys.argv)
