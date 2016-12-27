import data

def open_file(argv, mode):
   if len(argv) == 1:
      print 'usage: python ray_caster.py <filename> [-eye x y z] [-view min_x max_x min_y max_y width height] [-light x y z r g b] [-ambient r g b]'
      exit()

   try:
      return open(argv[1], mode)
   except:
      print 'error: cannot open file'
      exit()

def readfile(argv): 
   f = open_file(argv, 'rb')
   s = []
   for num, line in enumerate(f):
      n = line.split()
      if len(n) == 11:
         try:
            center = data.Point(float(n[0]), float(n[1]), float(n[2]))
            radius = float(n[3])
            color = data.Color(float(n[4]), float(n[5]), float(n[6]))
            finish = data.Finish(float(n[7]), float(n[8]), float(n[9]), float(n[10]))

            s.append(data.Sphere(center, radius, color, finish))

         except:
            print 'malformed sphere on line {0} ... skipping'.format(num+1)
      else:
         print 'malformed sphere on line {0} ... skipping'.format(num+1)

   f.close()

   return s

def options(argv):
   eye = data.Point(0.0, 0.0, -14.0)
   view = [-10, 10, -7.5, 7.5, 1024, 768]
   light = data.Light(data.Point(-100.0, 100.0, -100.0), data.Color(1.5, 1.5, 1.5))
   amb = data.Color(1.0, 1.0, 1.0)

   for num, e in enumerate(argv):
      if e == '-eye':
         try:
            eye = set_eye(argv, num)
         except:
            print 'error: cannot read eye flag'

      elif e == '-view':
         try:
            view = set_view(argv, num)
         except:
            print 'error: cannot read view flag'

      elif e == '-light':
         try:
            light = set_light(argv, num)
         except:
            print 'error: cannot read light flag'

      elif e == '-ambient':
         try:
            amb = set_amb(argv, num)
         except:
            print 'error: cannot read ambient flag'

   return [view, eye, amb, light] 

def set_eye(argv, num):
   x = float(argv[num + 1])
   y = float(argv[num + 2])
   z = float(argv[num + 3])
   return data.Point(x, y, z)

def set_view(argv, num):
   min_x = float(argv[num + 1])
   max_x = float(argv[num + 2])
   min_y = float(argv[num + 3])
   max_y = float(argv[num + 4])
   width = int(argv[num + 5])
   height = int(argv[num + 6])
   return [min_x, max_x, min_y, max_y, width, height]

def set_light(argv, num):
   x = float(argv[num + 1])
   y = float(argv[num + 2])
   z = float(argv[num + 3])
   r = float(argv[num + 4])
   g = float(argv[num + 5])
   b = float(argv[num + 6])
   return data.Light(data.Point(x, y, z), data.Color(r, g, b))

def set_amb(argv, num):
   r = float(argv[num + 1])
   g = float(argv[num + 2])
   b = float(argv[num + 3])
   return data.Color(r, g, b)

