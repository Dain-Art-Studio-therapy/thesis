import math
import sys

def main(argv):
        fileName = validate_args(argv)
        fileObject = readFile(fileName)
        dest = 'faded.ppm'
        with open(dest,'wb') as destination:
                processAllInList(fileObject,destination,argv)
        fileObject.close()

def processAllInList(fileObject,dest,args):
        list = []
        counter = 1
        printcount = 1
        xcount = 1
        ycount = 1
        width = 0
        height = 0
        centerx = float(args[2])
        centery = float(args[3])
        rad = float(args[4])
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
                                if len(list) < 3:
                                        list.append(v)
                                elif len(list) == 3:
                                        list = convertInt(list)
                                        list = fade(list,centerx,centery,rad,xcount,ycount)
                                        printToPic(list,dest)
                                        list = [v]
                                        printcount += 1
                                        xcount = incrementX(xcount,width)
                                        ycount = printcount/width + 1
                                elif len(list) > 3:
                                        print >> sys.stderr, 'length longer than 3'
                                        exit(1)
                counter += 1

def fade(list, centerx,centery, rad,xcount,ycount):
        distance = dist(centerx,centery,xcount,ycount)
        print >> sys.stderr, 'x' , xcount
        print >> sys.stderr, 'y', ycount
        fadeAmt = (rad-distance)/rad
        fadeAmt = capFade(fadeAmt)
        newList = []
        for i in list:
                newVal = int(i*fadeAmt)
                newList.append(str(newVal))
        return newList
                
        

def capFade(amount):
        if amount < 0.2:
                return 0.2
        else:
                return amount

def dist(x1,y1,x2,y2):
        return math.sqrt((x1-x2)**2 + (y1-y2)**2)
        



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
        if len(args) == 5:
                return args[1]
        else:
                print >> sys.stderr,'Please include: ',getInstructions()
                exit(1)

def getInstructions():
        return 'python fade.py {imagefile} {row} {column} {radius}'


if __name__ == '__main__':
        main(sys.argv)
