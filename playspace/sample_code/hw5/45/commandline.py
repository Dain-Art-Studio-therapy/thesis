# Name: Allison Lee
# Instructor: Aaron Keen
# Section: 09
import data

def file_open(filename):
    try:
        return open(filename,'r')
    except:
        print 'The file cannot be opened.'
        exit()
        
#called to check through the file. If it returns True, the file is valid. 
def file_check(filename):
    filevalid = False
    valid = []
    for idx,line in enumerate(filename):
        str = line.split()
        if line=='\n':
            print 'No sphere on line ',idx+1,'... skipping'
            valid.append(False)
        elif len(str)>11 or len(str)<11:
            print 'Malformed sphere on line ',idx+1,'... skipping'
            valid.append(False)
        else:
            for number in str:
                try:
                    float(number)
                except:
                    print 'Values are not floats on line ',idx+1,'... skipping'
                    valid.append(False)
    if not valid:
        filevalid = True
    #returns whether or not the file is valid or not
    return filevalid

# assumes a valid file. filecheck has to be called first and true.
def output_spheres(filename):
    sphere_list = []
    f = file_open(filename)
    for line in f:
        str = line.split()
        center = data.Point(float(str[0]),float(str[1]),float(str[2]))
        radius = float(str[3])
        color = data.Color(float(str[4]),float(str[5]),float(str[6]))
        finish = data.Finish(float(str[7]),float(str[8]),
                             float(str[9]),float(str[10]))
        sphere = data.Sphere(center,radius,color,finish)
        sphere_list.append(sphere)
        #appends each sphere to a list and returns it.
        
    return sphere_list

