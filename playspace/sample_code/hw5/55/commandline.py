import sys
argv = sys.argv
from data import *

def open_file(name, mode):
   try: 
      return open(name, mode)
   except IOError as e:
      print >> sys.stderr, '{0}:{1}'.format(name, e.strerror)
      sys.exit()
#test3= open_file("crapdoc.tx", 'r')


def eye_arg(argv, argindex):
   try:
      ex= float(argv[argindex+1])
   except:
      print "Error: Missing/Wrong parameters for argument [-eye x]"
      ex= 0.0
   try:
      ey= float(argv[argindex+2])
   except:
      print "Error: Missing/Wrong parameters for argument [-eye y]"
      ey= 0.0
   try:
      ez= float(argv[argindex+3])
   except:
      print "Error: Missing/Wrong parameters for argument [-eye z]"
      ez= -14.0
   return Point(ex,ey,ez)

def view_arg(argv, argindex):
   try:
      min_x= float(argv[argindex+1])
   except:
      print "Error: Missing/Wrong parameters for argument [-view min_x]"
      min_x= -10
   try:
      max_x= float(argv[argindex+2])
   except:
      print "Error: Missing?Wrong parameters for argument [-view max_x]"
      max_x= 10
   try:
      min_y= float(argv[argindex+3])
   except:
      print "Error: Missing/Wrong parameters for argument [-view min_y]"
      min_y=-7.5
   try:
      max_y= float(argv[argindex+4])
   except:
      print "Error: Missing/Wrong parameters for argument [-view max_y]"
      max_y= 7.5
   try:
      width= float(argv[argindex+5])
   except:
      print "Error: Missing/Wrong parameters for argument [-view width]"
      width= float(1024)
   try:
      height= float(argv[argindex+6])
   except:
      print "Error: Missing/Wrong parameters for argument [-view height]"
      height= float(768)
   return [min_x, max_x, min_y, max_y, width, height]

def light_arg(argv, argindex):
   try: 
      lx= float(argv[argindex+1])
   except:
      print "Error: Missing/Wrong parameters for argument [-light x]"
      lx= -100
   try:
      ly= float(argv[argindex+2])
   except:
      print "Error: Missing/Wrong parameters for argument [-light y]"
      ly= 100
   try:
      lz= float(argv[argindex+3])
   except:
      print "Error: Missing/Wrong parameters for argument [-light z]"
      lz= -100
   lpoint = Point(lx, ly, lz)
   try:
      lr= float(argv[argindex+4])
   except:
      print "Error: Missing/Wrong parameters for argument [-light r]"
      lr= 1.5
   try:
      lg= float(argv[argindex+5])
   except:
      print "Error: Missing/Wrong parameters for argument [-light g]"
      lg= 1.5
   try:
      lb= float(argv[argindex+6])
   except:
      print "Error: Missing/Wrong parameters for argument [-light b]"
      lb= 1.5
   lcolor= Color(lr, lg, lb)
   return Light(lpoint, lcolor)

def ambient_arg(argv, argindex):
   try:
      ar= float(argv[argindex+1])
   except:
      print "Error: Missing/Wrong parameters for argument [-ambient r]"
      ar= 1.0
   try:
      ag= float(argv[argindex+2])
   except:
      print "Error: Missing/Wrong parameters for argument [-ambient g]"
      ag= 1.0
   try:
      ab= float(argv[argindex+3])
   except:
      print "Error: Missing/Wrong parameters for argument [-ambient b]"
      ab= 1.0
   return Color(ar, ag, ab)
      
def opt_args_func(argv, args_to_change, args_to_default):
   if '-eye' in args_to_change:
      argindex= args_to_change[args_to_change.index('-eye')+1]
      eye_point= eye_arg(argv, argindex)
   if '-eye' in args_to_default:
      eye_point= Point(0.0, 0.0, -14.0)
   
   if '-view' in args_to_change:
      argindex= args_to_change[args_to_change.index('-view')+1]
      view= view_arg(argv,argindex)
   if '-view' in args_to_default:
      view= [-10.0, 10.0, -7.5, 7.5, 1024, 768]

   if '-light' in args_to_change:
      argindex= args_to_change[args_to_change.index('-light')+1]
      lightsource= light_arg(argv, argindex)
   if '-light' in args_to_default:
      lightsource= Light(Point(-100,100,-100), Color(1.5,1.5,1.5))

   if '-ambient' in args_to_change:
      argindex= args_to_change[args_to_change.index('-ambient')+1]
      acolor= ambient_arg(argv, argindex)
   if '-ambient' in args_to_default:
      acolor= Color(1.0, 1.0, 1.0)
         
   return [view, eye_point, acolor, lightsource] 

#test1= opt_args_func(['-eye', 1, 'a', 3], 0, ['-eye'], ['-light', '-view', '-ambient'])

def commands(argv):
   if len(argv) <=1:
      print "Provide a file name"
      sys.exit()
   file1= open_file(argv[1], 'r')
   file1.close() 
   args_to_change=[]
   args_to_default=[]
   opt_args= ['-eye','-view','-light','-ambient']
   for argindex in range(2, len(argv)):
      if argv[argindex] in opt_args:
         args_to_change.append(argv[argindex])
         args_to_change.append(argindex)
   #print args_to_change
   for i in opt_args:
      if i not in argv:
         args_to_default.append(i)
   #print args_to_default
   list_of_lists= opt_args_func(argv, args_to_change, args_to_default)
   return list_of_lists
   

   

#test2= commands(['python', 'caster.py', 'crapdoc.txt', '-eye', 1, 2, 'a', '-light', 3, 4, 5])


