# Han Tran
# fade_image_reading.py


import sys
import group_function
import fade_commandline



#mode = 'r'
def fade_image_read(argv, mode):
      fade_commandline.parse_commandline(argv)
      newls = []
      final = []
      f = open_file(argv[1], mode)
      headerType = (f.readline()).strip()
      headerDime = (f.readline()).strip()
      headerColor = (f.readline()).strip()
      first3Lines = [headerType, headerDime, headerColor]
      fade_header_check(first3Lines) 
      for line in f:
         newLine = split_strip_line(line)
         for i in newLine:
            newls.append(i)
      f.close()
      final.append(group_function.group_of_3(newls))
      final.append([headerType, headerDime, headerColor])
      return final


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


def fade_header_check(first3Lines):
   if first3Lines[0].strip() != 'P3':
      print >> sys.stderr, 'Not ppm P3 format'
      exit
   line2 = first3Lines[1].split()
   if len(line2) != 2 \
          and not first3Lines[1][0].isdigit() \
          and not first3Lines[1][1].isdigit() :
      print >> sys.stderr, 'Width and Height are not defined'
      exit
   if int(first3Lines[2].strip()) != 255:
      print >> sys.stderr, 'Max color component is not defined'
      exit
   return True





#if __name__ == '__main__':
#   fade_image_read(sys.argv, mode)
