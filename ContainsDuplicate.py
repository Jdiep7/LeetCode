from collections import Counter

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        counterList = Counter(nums)
        for i in counterList.values():
            if(i >= 2):
                return True
