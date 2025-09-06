def findMaxAverage(nums, k):
    n = len(nums)
    s = sum(nums[:k])
    best = s

    for right in range(k, n):
        s += nums[right] - nums[right-k]
        if s > best:
            best = s

    
    return best / k

print(findMaxAverage([1,12,-5,-6,50,3], 4))