# Han Tran || CPE101-01,02 || Assignment 6
# puzzle_commandline 

import sys


def parse_commandline(argv):
   if len(argv) != 2:
      print >> sys.stderr, 'Usage: python puzzle.py <filename>'
      sys.exit()

