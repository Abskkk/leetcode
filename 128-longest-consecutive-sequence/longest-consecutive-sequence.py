class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums)
        res = 0
        for num in hashset:
            if num - 1 not in hashset:
                currNum = num
                cnt = 1
                while currNum + 1 in hashset:
                    currNum += 1
                    cnt += 1
                res = max(res, cnt)
        return res