import sys
from data import *
def process_args(args, objectList):
   #each method should change the value in the list if requested, if not, it will return unchanged.
        objectList = eye(args,objectList)
        objectList = view(args,objectList)
        objectList = light(args,objectList)
        objectList = ambient(args,objectList)
        return objectList

def eye(args,objectList):
        new = check_for_eye(args)
        if new != []:
                try:
                        eye = Point(new[0],new[1],new[2])
                        objectList[0] = eye
                except Exception as e:
                        giveError('eye',e)
        else:
                pass
        return objectList

def view(args,objectList):
        new = check_for_view(args)
        if new != []:
                try:
                        objectList[1] = new
                except Exception as e:
                        giveError('view',e)
        else:
                pass
        return objectList

def light(args,objectList):
        new = check_for_light(args)
        if new != []:
                try:
                        lightPoint = Point(new[0],new[1],new[2])
                        lightColor = Color(new[3],new[4],new[5])
                        light = Light(lightPoint,lightColor)
                        objectList[2] = light
                except Exception as e:
                        giveError('light',e)
        else:
                pass
        return objectList

def ambient(args,objectList):
        new = check_for_ambient(args)
        if new != []:
                try:
                        ambientColor = Color(new[0],new[1],new[2])
                        objectList[3] = ambientColor
                except Exception as e:
                        giveError('ambient',e)
        else:
                pass
        return objectList

def check_for_eye(args):
        for i in range(len(args)):
                if args[i] == '-eye':
                        try:
                                return set_next(args, i, 3)
                        except Exception as e:
                                giveError('eye',e)
                                print >> sys.stderr, instructions(3)
                                argument = []
                else:
                        argument = []
        return argument
def check_for_view(args):
        for i in range(len(args)):
                if args[i] == '-view':
                        try:
                                return set_next(args,i,6)
                        except Exception as e:
                                giveError('view',e)
                                argument = []
                                print >> sys.stderr, instructions(4)
                else:
                        argument = []
        return argument
def check_for_light(args):
        for i in range(len(args)):
                if args[i] == '-light':
                        try:
                               return set_next(args,i,6)
                        except Exception as e:
                               giveError('light',e)
                               print >> sys.stderr, instructions(5)
                               argument = []
                else:
                        argument = []
        return argument
def check_for_ambient(args):
        for i in range(len(args)):
                if args[i] == '-ambient':
                        try:
                                return set_next(args,i,3)
                        except Exception as e:
                                giveError('ambient',e)
                                argument = []
                                print >> sys.stderr,instructions(6)
                else:
                        argument = []
        return argument

def giveError(stringType, error):
        print >> sys.stderr, 'Error in ', stringType, 'flag: ', error
        print >> sys.stderr, 'Using default values for ', stringType

def set_next(list,index,amount):
        output = []
        for i in range(index+1,index+1+amount):
                output.append(float(list[i]))
        return output

def findfile(args):
        try:
                filename = args[1]
                with open(filename) as af:
                        pass
                        
                return filename
        except:
                print >> sys.stderr, 'Please specify an existing file with the extension. Ex: <file.txt>'
                print >> sys.stderr, instructions(0)
                return None

def instructions(case):
        stringList = []
        stringList.append('usage: ')
        stringList.append('python ray_caster.py ')
        stringList.append('<filename> ')
        stringList.append('[-eye x y z] ')
        stringList.append('[-view min_x max_x min_y max_y width height] ')
        stringList.append('[-light x y z r g b] ')
        stringList.append('[-ambient r g b] ' )
        if case == 0 or case == 1 or case == 2:
                return ''.join(stringList)
        else:
                return stringList[case]
