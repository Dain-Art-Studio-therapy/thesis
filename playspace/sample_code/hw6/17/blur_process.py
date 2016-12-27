import math

def process_file(f,width):
   unsorted = f.read().split()
   pixels = groups_of_n(groups_of_n(unsorted,3),width)
   return pixels

# list of list of list of numbers. -> list of list of list of numbers
# in other words, grouped, ordered pixels -> grouped ordered pixels
def blur_pixels(pixels,blurPx, blurReach, width, height):  
   for rowInd in range(height):
      for colInd in range(width):
         blurPx[rowInd][colInd] = compute_blur(pixels,rowInd, colInd,blurReach,
            width, height)

def compute_blur(pixels,rowInd, colInd, blurReach, width, height):
   checkL, checkR, checkT, checkB = find_viable_range(rowInd, colInd, 
      blurReach, width, height)
   lowestRInd = rowInd - checkT
   lowestCInd = colInd - checkL
   rangeRCheck = range(checkT + checkB + 1)
   rangeCCheck = range(checkL + checkR + 1)
   return average_of_pixels(pixels, lowestRInd, lowestCInd, rangeRCheck,
      rangeCCheck)

def average_of_pixels(pixels, baseRInd, baseCInd, rowRange, colRange):
   redSum, greenSum, blueSum = (0,0,0)
   totalPx = len(rowRange) * len(colRange)
   for dy in rowRange:
      for dx in colRange:
         redSum += int(pixels[baseRInd+dy][baseCInd+dx][0])
         greenSum += int(pixels[baseRInd+dy][baseCInd+dx][1])       
         blueSum += int(pixels[baseRInd+dy][baseCInd+dx][2])
   rAvg, gAvg, bAvg = (redSum/totalPx, greenSum/totalPx, blueSum/totalPx)
   return [rAvg, gAvg, bAvg]

def find_viable_range(row, col, blurReach, width, height):
   checkRange = range(blurReach, -1, -1)
   for dr in checkRange:
      if col - dr >= 0:
         left = dr
         break
   for dr in checkRange:
      if col + dr <= width - 1:
         right = dr
         break
   for dr in checkRange:
      if row - dr >= 0:
         top = dr
         break
   for dr in checkRange:
      if row + dr <= height - 1:   
         bot = dr
         break
   return (left,right,top,bot) 

def print_header(size, maxColor, output):
   print >> output, 'P3'
   print >> output, size[0], size[1]
   print >> output, maxColor

def print_pixels(pixels, output, maxColor):
   for row in pixels:
      for col in row:
         for color in col:
            print >> output, min(int(float(color)), maxColor),
      print >> output, ''

# takes in a list of values and returns a grouped list of values
def groups_of_n(list, n):
   grouped = []
   curGroup = -1
   
   for i in range(len(list)):
      if i % n == 0:
         grouped.append([list[i]])
         curGroup += 1
      else: 
         grouped[curGroup].append(list[i])
   return grouped
