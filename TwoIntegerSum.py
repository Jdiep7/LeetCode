def twoSum(numbers, target):
    left = 0
    right = len(numbers) - 1

    while(left < right):
        num = numbers[left] + numbers[right]
        if (num == target):
            return [left+1, right+1]
        elif num > target:
            right -= 1
        else:
            left += 1
            
print(twoSum([1,2,3,4], 3))