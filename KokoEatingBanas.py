import math

def minEatingSpeed(piles, h):
    left = 1
    right = max(piles)
    res = right
    
    while left <= right:
        k = (left + right)//2
        hours  = 0
        for i in piles:
            hours += math.ceil(i/k)
        if  hours <= h:
            res = k
            right = k-1
        else:
            left = k+1

    return res



print(minEatingSpeed([1,4,3,2], 9))