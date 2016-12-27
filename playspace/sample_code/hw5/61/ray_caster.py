from sys import argv
import cast
import commandline

def main():
   sf= commandline.open_file(argv[1], 'r')
   sphere_lists= commandline.make_spheres(sf)
   cast_other_constants= commandline.rays_other_values(argv)
   view= cast_other_constants[1]
   cast.cast_all_rays(view[0], view[1], view[2], view[3], view[4], view[5], cast_other_constants[0], sphere_lists, cast_other_constants[3], cast_other_constants[2])

if __name__ == '__main__':
   main()
