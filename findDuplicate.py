from collections import defaultdict

def findDuplicateSort(nums):
        nums.sort()
        print(nums)
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                return nums[i]
            

def findDuplicateHash(nums):
    map = defaultdict(int)
    
    for i in nums:
        if i in map:
            return i
        else:
            map[i] = 1
        
def findDuplicateSet(nums):
    myset = set()
    
    for i in nums:
        if i in myset:
            return i
        else:
            myset.add(i)
        



print(findDuplicateHash([3,1,3,4,2]))