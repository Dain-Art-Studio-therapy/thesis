from sys import argv
import sys
from math import sqrt

def main(argv):
   try:
        with open('faded.ppm', 'w') as output:
              return read(argv, output)
   except IndexError:
       print >> sys.stderr, 'parameter not received'
       exit()
   except AttributeError:
       print >> sys.stderr, 'completed'
       exit()
   except TypeError:
       print >> sys.stderr, 'completed'
       exit()

def read(argv, output):
   try:
       with open(argv[1], 'r') as input:
            return fade(input, output)
   except IOError:
       print >> sys.stderr, 'file could not be opened'
       exit()

def groups_of_3(nums):
    return  [nums[i:i+3] for i in range(0, len(nums), 3)]

def distance(x1,y1,x2,y2):
    return sqrt((x2-x1)**2 + (y2-y1)**2)

def calcColorValue(row, col, x, y, radius):
    value =  (radius - distance(col, row, x, y))/ radius
    if value < 0.2:
        value = 0.2
    return value

def printValues(r, g, b, output):
    print >> output, str(int(r))+ ' ' +str(int(g))+ ' ' +str(int(b))

def checkMaxPixelValue(value):
    if value > 255:
        value = 255
    return value

def printHeader(ppm, width, height, colorMax, output):
    print >> output, str(ppm)
    print >> output, str(width)
    print >> output, str(height)
    print >> output, str(colorMax)

def fade(input, output):
    row = int(argv[2])
    col = int(argv[3])
    radius = float(argv[4])
    #(row,col)
    values = input.read().split()
    printHeader(values[0], values[1], values[2], values[3], output)

    MAX_WIDTH = int(values[1])
    MAX_HEIGHT = int(values[2])
    pixels = groups_of_3(values[4:len(values)])
    x = 1
    y = 1
    for pixel in pixels:
         if x < MAX_WIDTH:
             x+=1
             colorValue = calcColorValue(row, col, x, y, radius)

             redValue = float(pixel[0]) * colorValue
             checkMaxPixelValue(redValue)

             greenValue = float(pixel[1]) * colorValue
             checkMaxPixelValue(greenValue)

             blueValue = float(pixel[2]) * colorValue
             checkMaxPixelValue(blueValue)

             printValues(redValue, greenValue, blueValue, output)

         elif x == MAX_WIDTH:
             x = 1
             y += 1

             colorValue = calcColorValue(row, col, x, y, radius)

             redValue = float(pixel[0]) * colorValue
             checkMaxPixelValue(redValue)

             greenValue = float(pixel[1]) * colorValue
             checkMaxPixelValue(greenValue)

             blueValue = float(pixel[2]) * colorValue
             checkMaxPixelValue(blueValue)

             printValues(redValue, greenValue, blueValue, output)



if __name__ == '__main__':
    main(argv)


