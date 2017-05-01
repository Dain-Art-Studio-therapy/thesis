from sys import *
import math

def main():
   file_name = "error"
   outFile = open("blurred.ppm", "w")
   
   try:
      if len(argv) == 2:
         file_name = argv[1]
         reach = 4
         
         inFile = open(file_name, 'r') 
         
      elif len(argv) == 3:
         file_name = argv[1]
         reach = int(argv[2])
         
         inFile = open(file_name, 'r') 
      else:
         print("Usage: python blur.py <image> <OPTIONAL:reach>")
         exit()         
   except IOError:
      print("Unable to open %s" %file_name)
      exit()
  
   header = inFile.readline() #"P3"
   w_and_h = inFile.readline().split()
   width = int(w_and_h[0])
   height = int(w_and_h[1])
   MAX_COMP_NUM = int(inFile.readline()) #default is 255
   
   outFile.write(header + str(width) + " " + str(height) + "\n" + str(MAX_COMP_NUM) + "\n")

   pixels = []
   rgb = []
   for line in inFile:
      line = line.split()
      for comp in line:
         if len(rgb) != 3:
            rgb.append(comp)
         if len(rgb) == 3:
            pixels.append(rgb)
            rgb = []
            
   picture = []
   i = 0
   for row in range(height):
      row = []
      for col in range(width):
         row.append(pixels[i])
         i += 1
      picture.append(row)
    
   #print(picture)
   #exit()
   
   cCol = 0
   cRow = 0
   for pixel in pixels:
      totalR = 0
      totalB = 0
      totalG = 0
      totalP = 0

      #calculate lower bounds of neighborhood
      lowCol = 0
      if cCol - reach > 0:
         lowCol = cCol - reach        
      lowRow = 0
      if cRow - reach > 0:
         lowRow = cRow - reach

      #calculate upper bounds of neighborhood
      upCol = width
      if cCol + reach < upCol:
         upCol = cCol + reach        
      upRow = height
      if cRow + reach < upRow:
         upRow = cRow + reach
      
      ###print("upCol:", upCol)###
      ###print("lowCol:", lowCol)###
      ###print("upRow:", upRow)###
      ###print("lowRow:", lowRow)###
      ###print("posn: [" + str(cCol) + ", " + str(cRow) + "]")
         
      #calculate neighborhood totals
      rows = picture[lowRow:upRow] #cuts out irrelevant rows
      #print(rows)
      for row in rows:
         cols = row[lowCol:upCol]
         
         #if cCol == 4 and cRow == 4:
            #print(cols)  
            
         for neighbor in cols:
            totalR += int(neighbor[0])
            totalG += int(neighbor[1])
            totalB += int(neighbor[2])
            totalP += 1
            
              
      red = int(totalR / totalP)
      green = int(totalG / totalP)
      blue = int(totalB / totalP)
      
      #write out new pixel
      newPixel = str(red) + " " + str(green) + " " + str(blue) + "\n"
      outFile.write(newPixel)
      
      #updates position
      if cCol == width - 1:
         cCol = 0
         cRow += 1
      else:
         cCol += 1
            
            
           
           
   inFile.close()
   outFile.close()
               
               

if __name__ == '__main__':
   main()
