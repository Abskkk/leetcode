class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = defaultdict(int)
        for i, num in enumerate(nums):
            if target - num in hashmap:
                return [hashmap[target - num], i]
            else:
                hashmap[num] = i
        return [-1, -1]
