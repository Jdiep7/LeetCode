def trap(height):
    left = 0
    right = len(height) - 1
    maxL, maxR = 0,0
    result = 0
    while left <= right:
        if height[left] < height[right]: 
            maxL = max(height[left], maxL)
            result += maxL - height[left]
            left += 1
        else:
            maxR = max(height[right], maxR)
            result += maxR - height[right]
            right -= 1
    
    return result

print(trap([0,1,0,2,1,0,1,3,2,1,2,1]))
        