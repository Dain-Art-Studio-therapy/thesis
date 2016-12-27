def groups_of_3(nums):
    new = []
    for i in range(0,len(nums),3):
        new.append(nums[i:i+3])
    return new

def grid(pixel_list,width):
    grid = []
    for i in range(0,len(pixel_list),width):
        grid.append(pixel_list[i:i+width])
    return grid
