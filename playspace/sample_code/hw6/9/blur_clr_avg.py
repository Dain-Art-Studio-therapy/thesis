

def blur_clr_avg(pixel_grid, row_i, col_i, blur):
    total_r = total_g = total_b = 0
    num_of_r = num_of_g = num_of_b = 0
    top_left_limit = Point((col_i - blur), (row_i - blur))
    bottom_right_limit = Point((col_i + blur), (row_i + blur))
    for y in range(top_left_limit.y, bottom_right_limit.y):
        for x in range(top_left_limit.x, bottom_right_limit.x):
            try:
                total_r += pixel_grid[y][x][0]
                num_of_r += 1
                total_g += pixel_grid[y][x][1]
                num_of_g += 1
                total_b += pixel_grid[y][x][2]
                num_of_b += 1
            except:
                None
    avg_r = total_r/float(num_of_r)
    avg_g = total_g/float(num_of_g)
    avg_b = total_b/float(num_of_b)
    blur_clr_avg = (avg_r, avg_g, avg_b)
    return blur_clr_avg


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

