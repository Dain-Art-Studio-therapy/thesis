import sys
import math

def parseargs(argv):
   if len(argv) <= 4:
      print "Command arguments: <filename> <row> <col> <radius>"
      exit(1)
   else:
      try:
         row = int(argv[2])
         col = int(argv[3])
         radius = int(argv[4])
      except:
         print "An argument was wrong."
         exit(1)
      with open_file(argv[1], 'rb') as f:
         print row,col,radius
         linearray = []
         for line in f:
            linearray.append(line.replace('\n', ''))
         pixels = groups_of_3(linearray)
         header = pixels[0]
         del pixels[0]
         loop_image(row, col, radius, pixels, header)
         

def loop_image(row, col, radius, pixels, header):
   width = int(header[1].split()[0])
   values = []
   for i in range(len(pixels)):
      current_col = i%width
      current_row = (i-current_col)/width
      scale = get_scale(row, col, radius, current_row, current_col)
      for color in pixels[i]:
         values.append(str(int(int(color) * scale)))
         values.append(' ')
   write_ppm(header, values)

def get_scale(row, col, radius, current_row, current_col):
   distance = math.sqrt((col - current_col)**2 + (row - current_row)**2)
   scale = (radius - distance) / radius
   scale = scale if scale >= 0.2 else 0.2
   return scale


def write_ppm(header, values):
   with open('faded.ppm', 'w') as f:
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
