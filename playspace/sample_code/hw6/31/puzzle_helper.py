from groups import *
import sys

def arg_check(cmdline):
   if (len(cmdline) < 2):
      print >> sys.stderr, "file name missing"
      sys.exit(1)

def open_file(name, mode):
   try:
      return open(name, mode)
   except IOError as e:
      print >> sys.stderr, '{0}:{1}'.format(name, e.strerror)
      exit(1)

def get_dimensions(file):
   dimensions = []
   with open_file(file, 'rb') as f:
      for line in f:
         s = line.split()
         dimensions.append(s)
         #print dimensions
   return dimensions[1]

def img_out(input):
   list = []
   output = open_file('hidden.ppm', 'wb')
   dimensions = get_dimensions(input)
   width = dimensions[0]
   height = dimensions[1]

   output.write('P3\n')
   output.writelines((width, ' ', height, '\n'))
   output.write('255\n') 

   with open_file(input, 'rb') as f:
      for line in f:
         s = line.split()
         for i in range(len(s)):
            list.append(s[i])
      list2 = list[4:len(list)]
      group = groups_of_3(list2)
      #print group
      for pix in group:
         color = str(decode_pix(int(pix[0])))
         output.writelines((color, ' ', color, ' ', color, '\n'))

def cap_value(num):
   if num > 255:
      num = 255
   return num

def decode_pix(num):
   return cap_value(num*10)
