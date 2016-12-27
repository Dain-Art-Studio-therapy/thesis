# Han Tran || CPE 101-01,02 || Assignment 6

import sys
import puzzle_commandline
import puzzle_image_reading
import puzzle_image_output


def main(argv):
   puzzle_commandline.parse_commandline(argv)
   read_image = puzzle_image_reading.puzzle_image_read(argv, 'r')
   puzzle_image_output.image_output(read_image)



if __name__ == '__main__':
   main(sys.argv)
