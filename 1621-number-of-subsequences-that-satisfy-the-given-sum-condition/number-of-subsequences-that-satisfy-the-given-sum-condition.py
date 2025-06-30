class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        MOD = 10 ** 9 + 7
        n = len(nums)
        nums.sort()
        l, r = 0, n - 1
        res = 0

        while l <= r:
            if nums[l] + nums[r] <= target:
                res += 2 ** (r - l) % MOD
                res %= MOD
                l += 1
            else:
                r -= 1
        return res 