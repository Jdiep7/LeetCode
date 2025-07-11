def evalRPN(tokens):
    stack = []
    for i in tokens:
        if i == "+":
            stack.append(stack.pop() + stack.pop())
        elif i == "-":
            temp = stack.pop()
            stack.append(stack.pop() - temp)
        elif i == "*":
            stack.append(stack.pop() * stack.pop())
        elif i == "/":
            temp = stack.pop()
            stack.append(float(stack.pop() / temp))
        else:
            stack.append(int(i))
    return stack[0]


print(evalRPN(["1","2","+","3","*","4","-"]))
    