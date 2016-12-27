from sys import argv
import sys
from math import sqrt

def main(argv):
   # try:
        with open('blurred.ppm', 'w') as output:
              return read(argv, output)
   # except IndexError:
   #     print >> sys.stderr, 'parameter not received'
   #     exit()
   # except AttributeError:
   #     print >> sys.stderr, 'completed'
   #     exit()
   # except TypeError:
   #     print >> sys.stderr, 'completed'
   #     exit()

def read(argv, output):
   try:
       with open(argv[1], 'r') as input:
            return blur(input, output)
   except IOError:
       print >> sys.stderr, 'file could not be opened'
       exit()
def groups_of_3(nums):
    return [nums[i:i+3] for i in range(0, len(nums), 3)]

def printValues(r, g, b, output):
    print >> output, str(int(r))+ ' ' +str(int(g))+ ' ' +str(int(b))

def printHeader(ppm, width, height, colorMax, output):
    print >> output, str(ppm)
    print >> output, str(width)
    print >> output, str(height)
    print >> output, str(colorMax)







#Calculate the radius of pixels that will be blurred
def getBlurFactor(argv):
    try:
        blurFactor = 4
        if len(argv) == 3:
            blurFactor = argv[2]
        return int(blurFactor)
    except :
        blurFactor = 4
        return blurFactor

#Calulate the new value of the pixel that will be modified
#by using the radius of the surrounding pixels
def getPixelsInRadius(xVal, yVal, width, height, blurFactor, grid):
    newPixelValues = []
    for y in range(yVal-blurFactor, yVal+blurFactor+1):
        for x in range(xVal-blurFactor, xVal+blurFactor+1):

            checkY = checkBounds(y, height)
            checkX = checkBounds(x, width)

            if checkY == True and checkX == True:

                newPixelValues.append(grid[y][x])
    return newPixelValues

#Get the final values of the components of the pixel
def getFinalValues(pixelList):
    rTotal = 0
    gTotal = 0
    bTotal = 0
    for pixel in pixelList:
        rTotal += int(pixel[0])
        gTotal += int(pixel[1])
        bTotal += int(pixel[2])
    rFinal = rTotal / len(pixelList)
    gFinal = gTotal / len(pixelList)
    bFinal = bTotal / len(pixelList)

    return rFinal, gFinal, bFinal





def checkBounds(num, maxValue):
    if num < 0:
        return False
    elif num >= maxValue:
        return False
    else:
        return True

def getGrid(width, height, valuesList):
    return[valuesList[i*width: (i+1)*width] for i in range(height)]


def blur(input, output):
    values = input.read().split()
    printHeader(values[0], values[1], values[2], values[3], output)

    MAX_WIDTH = int(values[1])
    MAX_HEIGHT = int(values[2])
    pixels = groups_of_3(values[4:len(values)])
    grid = getGrid(MAX_WIDTH, MAX_HEIGHT, pixels)
    blurNum = getBlurFactor(argv)

    for y,line in enumerate(grid):
        for x, pixel in enumerate(line):
            newPixels = getPixelsInRadius(x,y, MAX_WIDTH, MAX_HEIGHT, blurNum, grid)
            finalComponents = getFinalValues(newPixels)
            r = finalComponents[0]
            g = finalComponents[1]
            b = finalComponents[2]
            printValues(r, g, b, output)











if __name__ == '__main__':
    main(argv)


