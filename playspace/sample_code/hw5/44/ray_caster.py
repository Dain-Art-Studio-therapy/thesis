import cast
import commandline
import sys
import data

OUTPUT_FILE = "image.ppm"

def numeric_check(s):
   try:
      float(s)
   except ValueError:
      return False
   else:
      return True

def check_nums_in_list(ls):
   for e in ls:
      if numeric_check(e):
         pass
      else:
         return []
   return [float(el) for el in ls]

def file_to_spherelist(file):
#Format:   x y z radius r g b ambient diffuse specular roughness
   sphere_list = []
   with open(file,'rb') as f:
      i = 1
      for line in f:
         ls = line.split()
         if len(ls) == 11:
            nl = check_nums_in_list(ls) #nl = new_list
            if nl:
               sphere = data.Sphere(data.Point(nl[0],nl[1],nl[2]),nl[3],
                  data.Color(nl[4],nl[5],nl[6]),
                  data.Finish(nl[7],nl[8],nl[9],nl[10]))
               sphere_list.append(sphere)
         else:
            print 'malformed sphere on line ' + str(i) + ' ... skipping'
         i += 1
   return sphere_list

def main(argv):
   try:
      file,eye,mn_x,mx_x,mn_y,mx_y,w,h,lt,amb = commandline.cmd_processing(argv)
   except ValueError as e:
      print "Value Error({0}): {1}".format(e.errno, e.strerror)
      sys.exit(0)
   try:
      sphere_list = file_to_spherelist(file)
   except IOError as e:
      print "File error({0}): {1}".format(e.errno, e.strerror)
      sys.exit(0)
   output_list = cast.cast_all_rays(mn_x,mx_x,mn_y,mx_y,w,h,eye,
      sphere_list,amb,lt)
   print_to_file(output_list,OUTPUT_FILE)

def print_to_file(list,file):
   with open(file,'wb') as f:
      f.write('{0}\n'.format(list[0]))
      f.write('{0} {1}\n'.format(list[1],list[2]))
      f.write('{0}\n'.format(list[3]))
      for i in range(4,len(list)):
         f.write('{0} '.format(list[i]))

if __name__ == '__main__':
   main(sys.argv)
