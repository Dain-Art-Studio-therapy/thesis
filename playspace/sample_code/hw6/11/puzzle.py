import sys

def main(argv):
        fileName = validate_args(argv)
        fileObject = readFile(fileName)
        dest = 'hidden.ppm'
        with open(dest,'wb') as destination:
                processAllInList(fileObject,destination)
        fileObject.close()

def processAllInList(fileObject,dest):
        list = []
        counter = 1
        printcount = 0
        for line in fileObject:
                vals = line.split()
                if counter < 4:
                        ##print directly
                        printToPic(vals,dest)
                elif vals == []:
                        print 'empty line'
                        pass
                else:
                        for v in vals:
                                if len(list) < 3:
                                        list.append(v)
                                elif len(list) == 3:
                                        list = convertInt(list)
                                        list = depuzz(list)
                                        printToPic(list,dest)
                                        list = [v]
                                        printcount += 1
                                elif len(list) > 3:
                                        print >> sys.stderr, 'length longer than 3'
                                        exit(1)
                counter += 1

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
        if len(args) == 2:
                return args[1]
        else:
                print >> sys.stderr,'Please include: ',getInstructions()
                exit(1)

def getInstructions():
        return 'python puzzle.py {imagefile}'

def depuzz(list):
        newRed = list[0] * 10
        newRed = capNum(newRed)
        newRed = str(newRed)
        newList = [newRed,newRed,newRed]
        return newList

if __name__ == '__main__':
        main(sys.argv)
