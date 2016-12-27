# Han Tran || CPE101-01,02 || Assignment 6
# blur.py

import sys
import blur_commandline
import blur_image_reading
import blur_image_output
import group_function

def main(argv):
   blurFactor = blur_commandline.parse_commandline(argv)
   compute_RGB = blur_image_reading.blur_image_read(argv, 'r')
   #print compute_RGB.header
   RGB_grid = compute_RGB.grid
   RGB_header = compute_RGB.header
   blur_RGB = blur_calculation(compute_RGB, blurFactor)
   blur_image_output.image_output(RGB_header, blur_RGB)


def blur_calculation(GRID, blurFAC):
   header = GRID.header
   dim = map(int, (GRID.header[1]).split()) # get the dimension in header
   width = dim[0]
   height = dim[1]
   RGB_GRID = GRID.grid
   newLIST = []
   for row in range(len(RGB_GRID)):
      for col in range(len(RGB_GRID[row])):
         max_up = get_maxUp(row, blurFAC)
         max_down = get_maxDown(row, blurFAC, height)
         max_left = get_maxLeft(col, blurFAC)
         max_right = get_maxRight(col, blurFAC, width)
         newPix = blur_pixel(RGB_GRID, row, col, 
                             max_up, max_down, max_left, max_right)
         newLIST.append(newPix[0])
         newLIST.append(newPix[1])
         newLIST.append(newPix[2])
   newGRID = blur_image_reading.list_to_grid(newLIST, GRID.header)
   return newGRID


# ---- Supportive Function --- #
def blur_pixel(GRID, ROW_POS, COL_POS, MAXUP, MAXDOWN, MAXLEFT, MAXRIGHT):
   # ROW = Y-COORDINATE,    COL = X-COORDINATE
   red = 0
   green = 0
   blue = 0
   counter = 0
   for y in range(-MAXUP, MAXDOWN, 1): #+ 1):
      y_pos = ROW_POS + y
      for x in range(-MAXLEFT, MAXRIGHT, 1): # + 1):
         x_pos = COL_POS + x
         red += GRID[y_pos][x_pos][0]
         green += GRID[y_pos][x_pos][1]
         blue += GRID[y_pos][x_pos][2]
         counter = counter + 1
   red = float(red)/counter
   green = float(green)/counter
   blue = float(blue)/counter
   return [red, green, blue]


def get_maxUp(ROW, BLURFAC):
   max_up = 0
   if ROW < BLURFAC:
      max_up = ROW
   else:
      max_up = BLURFAC
   return max_up


def get_maxDown(ROW, BLURFAC, HEIGHT):
   max_down = 0
   if (ROW + BLURFAC) > HEIGHT:
      max_down = HEIGHT - ROW #- 1
   else:
      max_down = BLURFAC
   return max_down


def get_maxLeft(COL, BLURFAC):
   max_left = 0
   if COL < BLURFAC:
      max_left = COL
   else:
      max_left = BLURFAC
   return max_left


def get_maxRight(COL, BLURFAC, WIDTH):
   max_right = 0
   if (COL + BLURFAC) > WIDTH:
      max_right = WIDTH - COL #- 1
   else:
      max_right = BLURFAC
   return max_right



if __name__ == '__main__':
   main(sys.argv)
