from collections import defaultdict

def characterReplacement(s, k):
    thisdict = defaultdict(int)
    longest = 0
    left = 0
    
    for right in range(len(s)):
        thisdict[s[right]] += 1

        if (right - left + 1) - max(thisdict.values()) > k:
            thisdict[s[left]] -= 1
            left += 1
        
        if (right - left + 1) > longest:
            longest = right - left + 1
        
        
    return longest
            
     
print(characterReplacement("AAABABB", 1))       