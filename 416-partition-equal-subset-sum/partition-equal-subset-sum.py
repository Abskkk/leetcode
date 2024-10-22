class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        @cache
        def dfs(i, remain):
            if remain < 0:
                return False
            if i == len(nums):
                return True if remain == 0 else False
            return dfs(i + 1, remain) or dfs(i + 1, remain - nums[i])
        total = sum(nums)
        if total % 2 == 1:
            return False
        return dfs(0, total // 2)
        