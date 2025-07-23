from collections import deque

def maxSlidingWindow(nums, k):
    left = 0
    result = []
    q = deque()
    
    
    for right in range(len(nums)):
        while q and nums[q[-1]] < nums[right]:
            q.pop()
        q.append(right)
        
        if left > q[0]:
            q.popleft()

        if (right + 1) >= k:
            result.append(nums[q[0]])
            left += 1
        
    
    return result
        
    
print(maxSlidingWindow([1,2,1,0,4,2,6], 3))