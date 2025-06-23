from collections import Counter
from collections import defaultdict

def minWindow(s,t):
    tCount = Counter(t)
    shortest = ''
    num = len(s)+1
    left = 0
    for right in range(len(s)):
        if s[right] in t:
            tCount[s[right]] -= 1
            
        while all(v <= 0 for v in tCount.values()):
            if(right-left+1) < num:
                shortest = s[left: right + 1]
                num = len(s[left: right + 1])
                        
            if(s[left] in t):
                tCount[s[left]] += 1
            
            left += 1
    
    return shortest
        
        
print(minWindow("ab", "b"))
       
        
