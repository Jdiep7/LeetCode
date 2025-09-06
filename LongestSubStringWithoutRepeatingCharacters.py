def lengthOfLongestSubstring(s):
    currentString = ''
    longest = 0

    
    for i in s:
        currentString = ''
        longest = 0
        
        for i in s:
            if i in currentString:
                if len(currentString) > longest:
                    longest = len(currentString)
                currentString = currentString + i
                indexOfFirst = currentString.index(i) + 1
                currentString = currentString[indexOfFirst:len(currentString)]
            else:
                currentString = currentString + i
                if len(currentString) > longest:
                    longest = len(currentString)
        return longest
             


        

