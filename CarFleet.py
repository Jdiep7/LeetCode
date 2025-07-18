def carfleet(target, position, speed):
    stack = []
    cars = list(zip(position, speed))
    cars.sort(reverse=True)
    
    for p, s in cars:
        stack.append((target-p)/s)
        if len(stack) >= 2 and stack[-1] <= stack[-2]:
            stack.pop()
    return len(stack)
    
    

print(carfleet(10, [4,1,0,7], [2,2,1,1]))