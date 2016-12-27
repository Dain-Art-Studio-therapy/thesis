import data
def get_values(L):
   try:
      filename = L[1]
   except IndexError:
      print 'usage: python ray_caster.py <filename> [-eye x y z] [-view min_x max_x min_y max_y width height] [-light x y z r g b] [-ambient r g b]'
      exit
   c = 0
   for i in range(len(L)):
      if L[i] == '-view':
         c = i
   if c != 0:
      try:
         min_x = float(L[c+1])
      except:
         min_x = -10
      try:
         max_x = float(L[c+2])
      except:
         max_x = 10
      try:
         min_y = float(L[c+3])
      except:
         min_y = -7.5
      try:
         max_y = float(L[c+4])
      except:
         max_y = 7.5
      try:
         width = int(L[c+5])
      except:
         width = 1024
      try:
         height = int(L[c+6])
      except:
         height = 768
   else:
      min_x = -10
      max_x = 10
      min_y = -7.5
      max_y = 7.5
      width = 1024
      height = 768
   eye = create_eye(L)
   light = create_light(L)
   ambient = create_ambient(L)



   return [filename,eye,min_x,max_x,min_y,max_y,width,height,light,ambient]

def create_eye(L):
   c = 0
   for i in range(len(L)):
      if L[i] == '-eye':
         c = i
   if c != 0:
      try:
         x = float(L[c+1])
      except:
         x = 0.0
      try:
         y = float(L[c+2])
      except:
         y = 0.0
      try:
         z = float(L[c+3])
      except:
         z = -14.0
   else:
      x = 0.0
      y = 0.0
      z = -14.0
   return data.Point(x,y,z)

def create_light(L):
   c = 0
   for i in range(len(L)):
      if L[i] == '-light':
         c = i
   if c != 0:
      try:
         x = float(L[c+1])
      except:
         x = -100.0
      try:
         y = float(L[c+2])
      except:
         y = 100.0
      try:
         z = float(L[c+3])
      except:
         z = -100.0
      try:
         r = float(L[c+4])
      except:
         r = 1.5
      try:
         g = float(L[c+5])
      except:
         g = 1.5
      try:
         b = float(L[c+6])
      except:
         b = 1.5
   else:
      x = -100.0
      y = 100.0
      z = -100.0
      r = 1.5
      g = 1.5
      b = 1.5
   return data.Light(data.Point(x,y,z),data.Color(r,g,b))

def create_ambient(L):
   c = 0
   for i in range(len(L)):
      if L[i] == '-ambient':
         c = i
   if c != 0:
      try:
         r = float(L[c+1])
      except:
         r = 1.0
      try:
         g = float(L[c+2])
      except:
         g = 1.0
      try:
         b = float(L[c+3])
      except:
         b = 1.0
   else:
      r = 1.0
      g = 1.0
      b = 1.0
   return data.Color(r,g,b)


