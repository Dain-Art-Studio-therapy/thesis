# Han Tran
# blur_image_reading.py


import sys
import group_function
import blur_commandline
import collections


data = collections.namedtuple('Data', ['grid', 'header'])

#mode = 'r'
def blur_image_read(argv, mode):
      blur_commandline.parse_commandline(argv)
      newls = []
      f = open_file(argv[1], mode)
      headerType = (f.readline()).strip()
      headerDime = (f.readline()).strip()
      headerColor = (f.readline()).strip()
      headerVal = [headerType, headerDime, headerColor]
      blur_header_check(headerVal) 
      for line in f:
         newLine = split_strip_line(line)
         for i in newLine:
            newls.append(i)
      f.close()
      RGB_grid = list_to_grid(newls, headerVal)
      ret = data(RGB_grid, header = headerVal)
      #print ret.header
      #print ret[1]
      return ret


def list_to_grid(lst, headerName):
   dim = map(int, headerName[1].split())
   width = dim[0]
   height = dim[1]
   lstPixel = group_function.group_of_3(lst)
   grid = [[[] for x in range(width)] for y in range(height)]
   k = 0
   for row in range(height):
      for col in range(width):
         grid[row][col] = lstPixel[k]
         k += 1
   return grid


def split_strip_line(singleLine):
   stripLine = singleLine.strip()
   splitLine = stripLine.split()
   return  map(int, splitLine)


def open_file(fileName, mode):
   try:
      return open(fileName, mode)
   except IOError as e:
      print >> sys.stderr, '{0}:{1}'.format(fileName, e.strerror)
      exit()


def blur_header_check(first3Lines):
   if first3Lines[0].strip() != 'P3':
      print >> sys.stderr, 'Not ppm P3 format'
      exit()
   line2 = first3Lines[1].split()
   if len(line2) != 2 \
          and not first3Lines[1][0].isdigit() \
          and not first3Lines[1][1].isdigit() :
      print >> sys.stderr, 'Width and Height are not defined'
      exit()
   if int(first3Lines[2].strip()) != 255:
      print >> sys.stderr, 'Max color component is not defined'
      exit()
   return True





#if __name__ == '__main__':
#   blur_image_read(sys.argv, mode)
