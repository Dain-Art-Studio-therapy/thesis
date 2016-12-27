import sys
import data

def checkArgs(argv):
	if len(argv) < 2:
		sys.exit("Improper number of arguments")
	
	checkFile(argv[1])
	
def checkFile(fileName):	
	try:
		f = open(fileName)
		f.close()
	except:
		print "Error: File could not be opened"
		print "usage: python ray_caster.py <filename> "\
		"[-eye x y z] [-view min_x max_x min_y max_y width height] "\
		"[-light x y z r g b] [-ambient r g b]"
		sys.exit(1)
		
def getEye(argv):
	for i in range(len(argv)):
		if argv[i] == "-eye":
			try:
				eyeX = float(argv[i + 1])
				eyeY = float(argv[i + 2])
				eyeZ = float(argv[i + 3])
				return data.Point(eyeX, eyeY, eyeZ)
			except:
				return data.Point(0.0, 0.0, -14.0)
	return data.Point(0.0, 0.0, -14.0)
	
def getView(argv):
	for i in range(len(argv)):
		if argv[i] == "-view":
			try:
				min_x = float(argv[i + 1])
				max_x = float(argv[i + 2])
				min_y = float(argv[i + 3])
				max_y = float(argv[i + 4])
				width = int(argv[i + 5])
				height = int(argv[i + 6])
				return (min_x, max_x, min_y, max_y, width, height)
			except:
				return (-10.0, 10.0, -7.5, 7.5, 1024, 768)
	return (-10.0, 10.0, -7.5, 7.5, 1024, 768)
	
def getLight(argv):
	for i in range(len(argv)):
		if argv[i] == "-light":
			try:
				lightX = float(argv[i + 1])
				lightY = float(argv[i + 2])
				lightZ = float(argv[i + 3])
				lightR = float(argv[i + 4])
				lightG = float(argv[i + 5])
				lightB = float(argv[i + 6])
				lightPos = data.Point(lightX, lightY, lightZ)
				lightColor = data.Color(lightR, lightG, lightB)
				return (data.Light(lightPos, lightColor))
			except:
				return data.Light(data.Point(-100.0, 100.0, -100.0),\
						data.Color(1.5, 1.5, 1.5))
	return data.Light(data.Point(-100.0, 100.0, -100.0),\
			data.Color(1.5, 1.5, 1.5))
	
def getAmbient(argv):
	for i in range(len(argv)):
		if argv[i] == "-ambient":
			try:
				ambientR = float(argv[i + 1])
				ambientG = float(argv[i + 2])
				ambientB = float(argv[i + 3])
				return data.Color(ambientR, ambientG, ambientB)
			except:
				return data.Color(1.0, 1.0, 1.0)
	return data.Color(1.0, 1.0, 1.0)