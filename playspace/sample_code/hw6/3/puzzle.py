import sys

OUTFILE = 'hidden.ppm'

def main(argv):
	checkArgs(argv)
	
	infile = open(argv[1], "r")
	outfile = open(OUTFILE, "w")
	
	header = getHeader(infile)
	writeHeader(outfile, header)
	
	pixel = getNextPixel(infile)
	while pixel != (None, None, None):
		pixel = ampRed(pixel)
		writePixel(outfile, pixel)
		pixel = getNextPixel(infile)
		
	outfile.close()
	infile.close()

def writePixel(outfile, pixel):
	outfile.write(pixel[0] + " " + pixel[1] + " " +\
				  pixel[2] + "\n")
	
def ampRed(pixel):
	r = float(pixel[0]) * 10
	if r > 255:
		r = 255
	col = str(r)
	return (col, col, col)
	
def writeHeader(outfile, header):
	outfile.write(header[0] + "\n" + header[1] + " " +\
				  header[2] + "\n" + header[3] + "\n")
	
def getNextPixel(infile):
	pixel = (getNextParam(infile),\
			 getNextParam(infile),\
			 getNextParam(infile))
	return pixel
	
def getHeader(infile):
	header = (getNextParam(infile),\
			  getNextParam(infile),\
			  getNextParam(infile),\
			  getNextParam(infile))
	return header
	
def getNextParam(infile):
	string = ''
	c = infile.read(1)
	if c == '':
		return None
	while len(string) <= 3 and c != ' ' and c != '\n':
		string += c
		c = infile.read(1)
	return string
	
def checkArgs(argv):
	if len(argv) != 2:
		sys.exit("Invalid arguments")
	checkFile(argv[1])

def checkFile(fileName):	
	try:
		f = open(fileName)
		f.close()
	except:
		sys.exit("Error : File cannot be opened.")
	
if __name__ == "__main__":
	main(sys.argv)