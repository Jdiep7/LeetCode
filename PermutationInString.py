from collections import Counter
from collections import defaultdict


def checkInclusion(s1, s2):
    s1List = Counter(list(s1))
    l = 0
    fmap = Counter()
    
    for r in range(len(s2)):
        if s2[r] in s1:
            fmap[s2[r]] += 1
            
        if r - l > len(s1)-1:
            if s2[l] in s1:
                fmap[s2[l]] -= 1
            l += 1
         
        if fmap == s1List:
            return True 
    return False

print(checkInclusion("ab", "eidboaoo"))
            
            