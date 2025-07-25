def search(nums, target):
    left = 0
    right = len(nums)-1
    
    while left<=right:
        middle = (left + right)//2
        
        if nums[middle] == target:
            return middle
        elif target > nums[middle] and (nums[right] < nums[middle] or target <= nums[right]):
            left = middle + 1
        elif target < nums[middle] and target <= nums[right] and nums[right] < nums[middle]:
            left = middle + 1
        else:
            right = middle-1
    
    return -1
        
print(search([3,5,6,0,1,2], 4))