import math

def process_file(f,width):
   unsorted = f.read().split()
   pixels = groups_of_n(groups_of_n(unsorted,3),width)
   return pixels

# list of list of list of numbers. -> list of list of list of numbers
# in other words, grouped, ordered pixels -> grouped ordered pixels
def fade_pixels(pixels, row, col, radius):
   for rowInd in range(len(pixels)):
      for colInd in range(len(pixels[rowInd])):
         pixels[rowInd][colInd] = compute_fade(pixels,rowInd, colInd, row, 
            col,radius)

def compute_fade(pixels,rowInd, colInd, fadeRow, fadeCol, radius):
   distance = distance_between_pixels(rowInd, colInd, fadeRow, fadeCol)
   fade_multi = max(0.2, (radius - distance)/radius)
   return fade_pixel(fade_multi, pixels[rowInd][colInd])

def fade_pixel(fade_multi, pixel):
   return [str(int(pixel[0]) * fade_multi), str(int(pixel[1]) * 
      fade_multi), str(int(pixel[2]) * fade_multi)]


def distance_between_pixels(rowInd, colInd, fadeRow, fadeCol):
   return math.sqrt((rowInd - fadeRow) ** 2 + (colInd - fadeCol) ** 2)

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
