nums = [100, 4, 200, 1, 3, 2]

count = 0
sequence = []
print(nums)
uniqueList = sorted(set(nums))
n = len(uniqueList)
for i in range(1, n):
    if abs(uniqueList[i] - uniqueList[i-1]) == 1:
        count += 1
    else:
        sequence.append(count)
        count = 0
sequence.append(count)
max_value = max(sequence)

print (max_value+1)
