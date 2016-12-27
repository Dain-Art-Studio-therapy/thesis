import sys
import data
import cast
import commandline

# defaults
eye_x = 0.0
eye_y = 0.0
eye_z = -14.0
view_min_x = -10
view_max_x = 10
view_min_y = -7.5
view_max_y = 7.5
view_width = 1024
view_height = 768
light_x = -100.0
light_y = 100.0
light_z = -100.0
light_r = 1.5
light_g = 1.5
light_b = 1.5
ambient_r = 1.0 
ambient_g = 1.0
ambient_b = 1.0


def main(argv):
   sphere_list = commandline.main(argv)
                               
   cast.cast_all_rays(view_flag_min_x(argv), view_flag_max_x(argv), 
                      view_flag_min_y(argv), view_flag_max_y(argv),
                      view_flag_width(argv), view_flag_height(argv),
                      eye_flag(argv), sphere_list,
                      ambient_flag(argv), light_flag(argv))
      
         
def eye_flag(list):
   for (i, s) in enumerate(list):
      if '-eye' == s:
         try: 
            return data.Point(float(list[i+1]), float(list[i+2]),
                   float(list[i+3]))  
         except:
            return data.Point(eye_x, eye_y, eye_z)
   return data.Point(eye_x, eye_y, eye_z)  

def view_flag_min_x(list):
   for (i, s) in enumerate(list):
      if '-view' == s:
         try:
            return float(list[i+1])
         except:
            return view_min_x
   return view_min_x
   
def view_flag_max_x(list):
   for (i, s) in enumerate(list):
      if '-view' == s:
         try:
            return float(list[i+2])
         except:
            return view_max_x
   return view_max_x   

def view_flag_min_y(list):
   for (i, s) in enumerate(list):
      if '-view' == s:
         try:
            return float(list[i+3])
         except:
            return view_min_y
   return view_min_y  
   
def view_flag_max_y(list):
   for (i, s) in enumerate(list):
      if '-view' == s:
         try:
            return float(list[i+4])
         except:
            return view_max_y
   return view_max_y     
   
def view_flag_width(list):
   for (i, s) in enumerate(list):
      if '-view' == s:
         try:
            return float(list[i+5])
         except:
            return view_width
   return view_width  

def view_flag_height(list):
   for (i, s) in enumerate(list):
      if '-view' == s:
         try:
            return float(list[i+6])
         except:
            return view_height
   return view_height
              
def light_flag(list):
   for (i, s) in enumerate(list):
      if '-light' == s:
         try:
            return data.Light(data.Point(float(list[i+1]), 
                   float(list[i+2]), float(list[i+3])), 
                   data.Color(float(list[i+4]), 
                   float(list[i+5]), float(list[i+6])))
         except:
            return data.Light(data.Point(light_x, light_y, light_z), 
                   data.Color(light_r, light_g, light_b))
   return data.Light(data.Point(light_x, light_y, light_z), 
                     data.Color(light_r, light_g, light_b))  
                     
def ambient_flag(list):
   for (i, s) in enumerate(list):
      if '-ambient' == s:
         try: 
            return data.Color(float(list[i+1]), float(list[i+2]),
                   float(list))  
         except:
            return data.Color(ambient_r, ambient_g, ambient_b)
   return data.Color(ambient_r, ambient_g, ambient_b)                            
           

if __name__ == '__main__':
   main(sys.argv)
   