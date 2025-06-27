from collections import deque

def isValid(s):
    stack = deque()
    mapping = {')': '(', '}': '{', ']': '['}
        
    for i in s:
        if i in mapping:
            if stack:
                top = stack.pop()
            else:
                top = "#"

            if mapping[i] != top:
                return False
        else:
            stack.append(i)
    return not stack
                
            