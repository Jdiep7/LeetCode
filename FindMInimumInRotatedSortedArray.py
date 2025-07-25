def findMin(nums):
    left = 0
    right = len(nums)-1
    while left <= right:
        middle = (left + right)//2
        next = middle + 1
        if next > len(nums)-1:
            next = 0
        if nums[next] >= nums[middle] and nums[middle-1] >= nums[middle]:
            return nums[middle]
        elif nums[right] < nums[middle]:
            left = middle+1
        else:
            right = middle-1


print (findMin([5,1,2,3,4]))