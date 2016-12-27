import sys
import data
import commandline
import cast
def try_open(file,mode):
    try:
    	newfile=open(file,mode)
    	return newfile
    except:
    	print "usage: python ray_caster.py <filename> [-eye x y z] [-view min_x max_x min_y max_y width height]\
        [-light x y z r g b] [-ambient r g b]"
    	sys.exit()


def main(argv):
    
     check_length(argv)
 	
     file= try_open(argv[1],'r')

     eye=[False,0]
     view=[False,0]
     light=[False,0]
     ambient=[False,0]
     
     eyeArgs=[]
     viewArgs=[]
     lightArgs=[]
     ambientArgs=[]

     spList=[]
 	 #Check arguments for flags and if arguments not given go to default
     if len(argv)>2:
        
        for b in range(2,len(argv)):
           
        # looks for flags and puts true in tuple if found and the index
        
             if argv[b]=="-eye":
                eye[0]=True
                eye[1]=b
             if argv[b]=="-view":
                view[0]=True
                view[1]=b
             if argv[b]=="-light":
                light[0]=True
                light[1]=b
             if arg[b]=="-ambient":
                ambient[0]=True
                ambient[1]=b

        if eye[0]==True:
            eyeArgs=commandline.check_eye(argv,eye[1])
        else:
            eyeArgs=[0.0,0.0,-14.0]

        if view[0]==True:
            viewArgs=commandline.check_view(argv,view[1])
        else:
            viewArgs=[-10,10,-7.5,7.5,1024,768] 
         
        if light[0]==True:
            lightArgs=commandline.check_light(argv,light[1])
        else:
            lightArgs=[-100.0,100.0,-100.0,1.5,1.5,1.5]
         
        if ambient[0]==True:
            ambientArgs=commandline.check_ambient(argv,ambient[1])
        else:
            ambientArgs=[1.0,1.0,1.0]
     #All arguments set to default
     else:

     	eyeArgs=[0.0,0.0,-14.0]
        viewArgs=[-10,10,-7.5,7.5,1024,768]
        lightArgs=[-100.0,100.0,-100.0,1.5,1.5,1.5]
        ambientArgs=[1.0,1.0,1.0]

 	 # get the spheres from file and add to spList
     lineCount=0
     for line in file:
         lineCount+=1
         sp=commandline.get_sphere(line,lineCount)	  
        
         if sp != False:
              spList.append(commandline.get_sphere(line,lineCount))
 

     #OUTPUT IMAGE
     
     eyePt=data.Point(eyeArgs[0], eyeArgs[1], eyeArgs[2])

     lightPt=data.Point(lightArgs[0],lightArgs[1],lightArgs[2])
     lightCol=data.Color(lightArgs[3],lightArgs[4],lightArgs[5])
     light=data.Light(lightPt,lightCol)
     ambient=data.Color(ambientArgs[0],ambientArgs[1],ambientArgs[2])
 	 
     cast.cast_all_rays(viewArgs[0],viewArgs[1],viewArgs[2],viewArgs[3],\
     viewArgs[4],viewArgs[5],eyePt,spList,ambient,light)

def check_length(list):
    if len(list)<2:
        print "usage: python ray_caster.py <filename> [-eye x y z] [-view min_x max_x min_y max_y width height]\
        [-light x y z r g b] [-ambient r g b]"
        sys.exit()




if __name__== "__main__":
    main(sys.argv)



		


















