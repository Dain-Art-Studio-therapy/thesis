import sys
import commandline

def main(argv):
    fileout = sys.stdout
    with open('image.ppm','w') as f:
        sys.stdout = f
        commandline.run(argv)
    


if __name__ == '__main__':
    main(sys.argv)
