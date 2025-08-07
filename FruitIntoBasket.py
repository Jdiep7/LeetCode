def totalFruits(fruits):
    res = 0
    left = 0
    fruit1Index = 0
    fruit2Index = 0
    fruit1 = None
    fruit2 = None
    
    for right in range(len(fruits)):
        if fruit1 is None:
            fruit1 = fruits[right]
            fruit1Index = right
        elif fruits[right] == fruit1:
            fruit1Index = right  
        elif fruit2 is None:
            fruit2 = fruits[right]
            fruit2Index = right    
        elif fruits[right] == fruit2:
            fruit2Index = right
        else:
            if fruit1Index < fruit2Index:
                left = fruit1Index + 1
                fruit1 = fruits[right]
                fruit1Index = right
            else:
                left = fruit2Index + 1
                fruit2 = fruits[right]
                fruit2Index = right
               
        res = max(res, (right - left) + 1)
        
    return res

print(totalFruits([0, 1, 2, 2]))