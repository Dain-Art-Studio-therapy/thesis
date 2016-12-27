import math
import sys

def main(argv):
        fileName = validate_args(argv)
        fileObject = readFile(fileName)
        dest = 'blurred.ppm'
        with open(dest,'wb') as destination:
                pixList = cachePixels(fileObject,destination,argv)
                try:
                        reach = int(argv[2])
                except:
                        reach = 4
                blur(pixList,reach,destination)
        fileObject.close()

def toString(list):
        output = []
        for i in list:
                output.append(str(i))
        return output

def blur(pixList,reach,dest):
        for y in range(len(pixList)):
                for x in range(len(pixList[y])):
                        newPix = calcBlur(pixList,pixList[y][x],x,y,reach)
                        newPix = convertInt(newPix)
                        printToPic(toString(newPix),dest)

def calcBlur(pixList,pixColor,xpos,ypos,reach):
        rTot = 0.0
        gTot = 0.0
        bTot = 0.0
        span = reach*2 + 1
        yErr = 0
        xErr = 0
        counter = 0
        for y in range((ypos-reach),(ypos+reach+1)):
                try:
                        for x in range((xpos-reach),(xpos+reach+1)):
                                rTot += pixList[y][x][0]
                                gTot += pixList[y][x][1]
                                bTot += pixList[y][x][2]
                                counter += 1
                except Exception as e:
                        pass
        omit = xErr + yErr*span
        print span**2, counter
        newR = rTot/counter
        newG = gTot/counter
        newB = bTot/counter
        return [newR,newG,newB]

def cachePixels(fileObject,dest,args):
        cacheList = []
        counter = 1
        xlist = []
        color = []
        xcount = 1
        ycount = 1
        printcount = 0
        for line in fileObject:
                vals = line.split()
                if counter < 4:
                        ##print directly
                        printToPic(vals,dest)
                        if counter == 2:
                                width = int(vals[0])
                                height = int(vals[1])
                else:
                        for v in vals:
                                if len(color) < 3:
                                        color.append(v)
                                elif len(color) == 3:
                                        color = convertInt(color)
                                        xlist.append(color)
                                        if xcount >= width:
                                                cacheList.append(xlist)
                                                xlist = []
                                        color = [v]
                                        printcount += 1
                                        xcount = incrementX(xcount,width)
                                        ycount = printcount/width + 1
                counter += 1
        return cacheList

def incrementX(xAmt,width):
        if xAmt >= width:
                xAmt = 1
        else:
                xAmt += 1
        return xAmt

def printToPic(list,destFile):
        if len(list) > 1:
                text = ' '.join(list)
                print >> destFile,text
        else:
                print >> destFile,list[0]

def convertInt(list):
        newList = []
        for i in list:
                newList.append(int(i))
        return newList

def capNum(integer):
        if integer > 255:
                return 255
        else:
                return integer

def readFile(name):
        try:
                return open(name,'rb')
        except Exception as e:
                print >> sys.stderr, 'Could not open file..',
def validate_args(args):
        if len(args) >= 2:
                return args[1]
        else:
                print >> sys.stderr,'Please include: ',getInstructions()
                exit(1)

def getInstructions():
        return 'python blur.py {imagefile} OPT:[Neighbor Reach]'


if __name__ == '__main__':
        main(sys.argv)
