from collections import Counter

def checkInclusion(s1, s2):
    left = 0
    right = 0
    iterator = 0
    
    while iterator < len(s2):
        if s2[iterator] in s1:
            left = iterator
            right = iterator
 
            
            iterator = right   
            used = []
        iterator += 1    
       
            
    return False

print(checkInclusion("hello", "ooolleoooleh"))
            
            