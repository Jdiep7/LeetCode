def threeSum(nums):
    output = []
    sortednums = sorted(nums)
    
    left = 0
    right = len(nums)-1
    
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i-1]:
            continue
    
        left = i+1
        right = len(nums) - 1
        
        
        
    


print(threeSum([-1,0,1,2,-1,-4]))