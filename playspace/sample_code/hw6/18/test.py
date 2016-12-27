def d2_grid(pixels, width):
   y=[]
   x=[]
   for i in range(len(pixels)):
      x.append(pixels[i])
      if (i+1)%width==0:
         y.append(x)
         x =[]
   return y

def color_loop(grid, reach, height, width):
   newpixels= []
   for y in range(len(grid)):
      for x in range(len(grid[y])):
         avgcolor= average(grid, reach, y, x, height, width)
         newpixels.append(avgcolor)
   return newpixels

def average(grid, reach, y, x, height, width):
   localpixels=[]
   for ly in range(y-reach, y+reach+1):
      if ly >= 0 and ly <= height-1:
         for lx in range(x-reach, x+reach+1):
            if lx >= 0 and lx < width:
               localpixels.append(grid[ly][lx])
          
   return average_math(localpixels)

#test2= average([[[0,0,0],[1,1,1], [2,2,2]], [[3,3,3], [4,4,4], [5,5,5]], [[6,6,6], [7,7,7], [8,8,8]]], 1, 0, 0, 3, 3)       
#print test2

def average_math(localpixels):
   r =0
   g =0
   b =0
   length= len(localpixels)
   for n in range(length):
      r+= float(localpixels[n][0])
      g+= float(localpixels[n][1])
      b+= float(localpixels[n][2])

   r= r/float(length) 
   if r > 255:
      r = 255
   g= g/float(length) 
   if g > 255:
      g = 255
   b= b/float(length) 
   if b > 255:
      b = 255
   return str(int(r))+' '+str(int(g))+' '+str(int(b))+'\n'
   

#test3= average([[[0,0,0],[1,1,1], [2,2,2]], [[3,3,3], [4,4,4], [5,5,5]], [[6,6,6], [7,7,7], [8,8,8]]], 1, 2, 2, 3, 3)       


#test1= d2_grid([['0','0','0'],['1','1','1'], ['2','2','2'], ['3','3','3'], ['4','4','4'], ['5','5','5'], ['6','6','6',], ['7','7','7'], ['8','8','8']], 3)
#print test1
#color_loop(test1, 1, 3, 3)
def test_machine(num):
   testlist=[]
   for i in range(num):
      n= str(i)
      testlist.append([n,n,n])
   return testlist
test4= test_machine(197693)
temp4= d2_grid(test4, 493)
fin= color_loop(temp4, 1, 401, 493)
print 'P3'
print '493', '401'
print '255'
print ''.join(fin)
