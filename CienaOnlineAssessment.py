from collections import defaultdict, deque, Counter

A = [0, 1, 1, 3, 0]
B = [1, 2, 3, 4, 5]
H = [2, 4]

def solution(N, A, B, H):
    # Implement your solution here
    adjList = defaultdict(list)
    waitTime = [-1] * N
    hospitals = deque()
    
    for i in range(len(A)):
        adjList[A[i]].append(B[i])
        adjList[B[i]].append(A[i])

    
    for i in H:
        waitTime[i] = 0
        hospitals.append(i)
        
    while hospitals:
        district = hospitals.popleft()
        
        for i in adjList[district]:
            if waitTime[i] == -1:
                waitTime[i] = waitTime[district] + 1
                hospitals.append(i)

    if(min(waitTime) == -1):
        print(-1)
    else:
        print(max(waitTime))
    
    pass

def pairs(A):
    count = Counter(A)
    
    for i in count.values():
        if(i%2 == 0):
            return True
    return False

#solution(6, A, B, H)
print(pairs([1,2,2,1]))