class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        r = 0
        count = 0
        res = 0
        hashmap = defaultdict(int)
        for l in range(len(nums)):
            while count < k and r < len(nums):
                hashmap[nums[r]] += 1
                if hashmap[nums[r]] >= 2:
                    count += hashmap[nums[r]] - 1
                r += 1
            if count < k:
                break
            res += len(nums) - r + 1
            hashmap[nums[l]] -= 1
            if hashmap[nums[l]] >= 1:
                count -= hashmap[nums[l]]
        return res
                
