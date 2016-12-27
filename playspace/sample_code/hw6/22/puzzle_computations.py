MAX_COLOR = 255


def groups_of_three(list):
   groups = []
   last = []

   num_groups = len(list) // 3
   remainder = len(list) % 3

   for i in range(num_groups * 3):
      if i % 3 == 0:
         groups.append([list[i], list[i + 1], list[i + 2]])
 
   if remainder != 0:
      for j in range(remainder):
         last.append(list[num_groups * 3 + j])
 
      groups.append(last)

   return groups


def check_pixel(pixel):
   r, g, b = pixel

   if r > MAX_COLOR:
      r = MAX_COLOR
   if g > MAX_COLOR:
      g = MAX_COLOR
   if b > MAX_COLOR:
      b = MAX_COLOR

   return [r, g, b]


def convert_pixel(pixel):
   r = int(pixel[0]) * 10

   return check_pixel([r, r, r])
