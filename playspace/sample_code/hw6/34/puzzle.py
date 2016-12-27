import sys



def main(argv):

   f=try_open(argv[1],'r')
   head1=f.readline().split()
   head2=f.readline().split()
   head3=f.readline().split()
   mergedList=[]
   for line in f:
      
   		#color values split up and added to larger string
        mergedList.append(line.split())
    
   #NEED TO PUT LIST OF LISTS INTO A INT LISTS
   int_list=conv_list(mergedList)
   #color values divided into list of three into a list
   groupedList=groups_of_3(int_list)
   
   #Set up the image for writing
   try_write(groupedList,head2[0],head2[1])
   f.close()

def groups_of_3(list):
    mainList=[]
    for n in range(0,len(list),3):
          mainList.append(list[n:n+3])
          
    return mainList

def try_write(inputList,width,height):
    output=try_open('output.ppm','w')

    output.write("P3"+"\n") 
    #How do we calculate width and height?
    output.write(width+" "+height+"\n")
    output.write("255"+ "\n") 
   
    #print RGB Values from grouped list
    for col in range(len(inputList)):
        r=inputList[col][0]*10
        if r>255:
            r=255
        g=r
        b=r
        output.write(str(r)+" "+str(g)+" "+str(b)+"\n")
    output.close()

def conv_list(inputList):
    intList=[]
    for e in range(len(inputList)):
       for f in range(len(inputList[e])):
            intList.append(int(inputList[e][f]))
    return intList
        


def try_open(file,mode):
    try:
      newfile=open(file,mode)
      return newfile
    except:
      print "Cannot open file\n"
      print"Usage: Please enter filename only\n"    

if __name__== "__main__":
    main(sys.argv)