import sys
import math

def main():
   f = open_file()
   center = get_coords()
   radius = get_radius()
   numlist = split_file_nums(f)
   grouplist = groups_of_3(numlist)
   fade_cast(center, radius, numlist, grouplist)

def fade_cast(center, radius, numlist, grouplist):
   finalfile = open('faded.ppm', 'w')
   
   width = int(numlist[1])
   height = int(numlist[2])
   print >> finalfile, numlist[0]
   print >> finalfile, width, height
   print >> finalfile, numlist[3]
   index = 0
   for i in range(height):
      for j in range(width):
         
         current = grouplist[index]
         distance = get_distance([j, i], center)
         scaledcolor = scale_color(radius, distance, current)
         print >> finalfile, int(scaledcolor[0])
         print >> finalfile, int(scaledcolor[1])
         print >> finalfile, int(scaledcolor[2])
         index += 1
         

    


def open_file():
   
   f = open(sys.argv[1], 'r')
   return f
   #except:
   #   print 'Error: file does\'nt exist'
   #   exit()

def get_coords():
   arg = sys.argv
   coords = []
   coords.append(int(arg[3]))
   coords.append(int(arg[2]))
   return coords

def get_radius():
   arg = sys.argv
   return int(arg[4])

def split_file_nums(f):
   
   numlist = []
  
   for line in f:
      nums = line.split()
      for i in nums:
         numlist.append(i)
      
   return numlist

def groups_of_3(numlist):

   if numlist == []:
      return None
   grouplist = []
   
   newnum = numlist[4:]
   x = 0
   
   trilist = []
   while x < len(newnum):
      trilist.append(newnum[x])
      if len(trilist) == 3:
         temp = [int(i) for i in trilist]
         grouplist.append(temp)
         del trilist[:]
      x += 1

   if len(trilist) > 0:
      grouplist.append(trilist)

   return grouplist

def scale_color(radius, distance, color):
   scalar = scale_calc(radius, distance)
   scaledcolor = [max(color[0] * scalar, 0.2), max(color[1] * scalar, 0.2), max(color[2] * scalar, 0.2)]
   return scaledcolor

def get_distance(c, pt):
   distance = math.sqrt(((c[0] - pt[0]) ** 2) + ((c[1] - pt[1]) ** 2))
   return distance
def scale_calc(radius, distance):
   scalar = (radius - distance)/ radius
   return scalar   


if __name__ == '__main__':
   main()
