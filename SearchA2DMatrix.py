def searchMatrix(matrix, target):
    top = 0
    bottom = len(matrix) - 1
    resCol = 0
    left = 0
    
    while top <= bottom:
        midCol = (top + bottom) // 2
        
        if target < matrix[midCol][0]:
            bottom = midCol -1
        elif target > matrix[midCol][-1]:
            top = midCol + 1
        elif target == matrix[midCol][0] or target == matrix[midCol][-1]:
            return True
        else:
            resCol = midCol
            break
    
    right = len(matrix[resCol])-1
    if target == matrix[resCol][-1]:
        return True
    while left <= right:
        print('right: ', right)
        print('left: ', left)
        middle = (left + right) // 2
        
        if target < matrix[resCol][middle]:
            right = middle-1
        elif target > matrix[resCol][middle]:
            left = middle + 1
        else:
            return True
    
    return False

print(searchMatrix([[1]], 2))