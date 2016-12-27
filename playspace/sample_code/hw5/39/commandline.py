import data
   
def find_eye(arguments):
   x1 = 0.0
   y1 = 0.0
   z1 = -14.0
   for k in range(1, len(arguments)):
      if (arguments[k] == '-eye'):
        try:
            x1 = float(arguments[k+1])
            y1 = float(arguments[k+2])
            z1 = float(arguments[k+3])
        except:
            pass
   return data.Point(float(x1), float(y1), float(z1))
   

def find_view(arguments):
   new = []
   for k in range(1, len(arguments)):
      if(arguments[k] == '-view'):
         new.append(float(arguments[k+1]))
         new.append(float(arguments[k+2]))
         new.append(float(arguments[k+3]))
         new.append(float(arguments[k+4]))
         new.append(int(arguments[k+5]))
         new.append(int(arguments[k+6]))
   if (new == []):
      new = [-10, 10, -7.5, 7.5, 1024, 768]
   return new

def find_light(arguments):
   x1 = -100.0
   y1 = 100.0
   z1 = -100.0
   r1 = 1.5
   g1 = 1.5
   b1 = 1.5
   for k in range(1, len(arguments)):
      if(arguments[k] == '-light'):
         x1 = float(arguments[k+1])
         y1 = float(arguments[k+2])
         z1 = float(arguments[k+3])
         r1 = float(arguments[k+4])
         g1 = float(arguments[k+5])
         b1 = float(arguments[k+6])
   return data.Light(data.Point(x1, y1, z1), data.Color(r1, g1, b1))

def find_ambient(arguments):
   r1 = 1.0
   g1 = 1.0
   b1 = 1.0
   for k in range(1, len(arguments)):
      if (arguments[k] == '-ambient'):
         r1 = float(arguments[k+1])
         g1 = float(arguments[k+2])
         b1 = float(arguments[k+3])
   return data.Color(r1, g1, b1)
