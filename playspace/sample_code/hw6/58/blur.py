import commandline
import sys

def main():
   cmdline = commandline.process(sys.argv)
   outfile = open('blurred.ppm', 'w')
 
   print_header(cmdline[0][0], outfile)
   pixels = cmdline[0][1]
   blur = int(cmdline[1])
   width = int(cmdline[0][0][1])
   height = int(cmdline[0][0][2])
   
   print_pixels(pixels, blur, width, height, outfile)
   outfile.close()

def print_header(list, outfile):
   print >> outfile, list[0]
   print >> outfile, list[1], list[2]
   print >> outfile, list[3]

def print_pixels(pixels, blur, width, height, file):
   numb = 0
   M = create_matrix(pixels, width, height)
   for y in range(height):
      for x in range(width):
         rtotal = 0
         gtotal = 0
         btotal = 0
         for i in range(y - blur, y + blur + 1):
            for j in range(x - blur, x + blur + 1):
                if is_inrange(j, width, i, height):
                   numb += 1
                   rtotal += int(M[i][j][0])
                   gtotal += int(M[i][j][1])
                   btotal += int(M[i][j][2])
         r = int(rtotal / numb)
         g = int(gtotal / numb)
         b = int(btotal / numb)
         print >> file, r, g, b
         numb = 0       
         
def create_matrix(pixels, width, height):
   M = [[[0, 0, 0] for x in range(width)] for y in range(height)]
   count = 0
   for y in range(height):
      for x in range(width):
         M[y][x] = pixels[count]
         count += 1
   return M
   
def is_inrange(i, width, j, height):
   if (i >= 0) and (i < width) and (j >= 0) and (j < height):
      return True
   return False

if __name__ == '__main__':
   main()


