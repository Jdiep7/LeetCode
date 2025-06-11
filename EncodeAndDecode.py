def encode(strs) -> str:
        nums = ""
        for i in strs:
            nums = nums+str(len(i)) + ","
        encoded = str(len(strs)) + "," + nums + "|" + ("".join(strs))
        return encoded
    
def decode(s):
    decodeList = []
    wordLens = (s[0:s.index("|")]).split(",")
    numWords = wordLens[0]
    newStr = s[(s.index("|"))+1: len(s)]
    current = 0
    
    print(wordLens)
    print(newStr)
    
    for i in range(int(numWords)):
        decodeList.append(newStr[current : current + int(wordLens[i+1])])
        current = current + int(wordLens[i+1])
        
        
    return decodeList


print(encode(["123","456","789","10","11","12","13","14","15","16","17","18","19","20"]))
print(decode("14,3,3,3,2,2,2,2,2,2,2,2,2,2,2,|1234567891011121314151617181920"))

