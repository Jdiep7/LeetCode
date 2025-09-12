def doesAliceWin(s: str) -> bool:
        if s == "":
            return False

        vowels = ['a','e','i','o','u']
        vcount = 0
        
        for i in s:
            if i in vowels:
                vcount += 1

        if vcount%2 == 1:
            return True
        
         

print(doesAliceWin("leetcod"))