import data

def open_file(name,mode):
   try:
      return open(name,mode)
   except:
      print 'Error: could not open file'
      exit()

def process_file(f):
   sphere_values = []
   sphere_list = []
   for line in f:
      try:
         nums = line.split()
         sphere_values.append((float(nums[0]),float(nums[1]),float(nums[2]),float(nums[3]),float(nums[4]),float(nums[5]),
                               float(nums[6]),float(nums[7]),float(nums[8]),float(nums[9]),float(nums[10])))
      except:
         print 'Error: file could not be read'

   for i in range(len(sphere_values)):
      sphere = data.Sphere(data.Point(sphere_values[i][0],sphere_values[i][1],sphere_values[i][2]),sphere_values[i][3],
                           data.Color(sphere_values[i][4],sphere_values[i][5],sphere_values[i][6]),
                           data.Finish(sphere_values[i][7],sphere_values[i][8],sphere_values[i][9],sphere_values[i][10]))
      sphere_list.append(sphere)

   return sphere_list

def test_argvs_float(argv,default):
   try: 
      return float(argv)
   except:
      return default

def test_argvs_int(argv,default):
   try:
      return int(argv)
   except:
      return default
