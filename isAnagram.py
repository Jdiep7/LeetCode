from collections import Counter

def isAnagram(s: str, t: str) -> bool:
    
    sList = Counter(list(s))
    tList = Counter(list(t))

    for i in sList.keys():
        if tList.get(i) != sList.get(i):
            return False
    return True

isAnagram("racecar", "carrace")