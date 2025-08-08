def numOfUnplacedFruits(fruits: list[int], baskets: list[int]):
    unplaced = 0
    count = 0
    for i in fruits:
        unplaced = 1
        for j in range(len(baskets)):
            if i <= baskets[j]:
                baskets[j] = -1
                unplaced = 0
                break
            
        count += unplaced
    
    return count

print(numOfUnplacedFruits([4,2,5], [1,2,3]))