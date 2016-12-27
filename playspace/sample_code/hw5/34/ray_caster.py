import sys
from cast import *
from data import *
from commandline import *

def open_file(filename, mode):
   try:
      return open(filename, mode)
   except IOError as e:
      print>>sys.stderr, '{0}:{1}'.format(filename, e.strerror)
      exit(1)

def default_values():
   eye = Point(0.0,0.0,-14.0)
   min_x = -10
   max_x = 10
   min_y = -7.5
   max_y = 7.5
   width = 1024
   height = 768
   view = [min_x,max_x,min_y,max_y,width,height]
   light = Light(Point(-100.0,100.0,-100.0), Color(1.5,1.5,1.5))
   ambient = Color(1.0,1.0,1.0)   
   list = [view[0],view[1],view[2],view[3],view[4],view[5],eye,ambient,light]
   return list

def process_file(filename):
   list_of_spheres = []
   line_num = 0
   for line in filename:
      strang = line.split()
      line_num += 1
      s = []
      for flt in strang:
         try:
            att = float(flt)
            s.append(att)
         except:
            print>>sys.stderr, 'malformed sphere on line',line_num , '...skipping'
      if len(s) == 11:
            sffere = Sphere(Point(s[0],s[1],s[2]),s[3],Color(s[4],s[5],s[6]),Finish(s[7],s[8],s[9],s[10]))
            list_of_spheres.append(sffere)
      else:
         print>>sys.stderr, 'malformed sphere on line', line_num, '...skipping'   
   return list_of_spheres

def main(argv):
   IMG = open('image.ppm', 'wb')
   with open_file(argv[1], 'rb') as f:
      l = default_values()
      l[6] = comi_eye(argv, l[6])
      view_list = comi_view(argv, l[0],l[1],l[2],l[3],l[4],l[5])
      l[0] = view_list[0]
      l[1] = view_list[1]
      l[2] = view_list[2]
      l[3] = view_list[3]
      l[4] = view_list[4]
      l[5] = view_list[5]
      l[8] = comi_light(argv, l[8])
      l[7] = comi_ambient(argv, l[7])
      spheres = process_file(f)
      print>>IMG, 'P3', l[4], l[5], 255
      cast_all_rays(l[0],l[1],l[2],l[3],l[4],l[5],l[6],spheres,l[7],l[8])
   IMG.close()

if __name__=='__main__':
   main(sys.argv)
