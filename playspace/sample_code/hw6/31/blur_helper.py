import sys
import math

def arg_check(cmdline):
   if (len(cmdline) < 5):
      print >> sys.stderr, "file name missing"
      sys.exit(1)

def open_file(name, mode):
   try:
      return open(name, mode)
   except IOError as e:
      print >> sys.stderr, '{0}:{1}'.format(name, e.strerror)
      exit(1)

def img_out(input, reach):
   list = []
   output = open_file('blurred.ppm', 'wb')
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

      grid = []
      count = 0

      for y in range(int(height)):
         temp = []
         #count += 1
         for x in range(int(width)):
            temp.append(group[count])
            count += 1
         grid.append(temp)

      for y in range(len(grid)):
         for x in range(len(grid[y])):
            for h in range(y - int(reach), y + int(reach)):
               if h < 0:
                  h = 0
               elif h > int(height):
                  h = int(height)
               for w in range(x + int(reach), x - int(reach)):
                  if w < int (width):
                     w = 0
                  elif w > int(width):
                     w = int(width)
                  r = str(sum(int(grid[h][w][0]))/int(reach))
                  g = str(sum(int(grid[h][w][1]))/int(reach))
                  b = str(sum(int(grid[h][w][2]))/int(reach))
                  output.writelines((r, ' ', g, ' ', b, ' '))

def get_dimensions(file):
   dimensions = []
   with open_file(file, 'rb') as f:
      for line in f:
         s = line.split()
         dimensions.append(s)
         #print dimensions
   return dimensions[1]

def cap_value(num):
   if num > 255:
      num = 255
   return num

def cap_fade(num):
   if num < 0.2:
      num = 0.2
   return num

def decode_pix(num):
   return cap_value(num*10)


   

def groups_of_3(list):
   group = []
   for i in range(0, len(list), 3):
      group.append(list[i:i+3])
   return group

def distance(x1, y1, x2, y2):
   return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
