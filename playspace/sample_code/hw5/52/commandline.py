#contains processes for managing command line arguments, and therefore the sphere list processing functionality
import data
import sys
import cast
import time #because I want to know how insufferably long some of these take to render
import random

#gotta define these somewhere, why not here
class ParamError(Exception):
    pass

class ExitError(Exception):
    pass

def run(args):
    #AWESOME TIMER FUNCTIONALITY FROM THE FUTURE
    #WOAH (honestly this exists to tell me how long the big stuff takes to render when I leave it on overnight or whatever)
    s = time.time()
    #args is argv expecting python ray_caster.py <filename> [-eye x y z] [-view min_x max_x min_y max_y width height] [-light x y z r g b] [-ambient r g b]
    #check validity of sphere file
    try:
        with open (args[1],'rb') as f:
            print >> sys.stderr, 'Attempting to build sphere list'
            slist = build_sphere_list(f)
            print >> sys.stderr, 'Sphere list complete'
    except:
        print >> sys.stderr, 'Invalid or missing file'
        print >> sys.stderr, 'Ray Caster supports <filename> [-eye x y z] [-view min_x max_x min_y max_y width height] [-light x y z r g b] [-ambient r g b]'
        sys.exit()


    if len(args) == 2: #only a file definied, no eye/view/light/amb definitions
        try:
            print >> sys.stderr, 'Casting...'
            
            default_cast(slist)
            e = time.time()
            
            print >> sys.stderr, 'Casting complete'
        except:
            print >> sys.stderr, 'There was an error in casting'
            sys.exit()
            
    else:
        try:
            advanced_cast(args,command_handler(args),slist)        
        except ParamError:
            print >> sys.stderr, 'There was an error in handling your parameters'
            print >> sys.stderr, 'Ray Caster supports <filename> [-eye x y z] [-view min_x max_x min_y max_y width height] [-light x y z r g b] [-ambient r g b]'
            sys.exit()
        except ExitError:
            print >> sys.stderr, 'Ray Caster supports <filename> [-eye x y z] [-view min_x max_x min_y max_y width height] [-light x y z r g b] [-ambient r g b]'
            sys.exit()
        except:
            print >> sys.stderr, 'There was an error in handling your parameters'
            print >> sys.stderr, 'Ray Caster supports <filename> [-eye x y z] [-view min_x max_x min_y max_y width height] [-light x y z r g b] [-ambient r g b]'
            sys.exit()
            
            
    #REST OF THE AWESOME TIMER FUNCTIONALLITY
    e = time.time()
    t = e-s #total time
    if t > 60:
        m = int(t/60)
        s = int(t%60)
        print >> sys.stderr, 'Casting took',m,'minutes and',s,'seconds'
    else:
        print >> sys.stderr, 'Casting took',int(t),'seconds'

        
      


def build_sphere_list(f):
    linenum = 1
    slist = []
    try:
        for line in f:
            s = build_sphere(line,linenum) #attemts sphere construction based on the current line's data
            if s != None:   #ensures the sphere was instanced correctly, otherwise ignores that line
                slist.append(s)
                linenum += 1
            else:
                linenum += 1
        return slist

    except:
        print >> sys.stderr, 'There was an error processing the sphere list'
        exit



def build_sphere(line,ln):
    tents = [] #tentative sphere list, will be used to build the line's sphere
    s = str.split(line)
    #print >> sys.stderr, s (re-enale for testing if needed)
    if len(s) != 11:
        print >> sys.stderr, 'Incorrect sphere format on line ' + str(ln)
        return None

    else:
        for val in s:
            try:
                temp = float(val)
                tents.append(temp)
                
            except:
                print >> sys.stderr, 'Invalid valule on line ' + str(ln)
                return None
            
    return data.Sphere(data.Point(tents[0],tents[1],tents[2]),
                        tents[3],
                        data.Color(tents[4],tents[5],tents[6]),
                        data.Finish(tents[7],tents[8],tents[9],tents[10]))

def command_handler(args):
    #ensures handlability additional arguments based on the length of the args list as a baseline for the possible commands
    #checks args to make sure that it has the proper # of params for a valid imput possibility
    print >> sys.stderr, 'Checking parameter(s)'
    if len(args) < 28: #maximum possible parameter check, includes rcol
        return len(args)       
    else:
        print >> sys.stderr, 'Excessive parameters imput, please double check your parameters'
        raise ExitError()
    
def default_cast(slist):
    WHITE = data.Color(1.0,1.0,1.0)
    lightpt = data.Point(-100.0,100.0,-100.0)
    lcol = data.Color(1.5,1.5,1.5)
    light = data.Light(lightpt,lcol)
    eye = data.Point(0.0,0.0,-14.0)
    cast.cast_all_rays(-10,10,-7.5,7.5,1024,768,eye,slist,WHITE,light)


def advanced_cast(inlist,ll,slist):
    #establishing defualts
    AMB = data.Color(1.0,1.0,1.0)
    lightpt = data.Point(-100.0,100.0,-100.0)
    lcol = data.Color(1.5,1.5,1.5)
    light = data.Light(lightpt,lcol)
    eye = data.Point(0.0,0.0,-14.0)
    minx = -10
    maxx = 10
    miny = -7.5
    maxy = 7.5
    width = 1024
    height= 768

    #checks locations then scales the next location based on the previous parameter
    #I did this really wrong the first time lol
    #this was once an if tree. we won't speak of that ever again

    indx = 2
    #while loop reads passed arguments
    #does not require try because the exceptions are handled in run
    while indx < len(inlist)-1: 
        if inlist[indx] == '-eye':
            eye = data.Point(float(inlist[indx+1]),float(inlist[indx+2]),float(inlist[indx+3]))
            print >> sys.stderr, 'Eye parameter OK'
            indx += 4

        elif inlist[indx] == '-ambient':
            AMB = data.Color(float(inlist[indx+1]),float(inlist[indx+2]),float(inlist[indx+3]))
            print >> sys.stderr, 'Ambient parameter OK'
            indx += 4

        elif inlist[indx] == '-view':
            minx = float(inlist[indx+1])
            maxx = float(inlist[indx+2])
            miny = float(inlist[indx+3])
            maxy = float(inlist[indx+4])
            width = int(inlist[indx+5])
            height = int(inlist[indx+6])
            print >> sys.stderr, 'View parameter OK'
            indx += 7

        elif inlist[indx] == '-light':
            lightpt = data.Point(float(inlist[indx+1]),float(inlist[indx+2]),float(inlist[indx+3]))
            lcol = data.Color(float(inlist[indx+4]),float(inlist[indx+5]),float(inlist[indx+6]))
            print >> sys.stderr, 'Light parameter OK'
            indx += 7

        elif inlist[indx] == '-rcol': #secret function, pass as [-rcol minc maxc] (I highly reccomend using 0 1.5, try it)
            minc = float(inlist[indx+1])
            maxc = float(inlist[indx+2])
            for s in slist:
                s.color = data.Color(random.uniform(minc,maxc),random.uniform(minc,maxc),random.uniform(minc,maxc))
            print >> sys.stderr, 'Color randomization OK'
            indx += 3

        else:
            raise ParamError()
        
    print >> sys.stderr, 'Parameters ok. Casting'
    cast.cast_all_rays(minx,maxx,miny,maxy,width,height,eye,slist,AMB,light)
    print >> sys.stderr, 'Casting completed without error'


    
                        
                    
                
                    


    
            
