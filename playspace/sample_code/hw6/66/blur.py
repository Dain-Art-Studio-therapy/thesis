import sys
import math

def parseargs(argv):
   if len(argv) <= 1:
      print "Please supply a file name"
      exit(1)
   else:
      reach = 4
      if len(argv) > 2:
         try:
            reach = int(argv[2])
         except:
            print "Reach needs to be an int"
      with open_file(argv[1], 'rb') as f:
         linearray = []
         for line in f:
            linearray.append(line.replace('\n', ''))
         pixels = groups_of_3(linearray)
         header = pixels[0]
         width = int(header[1].split()[0])
         del pixels[0]
         color_2d = color_2d_array(pixels, width)

         loop_image(reach, color_2d, header)

def color_2d_array(pixels, width):
   color = []
   row = []
   for i in range(len(pixels)):
      pixel = []
      for rgb in pixels[i]:
         pixel.append(int(rgb))
      row.append(pixel)
      if (i+1)%width == 0:
         color.append(row)
         row = []
   return color

def loop_image(reach, color_2d, header):
   values = []
   for x in range(len(color_2d)):
      for y in range(len(color_2d[x])):
         average = get_average(color_2d, reach, x, y)
         for color in average:
            values.append(str(color) + ' ')
   write_ppm(header, values)

def get_average(color_2d, reach, x, y):
   pixels = []
   x_min = x-reach
   if x_min < 0:
      x_min = 0
   y_min = y-reach
   if y_min < 0:
      y_min = 0
   for x_p in range(x_min, x+reach+1):
      for y_p in range(y_min, y+reach+1):
         try:
            pixel = color_2d[x_p][y_p]
            pixels.append(pixel)
         except IndexError:
            pass
   return average_color(pixels)

def average_color(pixels): #[colors]
   average = [0,0,0] #[r,g,b]
   for i in range(len(pixels)): #each color
      for j in range(len(pixels[i])): #each value
         average[j] += pixels[i][j]
   for color in range(len(average)):
      average[color] = average[color]/len(pixels)
   return average


def write_ppm(header, values):
   with open('blurred.ppm', 'w') as f:
      f.write(header[0] + '\n' + header[1] + '\n' + header[2] + '\n')
      f.write(''.join(values))

def open_file(name, mode):
   try:
      return open(name, mode)
   except IOError as e:
      print >> sys.stderr, '{0} : {1}'.format(name, e.strerror)
      exit(1)

def groups_of_3(values):
   if values == []:
      return -1
   else:
      return [values[i:i+3] for i in range(0, len(values), 3)]

if __name__ == "__main__":
   parseargs(sys.argv)
