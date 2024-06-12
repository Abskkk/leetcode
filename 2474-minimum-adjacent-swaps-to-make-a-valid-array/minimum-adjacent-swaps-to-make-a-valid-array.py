'''
find the max and minimum number: maxNum, minNum
initialize minCount = 0, maxCount = 0
iterate over nums, 
when meeting a minNum, res += index - minCount - maxCount
for a maxNum, res += len(nums) - index - 1 - maxCount
'''
class Solution:
    def minimumSwaps(self, nums: List[int]) -> int:
        minNum, maxNum = min(nums), max(nums)
        if minNum == maxNum:
            return 0
        minIndex, maxIndex = len(nums) - 1, 0
        for i in range(len(nums)):
            if nums[i] == minNum:
                minIndex = min(i, minIndex)  
            if nums[i] == maxNum:
                maxIndex = max(i, maxIndex)      
        return minIndex + len(nums) - 1 - maxIndex if minIndex < maxIndex else \
        minIndex + len(nums) - 2 - maxIndex