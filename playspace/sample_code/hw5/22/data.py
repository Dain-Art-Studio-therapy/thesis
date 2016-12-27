import utility

class Point():
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __eq__(self,other):
        check_x = utility.epsilon_equal(self.x,other.x)
        check_y = utility.epsilon_equal(self.y,other.y)
        check_z = utility.epsilon_equal(self.z,other.z)

        return check_x and check_y and check_z
    
class Vector():
    def __init__(self, vx, vy, vz):
        self.vx = vx
        self.vy = vy
        self.vz = vz

    def __eq__(self,other):
        check_vx = utility.epsilon_equal(self.vx,other.vx)
        check_vy = utility.epsilon_equal(self.vy,other.vy)
        check_vz = utility.epsilon_equal(self.vz,other.vz)

        return check_vx and check_vy and check_vz

class Ray():
    def __init__(self, point, dir):
        self.point = point
        self.dir = dir

    def __eq__(self,other):
        check_ptx = utility.epsilon_equal(self.point.x,other.point.x)
        check_pty = utility.epsilon_equal(self.point.y,other.point.y)
        check_ptz = utility.epsilon_equal(self.point.z,other.point.z)
        check_all_pt = check_ptx and check_pty and check_ptz

        check_dirVX = utility.epsilon_equal(self.dir.vx,other.dir.vx)
        check_dirVY = utility.epsilon_equal(self.dir.vy,other.dir.vy)
        check_dirVZ = utility.epsilon_equal(self.dir.vz,other.dir.vz)
        check_all_dir = check_dirVX and check_dirVY and  check_dirVZ

        return check_all_pt and check_all_dir
    
class Sphere():
    def __init__(self, center, radius, color, finish):
        self.center = center
        self.radius = radius
        self.color = color
        self.finish = finish

    def __eq__(self,other):
        return utility.epsilon_equal(self.center.x,other.center.x) and utility.epsilon_equal(self.center.y,other.center.y) and utility.epsilon_equal(self.center.z,other.center.z) and utility.epsilon_equal(self.radius,other.radius) and utility.epsilon_equal(self.color.r,other.color.r) and utility.epsilon_equal(self.color.g,other.color.g) and utility.epsilon_equal(self.color.b,other.color.b) and utility.epsilon_equal(self.finish,other.finish)

class Color():
    def __init__(self,r,g,b):
        self.r = r
        self.g = g
        self.b = b
        
    def __eq__(self,other):
        return utility.epsilon_equal(self.r,other.r) and utility.epsilon_equal(self.g,other.g)and utility.epsilon_equal(self.b,other.b)

class Finish():
    def __init__(self, ambient, diffuse, specular, roughness):
        self.ambient = ambient
        self.diffuse = diffuse
        self.specular = specular
        self.roughness = roughness
    def __eq__(self,other):
        return utility.epsilon_equal(self.ambient,other.ambient) and utility.epsilon_equal(self.diffuse,other.diffuse) and utility.epsilon_equal(self.specular,other.specular) and utility.epsilon_equal(self.roughness,other.roughness)

class Light():
    def __init__(self, point, color):
        self.point = point
        self.color = color
    def __eq__(self,other):
        return utility.epsilon_equal(self.point.x,other.point.x) and utility.epsilon_equal(self.point.y,other.point.y) and utility.epsilon_equal(self.point.z,other.point.z) and utility.epsilon_equal(self.color.r,other.color.r) and utility.epsilon_equal(self.color.g,other.color.g) and utility.epsilon_equal(self.color.b,other.color.b)