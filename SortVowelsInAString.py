def sortVowels(s):
    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    vSorted = sorted([ch for ch in s if ch in vowels])
    
    vCount = 0
    s_list = list(s)
    
    for i in range(len(s_list)):
        if s_list[i] in vowels:
            s_list[i] = vSorted[vCount]
            vCount += 1
    
    return "".join(s_list)
    

print(sortVowels("lEetcOde"))