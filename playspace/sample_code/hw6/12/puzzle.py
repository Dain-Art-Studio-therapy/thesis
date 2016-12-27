import sys
from puzzle_commandline import *

def open_file(name, mode):
	try:
		return open(name, mode)
	except IOError as e: # return error if the file does not exist
		print >> sys.stderr, '{0}:{1}'.format(name, e.strerror)
		sys.exit(1) # exit open file

def main(argv):
	# check if the arguments amount are correct
	if len(sys.argv) != 2:
		print 'usage: python puzzle.py <filename>' # instruction
	else:
		with open_file(argv[1], 'rb') as f: # open the input file
			ppm_format = process_file(f)
		with open_file('hidden.ppm', 'wb') as g: # open the output file
			puzzle_print_out(ppm_format, g)
			# print the decoded image onto 'hidden.ppm' output file


if __name__ == '__main__':
	main(sys.argv)
