class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(i, curr):
            if i == len(nums):
                res.append(curr[:])
                return
            backtrack(i + 1, curr)
            curr.append(nums[i])
            backtrack(i + 1, curr)
            curr.pop()
        res = []
        backtrack(0, [])
        return res