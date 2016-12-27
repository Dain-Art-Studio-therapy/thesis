import sys
import data



def get_sphere(line,num): 
        
      l=line.split()
      if len(l)==11:
          try: 
             pt=data.Point=(float(l[0]),float(l[1]),float(l[2]))
             col=data.Color(float(l[4]),float(l[5]),float(l[6]))
             finish=data.Finish(float(l[7]),float(l[8]),float(l[9]),float(l[10]))
             sp=data.Sphere(pt,float(l[3]),col,finish)
             return sp
         
          except:
              print "malformed sphere on line:", "\t", num, "\t", "Skipping"
              return False
        
      else:
          print "malformed sphere on line:", "\t", num, "\t", "Skipping"
          return False

def check_eye(l,index):
		
  argList=[]
  defaultList=[0.0,0.0,-14.0]


  try: 
     arglist.append(float(l[index+1]))
     arglist.append(float(l[index+2]))
     arglist.append(float(l[index+3]))

  except:
     return defaultList

  return argList

def check_view(l,index):
		
    argList=[]
    defaultList=[-10,10,-7.5,7.5,1024,768]
    
    
        
    try:
        arglist.append(float(l[index+1]))
        arglist.append(float(l[index+2]))
        arglist.append(float(l[index+3]))
        arglist.append(float(l[index+4]))
        arglist.append(float(l[index+5]))
        arglist.append(float(l[index+6]))

    except:
        return defaultList
    return argList    

def check_light(l,index):
	
    argList=[]
    defaultList=[-100.0,100.0,-100.0,1.5,1.5,1.5]
    
    try:
        arglist.append(float(l[index+1]))
        arglist.append(float(l[index+2]))
        arglist.append(float(l[index+3]))
        arglist.append(float(l[index+4]))
        arglist.append(float(l[index+5]))
        arglist.append(float(l[index+6]))
         
    except:
        return defaultList
    return argList

def check_ambient(l,index):
     argList=[]
     defaultList=[1.0,1.0,1.0]
    
    
     try:
         arglist.append(float(l[index+1]))
         arglist.append(float(l[index+2]))
         arglist.append(float(l[index+3]))

     except:
         return defaultList
   
     return argList







    


 


