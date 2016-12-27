import sys
from data import * 


def eye(argv,index):
      x = float(argv[index+1])
      y = float(argv[index+2])
      z = float(argv[index+3])
      new_eye = Point(x,y,z)
      return new_eye

def light(argv,index):
     x = float(argv[index+1])
     y = float(argv[index+2])
     z = float(argv[index+3])
     r = float(argv[index+4])
     g = float(argv[index+5])
     b = float(argv[index+6])
     new_light = Light(Point(x,y,z),Color(r,g,b))
     return new_light
   
def ambient(argv,index):
       r = float(argv[index+1])
       g = float(argv[index+2])
       b = float(argv[index+3])
       new_amb = Color(r,g,b)
       return new_amb
   
        

def view(argv,index):
    
    min_x = int(float(argv[index+1])) # invalid literal
    max_x = int(float(argv[index+2])) 
    min_y = int(float(argv[index+3]))
    max_y = int(float(argv[index+4]))
    width = int(float(argv[index+5]))
    height= int(float(argv[index+6]))
    new_view = [min_x,max_x,min_y,max_y,width,height]
    return new_view
