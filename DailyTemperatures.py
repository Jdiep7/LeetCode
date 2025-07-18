def dailyTemperatures(temperatures):
    n = len(temperatures)
    result = [0]*n
    stack = []
    
    for i, t in enumerate (temperatures):
        print(stack)
        while stack and t > stack[-1][0]:
            stackT, stackInd = stack.pop()
            result[stackInd] = (i - stackInd)
        stack.append([t, i])
    
    return result
        
    
print(dailyTemperatures([73,74,75,71,69,72,76,73]))