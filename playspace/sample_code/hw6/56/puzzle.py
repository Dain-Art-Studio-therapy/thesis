import sys

def try_open(file_name): 
    try:
        file_handle = open(file_name, 'r') 
        return file_handle 
    except:
        print 'Error - Does not open' 
        exit() 

def make_raster(file_handle):
    raster = []
    count = 0
    for line in file_handle:
        if count > 2: 
            if count % 3 == 0:
                raster.append(int(line))  
        count += 1 
    return raster

def initialize(file_name, out_fh):
    a = open(file_name, 'r')
    out_fh.write(a.readline())
    out_fh.write(a.readline())
    out_fh.write(a.readline())
    a.close()

def output(file_name, raster):
    out_fh = open('hidden.ppm', 'w')
    initialize(file_name, out_fh) 
    for color in raster:
        for _ in xrange(3):
            out_fh.write(str(min(color * 10, 255))+'\n')

def main():
    file_name = sys.argv[1]
    file_handle = try_open(file_name) 
    raster = make_raster(file_handle) 
    output(file_name, raster) 
    

if __name__ == '__main__':
    main() 
    
        
    
