heights = [2,2,2]

def MaxArea(heights):
    n = len(heights)
    left = 0
    right = n-1
    maxheight = 0
    while(left < right):
        leftHeight = heights[left]
        rightHeight = heights[right]
        height = min(leftHeight, rightHeight) * (right - left)
        
        if(height > maxheight):
            maxheight = height
        
        if(leftHeight == rightHeight):
            left +=1
            right -=1
        elif(leftHeight < rightHeight):
            left += 1
        elif(leftHeight > rightHeight):
            right -= 1
    
    return maxheight
    
    
print(MaxArea(heights))