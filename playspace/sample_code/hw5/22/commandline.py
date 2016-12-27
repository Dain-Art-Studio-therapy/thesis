from sys import *
from cast import *
from data import *

def checkInputs(arguments):
	argument_list = []

	minX = -10
	maxX = 10
	minY = -7.5
	maxY = 7.5
	w = 1024	
	h = 768
	eye = Point(0.0,0.0,-14.0)
	amb = Color(1.0,1.0,1.0)
	lte = Light(Point(-100.0,100.0,-100.0),Color(1.5,1.5,1.5))
	
	for arg in arguments:
		if ("-view" in arg):
			view_list = checkView(arg,arguments)
			minX = view_list[0]
			maxX = view_list[1]
			minY = view_list[2]
			maxY = view_list[3]
			w = view_list[4]
			h = view_list[5]

		if ("-eye" in arg): 
			eye = checkEye(arg,arguments)

		if ("-ambient" in arg):
			amb = checkAmbient(arg,arguments)

		if ("-light" in arg):
			lte = checkLight(arg,arguments)

	return [minX,maxX,minY,maxY,w,h,eye,amb,lte]

def checkEye(val,arg_list):
	try:
		counter = arg_list.index(val)

		pt_x = float(arg_list[counter+1])
		pt_y = float(arg_list[counter+2])
		pt_z = float(arg_list[counter+3])

		returned_eye = Point(pt_x,pt_y,pt_z)
		return returned_eye 
	except:
		pass

def checkView(val,arg_list):
	try:
		counter = arg_list.index(val)

		minX = float(arg_list[counter+1])
		maxX = float(arg_list[counter+2])
		minY = float(arg_list[counter+3])
		maxY = float(arg_list[counter+4])
		w = int(arg_list[counter+5])
		h = int(arg_list[counter+6])

		returned_view = [minX,maxX,minY,maxY,w,h]
		return returned_view
	except:
		pass

def checkLight(val,arg_list):
	try:
		counter = arg_list.index(val)

		pt_x = float(arg_list[counter+1])
		pt_y = float(arg_list[counter+2])
		pt_z = float(arg_list[counter+3])
		lte_pt = Point(pt_x,pt_y,pt_z)

		lte_r = float(arg_list[counter+4])
		lte_g = float(arg_list[counter+5])
		lte_b = float(arg_list[counter+6])
		lte_color = Color(lte_r,lte_g,lte_b)

		returned_lte = Light(lte_pt,lte_color)
		return returned_lte
	except:
		pass

def checkAmbient(val,arg_list):
	try:
		counter = arg_list.index(val)

		amb_r = float(arg_list[counter+1])
		amb_g = float(arg_list[counter+2])
		amb_b = float(arg_list[counter+3])

		returned_amb = Color(amb_r,amb_g,amb_b)
		return returned_amb
	except:
		pass