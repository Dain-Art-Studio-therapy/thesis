from sys import *
import math

def main():
   file_name = "error"
   outFile = open("faded.ppm", "w")
   

   
   if len(argv) == 5:
      try:
         file_name = argv[1]
         row = int(argv[2])
         col = int(argv[3])
         radius = int(argv[4])
         
         inFile = open(file_name, 'r')     
      except:
         print("Unable to open %s" %file_name)
         exit()
   else:
      print("Usage: python fade.py <image> <row> <column> <radius>")
      exit()
      
   header = inFile.readline() #"P3"
   w_and_h = inFile.readline().split()
   width = int(w_and_h[0])
   height = int(w_and_h[1])
   MAX_COMP_NUM = int(inFile.readline()) #default is 255
   
   outFile.write(header + str(width) + " " + str(height) + "\n" + str(MAX_COMP_NUM) + "\n")

   rgb = []
   cRow = 0
   cCol = 0
   for line in inFile:
      line = line.split()
      for comp in line:
         if len(rgb) != 3:
            ###print(rgb)###
            rgb.append(comp)
            
         if len(rgb) == 3:
            distance = math.sqrt((row-cRow)**2 + (col-cCol)**2)
            scalar = (radius - distance) / radius                          
            if scalar < 0.2:
               scalar = 0.2
               
            red = int(int(rgb[0]) * scalar)
            green = int(int(rgb[1]) * scalar)
            blue = int(int(rgb[2]) * scalar)
            
            newPixel = str(red) + " " + str(green) + " " + str(blue) + "\n"
            outFile.write(newPixel)
            rgb = []
            
            #update current Pixel location to be next pixel
            if cCol == width - 1:
               cCol = 0
               cRow += 1
            else:
               cCol += 1
            
           
           
   inFile.close()
   outFile.close()
               
               

if __name__ == '__main__':
   main()
