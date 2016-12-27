import sys

def main(argv):
   reach = check_length(argv)

   infile = open_with(argv[1], 'r')
   outfile = open_with('blurred.ppm', 'w')

   unorganized = read_with(infile)

   header = unorganized[0 : 4]
   organized = unorganized[4 : len(unorganized)]

   width = int(header[1])
   height = int(header[2])
   reach = int(argv[2])

   organized_1 = str_to_float(organized)
   organized_2 = list_splicer(organized_1, 3)
   organized_3 = list_splicer(organized_2, width)

   header_writer(header, outfile)
   blurrer(organized_3, reach, outfile, width, height)

   infile.close()
   outfile.close()

def check_length(argv):
   if len(argv) == 3:
      try:
         if int(argv[2]) >= 0:
            return int(argv[2])
         else:
            print 'Reach must be positive'
            exit(1)
      except IOError as e:
         print >> sys.stderr, '{0} : {1}'.format(name, e.strerror)

   elif len(argv) == 2:
      return 4

   elif len(argv) == 1 or len(argv) > 3:
      print 'usage: python blur.py image.ppm optional_reach'
      exit(1)
   
   return reach

def open_with(name, method):
   try:
      return open(name, method)
   except IOError as e:
      print >> sys.stderr, '{0} : {1}'.format(name, e.strerror)

def str_to_float(list):
   try:
      return [float(v) for v in list]
   except IOError as e:
      print >> sys.stderr, '{0} : {1}'.format(name, e.strerror)

def read_with(file):
   newList = []
   for line in file:
      l = line.split()
      for y in l:
         newList.append(y)
   return newList

def list_splicer(list, number):
   newList = []
   for i in range(0, len(list), number):
      newList.append(list[i : i + number])
   return newList

def header_writer(header, file):
   file.write(header[0] + '\n')
   file.write(header[1] + ' ' + header[2] + '\n')
   file.write(header[3] + '\n')

def blurrer(list, number, file, width, height):
   for i in range(len(list)):
      for j in range(len(list[i])):
         point = (j, i)
         boundaries = find_boundaries(point, number, width, height)
         color = average(list, boundaries)
         file.write(str(color[0]) + '\n')
         file.write(str(color[1]) + '\n')
         file.write(str(color[2]) + '\n')

def find_boundaries(point, number, width, height):
   boundaries = []

   x = point[0]
   y = point[1]

   left = x - number
   right = x + number
   up = y - number
   down = y + number

   if left < 0:
      left = 0
   boundaries.append(left)

   if right >= width:
      right = width - 1
   boundaries.append(right)

   if up < 0:
      up = 0
   boundaries.append(up)

   if down >= height:
      down = height - 1
   boundaries.append(down)

   return boundaries

def average(pixels, boundaries):
   red = 0.0
   green = 0.0
   blue = 0.0

   left = boundaries[0]
   right = boundaries[1]
   up = boundaries[2]
   down = boundaries[3]

   d = 0

   for i in range(up, down + 1):
      for j in range(left, right + 1):
         red += pixels[i][j][0]
         green += pixels[i][j][1]
         blue += pixels[i][j][2]
         d += 1

   red  = min(255, int(red / d))
   green = min(255, int(green / d))
   blue = min(255, int(blue / d))

   return [red, green, blue]

if __name__ == '__main__':
   main(sys.argv)
