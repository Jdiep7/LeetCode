import math
def isPowerOfThree(n: int) -> bool:
    
    if n <= 0:
        return False
    
    result = round(math.log(n, 3))
    if 3 ** result == n:
        return True
    
    return False

print(isPowerOfThree(243))