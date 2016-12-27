# Han Tran || CPE 101-01,02 || Assignment 6
# fade.py

import math
import sys
import fade_commandline
import fade_image_reading
import fade_image_output


def main(argv):
   fade_commandline.parse_commandline(argv)
   # makeList_RGB = [[[r,g,b], [r,g,b], etc], ['P3', 'width height', '255']]
   makeList_RGB = fade_image_reading.fade_image_read(argv, 'r')
   row = int(argv[2])
   col = int(argv[3])
   radius = int(argv[4])
   headerList = makeList_RGB[1]
   rgb_fade = fading_pixel(makeList_RGB, col, row, radius)
   fade_image_output.image_output(headerList, rgb_fade)


# ---- Supportive Functions ---- #

def fading_pixel(list_rgb, x_coor, y_coor, RADIUS):
   # x_coor = COL in argv, y_coor = ROW in agrv
   dim = map(int, (list_rgb[1][1].split()))
   width = dim[0]
   height = dim[1]
   RGB_pixel = list_rgb[0]
   RGB_fadeImage = []
   i = 0   
   for row in range(0, height):
      for col in range(0, width): 
         dis = distance( [col, row], [x_coor, y_coor])
         scale = float(RADIUS - dis)/RADIUS
         if scale < 0.2:
            scale = 0.2
         newRGB = scale_rgb(RGB_pixel[i], scale)
         i += 1
         RGB_fadeImage.append(newRGB)
   return RGB_fadeImage



def distance(pt1, pt2):
   return math.sqrt( (pt1[0] - pt2[0])**2 + (pt1[1] - pt2[1])**2 )



def scale_rgb(PIXEL, SCALE):
   return [SCALE * component for component in PIXEL]




if __name__ == '__main__':
   main(sys.argv)
