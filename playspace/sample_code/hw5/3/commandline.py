from sys import argv
import sys
import cast
import data



def read(argv):

   try:
       #argv[1] is the file name
       with open(argv[1], 'r') as f:
            return readFile(f)
   except IOError:
       print >> sys.stderr, 'file could not be opened'
       exit()

def readFile(fileName):
    lineValue = 1
    sphereList = []
    for line in fileName:
            sphereValues = line.split()

            if len(sphereValues) == 11:
                x         = float(sphereValues[0])
                y         = float(sphereValues[1])
                z         = float(sphereValues[2])
                radius    = float(sphereValues[3])
                r         = float(sphereValues[4])
                g         = float(sphereValues[5])
                b         = float(sphereValues[6])
                ambient   = float(sphereValues[7])
                diffuse   = float(sphereValues[8])
                specular  = float(sphereValues[9])
                roughness = float(sphereValues[10])
                sphereList.append(data.Sphere(data.Point(x, y, z),\
                                              radius,\
                                              data.Color(r, g, b),\
                                              data.Finish(ambient, diffuse\
                                                        ,specular, roughness)))
            #If there is not input file, run this
            elif len(argv) < 2:
                print >> sys.stderr,'usage: python ray_caster.py <filename>' \
                                    ' [-eye x y z][-view min_x max_x min_y' \
                                    ' max_y width height] [-light x y z r g b]'\
                                    ' [-ambient r g b]'
            #This statement checks to see if the sphere's from the input file are properly formatted
            elif len(sphereValues) != 11:
                print >> sys.stderr, 'malformed sphere on line ' \
                                   + str(lineValue) + ' ... skipping'
            lineValue += 1
    return sphereList, checkFlag(argv)

def checkFlag(argv):
    min_x  = -10
    max_x  =  10
    min_y  =  -7.5
    max_y  = 7.5
    height = 400
    width  = 400
    color = data.Color(1.0,1.0,1.0)
    eye_point = data.Point(0,0,-14.0)
    light = data.Light(data.Point(-100.0,100.0,-100.0),data.Color(1.5, 1.5, 1.5))

    for flag in range(len(argv)):
        if argv[flag] == '-eye':
            eyeX = float(argv[flag+1])
            eyeY = float(argv[flag+2])
            eyeZ = float(argv[flag+3])
            eye_point = data.Point(eyeX, eyeY, eyeZ)
        elif argv[flag] == '-view':
            min_x  = float(argv[flag+1])
            max_x  = float(argv[flag+2])
            min_y  = float(argv[flag+3])
            max_y  = float(argv[flag+4])
            width  = int(argv[flag+5])
            height = int(argv[flag+6])
        elif argv[flag] == '-light':
            lightX = float(argv[flag+1])
            lightY = float(argv[flag+2])
            lightZ = float(argv[flag+3])
            lightR = float(argv[flag+4])
            lightG = float(argv[flag+5])
            lightB = float(argv[flag+6])
            light = data.Light(data.Point(lightX,lightY,lightZ),
                               data.Color(lightR, lightG, lightB))
        elif argv[flag] == '-ambient':
            ambientR = float(argv[flag+1])
            ambientG = float(argv[flag+2])
            ambientB = float(argv[flag+3])
            color = data.Color(ambientR, ambientG, ambientB)
    return (min_x, max_x, min_y, max_y, width, height, eye_point, color, light)




if __name__ == '__main__':
    read(argv)