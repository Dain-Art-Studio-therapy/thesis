import collisions
import data
import vector_math
import math



def difference_vector(vector1, vector2):
    diffvec = data.Vector(vector1.x-vector2.x,vector1.y-vector2.y
                          ,vector1.z-vector2.z)
    return diffvec
def scale_vector(vector, scalar):
    scaled = data.Vector(vector.x*scalar, vector.y*scalar
                         , vector.z*scalar)
    return scaled
def normalize_vector(vector):
    veclen = math.sqrt((vector.x)**2 + (vector.y)**2 + (vector.z)**2)
    normal = data.Vector(vector.x/veclen, vector.y/veclen, vector.z/veclen)
    return normal
def dot_vector(vector1, vector2):
    product = (vector1.x * vector2.x) + (vector1.y
                                         * vector2.y) + (vector1.z
                                                         *vector2.z)
    return product
def translate_point(point, vector):
    translated = data.Point(point.x + vector.x, point.y
                            + vector.y, point.z+ vector.z)
    return translated
def len_vec(vector):
    thelength = math.sqrt((vector.x)**2 +(vector.y)**2 + (vector.z)**2)
    return thelength
def di_pt(point1, point2):
    diff = data.Vector(point1.x-point2.x,point1.y -
                       point2.y, point1.z - point2.z)
    return diff
def vector_from_to(from_point, to_point):
    vecfromto = data.Vector(to_point.x-from_point.x,
                            to_point.y-from_point.y,
                            to_point.z-from_point.z)
    return vecfromto

def cast_ray(ray, sphere_list, color, the_light, eye_point):
   only_inters = collisions.find_intersection_points(sphere_list, ray)
   if only_inters !=[]:
      smallest_index = 0
      for lgr in range(1,len(only_inters)):
          if len_vec(di_pt(only_inters[lgr][1], ray.pt)
                     ) <len_vec(di_pt(only_inters[smallest_index][1],
                     ray.pt)):
             smallest_index = lgr

      N = collisions.sphere_normal_at_point(only_inters[smallest_index][0]
                                            , only_inters
                                            [smallest_index][1])
      scaled_N=scale_vector(N, .01)
      Pe=translate_point(only_inters[smallest_index][1], scaled_N)


      L = vector_from_to(Pe,the_light.pt)
      L_dir = normalize_vector(L)
      dotter = dot_vector(L_dir,N)


      refl_vector = difference_vector(L_dir,scale_vector(N,(2*dotter)))
      V_dir = normalize_vector(vector_from_to(eye_point,Pe))
      specs_intense = dot_vector(refl_vector,V_dir)
      
      if dotter <= 0:
         real_r=(only_inters[smallest_index][0].color.r
                 * only_inters[smallest_index][0].finish.ambient * color.r)
         real_g=(only_inters[smallest_index][0].color.g
                 * only_inters[smallest_index][0].finish.ambient * color.g)
         real_b=(only_inters[smallest_index][0].color.b
                 * only_inters[smallest_index][0].finish.ambient * color.b)
         with_finish = data.Color(real_r,real_g,real_b)
      else:
          if in_its_path(ray,sphere_list,Pe,L_dir,the_light) == True:
             real_r=(only_inters[smallest_index][0].color.r
                     * only_inters[smallest_index][0].finish.ambient
                     * color.r)
             real_g=(only_inters[smallest_index][0].color.g
                     * only_inters[smallest_index][0].finish.ambient
                     * color.g)
             real_b=(only_inters[smallest_index][0].color.b
                     * only_inters[smallest_index][0].finish.ambient
                     * color.b)
             with_finish = data.Color(real_r,real_g,real_b)

          elif in_its_path(ray,sphere_list,Pe,L_dir,the_light) == False:
             if spec_intense(L_dir,dotter,N,eye_point,Pe) == False: 
                real_r=(only_inters[smallest_index][0].color.r
                        * only_inters[smallest_index][0].finish.ambient
                        * color.r)+(dotter * the_light.color.r
                                    *only_inters[smallest_index][0].color.r
                                    *only_inters[smallest_index][0]
                                    .finish.diffuse)
                real_g=(only_inters[smallest_index][0].color.g
                        * only_inters[smallest_index][0].finish.ambient
                        * color.g)+(dotter * the_light.color.g
                                    *only_inters[smallest_index][0].color.g
                                    *only_inters[smallest_index][0].
                                    finish.diffuse)
                real_b=(only_inters[smallest_index][0].color.b
                        * only_inters[smallest_index][0].finish.ambient
                        * color.b)+(dotter * the_light.color.b
                                    *only_inters[smallest_index][0].color.b
                                    *only_inters[smallest_index][0].finish
                                    .diffuse)
                with_finish = data.Color(real_r,real_g,real_b)
             elif spec_intense(L_dir,dotter,N,eye_point,Pe) == True:
                real_r=((only_inters[smallest_index][0].color.r
                         * only_inters[smallest_index][0].finish.ambient
                         * color.r)+(dotter* the_light.color.r
                         *only_inters[smallest_index][0].color.r
                         *only_inters[smallest_index][0]
                         .finish.diffuse)+(the_light.color.r
                         *only_inters[smallest_index][0]
                         .finish.specular
                         *(specs_intense**
                         (1/only_inters[smallest_index][0]
                         .finish.roughness))))
                real_g=((only_inters[smallest_index][0].color.g
                        * only_inters[smallest_index][0].finish.ambient
                        * color.g)+(dotter * the_light.color.g
                        *only_inters[smallest_index][0].color.g
                        *only_inters[smallest_index][0].
                        finish.diffuse)+(the_light.color.g
                        *only_inters[smallest_index][0]
                        .finish.specular
                        *(specs_intense**(1/
                        only_inters[smallest_index][0]
                        .finish.roughness))))

                real_b=((only_inters[smallest_index][0].color.b
                         * only_inters[smallest_index][0].finish.ambient
                         * color.b)+(dotter * the_light.color.b
                         *only_inters[smallest_index][0].color.b
                         *only_inters[smallest_index][0]
                         .finish.diffuse)+(the_light.color.b
                         *only_inters[smallest_index][0].finish.specular
                         *(specs_intense**
                         (1/only_inters[smallest_index][0]
                         .finish.roughness))))
                with_finish = data.Color(real_r,real_g,real_b)
      
      return with_finish    
   else:
       return data.Color(1.0,1.0,1.0)

def in_its_path(ray,sphere_list,Pe,L_dir,the_light):
    inters = collisions.find_intersection_points(sphere_list,
                                                 data.Ray(Pe,L_dir))
                        
    
    if inters == []:
        return False
    for inte in range(len(inters)):
        if (len_vec(di_pt(the_light.pt,Pe)) >
            len_vec(di_pt(inters[inte][1], Pe))):
            return True
    else:   
            return False


def spec_intense(L_dir, dotter,N,eye_point,Pe):
    refl_vector = difference_vector(L_dir,scale_vector(N,(2*dotter)))
    V_dir = normalize_vector(vector_from_to(eye_point,Pe))
    spec_intense = dot_vector(refl_vector,V_dir)
    if spec_intense > 0:
        return True
    elif spec_intense <=0:
        return False


def cast_all_rays(min_x,max_x,min_y,max_y,width,
                  height,eye_point,sphere_list, color, the_light):
   print 'P3'
   print width, height
   print 255
   
   increment_y = (max_y-min_y)/height
   increment_x = (max_x-min_x)/width
   
   for y in range(height):
      amt_change_ud = max_y- increment_y*y
      for x in range(width):
         amt_change_lr=min_x + increment_x*x
         call= cast_ray(data.Ray(eye_point,vector_math
                                 .vector_from_to
                                 (eye_point, data.Point(amt_change_lr,
                                 amt_change_ud,0))),sphere_list, color,
                                 the_light, eye_point)
         print int(call.r * 255),int(call.g *255),int (call.b *255)

