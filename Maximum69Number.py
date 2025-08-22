def maximum69Number(num):
    myString = str(num)
    
    result = myString.replace("6", "9", 1)
            
    return int(result)


maximum69Number(9999)