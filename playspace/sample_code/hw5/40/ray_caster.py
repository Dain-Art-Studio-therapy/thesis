import commandline
import sys
import cast
import data

def main(argv):
	commandline.checkArgs(argv)
	file = argv[1]
	eye = commandline.getEye(argv)
	view = commandline.getView(argv)
	light = commandline.getLight(argv)
	ambient = commandline.getAmbient(argv)
	sphereList = getSpheres(file)
	
	f = open('image.ppm', 'w')
	sys.stdout = f
	cast.cast_all_rays(view[0], view[1], view[2], view[3], view[4], view[5],\
					   eye, sphereList, ambient, light)
	f.close()
	
def getSpheres(file):
	sphereList = []
	with open(file) as f:
		lines = [line.rstrip() for line in f]
		for i in range(len(lines)):
			params = lines[i].split(' ')
			if len(params) != 11:
				print "malformed sphere on line", i, "... skipping"
			try:
				sX = float(params[0])
				sY = float(params[1])
				sZ = float(params[2])
				sRadius = float(params[3])
				sR = float(params[4])
				sG = float(params[5])
				sB = float(params[6])
				sAmbient = float(params[7])
				sDiffuse = float(params[8])
				sSpecular = float(params[9])
				sRoughness = float(params[10])
				sPos = data.Point(sX, sY, sZ)
				sColor = data.Color(sR, sG, sB)
				sFinish = data.Finish(sAmbient, sDiffuse,\
									  sSpecular, sRoughness)
				sphere = data.Sphere(sPos, sRadius, sColor, sFinish)
				sphereList.append(sphere)
			except:
				print "malformed sphere on line", i, "... skipping"
	return sphereList
	f.closed
	
if __name__ == "__main__":
	main(sys.argv)