import math

SCALE_LIMIT = 0.2
MAX_COLOR = 255


def groups_of_three(list):
   num_groups = len(list) // 3
   remainder = len(list) % 3

   groups = []
   last = []

   for i in range(num_groups * 3):
      if i % 3 == 0:
         groups.append([list[i], list[i + 1], list[i + 2]])

   if remainder != 0:
      for j in range(remainder):
         last.append(list[num_groups * 3 + i])

      groups.append(last)

   return groups


def distance(from_x, from_y, to_x, to_y):
   return math.sqrt((to_x - from_x) ** 2 + (to_y - from_y) ** 2)


def check_pixel(pixel):
   r, g, b = pixel

   if r > MAX_COLOR:
      r = MAX_COLOR
   if g > MAX_COLOR:
      g = MAX_COLOR
   if b > MAX_COLOR:
      b = MAX_COLOR

   return [r, g, b]


def scale_pixel(pixel, scale):
   if scale < SCALE_LIMIT:
      scale = SCALE_LIMIT

   r = int(pixel[0] * scale)
   g = int(pixel[1] * scale)
   b = int(pixel[2] * scale)

   return check_pixel([r, g, b])
