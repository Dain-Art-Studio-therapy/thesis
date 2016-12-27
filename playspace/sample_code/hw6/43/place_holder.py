def find_neigbors(pos_grid, x, y, blur): # x and y represents the current pixel coordinate
    target_x = x - blur #start point
    target_y = y - blur #start point
    blur_dimension = (blur * 2) + 1
    rgb_totals = [0, 0, 0]
    for y in blur_dimension:
        for x in blur_dimension:
            rgb_totals[0] += pos_grid[target_y + y][target_x + x][0]
            rgb_totals[1] += pos_grid[target_y + y][target_x + x][1]
            rgb_totals[2] += pos_grid[target_y + y][target_x + x][2]
    rgb_average = [rgb_totals[0]/(blur_dimension**2), rgb_totals[1]/(blur_dimension**2), rgb_totals[2]/(blur_dimension**2)]
    return rgb_average










def find_averages(width, height, neighbor_grid):
    red_sum = 0
    blue_sum = 0
    green_sum = 0
    for y in range(int(height)):#new height
        for x in range(int(width)): #new width
            r = pix_pos_grid[0]
            g = pix_pos_grid[1]
            b = pix_pos_grid[2]
            red_sum += r
            green_sum += g
            blue_sum += b