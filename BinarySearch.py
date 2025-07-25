def search(nums, target):
    left = 0
    right = len(nums)-1
    
    if target == nums[-1]:
        return len(nums)-1
    while left <= right:
        print("right: ", right)
        print("left", left)
        middle = (right + left)//2
        
        if target > nums[middle]:
            left = middle + 1
        elif target < nums[middle]:
            right = middle - 1
        else:
            return middle
    
    return -1
    

print(search([1],2))
                   