import sys
import math

def main(argv):
   try:
      file = open(argv[1], 'r')
   except:
      print "failed to open input"
      sys.exit()
   myFile = open('faded.ppm', 'w')
   waste = 0
   final = []
   finale = []
   for line in file:
      temp = line.split()
      waste = waste + 1
      if (waste < 4):
         if (waste == 2):
            print >> myFile, temp[0], temp[1]
            width = temp[0]
            height = temp[1]
         else:
            print >> myFile, temp[0]
      else:
         for i in temp:
            final.append(int(i))
   pixels = fade_groups_of_3(final)
   finale = fade_rc(pixels, height, width)
   for e in finale:
      d = fade_distance(e, int(argv[2]), int(argv[3]))
      scaled = fade_scale (d, argv[4])
      prod = fade_color_fix(e, scaled)
      red = int(prod[0])
      green = int(prod[1])
      blue = int(prod[2])
      print >> myFile, red, green, blue


def fade_rc(list, y, x):
   num = 0
   new = []
   work = list
   for row in range(0, int(y)):
      for col in range(0, int(x)):
         pt = [row, col]
         work[num].append(pt)
         new.append(work[num])
         num = num + 1
   return new


def fade_groups_of_3(list):
   if (list == []):
      return None
   new = []
   for e in range(0, len(list)):
      if (list[(3 * e):(3 * e + 3)] != []):
         new.append(list[3 * e : 3 * e + 3])
   return new


def fade_distance(list, y, x):
   d = math.sqrt((list[3][0] - y) ** 2 + (list[3][1] - x) ** 2)
   return  float(d)


def fade_scale(distance, radius):
   scalar = (int(radius) - distance)/int(radius)
   if (scalar < 0.2):
      scalar = 0.2
   return scalar


def fade_color_fix(list, scalar):
   new = []
   red = list[0] * scalar
   green = list[1] * scalar
   blue = list[2] * scalar
   if (red > 255):
      red = 255
   if (green > 255):
      green = 255
   if (blue > 255):
      blue = 255
   new.append(red)
   new.append(green)
   new.append(blue)
   return new


if __name__ == "__main__":
   main(sys.argv)

