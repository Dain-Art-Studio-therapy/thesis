import sys
import data
import vector_math
import collisions
import cast
import commandline


def main(argv):
   args = commandline.get_values(argv)
   fileobject = open('image.ppm','wb') 

   print >> fileobject,  'P3',args[6],args[7],'255'
   try:
      with open(args[0],'rb') as spheres:
         Sphere_list = create_sphere_list(spheres)
         cast.cast_all_rays(args[2],
                   args[3],
                   args[4],
                   args[5],
                   args[6],
                   args[7],
                   args[1],
                   Sphere_list,
                   args[9],
                   args[8],
                   fileobject)
   except IOError:
      print 'Invalid File Name'
      exit


def create_sphere_list(s):
   Sphere_list = []
   current_line = 0
   for line in s:
      current_line += 1
      values = line.split()
      try:
         position = data.Point(float(values[0]),
                               float(values[1]),
                               float(values[2]))
         radius = float(values[3])
         color = data.Color(float(values[4]),
                            float(values[5]),
                            float(values[6]))
         finish = data.Finish(float(values[7]),
                              float(values[8]),
                              float(values[9]),
                              float(values[10]))
         sphere = data.Sphere(position,
                 radius,
                 color,
                 finish)     
         Sphere_list.append(sphere) 
      except IndexError:
         print  'Invalid sphere on line',current_line,'..skipping'
      except ValueError:
         print  'Invalid sphere on line',current_line,'..skipping'
   return   Sphere_list




if __name__=='__main__':
   main(sys.argv)
