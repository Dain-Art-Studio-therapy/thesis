import cast
import commandline
import data
import sys

def main():
   sphere_list = input_to_sphere_list() 
   try:
      pixel_list = commandline.process_cmdline(sphere_list)
   except:
      print >> sys.stderr, "Failed to run program."
      exit(1)

   try:
      output_file('image.ppm', pixel_list)
   except: 
      print >> sys.stderr, "Cannot print to file."
      exit(1)


# HELPER FUNCTIONS 

def output_file(file_name, pixel_list):
   HEADER = 'P3 \n1024 768 \n255 \n'
   output = open(file_name, 'w')
   output.write(HEADER)
   for pixel in pixel_list:
      print >> output, pixel[0], pixel [1], pixel[2]
   output.close()


def input_to_sphere_list():
   sphere_list = []
   try:
      input_file = open(sys.argv[1], 'rb')
   except:
      print >> sys.stderr,"Cannot open file given."
      exit(1)
   for num, line in enumerate(input_file, 1):
      sphere = make_sphere(line)
      if sphere is False:
         print >> sys.stderr, "Malformed sphere on line", num, "...skipping"
      else:
         sphere_list.append(sphere)
   input_file.close()
   return sphere_list

def make_sphere(line):
   parts = line.split( ) #sphere elements in a list
   if len(parts) != 11:
      return False
   try:
      sCenter = data.Point(float(parts[0]), float(parts[1]), float(parts[2]))
      sRadius = float(parts[3])
      sColor = data.Color(float(parts[4]), float(parts[5]), float(parts[6]))
      sFinish = data.Finish(float(parts[7]), float(parts[8]), float(parts[9]),\
         float(parts[10]))
      sphere = data.Sphere(sCenter, sRadius, sColor, sFinish)
      return sphere
   except:
      return False

if __name__ == "__main__":
   main()




# Extras//Left-out Code
##   larger_sphere = data.Sphere(data.Point(1.0, 1.0, 0.0), 2.0, \
#      data.Color(0.0, 0.0, 1.0), data.Finish(0.2, 0.4, 0.5, 0.05))
#   smaller_sphere = data.Sphere(data.Point(0.5, 1.5, -3.0), 0.5,\
#      data.Color(1.0, 0.0, 0.0), data.Finish(0.4, 0.4, 0.5, 0.05))   
#   sphere_list1 = [larger_sphere, smaller_sphere]
#   
##       pixel_list = cast.cast_all_rays(-10, 10, -7.5, 7.5, 1024, 768,\
#         data.Point(0.0, 0.0, -14.0), sphere_list, \
#         data.Color(1.0, 1.0, 1.0),\
#         data.Light(data.Point(-100.0, 100.0, -100.0), \
#         data.Color(1.5, 1.5, 1.5)))