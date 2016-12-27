
import cast
import data

eyePt= data.Point(0.0,0.0,-14.0)
center1=data.Point(1.0,1.0,0.0)
center2=data.Point(0.5,1.5,-3.0)
color1=data.Color(1.0,0.0,0.0)
color2=data.Color(0.0,0.0,1.0)
rFinish=data.Finish(.4)
bFinish=data.Finish(.2)
ambient=data.Color(1.0,1.0,1.0)
spList=[data.Sphere(center1,2.0,color2,bFinish), data.Sphere(center2,0.5,color1,rFinish)]
cast.cast_all_rays(-10,10,-7.5,7.5,1024,768,eyePt,spList,ambient)

