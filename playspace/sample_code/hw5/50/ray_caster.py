#Contains main function and supporting I/O functions
#I/O functions implement the required functionality of the assignment
import sys
import data
import commandline
import cast

def set_comp(components, line):
   if len(components) == 11:
      color = data.Color(0.0, 0.0, 0.0)
      finish = data.Finish(0.0, 0.0, 0.0, 0.0)
      center = data.Point(0.0, 0.0, 0.0)
      radius = 0.0
      center.x = float(components[0])
      center.y = float(components[1])
      center.z = float(components[2])
      radius = float(components[3])
      color.r = float(components[4])
      color.g = float(components[5])
      color.b = float(components[6])
      finish.ambient = float(components[7])
      finish.diffuse = float(components[8])
      finish.specular = float(components[9])
      finish.roughness = float(components[10])
      sphere = data.Sphere(center, radius, color, finish)
   
   else:
      print >> sys.stderr,"malformed sphere on line %d ... skipping" % (line)

   return sphere

def get_spheres(file):
   spheres = []
   line_num = 0
   with commandline.open_file(file, 'rb') as f:
      for line in f:
         line_num += 1
         components = line.split()
         spheres.append(set_comp(components, line))
   return spheres
   
def main(argv):
   if len(argv) >= 2 and len(argv) <= 24:
      sphere_list = get_spheres(argv[1])
      eye_point = data.Point(0.0, 0.0, -14.0)
      min_x = -10
      max_x = 10
      min_y = -7.5
      max_y = 7.5
      width = 1024
      height = 768
      point_light = data.Light(data.Point(-100.0, 100.0, -100.0), \
         data.Color(1.5, 1.5, 1.5))
      a_color = data.Color(1.0, 1.0, 1.0)
      
      variable_list = [eye_point, min_x, max_x, min_y, max_y, width, height,\
         point_light, a_color]
      
      for i in range(2, len(argv)):
         commandline.set_components(i, argv, variable_list)
   
      with open("image.ppm", "r+b") as f:
         f.write("P3\n%d %d\n255\n" %(width, height))
         cast.cast_all_rays(variable_list[1], variable_list[2], 
            variable_list[3], variable_list[4], variable_list[5], 
            variable_list[6], variable_list[0], sphere_list, variable_list[8],
            variable_list[7], f)

   else:
      print >> sys.stderr, "usage: python ray_caster.py <filename> \
         [-eye x y z] [-view min_x max_x min_y max_y width height] \
         [-light x y z r g b] [ambient r g b]"
      
if __name__ == '__main__':
   main(sys.argv)
   
   
