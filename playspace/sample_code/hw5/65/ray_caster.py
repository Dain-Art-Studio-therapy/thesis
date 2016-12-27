# Han Tran || CPE101-01,02 || Assignment 5
# ray_caster.py -- contains a main function and supporting I/O functions
#               that implement the required functionality of the assignment

import commandline
import cast
import data
import sys



def main():
   setting_vals = commandline.read_commandline(sys.argv)
   print 'Current flags values are: \n'
   print setting_vals
   min_x = setting_vals[3]
   max_x = setting_vals[4]
   min_y = setting_vals[5]
   max_y = setting_vals[6]
   width = setting_vals[7]
   height = setting_vals[8]
   eye_pt = data.Point(setting_vals[0], setting_vals[1], setting_vals[2])
   ambient = data.Color(setting_vals[15], setting_vals[16], setting_vals[17])
   light = data.Light(data.Point(setting_vals[9], setting_vals[10],
                                 setting_vals[11]), 
                      data.Color(setting_vals[12], setting_vals[13],
                                 setting_vals[14]))
   sp_list = read_file(sys.argv, 'r')
   final_ls = cast.cast_all_rays(min_x, max_x, min_y, max_y, width,
                                height, eye_pt, sp_list, ambient, light)
   header = final_ls[0:4]
   colors = final_ls[4:len(final_ls)]
   write_into_file(header, colors)


# ---- Supportive Function ---- #
def write_into_file(header_argv, colors_argv):
   with open('image.ppm', 'w') as f:
      print_header(header_argv, f) 
      print_colors(colors_argv, f)



def print_header(printstuff, f):
   f.write(str(printstuff[0]) + '\n')   # 'P3'
   f.write(str(printstuff[2]) + ' ' + str(printstuff[3]) + '\n') # w + h
   f.write(str(printstuff[1]) + '\n')   # '255'



def print_colors(printcolor, f):
   max_output_color = 255
   for i in range(0, len(printcolor)/3):
      f.write(str(int(min(printcolor[i*3], 1.0)*max_output_color)) + ' ')
      f.write(str(int(min(printcolor[i*3 + 1], 1.0)*max_output_color)) + ' ')
      f.write(str(int(min(printcolor[i*3 + 2], 1.0)*max_output_color)) + '\n')



# Read the input file and convert them into a sphere list
def read_file(argv, mode):
   if len(argv) < 2:
      print 'Error: Not enough input argument.' 
      exit
   else:
      with open_file(argv[1], mode) as f:
         sp_list = []
         for line in f:
            newLine = line.split()
            if len(newLine) == 11 and list_is_numeric(newLine):
                  newLine = map(float, newLine)
                  center = data.Point(newLine[0], newLine[1], newLine[2])
                  radius = newLine[3]
                  color = data.Color(newLine[4], newLine[5], newLine[6])
                  finish = data.Finish(newLine[7], newLine[8],
                                       newLine[9], newLine[10])
                  sphere = data.Sphere(center, radius, color, finish)
                  sp_list.append(sphere)
         return sp_list



def open_file(argv, mode):
   try:
      return open(argv, mode)
   except IOError as e:
      print >> sys.stderr, '{0}: {1}'.format(name, e.strerror)
      exit(1)
 

 
def list_is_numeric(L, start = 0, end = 0):
   if end == 0:
      end = len(L)
   if L == []:
      return False
   else:
      for i in range(start, end):
         if float_default(L[i], None) ==  None:
            return False
      return True



def float_default(st, flo):
   try:
      n = float(st)
   except:
      n = flo
   return n



if __name__ == '__main__':
   main()
