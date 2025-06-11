givenList = [2,1,3]
thisList = set()


def checkSwap(modList):
    for i in range(len(modList)):
        temp = modList[0]
        modList[0] = modList[i]
        modList[i] = temp
    
        
        if(modList not in thisList):
            thisList.add(tuple(modList.copy())) 
            checkSwap(modList.copy())
            


checkSwap(givenList)
print(thisList)
