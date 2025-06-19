def twoSum(nums, target: int):
    hashMap = {}
    if len(nums) == 2:
        return [0, 1]
    for index, item in enumerate(nums):
        hashMap[item] = index
    print(hashMap)
    for index, item in enumerate(nums):
        search = target - item
        if search in hashMap:
            if index != hashMap[search]:
                return [index, hashMap[search]]

twoSum([1,2,3,4,6,5], 10)