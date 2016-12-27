import sys
from cast import *
import commandline
from data import *

def main(args):
        custom_items = set_defaults()
        custom_items = commandline.process_args(args,custom_items)
        filename = commandline.findfile(args)
        sphList = cacheFile(filename)
        eyePoint = custom_items[0]
        view = custom_items[1]
        light = custom_items[2]
        ambient = custom_items[3]
        cast_all_rays(view[0],view[1],view[2],view[3],view[4],view[5],eyePoint,sphList,ambient,light)

def cacheFile(filename):
	try:
        	with open(filename) as f:
                        sphList = read_file(f)
			return sphList
        except Exception as e:
                print >> sys.stderr,e
                return[]
def set_defaults():
        #sets a list with EYE,VIEWlist,LIGHT,AMBIENT
        eye = Point(0.0,0.0,-14.0)
        view = [-10.0,10.0,-7.5,7.5,1024,768]
        light = Light(Point(-100.0,100.0,-100.0),Color(1.5,1.5,1.5))
        ambient = Color(1.0,1.0,1.0)
        L = [eye,view,light,ambient]
        return L
def read_file(filename):
        sphList = []
        counter = 1
        for line in filename:
                try:
                        vals = line.split( )
                        ##make a sphere... add to spherelist
                        point = Point(float(vals[0]),float(vals[1]),float(vals[2]))
                        rad = float(vals[3])
                        color =Color(float(vals[4]),float(vals[5]),float(vals[6]))
                        finish = Finish(float(vals[7]),float(vals[8]),float(vals[9]),float(vals[10]))
                        sph = Sphere(point,rad,color,finish)
                        sphList.append(sph)
                        #print >> sys.stderr, 'sphere #',counter
                except:
                        a = 'Malformed Sphere on Line '
                        b ='...Skipping.'

                        print >> sys.stderr,a,counter,b
                counter += 1
        return sphList



if __name__ == '__main__':
        main(sys.argv)
