class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        hashmap = defaultdict(int)
        maxSum = float('-inf')
        prefixSum = [0] * (len(nums) + 1)
        for i in range(1, len(nums) + 1):
            prefixSum[i] = prefixSum[i - 1] + nums[i - 1]

        def sumOfSubarray(i, j):
        # prefix sum
            return prefixSum[j + 1] - prefixSum[i]

        for i in range(len(nums)):
            if nums[i] not in hashmap:
                hashmap[nums[i]] = i
            elif prefixSum[i] < prefixSum[hashmap[nums[i]]]:
                hashmap[nums[i]] = i
            target1, target2 = nums[i] - k, nums[i] + k
            if target1 in hashmap:
                maxSum = max(maxSum, sumOfSubarray(hashmap[target1], i))
            if target2 in hashmap:
                maxSum = max(maxSum, sumOfSubarray(hashmap[target2], i))
        return maxSum if maxSum != float('-inf') else 0
