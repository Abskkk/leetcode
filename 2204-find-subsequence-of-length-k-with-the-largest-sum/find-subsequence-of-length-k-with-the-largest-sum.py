class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        pairs = [[i, nums[i]] for i in range(len(nums))]
        pairs.sort(key=lambda x: -x[1])
        pairs = sorted(pairs[:k])
        res = [val for i, val in pairs]
        return res