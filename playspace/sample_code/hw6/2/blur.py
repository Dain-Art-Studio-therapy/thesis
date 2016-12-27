import sys


def main(argv):
   try:
      input = open(argv[1], 'r')
   except:
      print 'failed to open file'
      sys.exit()
   myFile = open('blurred.ppm', 'w')
   try:
      factor = argv[2]
   except:
      factor = 4
   waste = 0
   temporary = []
   preList = []
   for line in input:
      temporary = line.split()
      waste = waste + 1
      if (waste == 2):
         print >> myFile, temporary[0], temporary[1]
         height = temporary[0]
         width = temporary[1]
      elif(waste < 4):
         print >> myFile, temporary[0]
      else:
         for i in temporary:
            preList.append(i)
   pixel = blur_groups_of_3(preList)
   locations = blur_location(pixel, height, width)
   grid = blur_grid_finder(locations, factor, width)
   for pix in grid:
      print >> myFile, pix[0], pix[1], pix[2] 


def blur_location(list, y, x):
   num = 0
   new = []
   loc = list
   for row in range(0, int(y)):
      for col in range(0, int(x)):
         pt = [row, col]
         loc[num].append(pt)
         new.append(loc[num])
         num = num + 1
   return new


def blur_groups_of_3(list):
   if (list == []):
      return None
   new = []
   for e in range(0, len(list)):
      if (list[(3 * e):(3 * e + 3)] != []):
         new.append(list[3 * e : 3 * e + 3])
   return new


def blur_grid_finder(pixels, neighbor, width):
   new = []
   result = []
   for e in range(0, len(pixels) - 1):
      for i in range(0, 2 * neighbor + 2):
          row = int(width) * i
          for j in range(0, 2 * neighbor + 2):
             locs = e + row + j
             if(row == 0):
                if(locs - neighbor < 0 or locs - neighbor > width):
                   pass
                elif(locs - neighbor > len(pixels) - 1):
                   pass
                else:
                   new.append(pixels[locs - neighbor])
             if((locs - neighbor <  row) or (locs - neighbor > 2 * row)):
                pass
             else:
                new.append(pixels[locs - neighbor])
      avg = blur_avg(new)
      new = []
      result.append(avg)
   return result


def blur_avg(pixels):
   red = 0.0
   green = 0.0
   blue = 0.0
   number = 0
   for e in pixels:
      red = red + int(e[0])
      green = green + int(e[1])
      blue = blue + int(e[2])
      number = number + 1
   redf = red / number
   greenf = green / number
   bluef = blue / number
   if (redf > 255):
      redf = 255
   if (greenf > 255):
      greenf = 255
   if (bluef > 255):
      bluef = 255
   color = [int(redf), int(greenf), int(bluef)]
   return color


if __name__ == "__main__":
   main(sys.argv)
