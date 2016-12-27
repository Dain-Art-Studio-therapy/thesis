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
         last.append(list[num_groups * 3 + j])

      groups.append(last)

   return groups
      

def find_neighbors(pixels, width, height, row, column, radius):
   neighbors = []

   start_row = row - radius
   if start_row < 0:
      start_row = 0

   start_column = column - radius
   if start_column < 0:
      start_column = 0

   end_row = row + radius
   if end_row > height - 1:
      end_row = height - 1

   end_column = column + radius
   if end_column > width - 1:
      end_column = width - 1

   for y in range(start_row, end_row + 1):
      for x in range(start_column, end_column + 1):
         position = x + y * width
         neighbors.append(pixels[position])

   return neighbors


def check_pixel(pixel):
   r, g, b = pixel

   if r > MAX_COLOR:
      r = MAX_COLOR
   if g > MAX_COLOR:
      g = MAX_COLOR
   if b > MAX_COLOR:
      b = MAX_COLOR

   return [r, g, b]

   
def average_pixels(pixels):
   if len(pixels) == 0:
      return [0, 0, 0]

   r = 0
   g = 0
   b = 0

   for i in pixels:
      r += i[0]
      g += i[1]
      b += i[2]

   pixel = [r // len(pixels), g // len(pixels), b // len(pixels)]

   return check_pixel(pixel)
   
