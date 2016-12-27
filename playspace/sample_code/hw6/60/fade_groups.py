def groups_of_3(nums):
    new = []
    for i in range(0,len(nums),3):
        new.append(nums[i:i+3])
    return new
